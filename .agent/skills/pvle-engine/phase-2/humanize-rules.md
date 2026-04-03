# HUMANIZE RULES — Phase 2 Post-Processing

> **Load:** After /pvle-gen-vo produces vo_script_table.csv  
> **Purpose:** Transform AI narration into human memory narration  
> **Output:** vo_script_humanized.csv (replaces vo_script_table.csv when approved)

---

## 0. CORE PHILOSOPHY

```
AI writes clean. Humans don't.
AI writes with structure. Humans think in fragments.
AI improves clarity. Humans introduce noise.

GOAL: Sound like someone REMEMBERING — not NARRATING.

If it feels slightly unnecessary, slightly unsure,
slightly imperfect → it's working.
```

---

## 1. LAYER SYSTEM

Apply in this exact order. Each layer builds on the previous.

```yaml
LAYER_1_RHYTHM:        # Sentence rhythm variation
LAYER_2_SENSORY:       # Physical/touch/temperature details
LAYER_3_BEHAVIORAL:    # Observable actions, fidgets, micro-movements
LAYER_4_IMPERFECT:     # False starts, interrupted thoughts, logic breaks
LAYER_5_NOISE:         # Meaningless lines, memory glitches, confusion
LAYER_6_CONTRACTION:   # Grammar naturalization
LAYER_7_PATTERN_AUDIT: # De-duplicate AI-detectable patterns
```

---

## 2. LAYER 1 — RHYTHM VARIATION

### Rules

```yaml
RULE_RHYTHM_MIX:
  description: "Vary sentence length within each 5-line block"
  requirement: "At least 2 different lengths per 5 lines"
  forbidden: "5+ consecutive lines of similar word count"

RULE_CRISIS_HEARTBEAT:
  description: "PHASE_CRISIS uses short staccato (2-6 words)"
  pattern: "[Short.] [Short.] [Short.]"
  max_words: 8
  
RULE_PRESENT_IRREGULARITY:
  description: "PHASE_PRESENT alternates between flowing and broken"
  pattern: "[Long thought] → [short fragment] → [medium]"
```

### Examples

```
# BAD (uniform rhythm)
"You walk down the hallway. You open the door. You step inside."

# GOOD (varied rhythm)  
"You walk down the hallway.
The door's already open.
You step inside — it smells like cleaning product. Or maybe paint."
```

---

## 3. LAYER 2 — SENSORY DEPTH

### Rules

```yaml
RULE_SENSORY_DIVERSITY:
  description: "Don't default to visual/audio only"
  required_per_episode:
    touch: 3+        # temperature, texture, pressure
    smell: 1+        # chemical, food, environment
    proprioception: 2+ # body awareness, spatial sense
  forbidden: "All sensory = sight + sound"

RULE_SENSORY_STANDALONE:
  description: "Sensory detail on its own line, no explanation"
  pattern: '"[sensory observation]." — own VO row'
  forbidden: "Embedding sensory into narrative sentence"

RULE_AWKWARD_PHYSICAL:
  description: "Include 1-2 uncomfortable physical moments per episode"
  examples:
    - "The receipt is warm in your hand."
    - "Your fingers feel stiff."
    - "The table's sticky. You don't wipe it."
    - "The air feels thick. Too many people."
```

---

## 4. LAYER 3 — BEHAVIORAL DETAIL

### Rules

```yaml
RULE_SHOW_DONT_TELL:
  description: "Replace mental narration with observable action"
  example:
    bad:  "You feel nervous."
    good: "You adjust your backpack straps. You don't look at it."

RULE_MICRO_FIDGET:
  frequency: "1 per ~30 lines"
  description: "Meaningless physical action, no narrative purpose"
  examples:
    - "You wipe your hands on a napkin. Then again."
    - "You peel the label off a bottle. Halfway. Then stop."
    - "You tap the screen once. Just to see it light up."
    - "You open a message. Don't read it. Close it."
  forbidden: "Explaining WHY the fidget happens"

RULE_SOCIAL_AWKWARD:
  frequency: "1-2 per episode"
  description: "Real, slightly uncomfortable social micro-moments"  
  examples:
    - "Someone says your name wrong. You don't correct them."
    - "You shake someone's hand. They hold it too long."
    - "A kid tries to sit with you once. You don't know if he's being nice or if his parents told him to."
```

---

## 5. LAYER 4 — IMPERFECT THINKING

### Rules

```yaml
RULE_FALSE_START:
  frequency: "2-3 per episode"
  description: "Thought begins, gets cut off, restarts differently"
  pattern: '"You think —" / "No." / "[simpler restatement]"'
  examples:
    - '"You think —" → "No." → "You chose this because you wanted to."'
    - '"Not because you stop liking things. Just —"'
    - '"You almost —" → "Nothing."'

RULE_LOGIC_BREAK:
  frequency: "2-3 per episode"
  description: "Unrelated detail interrupts narrative flow"
  examples:
    - "Your phone is at eleven percent."  # during emotional scene
    - "You buy a lightbulb. That's it."   # after significant moment
    - "Your phone buzzes once. You don't check it."
  rule: "Must feel random. If it feels intentional → too clean."

RULE_OVERLAPPING_THOUGHT:
  frequency: "1-2 per episode"
  description: "Second thought cuts in before first completes"
  pattern: '"[thought A]" → "Or —" → "[unrelated]"'
```

---

## 6. LAYER 5 — NOISE (HUMAN ARTIFACTS)

### Rules

```yaml
RULE_MEANINGLESS_LINE:
  frequency: "1-2 per episode"
  description: "Line with zero narrative value"
  examples:
    - "Nothing."           # after action loop
    - "That's it."         # after significant event
    - "You leave it."      # no context needed
  rule: "Reader should think 'why is this here?' That's the point."

RULE_MEMORY_GLITCH:
  frequency: "1 per ~40 lines (3-5 per episode)"
  description: "Narrator unsure about own memory"
  examples:
    - "You don't remember when that became normal."
    - "Or maybe it was always like that."
    - "You try to remember the first time. You can't."
    - "You don't remember falling asleep."
  forbidden: "Using same phrasing twice"

RULE_MICRO_CONFUSION:
  frequency: "1 per episode"
  description: "Narrator loses thread mid-thought"
  examples:
    - "You forget what you were about to say. It doesn't come back."

RULE_RAW_LINE:
  frequency: "Max 1 per episode"  
  description: "Narrator breaks 4th wall of memory — comments on the process"
  examples:
    - "You don't like thinking about any of this."
  rule: "Extremely rare. High impact. Never more than 1."
```

---

## 7. LAYER 6 — CONTRACTION PASS

### Rules

```yaml
RULE_CONTRACTION_DEFAULT:
  description: "Use contractions by default in narration"
  convert:
    "do not"  → "don't"
    "does not" → "doesn't"
    "did not"  → "didn't"
    "is not"   → "isn't"
    "it is"    → "it's"
    "you are"  → "you're"
    "that is"  → "that's"
    "have not" → "haven't"
    "there is" → "there's"

RULE_FORMAL_EXCEPTIONS:
  description: "Keep formal ONLY for intentional weight"
  keep_formal:
    - WEIGHT_LINE with declarative gravity:
        "You did not choose this family."
        "It is not freedom."
    - AGE_MARKER pattern:
        "You are four."
        "You are ten."
        "You are twenty years old."
    - FINAL_CALLBACK closing weight:
        "And you still have not decided who you are."
  
  test: "If removing contraction adds gravitas → keep formal.
         If it just sounds stiff → convert."
```

---

## 8. LAYER 7 — PATTERN AUDIT

### Rules

```yaml
RULE_MAX_PATTERN_3:
  description: "No single uncertainty phrase > 3 instances per episode"
  patterns_to_track:
    - "You don't know"
    - "You think"
    - "Maybe"
    - "Or —"
    - "You're not sure"
    - "Nothing."
  max_per_pattern: 3
  on_violation: "Replace excess with behavioral equivalent"
  
  replacement_map:
    "You don't know" → "Your shoulders drop a little." | "You just sit there."
    "You think"      → (DELETE if standalone) | "You don't say anything."
    "Maybe"          → "You leave it."
    "You're not sure" → "You look away."

RULE_NO_SYMMETRIC_DOUBT:
  description: "Don't stack uncertainty patterns"
  forbidden:
    - '"You don't know." followed by "Maybe."'
    - '"Or —" followed by "You think."'
  rule: "2+ uncertainty markers within 3 lines = AI pattern"

RULE_BREAK_TRIPLE_SYMMETRY:
  description: "If 3 items listed symmetrically, break the pattern"
  bad:  '"Your clothes. Your face. Even your name."'
  good: '"Your clothes. Your face. Even your name — something about it."'
  rule: "Add trailing fragment OR cut one item"
```

---

## 9. DENSITY CONTROL

```yaml
DENSITY_RULES:
  per_5_lines:
    max_sensory: 1
    max_behavioral: 1
    rule: "No stacking same type consecutively"
    
  per_30_lines:
    memory_glitch: 1
    micro_fidget: 1
    false_start: 1
    rule: "Spread evenly — never cluster"
    
  per_episode:
    logic_breaks: 2-3
    false_starts: 2-3
    meaningless_lines: 1-2
    memory_glitches: 3-5
    micro_fidgets: 3-4
    social_awkward: 1-2
    raw_line: 0-1
    micro_confusion: 1
    
  pacing_guard:
    max_phase_lines: 50  # no single phase exceeds this
    check: "If PRESENT > 50 lines → trim non-essential noise"
```

---

## 10. ENDING RULES

```yaml
RULE_IMPERFECT_ENDING:
  description: "Ending must NOT feel like a neat conclusion"
  forbidden:
    - Perfect 3-beat closure
    - Resolved emotional arc
    - "Beautiful" final line
  required:
    - At least 1 fragment in final 5 lines
    - Slight ambiguity (not poetic ambiguity — cognitive ambiguity)
  
  good_pattern:
    - '"And that's fine."'
    - '"Or it's not."'
    - '"You haven't figured that out yet."'
    # Each on own line. Not combined.
    
RULE_SPLIT_COMPOUND_ENDINGS:
  description: "Split multi-clause endings into separate VO lines"
  bad:  '"And that's fine. Or it's not. You haven't figured that out yet."'
  good: '3 separate VO rows — each lands individually'
```

---

## 11. WEAKENING RULES

```yaml
RULE_WEAKEN_CLEAN_LINES:
  description: "Long, well-written lines must be broken"
  threshold: "Any line that 'sounds good' → suspect"
  
  technique_1_SPLIT:
    bad:  '"You eat and watch them and it's the most normal you've felt in years."'
    good: |
      "You eat and watch them."
      "It feels normal."
      "Or close to it."
      
  technique_2_DOWNGRADE:
    bad:  '"You know what they respond to. Sincerity, mostly."'
    good: |
      "You think you know what they respond to."
      "Sincerity. Probably."
    # "know" → "think you know", "mostly" → "probably"
```

---

## 12. EXECUTION WORKFLOW

```yaml
humanize_workflow:
  input: vo_script_table.csv (from /pvle-gen-vo)
  output: vo_script_humanized.csv → replaces vo_script_table.csv

  steps:
    1_COPY:
      action: "Copy vo_script_table.csv → vo_script_humanized.csv"
      
    2_LAYER_1_RHYTHM:
      action: "Scan for uniform rhythm blocks → vary"
      
    3_LAYER_2_SENSORY:
      action: "Add touch/temperature/space details"
      frequency: "3-5 per episode"
      
    4_LAYER_3_BEHAVIORAL:
      action: "Add fidgets + social awkward"
      frequency: "4-6 per episode"
      
    5_LAYER_4_IMPERFECT:
      action: "Add false starts + logic breaks"
      frequency: "4-6 per episode"
      
    6_LAYER_5_NOISE:
      action: "Add memory glitches + meaningless + confusion + raw"
      frequency: "5-8 per episode"
      
    7_LAYER_6_CONTRACTION:
      action: "Convert formal → contractions (except weight lines)"
      
    8_LAYER_7_PATTERN_AUDIT:
      action: "Count all uncertainty patterns → cap at 3 each"
      action2: "Break symmetry in lists"
      action3: "Weaken clean lines"
      action4: "Split compound endings"
      
    9_DENSITY_CHECK:
      action: "Verify spacing rules per 5/30/episode"
      
    10_RENUMBER:
      action: "Sequential VO_ID renumber"
      
    11_VERIFY:
      action: "Word count + duration estimate + pattern count"

  validation:
    - "No pattern > 3 instances"
    - "Contractions applied (except formal exceptions)"  
    - "At least 1 each: fidget, memory glitch, false start, sensory"
    - "Ending is NOT neat"
    - "Duration within target range"
```

---

## 13. QUALITY SCORE RUBRIC

```yaml
score_rubric:
  9.0_baseline:
    - Structure intact
    - Rhythm varies
    - Behavioral details present
    - Contractions done
    
  9.5_target:
    - All above PLUS
    - Sensory = touch/temperature (not just sight/sound)
    - False starts present
    - Logic breaks present
    - No pattern > 3
    
  9.7_near_human:
    - All above PLUS
    - Memory glitches
    - Micro-fidgets
    - Social awkward moments
    - Clean lines weakened
    - Ending imperfect
    - "Written feel" almost gone
    
  9.8_ceiling:
    - All above PLUS
    - Raw line (1 max)
    - Micro confusion
    - No detectable AI pattern
    - Reads like transcript of someone remembering
```

---

## 14. ANTI-PATTERNS (ABSOLUTE PROHIBITION)

```yaml
FORBIDDEN:
  - Poetic uncertainty: "Perhaps the answer lies in..."
  - Symmetric doubt: "You don't know. / Maybe. / Or —" (3-beat stack)
  - Explained fidgets: "You adjust your collar because you're nervous"
  - Narrator awareness: "Looking back, you realize..."
  - Clean parallel lists: "X. Y. Z." without breaking the third
  - Perfect endings: "And that was enough."
  - AI hedging: "In some ways..." / "Part of you..."
  - Over-introspection: "You wonder if..." (more than 1x per episode)
  - Controlled chaos: Adding imperfections in a detectable pattern
```
