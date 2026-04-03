# IDEATION RULES — Phase 1

> **Load:** /pvle-gen-outline, /pvle-gen-episode-brief, /pvle-extract-anchor  
> **Contains:** Story structures + Phase flow + Beat expansion + Hook library

---

## 1. STRUCTURE DEFINITIONS

### LIFE_PRIVILEGE
```yaml
core_tension: PRIVILEGE_VS_FREEDOM
emotional_arc: WONDER → CONSTRAINT → LONGING → BITTERSWEET
example_topics: ["Son of US President", "Heir to billion-dollar empire", "British royalty"]
```

### LIFE_ADVERSITY
```yaml
core_tension: DUTY_VS_SELF
emotional_arc: TENSION → DREAD → CLARITY → PRIDE
example_topics: ["Child in refugee camp", "Single parent household on minimum wage"]
```

### LIFE_HIDDEN_POWER
```yaml
core_tension: PROTECTION_VS_CONTROL
emotional_arc: WONDER → TENSION → DREAD → CLARITY
example_topics: ["Child of CIA agent", "Witness protection kid", "Secret criminal heir"]
```

### LIFE_IMPOSSIBLE_CHOICE
```yaml
core_tension: DUTY_VS_SELF
emotional_arc: WONDER → TENSION → DREAD → BITTERSWEET
example_topics: ["Last doctor in warzone", "Person who must shut down an AI"]
```

### LIFE_LEGACY
```yaml
core_tension: IDENTITY_VS_LEGACY
emotional_arc: WONDER → LONGING → CLARITY → PRIDE
example_topics: ["Child of Michael Jordan", "Daughter of Einstein", "Son of Einstein"]
```

---

## 2. PHASE FLOW (Universal)

```yaml
HOOK:
  purpose: "Establish extraordinary world in first 30s"
  beat_types: [ESTABLISH, PRIVILEGE/CONSTRAINT]
  target_emotion: WONDER
  typical_beats: 2-3
  scene_types: [NARRATIVE_SCENE, TEXT_OVERLAY, POV_SHOT]

PHASE_EARLY:
  purpose: "Childhood — innocence vs. reality"
  beat_types: [TIME_MARKER, PRIVILEGE, CONSTRAINT, REFLECT]
  target_emotion: WONDER → LONGING
  typical_beats: 3-4
  scene_types: [NARRATIVE_SCENE, TIME_SKIP_SCENE, CONTRAST_SPLIT]

PHASE_CONFLICT:
  purpose: "Adolescence — extraordinary starts to feel like a cage"
  beat_types: [CONFLICT, CONSTRAINT, REFLECT]
  target_emotion: TENSION → LONGING
  typical_beats: 4-5
  scene_types: [NARRATIVE_SCENE, EMOTIONAL_CLOSEUP, CONTRAST_SPLIT]

PHASE_CRISIS:
  purpose: "Point of no return — one event forces a choice"
  beat_types: [CRISIS, CONFLICT]
  target_emotion: DREAD → CLARITY
  typical_beats: 2-3
  scene_types: [NARRATIVE_SCENE, EMOTIONAL_CLOSEUP, POV_SHOT]

PHASE_RESOLUTION:
  purpose: "Acceptance, transformation, or legacy"
  beat_types: [RESOLVE, TIME_MARKER, REFLECT]
  target_emotion: BITTERSWEET → CLARITY → PRIDE
  typical_beats: 2-3
  scene_types: [NARRATIVE_SCENE, TIME_SKIP_SCENE, EMOTIONAL_CLOSEUP]

CALLBACK_CLOSE:
  purpose: "Return to opening — reframed by earned wisdom"
  beat_types: [CALLBACK, CTA]
  target_emotion: DEEP_CONNECTION
  typical_beats: 1-2
  scene_types: [NARRATIVE_SCENE, TEXT_OVERLAY, EMOTIONAL_CLOSEUP]
```

---

## 3. BEAT EXPANSION (4-step pattern)

```yaml
SETUP:    "1 sentence — place viewer in moment"
EVENT:    "2-3 sentences — concrete, sensory, specific"
WEIGHT:   "1-2 sentences — emotional truth beneath event"
ANCHOR:   "1 sentence, 3-8 words — the line viewers remember"
```

### Time Marker Pattern
```yaml
format:       "You are [age]."
pause_after:  1.0
context_shift: "1-2 sentences — what changed at this age"
emotional_note: "1 sentence — how this age feels from inside"
```

---

## 4. EMOTIONAL ARC RULES

```yaml
RULE_EMOTION_PER_PHASE:
  HOOK:              WONDER (required)
  PHASE_EARLY:       WONDER or LONGING
  PHASE_CONFLICT:    TENSION (required)
  PHASE_CRISIS:      DREAD or CLARITY
  PHASE_RESOLUTION:  BITTERSWEET or CLARITY
  CALLBACK_CLOSE:    DEEP_CONNECTION or BITTERSWEET
  on_violation: ADD_MISSING_WEIGHT_LINE

RULE_EARNED_RESOLUTION:
  check: "PHASE_RESOLUTION must echo at least 1 element from PHASE_CRISIS"
  required: "CALLBACK_CLOSE must return to specific image/moment from HOOK"
  forbidden: "Happy ending without link to crisis experienced"
  on_violation: REVISE_RESOLUTION

RULE_NO_EMOTION_SKIP:
  "Progress WONDER → LONGING/TENSION → DREAD → CLARITY/BITTERSWEET"
  "Never jump from WONDER directly to DREAD"
```

---

## 5. DURATION PROFILES

```yaml
STANDARD:
  duration_min: 8-12
  word_count_target: 784-1176  # at 140 WPM × 70% clip time
  typical_beats: 16-22

EXTENDED:
  duration_min: 12-15
  word_count_target: 1176-1470
  typical_beats: 22-28

beat_duration_calc: "Beat_Duration_Sec = (Beat_Word_Count / 140) × 60 × (1/0.7)"
```

---

## 6. HOOK LIBRARY

### HOOK_BORN_DIFFERENT
```yaml
use_for: [LIFE_PRIVILEGE, LIFE_LEGACY, LIFE_HIDDEN_POWER]
pattern: "The moment you are born, [X] is already different."
examples:
  - "The moment you are born, there are men with guns outside the door."
  - "The moment you are born, your name is already in the newspapers."
```

### HOOK_FIRST_REALIZATION
```yaml
use_for: [LIFE_PRIVILEGE, LIFE_ADVERSITY, LIFE_HIDDEN_POWER]
pattern: "There is a moment — usually around [age] — when you understand."
```

### HOOK_CONTRAST_OPEN
```yaml
use_for: [LIFE_PRIVILEGE, LIFE_ADVERSITY, LIFE_LEGACY]
pattern: "Most [children/people] [ordinary thing]. You [extraordinary equivalent]."
```

### HOOK_PRIVILEGE_REVEAL
```yaml
use_for: [LIFE_PRIVILEGE, LIFE_LEGACY]
pattern: "You have [extraordinary thing]. And it costs you [unexpected price]."
```

### HOOK_WEIGHT_STATEMENT
```yaml
use_for: [LIFE_IMPOSSIBLE_CHOICE, LIFE_ADVERSITY, LIFE_HIDDEN_POWER]
pattern: "You never chose [X]. [X] chose you."
```

---

## 7. CALLBACK CLOSE TEMPLATES

```yaml
CALLBACK_RETURN:
  pattern: "Remember [opening moment]? [New understanding.]"
  pause_before: 1.5

CTA_QUIET:
  pattern: "If you've ever wondered what [X] would feel like — now you know."
  note: "Never pushy. Never cheerful."
```

---

## 8. PHASE TRANSITION PHRASES

```yaml
INTO_PHASE_EARLY:       "And so your childhood begins."
INTO_PHASE_CONFLICT:    "But here is where it starts to feel different."
INTO_PHASE_CRISIS:      "And then. The moment comes."
INTO_PHASE_RESOLUTION:  "Years pass. [Age stamp.] And you understand now."
INTO_CALLBACK:          "[Long pause 2.0] — Return to opening."

rule: "Transition phrases always own VO row with Pause_After: 1.5-2.0"
```
