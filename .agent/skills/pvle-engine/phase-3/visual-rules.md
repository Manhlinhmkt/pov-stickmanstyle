# VISUAL RULES — Phase 3

> **Load:** /pvle-gen-image-prompts, /pvle-gen-video-prompts  
> **Contains:** Stickman system + 6 scene types + prompt formulas + video motion rules

---

## 1. STICKMAN CHARACTER SYSTEM

### Style Lock (All Prompts)
```
STYLE_LOCK: "Simple stickman character with oversized round white circle head.
Body drawn with thin black lines.
Clothing as simple flat-colored shapes (no detail, no folds, no shading).
Character is deliberately simple — contrast against highly detailed,
semi-realistic painted background environment."
```

> **Note:** Face description (eyes, mouth) is NOT in STYLE_LOCK.
> Face comes from CHARACTER REGISTRY per character:
> - REAL_PERSON: "dot eyes + simple mouth" with expression matched to real person
> - ANONYMOUS_GROUP: "blank white circle head, no eyes, no mouth" (FACELESS)

### Character Visual Injection
```yaml
source: "character_anchors from WORLD_*.yaml"
flow:
  1. Load character_anchors → extract SUBJECT visual_traits_by_phase
  2. Map strip's Life_Phase → age phase (CHILD_0_6, CHILD_7_12, TEEN_13_17, ADULT_18_PLUS)
  3. Inject: height, hair, clothing, distinguishing traits into prompt
  4. For supporting characters: check appears_in_phases → inject if present

phase_to_age_mapping:
  HOOK:             "use episode-specific age (often CHILD_0_6)"
  PHASE_EARLY:      "CHILD_0_6 → CHILD_7_12 (evolves within phase)"
  PHASE_CONFLICT:   "CHILD_7_12 → TEEN_13_17"
  PHASE_CRISIS:     "TEEN_13_17 → ADULT_18_PLUS"
  PHASE_RESOLUTION: "ADULT_18_PLUS"
  PHASE_PRESENT:    "ADULT_18_PLUS"
  CALLBACK_CLOSE:   "ADULT_18_PLUS"

rule: "Character traits MUST match age phase — child stickman in early phases, tall adult in later"
rule: "SUBJECT always has the most visual detail among all characters"
rule: "Supporting characters have LESS detail than SUBJECT — no individual hair unless specified in anchor"
```

### Character Prompt Block Format
```
SUBJECT (REAL_PERSON): {height}. {hair}. {clothing}. {face — dot eyes + mouth from registry}. {distinguishing}.
SUPPORT — REAL_PERSON: {visual_summary}. {face — dot eyes + mouth from registry}.
SUPPORT — ANONYMOUS_GROUP: {visual_summary}. FACELESS blank white circle head, no eyes, no mouth.
BACKGROUND FIGURES: {generic stickmen, minimal, smaller than subject}. FACELESS.
```

### Supporting Character Rules
```yaml
rule_hierarchy: "SUBJECT > REAL_PERSON support > ANONYMOUS_GROUP support > crowd"
rule_detail: "Each tier has less visual detail than the one above"
rule_veil: "NEVER use real names in prompts — use role descriptors only"
rule_face:
  REAL_PERSON: "dot eyes + simple mouth — expression matched to real individual"
  ANONYMOUS_GROUP: "FACELESS (blank white circle head, no eyes, no mouth)"
rule_asset: "Check pvle/assets/characters/character_index.yaml for approved visual anchors"

RULE_FACE_INJECTION_MANDATORY:
  scope: "EVERY prompt where SUBJECT is visible (NARRATIVE_SCENE, EMOTIONAL_CLOSEUP, CONTRAST_SPLIT, TIME_SKIP_SCENE)"
  check: "Face descriptor block from CHARACTER REGISTRY must appear in EVERY subject-visible prompt — not just first per phase"
  injection_pattern: |
    The face block must appear as a SEPARATE sentence cluster after hair/clothing:
    "{hair}. {clothing}. Clean-shaven strong jawline circle head. Small {eye_color} dot eyes. {expression}."
  required_elements:
    face_shape: "clean-shaven strong jawline circle head" (or per-character variant from registry)
    eye_descriptor: "{adjective} {color} dot eyes" — color and adjective from character_index.yaml
    expression: "{personality-matched expression}" from registry (e.g. military-straight, warm stern)
  child_phases:
    face_shape: "round white circle head" (no jawline descriptor in youth)
    eye_descriptor: "small dot eyes" or "small {color} dot eyes"
  persistence_rule: |
    Face block MUST appear in EVERY slate where subject is visible.
    Do NOT assume reader remembers face from previous slate.
    Each prompt is standalone — face descriptor is MANDATORY in each.
  forbidden:
    - Dropping face block after first slate in a phase
    - Using bare "tall stickman" without face descriptors
    - Describing subject body/action without face block
    - Omitting eye color when registry specifies one
  on_violation: ABORT_AND_REWRITE_ALL_PROMPTS_IN_PHASE

RULE_SUPPORTING_CHAR_FACE:
  scope: "EVERY prompt containing supporting characters"
  REAL_PERSON_support:
    check: "Must include face descriptors from character_index.yaml"
    pattern: "{hair}. {eye_descriptor from registry}. {clothing}."
  ANONYMOUS_GROUP:
    check: "Must include explicit FACELESS marker"
    pattern: "(faceless, blank white circle head)"
    forbidden:
      - Omitting "blank white circle head" for anonymous characters
      - Using bare "faceless" without "blank white circle head"
  on_violation: REVISE_PROMPT
```

---

## 2. BACKGROUND STYLE

```
Rich, detailed, architecturally specific environment.
Color-accurate, location-specific. Not muted or abstract.
Matches key_locations from WORLD_*.yaml.
```

---

## 3. NEGATIVE SUFFIX (All Prompts)

```
--no realistic human faces, no complex facial features, no detailed clothing folds,
no body shading on stickman characters, no 3D render on characters, no anime style,
no chibi proportions, no filled body volume, no oversized main character,
no text overlay, no subtitles, no captions, no written words, no readable text in image,
no door signs, no name plates, no labels, no watermarks, no speech bubbles
```

> Note: "no photorealism" removed — background SHOULD be near-photorealistic painted style.
> Negative applies to CHARACTERS only, not backgrounds.
> Text prohibition applies to ENTIRE image — no readable text anywhere.

---

## 4. SCENE TYPES — Formulas

### NARRATIVE_SCENE
```
[STYLE_LOCK] [accessory]. [Action/position of stickman] in [detailed environment 
from world locations]. [Lighting/atmosphere]. Flat illustration, clean lines.
[NEGATIVE_SUFFIX]
```

### TIME_SKIP_SCENE
```
[STYLE_LOCK] [Two-panel layout. Clean vertical dividing line.]
Left panel: "[AGE X]" label top. [Younger stickman proportions] in [environment].
Right panel: "[AGE Y]" label top. [Older stickman proportions] in [environment].
Minimal flat color palette. [NEGATIVE_SUFFIX]
```

### POV_SHOT
```
[STYLE_LOCK — reference only] First-person view perspective.
Two simple flat stickman hands visible at bottom left and right frame corners.
[Detailed environment seen from eye level]: [specific location description].
Photorealistic background depth, stickman hands remain flat illustration.
[NEGATIVE_SUFFIX]
```

### EMOTIONAL_CLOSEUP
```
[STYLE_LOCK] [accessory]. [Specific posture communicating emotion — hunched/upright/
still]. [Minimal environment — fades to [color tint] at edges]. 
Single subject only, centered. [NEGATIVE_SUFFIX]
```

### TEXT_OVERLAY
```
Typography-only composition. [Dark background color]. 
Large centered bold text: "[EXACT LINE from VO_EN]".
[Optional second line in smaller text].
Minimal — no textures, no decoration. [Optional: tiny stickman silhouette bottom-right].
[NEGATIVE_SUFFIX]
```

### CONTRAST_SPLIT
```
[STYLE_LOCK] [accessory]. Vertical split composition. Clean dividing line center.
Left side — "YOU:": [Stickman in extraordinary environment, specific].
Right side — "OTHERS:": [Same stickman proportions in ordinary equivalent environment].
Equal sizing both sides. Flat color palette. [NEGATIVE_SUFFIX]
```

---

## 5. EMOTION → COLOR TINT (EMOTIONAL_CLOSEUP only)

```yaml
LONGING / TENSION:    "cool blue wash fading at edges"
DREAD:                "desaturated cold grey vignette at edges"
BITTERSWEET:          "warm amber glow at edges"
PRIDE / CLARITY:      "soft gold light from upper right"
WONDER:               "neutral bright — no tint"
DEEP_CONNECTION:      "soft warm white — edges slightly blurred"
```

---

## 6. SCENE TYPE → PHASE MAPPING

```yaml
HOOK:             [POV_SHOT, TEXT_OVERLAY, NARRATIVE_SCENE]
PHASE_EARLY:      [NARRATIVE_SCENE, TIME_SKIP_SCENE, CONTRAST_SPLIT]
PHASE_CONFLICT:   [NARRATIVE_SCENE, EMOTIONAL_CLOSEUP, CONTRAST_SPLIT]
PHASE_CRISIS:     [EMOTIONAL_CLOSEUP, POV_SHOT]
PHASE_RESOLUTION: [TIME_SKIP_SCENE, NARRATIVE_SCENE, EMOTIONAL_CLOSEUP]
CALLBACK_CLOSE:   [NARRATIVE_SCENE, TEXT_OVERLAY]
```

---

## 7. VISUAL VALIDATION RULES

```yaml
RULE_PROMPT_COMPONENTS:
  required_in_every_image_prompt:
    - STYLE_LOCK prefix
    - NEGATIVE_SUFFIX (full version including text prohibition)
    - Specific background (not generic)
  forbidden:
    - Generic backgrounds ("a room", "outside", "somewhere")
    - Realistic face descriptions
    - Photorealism keywords
  on_violation: REVISE_PROMPT

RULE_NO_VO_TEXT_IN_PROMPT:
  check: "Image prompt must contain ZERO verbatim sentences from VO_EN"
  rationale: "Image generators interpret verbatim VO text as subtitle/caption instructions"
  forbidden:
    - Copying VO_EN lines directly into prompt description
    - Including full VO sentences as 'context lines'
    - Quoting narrative phrases inside scene description block
  allowed:
    - Visual paraphrase of VO content (describe WHAT IS SEEN, not what is said)
    - Short location/action refs: 'stickman at school desk' not 'you sit at your desk'
  on_violation: REWRITE_PROMPT_AS_VISUAL_DESCRIPTION_ONLY

RULE_ACCESSORY_CONSISTENCY:
  check: "Same accessory description word-for-word in all prompts of same episode"
  forbidden: "Changing accessory mid-episode without explicit world change"
  on_violation: STANDARDIZE_TO_WORLD_YAML_accessory_tags

RULE_VIDEO_PARITY:
  check: "Every Slate_ID in image_prompts.csv has matching Clip_ID in video_prompts.csv"
  exception: "TEXT_OVERLAY may use STATIC camera only"
  on_violation: ADD_MISSING_VIDEO_PROMPT

RULE_SCENE_TYPE_DISTRIBUTION:
  HOOK: "Must start with POV_SHOT or TEXT_OVERLAY — not NARRATIVE_SCENE"
  PHASE_CRISIS: "Must include at least 1 EMOTIONAL_CLOSEUP"
  CALLBACK_CLOSE: "Must mirror HOOK scene type (if HOOK was POV_SHOT → CALLBACK is NARRATIVE_SCENE with same environment)"
  on_violation: ADJUST_SCENE_TYPE
```

---

## 8. VIDEO MOTION RULES (Veo)

```yaml
SLOW_ZOOM_IN:     "subject standing still at frame center"
SLOW_ZOOM_OUT:    "reveals wider environment — contrast effect"
SLOW_PAN_LEFT:    "environment scan — subject stationary or walking"
SLOW_PAN_RIGHT:   "same as pan_left"
STATIC:           "no camera movement — for TEXT_OVERLAY and WEIGHT moments"
PUSH_IN:          "slow dolly toward subject — emotional intensity moments"
PULL_OUT:         "isolation effect — subject getting smaller — CRISIS beats"

scene_type_to_camera:
  NARRATIVE_SCENE:    SLOW_ZOOM_IN or SLOW_PAN
  TIME_SKIP_SCENE:    SLOW_ZOOM_OUT (reveal both panels)
  POV_SHOT:           PUSH_IN (enhance immersion)
  EMOTIONAL_CLOSEUP:  PUSH_IN or STATIC
  TEXT_OVERLAY:       STATIC only
  CONTRAST_SPLIT:     SLOW_PAN_RIGHT (sweep left to right)

duration_calc: "Clip_Duration_Sec = Beat_Duration_Sec from l2_breakdown_table.csv"
```

---

## 9. VIDEO PROMPT FORMULA

```
[Still image description — 1 sentence]. [Camera_Movement] at [speed: slow/gentle].
Stickman [movement note: remains still / walks slowly / looks up].
Minimalist stickman animation style. Duration: [X] seconds.
--no fast cuts, no realistic faces, no camera shake, no rapid movement
```
