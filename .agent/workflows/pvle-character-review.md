---
description: Generate character visual review and save approved assets (PVLE P3.1 blocking gate)
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-character-review

> **Phase:** 3.1 - Pre-Image-Prompt Visual Validation  
> **Input:** `episode_brief.md` (CHARACTER REGISTRY section)  
> **Output:** Review artifact + approved character assets saved to `pvle/assets/characters/`  
> **Gate:** BLOCKING - user must approve before image prompt generation

## EXECUTION_CHECKLIST

```yaml
total_steps: 8
steps:
  - step: 1
    name: "Load Character Data"
    type: AUTO
    output: "inline (character data loaded)"

  - step: 2
    name: "Check Asset Library"
    type: AUTO
    output: "inline (HIT/MISS report)"

  - step: 3
    name: "Generate SUBJECT Evolution Sheet"
    type: AUTO
    output: "generated image (subject evolution)"

  - step: 4
    name: "Generate Supporting Characters Sheet"
    type: AUTO
    output: "generated image (supporting characters)"

  - step: 5
    name: "Generate Key Scene Samples"
    type: AUTO
    output: "generated images (1-2 scene samples)"

  - step: 6
    name: "Create Review Artifact"
    type: AUTO
    output: "character_review_{EP}.md"

  - step: 7
    name: "User Approval"
    type: BLOCKING
    gate: "Wait for user to approve character visuals"
    output: "inline (approval request)"

  - step: 8
    name: "Save Approved Assets"
    type: AUTO
    output: "pvle/assets/characters/ + character_index.yaml"

# On completion: verify all steps checked
# On skip: VIOLATION -> HALT_AND_REPORT
```

---

## STEP 1: Load Character Data

Load from `pvle/episodes/{EP}/episode_brief.md`:
- `character_table[]` — Char_ID, Veil_Name, Visual_Summary, Face, Appears_In_Phases
- `subject_phase_traits{}` — Phase → Height, Hair, Clothing, Face, Distinguishing
- `face_rule` — REAL_PERSON vs ANONYMOUS_GROUP classification

---

## STEP 2: Check Asset Library

For each **REAL_PERSON** character in `character_table[]`:

```
Check: pvle/assets/characters/character_index.yaml
→ Search by real_person name or CHAR_ID

FOUND:
  - Load asset file path from index
  - Mark character as ASSET_HIT — will embed existing image in review
  - Skip generation for this character

NOT FOUND:
  - Mark character as ASSET_MISS — must generate new visual
```

Report:
```
Asset Library Check:
  HIT:  [list of characters with existing approved assets]
  MISS: [list of characters needing new generation]
```

---

## STEP 3: Generate SUBJECT Evolution Sheet

> Skip if SUBJECT asset exists AND user has not requested re-review.

Using `generate_image` tool, create a **single character lineup image** showing the SUBJECT across all Life_Phases.

Prompt structure:
```
Character evolution design sheet, flat stickman illustration style,
clean white background. [N] stages of one character aging, left to right.

Each figure: oversized round white circle head with [FACE from phase traits],
body drawn with thin black lines, clothing as simple flat colored shapes.

Stage 1 — [Phase] (age [X]): [subject_phase_traits for this phase]
Stage 2 — [Phase] (age [Y]): [subject_phase_traits for this phase]
...

White background. Professional character sheet. Flat illustration.
KEY identifying features: [list top 3 visual anchors from registry]
```

**CRITICAL:** Face description, hair, clothing, accessories must ALL come from
the researched registry (Step 3b-VERIFY in episode_brief workflow).
Do NOT guess or improvise visual traits.

---

## STEP 4: Generate Supporting Characters Sheet

> Only generate characters marked ASSET_MISS. For ASSET_HIT, embed existing image.

For REAL_PERSON characters needing generation:
```
Character lineup design sheet, flat stickman illustration style.

Figure [N] — [CHAR_ID]:
  [Visual_Summary from registry]
  [Face from registry — dot eyes + mouth with specific expression]

ANONYMOUS_GROUP characters (if shown):
  Circle head COMPLETELY BLANK — NO eyes, NO mouth. FACELESS.
```

---

## STEP 5: Generate Key Scene Samples

Generate **1-2 sample scene images** using the most visually representative strips.

Selection priority:
1. Scene with SUBJECT + supporting REAL_PERSON character together
2. First NARRATIVE_SCENE in CRISIS or PRESENT phase
3. EMOTIONAL_CLOSEUP with signature motifs visible

Scene prompt must use actual prompt formula from image prompt workflow (Step 4c)
with correct CHARACTER BLOCK from researched registry.

---

## STEP 6: Create Review Artifact

Create markdown artifact `character_review_{EP}.md` containing:

1. **SUBJECT Evolution Image** — generated (Step 3) or loaded from assets
2. **Trait Matrix Table** — Phase → Hair / Clothing / Face / Key Anchors
3. **Supporting Characters Image** — generated (Step 4) or loaded from assets
4. **Scene Samples** — in carousel format
5. **Face Rule Summary** — which characters have faces, which are FACELESS
6. **Review Checklist:**
   - [ ] Visual traits match real person's appearance?
   - [ ] Face expressions match real person's demeanor?
   - [ ] Accessories/clothing accurate (no guessing)?
   - [ ] ANONYMOUS_GROUP characters properly FACELESS?
   - [ ] Signature motifs visible at correct phases?

---

## STEP 7: HALT — Wait for User Approval

```yaml
gate_type: BLOCKING
action: HALT_AND_REQUEST_REVIEW
message: "Character visual review created. Please review and approve."
on_approved: PROCEED_TO_STEP_8
on_rejected: REVISE_REGISTRY_AND_REGENERATE_FROM_STEP_3
```

> [!IMPORTANT]
> Do NOT proceed until user explicitly approves.
> If user requests changes → update registry in episode_brief.md → regenerate from Step 3.

---

## STEP 8: Save Approved Assets

After user approval, save character visuals to asset library:

### 8a: Copy Images
```
For each newly generated character image:
  Copy to: pvle/assets/characters/{CHAR_ID}.png
  - SUBJECT evolution: SUBJECT_{EP}.png
  - Supporting characters: {CHAR_ID}.png (reusable across episodes)
```

### 8b: Update character_index.yaml
```yaml
# Append or update entry:
{CHAR_ID}:
  real_person: "{actual person name}"
  visual_anchors:
    hair: "{from registry}"
    face: "{from registry}"
    clothing: "{from registry}"
    accessories: "{from registry}"
    build: "{from registry}"
  asset_file: "{CHAR_ID}.png"
  approved_in: {EP}
  approved_date: {date}
  reused_in: []
```

### 8c: Confirm
```
✅ Character assets saved:
  - [list of saved files]
  - character_index.yaml updated
→ Ready for: /pvle-gen-image-prompts Step 4
```

---

## USER INPUT

> `Episode_ID`: {{Episode_ID}}
