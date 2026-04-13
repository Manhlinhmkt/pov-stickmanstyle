# ILLUSTRATION MAPPING RULES — Phase 3

> **Load:** /pvle-gen-image-prompts (before prompt generation)  
> **Purpose:** Group VO lines into illustration strips with optimal pacing  
> **Output:** `illustration_strip_table.csv`

---

## 0. CORE PHILOSOPHY

```
One image = one visual moment.
Not one sentence. Not one beat.
One continuous visual context.

A strip changes when what the viewer SEES changes.
Not when what the narrator SAYS changes.
```

---

## 1. STRIP DURATION TARGETS

```yaml
duration_targets:
  minimum: 4       # seconds — below this feels like a flash
  sweet_spot: 6-10  # ideal for narration pacing
  maximum: 12       # above this = viewer fatigue on single image
  
  calculation: "duration_sec = total_words_en / 130 * 60 + sum(pause_after)"
  
  exceptions:
    TEXT_OVERLAY: 3-6       # text reads fast, short is punchy
    TIME_SKIP_SCENE: 6-8   # needs time to read both panels
    EMOTIONAL_CLOSEUP: 6-10 # lingers for emotional weight
    CONTRAST_SPLIT: 6-8    # needs time to compare both sides
```

### 1b. MANDATORY EXACT DURATION CALCULATION

```yaml
duration_calculation:
  method: EXACT_SUM
  forbidden: ESTIMATION
  
  per_strip:
    step_1: "List all VO_IDs in strip"
    step_2: "Look up Word_Count_EN for each VO_ID from vo_script_table.csv"
    step_3: "Look up Pause_After for each VO_ID from vo_script_table.csv"
    step_4: "duration_sec = sum(word_counts) / 130 * 60 + sum(pauses)"
    step_5: "Round to 1 decimal place"
  
  CRITICAL: |
    Do NOT estimate or guess durations.
    Must SUM actual Word_Count_EN values from the CSV for every VO line in the strip.
    Wrong: "this group covers 5 lines, about 7.5 seconds"
    Right: "words=[5,7,7,6,7]=32, pauses=[0,0,0,0.5,1.5]=2.0, duration=32/130*60+2.0=16.8s"
  
  example:
    strip: "PV_0009_001 covers VO_ID 1-5"
    word_counts: [5, 7, 7, 6, 7]   # looked up from csv
    pauses: [0, 0, 0, 0.5, 1.5]     # looked up from csv
    sum_words: 32
    sum_pauses: 2.0
    duration: "32 / 130 * 60 + 2.0 = 16.8s"
    result: "VIOLATION — exceeds 12s max → must split"
```

---

## 2. SPLIT RULES (create new strip when)

### Priority 1: Phase Boundary (MANDATORY)

```yaml
RULE_PHASE_SPLIT:
  trigger: "Life_Phase value changes between consecutive VO lines"
  action: "ALWAYS start new strip"
  priority: 1
  exception: NONE
  reason: "Phase = major story shift. Visual must change."
```

### Priority 2: Duration Cap

```yaml
RULE_DURATION_SPLIT:
  trigger: "Accumulated strip duration exceeds 12 seconds"
  action: "Split at nearest sentence boundary"
  priority: 2
  prefer: "Split at Beat_ID boundary if within 2 lines of cap"
  reason: "Single image > 12s = static, boring, loses viewer."
```

### Priority 3: Beat + Duration Threshold

```yaml
RULE_BEAT_SPLIT:
  trigger: "Beat_ID changes AND accumulated duration > 8 seconds"
  action: "Split at beat boundary"
  priority: 3
  note: "Short consecutive beats (< 8s combined) may stay together"
  reason: "Beat change often = new visual context."
```

### Priority 4: Visual Context Change

```yaml
RULE_CONTEXT_SPLIT:
  trigger: "Location, time period, or activity changes within same beat"
  action: "Split regardless of duration"
  priority: 4
  detect_keywords:
    location: ["walk into", "step outside", "drive to", "arrive at", "in the"]
    time: ["years later", "next morning", "that night", "the day"]
    activity: ["sit down", "stand up", "pick up", "open", "close"]
  reason: "What viewer sees has changed — need new image."
```

---

## 3. MERGE RULES (keep in same strip when)

```yaml
RULE_CONTINUATION:
  trigger: "Same Beat_ID, same visual context, total < 12s"
  action: "Keep in same strip"
  example: "5 lines about eating lunch in cafeteria = 1 strip"

RULE_MICRO_BEAT_MERGE:
  trigger: "Beat total < 3s (1-2 lines, few words)"
  action: "Merge with adjacent beat IF same visual context"
  examples:
    - "'Nothing.' (1 word) → merge with previous strip"
    - "'You leave it.' (3 words) → merge with previous strip"
    - "'Too long, probably.' + next narration → same strip"
  limit: "Merged strip must still respect 12s cap"

RULE_NARRATION_FLOW:
  trigger: "Consecutive NARRATION lines describing same moment"
  action: "Keep in same strip"
  example: "Lines about brothers eating cereal + talking about traffic = 1 strip"
```

---

## 4. SPECIAL STRIP TYPES

### Weight Line Strips

```yaml
RULE_WEIGHT_LINE_HANDLING:
  high_impact:
    condition: "WEIGHT_LINE with Pause_After ≥ 1.5 AND is clip moment or re-hook"
    action: "Own strip — Scene_Type = TEXT_OVERLAY"
    examples:
      - "You don't."
      - "Nobody actually knows you."
      - "Just like that."
      
  standard:
    condition: "WEIGHT_LINE at end of narrative sequence"
    action: "Attach as last line of previous strip"
    examples:
      - "That part you like." (stays with video game narration)
      - "She chose you over the spotlight." (stays with mother context)
```

### Clip Moment Strips

```yaml
RULE_CLIP_MOMENT:
  trigger: "Performance clip moment (2-line duality)"
  action: "Own strip — Scene_Type = TEXT_OVERLAY"
  duration: "3-5s"
  example:
    strip: "'Everyone knows your name. / Nobody actually knows you.'"
    scene_type: TEXT_OVERLAY
```

### Re-Hook Strips

```yaml
RULE_REHOOK_HANDLING:
  options:
    standalone: "Own strip if visually distinct from surrounding context"
    bridge: "Attach to NEXT strip as opening lines"
  default: "Attach to next strip"
```

---

## 5. SCENE TYPE ASSIGNMENT

### Per-Strip Selection

```yaml
scene_type_logic:
  step_1: "Check if strip is TEXT_OVERLAY candidate"
    condition: "Strip contains only WEIGHT_LINE(s) with ≤ 10 total words"
    action: "Scene_Type = TEXT_OVERLAY"
    
  step_2: "Check phase-based mapping (from visual-rules.md §6)"
    HOOK:             [POV_SHOT, TEXT_OVERLAY, NARRATIVE_SCENE]
    PHASE_EARLY:      [NARRATIVE_SCENE, TIME_SKIP_SCENE, CONTRAST_SPLIT]
    PHASE_CONFLICT:   [NARRATIVE_SCENE, EMOTIONAL_CLOSEUP, CONTRAST_SPLIT]
    PHASE_CRISIS:     [EMOTIONAL_CLOSEUP, POV_SHOT]
    PHASE_RESOLUTION: [TIME_SKIP_SCENE, NARRATIVE_SCENE, EMOTIONAL_CLOSEUP]
    PHASE_PRESENT:    [NARRATIVE_SCENE, EMOTIONAL_CLOSEUP, CONTRAST_SPLIT]
    CALLBACK_CLOSE:   [NARRATIVE_SCENE, TEXT_OVERLAY]
    
  step_3: "Check content cues in VO_EN"
    time_age_reference: "TIME_SKIP_SCENE"
    contrast_others: "CONTRAST_SPLIT"
    emotional_isolation: "EMOTIONAL_CLOSEUP"
    physical_description: "NARRATIVE_SCENE"
    first_person_seeing: "POV_SHOT"
    
  step_4: "Default = NARRATIVE_SCENE"
```

### Distribution Targets

```yaml
scene_type_distribution:
  NARRATIVE_SCENE: 45-55% of strips    # backbone
  EMOTIONAL_CLOSEUP: 10-15%            # emotional beats
  TEXT_OVERLAY: 10-15%                  # weight lines + clip moments
  POV_SHOT: 3-5%                       # immersion (HOOK + CRISIS)
  TIME_SKIP_SCENE: 2-4%                # age transitions
  CONTRAST_SPLIT: 3-5%                 # privilege vs normal
```

---

## 6. STRIP SUMMARY GENERATION

```yaml
RULE_STRIP_SUMMARY:
  description: "1-sentence summary of visual content for image prompt generation"
  source: "VO_EN lines in the strip"
  format: "[Subject action/state] in [location/context]. [Key visual detail]."
  max_words: 25
  
  examples:
    - "Stickman sitting at corner table near window, watching taxis pass. Cafeteria background."
    - "Two panels: age 10 in school uniform, age 13 in dark hoodie. Split layout."
    - "Bold white text on dark background: 'Everyone knows your name.'"
  
  forbidden:
    - Quoting full VO text (except TEXT_OVERLAY)
    - Abstract descriptions ("feeling lost")
    - Multiple locations in one summary
```

---

## 7. OUTPUT SCHEMA

### illustration_strip_table.csv

```csv
Strip_ID,Start_VO_ID,End_VO_ID,VO_Count,Life_Phase,Scene_Type,Duration_Sec,Strip_Summary
```

| Column | Type | Description |
|---|---|---|
| Strip_ID | string | `{EP}_{NNN}` — 3-digit sequential |
| Start_VO_ID | int | First VO line in strip |
| End_VO_ID | int | Last VO line in strip |
| VO_Count | int | Number of VO lines covered |
| Life_Phase | string | Phase of this strip |
| Scene_Type | string | Visual formula to use |
| Duration_Sec | float | Estimated duration (words/130*60 + pauses) |
| Strip_Summary | string | Visual summary for prompt generation |

---

## 8. VALIDATION RULES

```yaml
RULE_STRIP_COVERAGE:
  check: "Every VO_ID from 1 to max is covered by exactly 1 strip"
  forbidden: "Gaps or overlaps in VO_ID ranges"
  on_violation: FIX_RANGES

RULE_STRIP_DURATION:
  check: "All strips 3s ≤ duration ≤ 12s"
  warning: "Strips 12-15s — consider splitting"
  violation: "Strips > 15s — MUST split"
  on_violation: SPLIT_STRIP

RULE_STRIP_PHASE_PURITY:
  check: "Each strip contains VO lines from only 1 Life_Phase"
  on_violation: SPLIT_AT_PHASE_BOUNDARY

RULE_SCENE_TYPE_PRESENT:
  check: "At least 1 EMOTIONAL_CLOSEUP in PHASE_CRISIS"
  check2: "HOOK starts with POV_SHOT or TEXT_OVERLAY"
  check3: "CALLBACK_CLOSE mirrors HOOK scene type"
  on_violation: ADJUST_SCENE_TYPE

RULE_SEQUENTIAL_IDS:
  check: "Strip_IDs sequential, no gaps"
  on_violation: RENUMBER

RULE_DURATION_EXACT_CALC:
  check: "Duration_Sec per strip = exact sum(Word_Count_EN)/130*60 + sum(Pause_After)"
  method: "Sum actual values from vo_script_table.csv — no estimation"
  forbidden: "Approximated or guessed durations"
  on_violation: RECALCULATE_FROM_CSV

RULE_TOTAL_DURATION_CROSSCHECK:
  check: "sum(all strip Duration_Sec) ≈ total_speech_time"
  total_speech_time: "sum(all Word_Count_EN in VO CSV) / 130 * 60 + sum(all Pause_After)"
  tolerance: 5%
  on_violation: ABORT_AND_RECALCULATE
  example:
    total_words_en: 2400
    total_pauses: 85
    total_speech_time: "2400/130*60 + 85 = 1192s ≈ 19.9 min"
    sum_strip_durations_must_be: "within 1132s – 1252s"

RULE_STRIP_COUNT_SANITY:
  check: "strip_count >= total_speech_time / 12"
  rationale: "If max strip duration is 12s, minimum strips = total_time / 12"
  target: "strip_count ≈ total_speech_time / 8 (sweet spot)"
  on_violation: RE_SPLIT_LONGEST_STRIPS
```

---

## 9. EXECUTION WORKFLOW

```yaml
strip_generation:
  input: vo_script_table.csv
  output: illustration_strip_table.csv

  steps:
    0_PRE_CALCULATE:
      action: "Calculate total speech time BEFORE any grouping"
      method: |
        total_words = sum(all Word_Count_EN from vo_script_table.csv)
        total_pauses = sum(all Pause_After from vo_script_table.csv)
        total_speech_time = total_words / 130 * 60 + total_pauses
        min_strips = ceil(total_speech_time / 12)
        target_strips = round(total_speech_time / 8)
        max_strips = floor(total_speech_time / 4)
      output: "Display summary table before proceeding"
      
    1_PARSE:
      action: "Read all VO lines with VO_ID, Beat_ID, Life_Phase, VO_Type, Word_Count_EN, Pause_After"
      
    2_INITIAL_GROUP:
      action: "Group consecutive VO lines by Beat_ID"
      result: "Raw beat groups"
      
    2b_EXACT_DURATION:
      action: "For each beat group, calculate EXACT duration"
      method: "sum(Word_Count_EN) / 130 * 60 + sum(Pause_After)"
      CRITICAL: "Must use actual values from CSV. Estimation FORBIDDEN."
      output: "Each group annotated with exact calculated duration"
      
    3_APPLY_SPLITS:
      action: "Apply split rules in priority order (phase → duration → beat → context)"
      note: "Duration splits now based on EXACT calculated durations from step 2b"
      result: "Refined strip groups — all within 3-12s range"
      
    4_APPLY_MERGES:
      action: "Merge micro-beats (< 3s) with adjacent strips"
      constraint: "Never merge across phases. Never exceed 12s. Recalculate duration after merge."
      
    5_SPECIAL_STRIPS:
      action: "Extract clip moments + high-impact weight lines → standalone strips"
      
    6_ASSIGN_SCENE_TYPE:
      action: "Per strip: determine Scene_Type from phase mapping + content cues"
      
    7_GENERATE_SUMMARIES:
      action: "Write Strip_Summary per strip (max 25 words)"
      
    8_VALIDATE:
      action: "Run all validation rules (coverage, duration range, phase purity, scene types)"
      
    8b_CROSSCHECK:
      action: "Compare sum(all Duration_Sec) vs total_speech_time from step 0"
      tolerance: 5%
      on_fail: "ABORT — strip durations do not match speech time. Recalculate from scratch."
      
    8c_STRIP_COUNT_CHECK:
      action: "Verify strip_count is within [min_strips, max_strips] from step 0"
      on_fail: "WARNING — re-split longest strips or merge shortest ones"
      
    9_OUTPUT:
      action: "Write illustration_strip_table.csv"
```
