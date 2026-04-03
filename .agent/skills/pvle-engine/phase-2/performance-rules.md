# PERFORMANCE RULES — Phase 2 Post-Processing

> **Load:** After humanize pass completes  
> **Purpose:** Optimize VO script for viral potential, retention, and shareability  
> **Output:** Applied directly to `vo_script_table.csv`

---

## 0. CORE PHILOSOPHY

```
Good storytelling ≠ good performance.
A script can be beautiful and still lose viewers at minute 3.

GOAL: Every 2 minutes, the viewer has a reason to stay.
Every phase has a moment worth sharing.

Retention = architecture.
Virality = moments.
```

---

## 1. LAYER SYSTEM

Apply after humanize pass, in this order:

```yaml
LAYER_P1_REHOOK:     # Re-engagement points at retention dips
LAYER_P2_SPIKE:      # Emotional high-impact moments
LAYER_P3_CLIP:       # Short-able / shareable standalone moments
LAYER_P4_TRANSITION: # Energy bridges between phases
LAYER_P5_ROUGHEN:    # Break lines that sound "too written"
LAYER_P6_PATTERN:    # Final pattern audit (cross-check with humanize)
```

---

## 2. LAYER P1 — RE-HOOK MOMENTS

### Rules

```yaml
RULE_REHOOK_FREQUENCY:
  description: "1 re-hook per ~60 lines (every ~3 minutes)"
  minimum: 3 per episode
  maximum: 5 per episode
  
RULE_REHOOK_PLACEMENT:
  description: "Place at predicted retention dip zones"
  dip_zones:
    - Before phase transition (viewer expects change → might leave)
    - Mid-CONFLICT (pattern fatigue zone)
    - Post-CRISIS (energy drop after peak)
  forbidden:
    - Inside HOOK (already hooking)
    - Inside CRISIS peak (already at max engagement)

RULE_REHOOK_STRUCTURE:
  description: "2-line promise-correction pattern"
  pattern:
    line_1: "[Setup — viewer thinks they understand]"
    line_2: "[Correction — they don't]"
  examples:
    - '"You think you understand how this works." / "You don''t."'
    - '"The thing is —" / "Nobody warns you about the quiet parts."'
    - '"And then it''s over." / "Just like that."'
  properties:
    - line_1 = setup (declarative or trailing)
    - line_2 = short punch (≤ 6 words)
    - line_2 Pause_After ≥ 1.5
```

---

## 3. LAYER P2 — EMOTIONAL SPIKE

### Rules

```yaml
RULE_SPIKE_COUNT:
  description: "1-2 emotional spikes per episode"
  placement: "PHASE_CONFLICT or early PHASE_CRISIS"
  forbidden: "HOOK (too early) or CALLBACK (too late)"

RULE_SPIKE_STRUCTURE:
  description: "3-line try-fail-quit pattern"
  pattern:
    line_1: "[Character attempts something vulnerable]"
    line_2: "[It fails — not dramatically, just... doesn't work]"
    line_3: "[Character stops trying — quiet resignation]"
  examples:
    - '"You try to explain it to someone once."'
    - '"It doesn''t come out right."'
    - '"You stop trying after that."'
  properties:
    - Must be universally relatable (not unique to subject)
    - Failure must be mundane, not dramatic
    - Resignation must be behavioral, not analytical
    - line_3 = WEIGHT_LINE, Pause_After ≥ 1.5

RULE_SPIKE_RELATABILITY:
  description: "Spike must trigger 'I've felt that' response"
  test: "Would a viewer with zero context still feel this?"
  good:
    - Trying to explain something you can't articulate
    - Being in a room where everyone knows each other except you
    - Pretending to be okay when you're not sure what you feel
  bad:
    - Specific political situations
    - Wealth-specific problems
    - Niche experiences
```

---

## 4. LAYER P3 — CLIP MOMENT (SHORT-ABLE)

### Rules

```yaml
RULE_CLIP_COUNT:
  description: "1-2 clip moments per episode"
  purpose: "Standalone content for TikTok/Shorts/Reels + thumbnail caption"

RULE_CLIP_STRUCTURE:
  description: "2-line duality — works completely out of context"
  pattern:
    line_1: "[Universal truth A]"
    line_2: "[Contradiction B — same subject]"
  examples:
    - '"Everyone knows your name." / "Nobody actually knows you."'
    - '"The whole world is watching." / "And you haven''t said a single word."'
  properties:
    - Each line ≤ 6 words
    - No context needed to understand
    - Works as thumbnail text overlay
    - line_2 = WEIGHT_LINE, Pause_After ≥ 1.5

RULE_CLIP_TEST:
  description: "Isolation test"
  test_1: "Read only these 2 lines. Does it hit?"
  test_2: "Would someone screenshot this and share it?"
  test_3: "Could this be a video title?"
  pass: "All 3 = yes"

RULE_CLIP_PLACEMENT:
  description: "Place in CONFLICT or early PRESENT"
  reason: "Must be far enough into the story to feel earned"
  forbidden: "HOOK (too obvious) or CALLBACK (too late to share)"
```

---

## 5. LAYER P4 — PHASE TRANSITIONS

### Rules

```yaml
RULE_TRANSITION_BRIDGE:
  description: "No hard cuts between phases"
  problem: "Viewer drops when energy/topic shifts abruptly"
  
  bridge_patterns:
    CRISIS_TO_RESOLUTION:
      pattern: '"And then it''s over." / "Just like that."'
      purpose: "Acknowledge the peak is done — give viewer a landing"
      Pause_After: 2.0
      
    EARLY_TO_CONFLICT:
      pattern: '"[Promise of escalation]" / "[Short denial]"'
      purpose: "Signal that comfort phase is ending"
      
    CONFLICT_TO_CRISIS:
      pattern: "Usually handled by TIME_MARKER — no extra needed"
      
    RESOLUTION_TO_PRESENT:
      pattern: "TIME_MARKER + location shift — no extra needed"

RULE_ENERGY_CONTINUITY:
  description: "Energy must not drop > 2 levels between phases"
  energy_scale:
    HOOK: 8
    EARLY: 5
    CONFLICT: 7
    CRISIS: 10
    RESOLUTION: 4   # ← biggest drop risk
    PRESENT: 6
    CALLBACK: 7
  fix: "If CRISIS(10) → RESOLUTION(4): add bridge to soften drop"
```

---

## 6. LAYER P5 — ROUGHEN CLEAN LINES

### Rules

```yaml
RULE_SPLIT_POLISHED:
  description: "Long, well-crafted lines reduce authenticity"
  threshold: "Any line that sounds 'quotable' → suspect"
  
  technique_FRAGMENT:
    description: "Split into 3 beats"
    before: '"Same city. Same buildings. You''re bigger now though. Not just taller."'
    after:
      - '"Same city. Same buildings."'
      - '"You''re bigger now though."'
      - '"Not just taller."'   # WEIGHT_LINE
    rule: "Last fragment = shortest = most weight"
    
  technique_SEAL:
    description: "Add behavioral closure"
    before: '"Maybe ever."'
    after: '"Maybe ever. You don''t question it."'
    rule: "Seal = stops the thought from continuing"

RULE_ROUGHEN_DENSITY:
  frequency: "2-3 per episode"
  forbidden: "Roughening WEIGHT_LINEs (they're already short)"
```

---

## 7. LAYER P6 — CROSS-AUDIT

### Rules

```yaml
RULE_CROSS_AUDIT_PATTERNS:
  description: "Re-check patterns after performance edits"
  check_list:
    - "Or" pattern: max 3 per episode
    - "You think" pattern: max 3
    - "You don't know" pattern: max 3
    - New re-hooks don't create new repetitive pattern
  
  action: "If any pattern > 3 after performance edits → reduce"

RULE_NO_DOUBLE_WEIGHT:
  description: "Performance edits may add WEIGHT_LINEs"
  check: "No 2 consecutive WEIGHT_LINEs without NARRATION between"
  exception: "Clip moment (2 WEIGHT_LINEs = intentional duality)"

RULE_DURATION_GUARD:
  description: "Performance edits add lines — check duration"
  check: "Total word count still within ±15% of target"
  if_over: "Remove lowest-impact insertion (usually ROUGHEN)"
```

---

## 8. RETENTION MAP TEMPLATE

```yaml
retention_targets:
  HOOK:               95-100%   # Must be near-perfect
  EARLY:              85-90%    # Slight natural drop acceptable
  CONFLICT_start:     88-92%    # Re-hook should lift here
  CONFLICT_mid:       80-85%    # ← Primary dip zone, needs re-hook
  CONFLICT_end:       85-90%    # Spike should lift here
  CRISIS:             95-100%   # Peak engagement
  POST_CRISIS_gap:    75-85%    # ← Biggest risk, needs bridge
  RESOLUTION:         85-90%    # Clip moment lifts here
  PRESENT:            82-88%    # Steady
  CALLBACK:           90-95%    # Ending pull

minimum_overall: 85%
target_overall: 90%+
```

---

## 9. VIRAL CHECKLIST

```yaml
viral_elements:
  hook_strength:
    - High-status opening (wealth, power, fame)
    - Immediate contrast (privilege vs limitation)
    - Hidden tension (visible but unexplained)
    
  shareability:
    - At least 1 clip moment (short-able duality)
    - At least 1 emotional spike (universal relatability)
    - Title-worthy line exists in script
    
  debate_potential:
    - Core concept has 2 valid sides
    - Script doesn't resolve the debate — leaves it open
    - Comments section will argue
    
  rewatch_value:
    - Details that gain meaning on second viewing
    - Foreshadowing that isn't obvious first time
    - Layer count ≥ 3 (surface story + emotional undercurrent + philosophical question)
```

---

## 10. EXECUTION WORKFLOW

```yaml
performance_workflow:
  input: vo_script_table.csv (post-humanize)
  output: vo_script_table.csv (overwritten)

  steps:
    1_SCAN:
      action: "Map retention dip zones by phase"
      output: "List of VO ranges needing intervention"
      
    2_REHOOK:
      action: "Insert 3-5 re-hook moments at dip zones"
      rule: "1 per ~60 lines"
      
    3_SPIKE:
      action: "Insert 1-2 emotional spikes in CONFLICT"
      rule: "Must pass relatability test"
      
    4_CLIP:
      action: "Insert 1-2 clip moments"
      rule: "Must pass isolation test"
      
    5_BRIDGE:
      action: "Add transition bridges where energy drops > 2 levels"
      
    6_ROUGHEN:
      action: "Split 2-3 polished lines into fragments"
      
    7_CROSS_AUDIT:
      action: "Re-check all patterns from humanize pass"
      action2: "Verify duration still within target"
      
    8_RENUMBER:
      action: "Sequential VO_ID renumber"

  validation:
    - "Re-hook count ≥ 3"
    - "Spike count ≥ 1"
    - "Clip moment count ≥ 1"
    - "No pattern > 3 after edits"
    - "Duration within ±15% of target"
```

---

## 11. COMPLIANCE CHECK

```yaml
performance_compliance:
  REHOOK_CHECK:
    scan: "Count re-hook patterns"
    threshold: "≥ 3, ≤ 5"
    
  SPIKE_CHECK:
    scan: "Identify emotional spike blocks"
    threshold: "≥ 1"
    test: "Passes relatability test"
    
  CLIP_CHECK:
    scan: "Identify clip-worthy dualities"
    threshold: "≥ 1"
    test: "Passes isolation test"
    
  TRANSITION_CHECK:
    scan: "Verify bridges at CRISIS→RESOLUTION"
    threshold: "≥ 1 bridge"
    
  PATTERN_RECHECK:
    scan: "All uncertainty patterns still ≤ 3 each"
    
  DURATION_CHECK:
    scan: "Word count within budget"
```

---

## 12. ANTI-PATTERNS (ABSOLUTE PROHIBITION)

```yaml
FORBIDDEN:
  - Clickbait re-hooks: Making promises the script doesn't deliver
  - Forced spikes: Inserting emotion that doesn't fit the arc
  - Over-clipping: More than 2 clip moments = manufactured feel
  - Breaking humanize: Performance edits must not create new AI patterns
  - Double WEIGHT_LINE stacking (except clip duality)
  - Re-hooking inside CRISIS (already at peak — let it breathe)
  - Adding re-hooks that explain what's coming next (="narrator awareness")
  - Transition bridges longer than 2 lines (must be short punch)
```
