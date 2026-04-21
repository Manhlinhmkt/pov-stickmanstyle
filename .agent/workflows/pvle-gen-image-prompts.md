---
description: Generate illustration strip table and image prompts (PVLE P3.1)
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-gen-image-prompts

> **Phase:** 3.1 - Illustration  
> **Input:** `vo_script_table.csv` + `l2_breakdown_table.csv` + `episode_brief.md`  
> **Output:** `illustration_strip_table.csv` + `image_prompts.csv`  
> **Target tool:** Nano Banana (Gemini Image Generation)

## EXECUTION_CHECKLIST

```yaml
total_steps: 7
steps:
  - step: 1
    name: "Read Inputs"
    type: AUTO
    output: "inline (data loaded)"

  - step: 2
    name: "Load Rules"
    type: AUTO
    output: "inline (style constants extracted)"

  - step: 3
    name: "Generate Strip Table"
    type: AUTO
    output: "pvle/episodes/{EP}/illustration_strip_table.csv"

  - step: 3.5
    name: "Verify Character Review (prerequisite)"
    type: BLOCKING
    gate: "ABORT if character review not completed - run /pvle-character-review first"
    output: "inline (check result)"

  - step: 4
    name: "Generate Image Prompts"
    type: AUTO
    output: "inline (prompts generated)"

  - step: 5
    name: "Validate + Output Image Prompts"
    type: AUTO
    output: "pvle/episodes/{EP}/image_prompts.csv"

  - step: 7
    name: "Update Episode Registry"
    type: AUTO
    output: "episode_registry.csv updated"

# On completion: verify all steps checked
# On skip: VIOLATION -> HALT_AND_REPORT
```

---

## STEP 1: Read Inputs

Load:
- `vo_script_table.csv` → VO_ID, Beat_ID, Life_Phase, Beat_Type, VO_Type, VO_EN, Word_Count_EN, Pause_After
- `l2_breakdown_table.csv` → Beat_ID → Illustration_Note mapping
- `episode_brief.md` → Stickman_Accessory, Key_Locations, Opening_Scene, **CHARACTER REGISTRY**

From CHARACTER REGISTRY in `episode_brief.md`, extract:
- `character_table[]` — list of all Char_IDs with veil_name, visual_summary, appears_in_phases
- `subject_phase_traits{}` — map of Life_Phase → {height, hair, clothing, face, distinguishing}

---

## STEP 2: Load Rules

Load:
- `phase-3/illustration-mapping-rules.md` → strip grouping logic
- `phase-3/visual-rules.md` → scene type formulas + style constants + character injection rules

Extract style constants:
```
STYLE_LOCK: "Simple stickman character with oversized round white circle head.
Body drawn with thin black lines.
Clothing as simple flat-colored shapes (no detail, no folds, no shading).
Character is deliberately simple — contrast against highly detailed,
semi-realistic painted background environment."

# NOTE: Face description (eyes, mouth) is NOT in STYLE_LOCK.
# Face comes from CHARACTER REGISTRY per character:
#   REAL_PERSON → "dot eyes + simple mouth" with expression from registry
#   ANONYMOUS_GROUP → "blank white circle head, no eyes, no mouth"

NEGATIVE_SUFFIX: "--no realistic human faces, no complex facial features, no detailed clothing folds,
no body shading on stickman characters, no 3D render on characters, no anime style,
no chibi proportions, no filled body volume, no oversized main character"

PRIMARY_ACCESSORY: [from episode_brief.md Stickman_Accessory]
```

---

## STEP 3: Generate Strip Table

Apply smart grouping from `illustration-mapping-rules.md`:

### 3a-PRE: Speech Time Summary (MANDATORY FIRST STEP)

Before any grouping, calculate and display:

```
total_words = sum(all Word_Count_EN from vo_script_table.csv)
total_pauses = sum(all Pause_After from vo_script_table.csv)
total_speech_time = total_words / 130 * 60 + total_pauses
min_strips = ceil(total_speech_time / 12)
target_strips = round(total_speech_time / 8)
max_strips = floor(total_speech_time / 4)
```

Output summary table:
| Metric | Value |
|--------|-------|
| Total VO lines | {count} |
| Total Word_Count_EN | {sum} |
| Total Pause_After | {sum} seconds |
| Total Speech Time | {seconds} sec = {minutes} min |
| Min strip count (max 12s each) | {min_strips} |
| Target strip count (8s sweet spot) | {target_strips} |
| Max strip count (min 4s each) | {max_strips} |

> [!CAUTION]
> This summary MUST be calculated before proceeding.
> Final strip count must fall within [min_strips, max_strips] range.
> If final count < min_strips → duration calculation is wrong.

---

### 3a: Initial Grouping + EXACT Duration

Group consecutive VO lines by Beat_ID.

**MANDATORY: Calculate EXACT duration per group:**
1. List all VO_IDs in group
2. Look up each VO_ID's `Word_Count_EN` and `Pause_After` from `vo_script_table.csv`
3. `duration_sec = sum(Word_Count_EN) / 130 * 60 + sum(Pause_After)`

> [!CAUTION]
> Do NOT estimate durations. Must SUM actual values from CSV.
> Wrong: "this strip is about 7.5 seconds"
> Right: "words=[5,7,7,6,7]=32, pauses=[0,0,0,0.5,1.5]=2.0, duration=32/130*60+2.0=16.8s"

### 3b: Apply Split Rules (in priority order)

1. **Phase boundary** → ALWAYS split (never cross phases)
2. **Duration > 12s** → split at nearest sentence boundary
3. **Beat change + duration > 8s** → split at beat boundary
4. **Visual context change** → split (new location, time, activity)

### 3c: Apply Merge Rules

1. **Same beat + same visual + < 12s** → keep together
2. **Micro-beats < 3s** → merge with adjacent (same visual context)
3. **Consecutive narration of same moment** → keep together

### 3d: Handle Special Strips

- **Clip moments** (performance duality pairs) → own strip, TEXT_OVERLAY
- **High-impact WEIGHT_LINEs** (Pause_After ≥ 1.5, ≤ 10 words) → own strip, TEXT_OVERLAY
- **Standard WEIGHT_LINEs** → attach as last line of previous strip

### 3e: Assign Scene Types

Per strip, select Scene_Type using:
1. TEXT_OVERLAY check (weight-line-only strips ≤ 10 words)
2. Phase-based mapping (from visual-rules.md §6)
3. Content cues in VO_EN (time reference → TIME_SKIP, contrast → CONTRAST_SPLIT, etc.)
4. Default → NARRATIVE_SCENE

### 3f: Generate Strip Summaries

Write 1-sentence visual summary per strip (max 25 words):
- Format: "[Subject action/state] in [location/context]. [Key visual detail]."
- Source: VO_EN lines within the strip
- For TEXT_OVERLAY: exact quote from VO_EN

### 3g: Validate Strip Table

- [ ] Every VO_ID covered by exactly 1 strip (no gaps/overlaps)
- [ ] All strips 3s ≤ duration ≤ 12s (warning at 12-15s, violation at >15s)
- [ ] Each strip = 1 Life_Phase only
- [ ] Strip_IDs sequential
- [ ] At least 1 EMOTIONAL_CLOSEUP in PHASE_CRISIS
- [ ] HOOK starts with POV_SHOT or TEXT_OVERLAY
- [ ] **EXACT CALC**: Each Duration_Sec = sum(Word_Count_EN)/130*60 + sum(Pause_After) from CSV
- [ ] **CROSSCHECK**: `sum(all Duration_Sec)` within 5% of `total_speech_time` from Step 3a-PRE
- [ ] **SANITY**: `strip_count` within [min_strips, max_strips] from Step 3a-PRE

If CROSSCHECK fails → strip durations are wrong. ABORT and recalculate from CSV data.
If SANITY fails → strips are too long or too short. Re-split or re-merge.

### 3h: Output Strip Table

**RULE_SILENT_OUTPUT:** CSV only.

File: `pvle/episodes/{EP}/illustration_strip_table.csv`

Columns: `Strip_ID,Start_VO_ID,End_VO_ID,VO_Count,Life_Phase,Scene_Type,Duration_Sec,Strip_Summary`

---

## STEP 3.5: Verify Character Review (PREREQUISITE CHECK)

> **This is NOT a delegate.** Character review must be completed BEFORE running this workflow.

### Check:
1. Does `pvle/assets/characters/character_index.yaml` contain entries for REAL_PERSON characters in this episode?
2. Does the CHARACTER REGISTRY in `episode_brief.md` have accurate Face column with researched visual anchors?

```yaml
check_result:
  ALL_CHARACTERS_REVIEWED:
    action: "Load approved traits from registry → proceed to Step 4"
    
  MISSING_REVIEW:
    action: "ABORT workflow"
    message: "Character visual review not completed. Run /pvle-character-review {EP} first."
    
  PARTIAL_REVIEW:
    action: "ABORT workflow"
    message: "Some characters missing from asset library. Run /pvle-character-review {EP} to complete."
```

> [!IMPORTANT]
> If character review is missing, do NOT attempt to generate image prompts.
> Run `/pvle-character-review {EP}` as a separate workflow first, get user approval, then re-run this workflow.

---

## STEP 4: Generate Image Prompts

For each strip in `illustration_strip_table.csv`, generate 1 image prompt.

### 4a: Look up Character Traits

Before writing each prompt:
1. Get `Life_Phase` from strip
2. Look up `subject_phase_traits[Life_Phase]` → height, hair, clothing, face, distinguishing
3. Check if any supporting characters appear in this Life_Phase → look up their visual_summary from character_table
4. AGENTS: always FACELESS (blank white circle head, no eyes, no mouth) whenever in scene

Phase-to-traits lookup order:
```yaml
# Use subject_phase_traits{} extracted from CHARACTER REGISTRY in Step 1
# and VALIDATED by user in Step 3.5 (Character Visual Review)
#
# Each Life_Phase maps to its OWN trait set — do NOT use generic defaults.
# The traits were confirmed via generate_image in Step 3.5a.
#
# Lookup: subject_phase_traits[strip.Life_Phase] → {height, hair, clothing, face, distinguishing}
#
# If a phase has sub-phases (e.g. EARLY child vs EARLY teen),
# use Beat_ID sequence to determine which sub-trait applies:
#   - Early beats in phase → younger sub-trait
#   - Later beats in phase → older sub-trait
#
# CRITICAL: traits MUST match the visuals approved by user in Step 3.5
```

### 4b: Build CHARACTER BLOCK

For NARRATIVE_SCENE, CONTRAST_SPLIT, EMOTIONAL_CLOSEUP:
```
SUBJECT_BLOCK: "{height}. {hair}. {clothing}. {FACE_BLOCK}. {distinguishing}."

  FACE_BLOCK (MANDATORY — from character_index.yaml):
    Adult phases: "{jawline descriptor} circle head. Small {eye_color} dot eyes. {expression}."
    Child phases: "round white circle head. Small dot eyes."
    Example: "Clean-shaven strong jawline circle head. Small hazel-green dot eyes. Military-straight expression."

  ⚠️ FACE_BLOCK must appear in EVERY subject-visible prompt.
  Do NOT omit after first slate. Each prompt is standalone.

SUPPORT_BLOCK (only if character.appears_in_phases includes this strip's Life_Phase):
  REAL_PERSON: "{character.veil_name}: {character.visual_summary}. {face from registry}."
  ANONYMOUS_GROUP: "{role descriptor} stickman (faceless, blank white circle head)."

AGENTS_BLOCK (if agents are in scene context):
  "FACELESS dark-suited stickman figures (blank white circle head, small earpiece dot, rigid upright posture)."
```

For TIME_SKIP_SCENE:
```
Per panel, use the respective phase's subject_phase_traits
LEFT_PANEL_BLOCK: "{younger_phase traits}"
RIGHT_PANEL_BLOCK: "{older_phase traits}"
```

For POV_SHOT:
```
HANDS_BLOCK: "Two simple flat black stickman hands at bottom frame corners —
{small child hands / large adult hands per Life_Phase}, {clothing cue from phase traits}."
```

### 4c: Select Formula by Scene_Type

```yaml
NARRATIVE_SCENE:
  formula: "{STYLE_LOCK} {SUBJECT_BLOCK} {SUPPORT_BLOCK if applicable}. {ACTION from Strip_Summary} in {LOCATION — detailed, colorful, architectural}. {AGENTS_BLOCK if applicable}. Flat illustration, clean lines. {NEGATIVE_SUFFIX}"

TIME_SKIP_SCENE:
  formula: "{STYLE_LOCK} Two-panel layout. Clean vertical dividing line. Left panel label '{AGE X}': {LEFT_PANEL_BLOCK} in {EARLIER_LOCATION}. Right panel label '{AGE Y}': {RIGHT_PANEL_BLOCK} in {LATER_LOCATION}. Minimal flat color palette. {Strip_Summary context line}. {NEGATIVE_SUFFIX}"
  note: "Use subject_phase_traits for EACH panel's respective age phase separately"

POV_SHOT:
  formula: "First-person POV illustration. {HANDS_BLOCK}. Rich, detailed background: {DETAILED_LOCATION from key_locations, specific architecture}. {Strip_Summary context line}. Flat illustration, immersive perspective. {NEGATIVE_SUFFIX}"

EMOTIONAL_CLOSEUP:
  formula: "{STYLE_LOCK} {SUBJECT_BLOCK} {POSTURE_CUE: hunched forward/standing rigid/standing still head tilted}. Background fades from {LOCATION_REFERENCE} on one side to pure white opposite. {COLOR_TINT from visual-rules.md §5}. Single subject, centered. {Strip_Summary context line}. Flat illustration. {NEGATIVE_SUFFIX}"

TEXT_OVERLAY:
  formula: "{BACKGROUND_COLOR} background. Large bold {TEXT_COLOR} sans-serif text centered: '{KEY_PHRASE from Strip_Summary}'. {Optional smaller secondary text line}. Flat design, premium typography. {NEGATIVE_SUFFIX}"

CONTRAST_SPLIT:
  formula: "{STYLE_LOCK} {SUBJECT_BLOCK}. Vertical split composition. Clean dividing line center. Left side label 'YOU': {SUBJECT in extraordinary/exclusive context}. Right side label '{CONTRAST_LABEL}': same stickman proportions in ordinary equivalent context. {Strip_Summary context}. Equal sizing both sides. Flat color palette. {NEGATIVE_SUFFIX}"
```

**COLOR_TINT rules (from visual-rules.md §5):**
```
LONGING / TENSION     → cool blue wash fading at edges
DREAD                 → desaturated cold grey vignette at edges
BITTERSWEET           → warm amber glow at edges
PRIDE / CLARITY       → soft gold light from upper right
WONDER                → neutral bright (no tint)
DEEP_CONNECTION       → soft warm white — edges slightly blurred
```

---

## STEP 5: Validate Image Prompts

> **CRITICAL RULE — RULE_NO_VO_TEXT_IN_PROMPT:**  
> Image prompt phải mô tả thuần visual — KHÔNG được copy VO_EN vào prompt.  
> VO text trong prompt = image generator tạo subtitle/caption text trong ảnh.  
> Hãy diễn đạt bằng visual description: "stickman sitting at desk" thay vì "you sit at your desk".

- [ ] Prompt count == Strip count (1:1 mapping from strips, NOT from VO lines)
- [ ] Every NARRATIVE_SCENE / EMOTIONAL_CLOSEUP / CONTRAST_SPLIT / TIME_SKIP_SCENE starts with STYLE_LOCK
- [ ] Every prompt ends with full NEGATIVE_SUFFIX (including text prohibition block)
- [ ] **ZERO verbatim VO_EN sentences in any prompt** (RULE_NO_VO_TEXT_IN_PROMPT)
- [ ] Slate IDs match Strip_IDs exactly
- [ ] No generic backgrounds ("a room", "outside", "somewhere")
- [ ] No realistic face descriptions in any prompt
- [ ] CHARACTER BLOCK traits match the strip's Life_Phase (height / hair / clothing must be phase-consistent)
- [ ] **FACE_BLOCK present in EVERY subject-visible prompt** (RULE_FACE_INJECTION_MANDATORY)
- [ ] **FACE_BLOCK matches character_index.yaml** — eye color, jawline, expression must be exact
- [ ] **Supporting characters: REAL_PERSON has face from registry, ANONYMOUS_GROUP has "(faceless, blank white circle head)"**
- [ ] AGENTS described as FACELESS in every scene they appear in
- [ ] Supporting characters (FATHER, MOTHER, SIBLINGS) only appear in prompts when appears_in_phases matches
- [ ] Real names ABSENT from all prompts — veil_name used throughout
- [ ] POV_SHOT hand descriptions match Life_Phase (child hands in HOOK/EARLY, adult hands in CRISIS+)

---

## STEP 6: Output Image Prompts

**RULE_SILENT_OUTPUT:** CSV only.

File: `pvle/episodes/{EP}/image_prompts.csv`

Columns: `Slate,Start_VO_ID,End_VO_ID,Life_Phase,Scene_Type,Image_Prompt`

> **Note:** Slate maps to Strip_ID (1:1 with strips, not with VO lines).
> `Start_VO_ID` and `End_VO_ID` indicate which VO lines this image covers.

---

## STEP 7: Update Episode Registry

After image_prompts.csv is written successfully:

1. Read `episode_registry.csv` (root directory)
2. Check if Episode_ID already exists:
   - EXISTS: Update row (in case title changed)
   - NOT EXISTS: Append new row
3. Extract from episode_brief.md:
   - **Episode_Title**: from METADATA table
   - **Main_Character**: from CHARACTER REGISTRY SUBJECT row
     - TRANSPARENT_VEIL: use implied_person from world YAML (internal only)
     - GENERIC_ARCHETYPE: use role descriptor from Veil_Name or world display_name
   - **Theme**: derive from world domain + tags (1 short keyword)
4. Write updated CSV (UTF-8 BOM)

Confirm:
```
Episode registered: [Episode_ID] | [Title] | [Main_Character] | [Theme]
```

---

## USER INPUT

> `Episode_ID`: {{Episode_ID}}

