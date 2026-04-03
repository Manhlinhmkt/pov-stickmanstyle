---
description: Generate illustration strip table and image prompts (PVLE P3.1)
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-gen-image-prompts

> **Phase:** 3.1 — Illustration  
> **Input:** `vo_script_table.csv` + `l2_breakdown_table.csv` + `episode_brief.md`  
> **Output:** `illustration_strip_table.csv` + `image_prompts.csv`  
> **Target tool:** Nano Banana (Gemini Image Generation)

---

## STEP 1: Read Inputs

Load:
- `vo_script_table.csv` → VO_ID, Beat_ID, Life_Phase, Beat_Type, VO_Type, VO_EN, Word_Count_EN, Pause_After
- `l2_breakdown_table.csv` → Beat_ID → Illustration_Note mapping
- `episode_brief.md` → Stickman_Accessory, Key_Locations, Opening_Scene

---

## STEP 2: Load Rules

Load:
- `phase-3/illustration-mapping-rules.md` → strip grouping logic
- `phase-3/visual-rules.md` → scene type formulas + style constants

Extract style constants:
```
STYLE_LOCK: "Minimalist stickman illustration. Simple stick figure with round white circle head and thin black body lines, no facial features."

NEGATIVE_SUFFIX: "--no realistic human faces, no photorealism, no anime style, no chibi proportions, no 3D render, no facial features on stickman, no complex shading on characters"

PRIMARY_ACCESSORY: [from episode_brief.md Stickman_Accessory]
```

---

## STEP 3: Generate Strip Table

Apply smart grouping from `illustration-mapping-rules.md`:

### 3a: Initial Grouping

Group consecutive VO lines by Beat_ID. Calculate accumulated duration per group:
```
duration_sec = total_words_en / 130 * 60 + sum(pause_after)
```

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

### 3h: Output Strip Table

**RULE_SILENT_OUTPUT:** CSV only.

File: `pvle/episodes/{EP}/illustration_strip_table.csv`

Columns: `Strip_ID,Start_VO_ID,End_VO_ID,VO_Count,Life_Phase,Scene_Type,Duration_Sec,Strip_Summary`

---

## STEP 4: Generate Image Prompts

For each strip in `illustration_strip_table.csv`, generate 1 image prompt.

**Select formula by Scene_Type (from visual-rules.md §4):**

```yaml
NARRATIVE_SCENE:
  formula: "{STYLE_LOCK} {ACCESSORY}. {ACTION from Strip_Summary} in {LOCATION — detailed, colorful, architectural}. Flat illustration, clean lines. {NEGATIVE_SUFFIX}"

TIME_SKIP_SCENE:
  formula: "Split panel illustration, time skip. Left panel labeled 'AGE {X}': {STYLE_LOCK} {CHILD_CONTEXT} in {CHILDHOOD_LOCATION}. Right panel labeled 'AGE {Y}': {STYLE_LOCK} {ADULT_CONTEXT} in {ADULT_LOCATION}. Clean dividing line. Flat illustration. {NEGATIVE_SUFFIX}"
  note: "Use when Strip_Summary references age transition"

POV_SHOT:
  formula: "First-person POV illustration. Two simple flat black stickman hands {HAND_POSITION} at bottom frame corners. {DETAILED_VIEW from Strip_Summary}. Flat illustration, immersive. {NEGATIVE_SUFFIX}"

EMOTIONAL_CLOSEUP:
  formula: "{STYLE_LOCK} {POSTURE_CUE from Mood_Tag: LONGING=hunched/DREAD=curled/PRIDE=upright}. Background fades from {LOCATION_DETAIL} on one edge to pure white opposite. {COLOR_TINT from visual-rules.md §5}. Flat illustration. {NEGATIVE_SUFFIX}"

TEXT_OVERLAY:
  formula: "{BACKGROUND_COLOR} background. Large bold {TEXT_COLOR} sans-serif text centered: '{KEY_PHRASE from Strip_Summary}'. {Optional: smaller second line}. Flat design, premium typography. {NEGATIVE_SUFFIX}"

CONTRAST_SPLIT:
  formula: "Split screen, vertical dividing line. LEFT labeled 'YOU': {STYLE_LOCK} {SUBJECT_WITH_PRIVILEGE} in {PRIVILEGE_ENVIRONMENT}. RIGHT labeled 'EVERYONE ELSE': same stickman in {NORMAL_EQUIVALENT_ENVIRONMENT}. Flat illustration. {NEGATIVE_SUFFIX}"
```

**COLOR_TINT rules (from visual-rules.md §5):**
```
LONGING / TENSION     → cool blue wash
DREAD                 → desaturated cold grey
BITTERSWEET           → warm amber glow
PRIDE / CLARITY       → soft gold light
WONDER                → neutral bright (no tint)
```

---

## STEP 5: Validate Image Prompts

- [ ] Prompt count == Strip count (1:1 mapping from strips, NOT from VO lines)
- [ ] Every prompt starts with STYLE_LOCK (except POV_SHOT and TEXT_OVERLAY)
- [ ] Every prompt ends with NEGATIVE_SUFFIX
- [ ] Slate IDs match Strip_IDs
- [ ] No generic backgrounds ("a room", "outside")
- [ ] No realistic face descriptions in any prompt
- [ ] Accessory description identical across all prompts in episode

---

## STEP 6: Output Image Prompts

**RULE_SILENT_OUTPUT:** CSV only.

File: `pvle/episodes/{EP}/image_prompts.csv`

Columns: `Slate,Start_VO_ID,End_VO_ID,Life_Phase,Scene_Type,Image_Prompt`

> **Note:** Slate now maps to Strip_ID (1:1 with strips, not with VO lines).
> `Start_VO_ID` and `End_VO_ID` indicate which VO lines this image covers.

---

## USER INPUT

> `Episode_ID`: {{Episode_ID}}
