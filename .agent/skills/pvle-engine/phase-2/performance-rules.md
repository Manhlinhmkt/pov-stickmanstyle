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

    7_RHYTHM:
      action: "Check rhythm distribution — add 4-8 surge sentences if missing"
      rule: "Surge (20-30w) must be 4-8% of lines; placement per P10"

    8_MICRO_CRACK:
      action: "Insert 1 micro-crack at peak CRISIS moment"
      rule: "Body betrayal + immediate suppression, per P11"

    9_NEAR_BREAK:
      action: "Insert 1 near-break in late escalation (RESOLUTION/PRESENT)"
      rule: "Bandwidth overload + instant recovery, per P12"
      
    10_CROSS_AUDIT:
      action: "Re-check all patterns from humanize pass"
      action2: "Verify duration still within target"
      
    11_RENUMBER:
      action: "Sequential VO_ID renumber"

  validation:
    - "Re-hook count >= 3"
    - "Spike count >= 1"
    - "Clip moment count >= 1"
    - "Surge sentences >= 4, <= 8"
    - "Micro-crack count = 1 (CRISIS only)"
    - "Near-break count = 1 (RESOLUTION/PRESENT only)"
    - "No pattern > 3 after edits"
    - "Duration within ±15% of target"
```

---

## 11. COMPLIANCE CHECK

```yaml
performance_compliance:
  REHOOK_CHECK:
    scan: "Count re-hook patterns"
    threshold: ">= 3, <= 5"
    
  SPIKE_CHECK:
    scan: "Identify emotional spike blocks"
    threshold: ">= 1"
    test: "Passes relatability test"
    
  CLIP_CHECK:
    scan: "Identify clip-worthy dualities"
    threshold: ">= 1"
    test: "Passes isolation test"
    
  TRANSITION_CHECK:
    scan: "Verify bridges at CRISIS->RESOLUTION"
    threshold: ">= 1 bridge"

  RHYTHM_CHECK:
    scan: "Count lines by word-count range"
    targets:
      short_1_5: "3-6%"
      base_6_14: "65-78%"
      long_15_19: "12-18%"
      surge_20_30: "4-8% (minimum 4 lines)"
    fail_action: "Rewrite medium lines at inflection points as surges"

  MICRO_CRACK_CHECK:
    scan: "Identify body-betrayal suppression lines in CRISIS"
    threshold: "= 1"
    test: "3-beat pattern (body act -> involuntary -> override)"
    integrity: "No verbal acknowledgment, no behavior change after"

  NEAR_BREAK_CHECK:
    scan: "Identify bandwidth-overload recovery lines in RESOLUTION/PRESENT"
    threshold: "= 1"
    test: "4-beat pattern (overwhelm -> blur -> recover -> seal)"
    placement: "Must NOT be in same phase as micro-crack"
    
  PATTERN_RECHECK:
    scan: "All uncertainty patterns still <= 3 each"
    
  DURATION_CHECK:
    scan: "Word count within budget"
```

---

## 12. LAYER P7 — NARRATOR TEXTURE

> **Principle:** Subject = declarative, never hesitates. Narrator = separate voice, has permission to search for words, self-correct, notice irrelevant things. When both layers are equally clean → loss of depth.

### Rules

```yaml
RULE_NARRATOR_SELF_CORRECTION:
  description: "Narrator occasionally finds the right word mid-sentence"
  frequency: "2-3 per episode"
  pattern: "[Statement]. Not [word] — [better word]."
  tone: "quiet, instinctive — low-energy correction"
  placement: "PHASE_EARLY or PHASE_CRISIS (reflective zones)"
  examples_good:
    - '"Not proud exactly. Not that. Something quieter."'
    - '"You leave. Not leave — you just stop going back."'
  examples_bad:
    - '"Not exactly confidence, but rather a form of heightened awareness."'
    - '"Perhaps it was more of a strategic repositioning."'
  avoid:
    - analytical phrasing
    - "because", "which means", "in other words"
    - narrator explaining WHY they're correcting

RULE_USELESS_MOMENT:
  description: "1-2 sensory details that serve zero narrative purpose"
  frequency: "1-2 per episode"
  test: "Remove it — does the story change? If NO → keep it"
  placement: "Before or during high-stakes moments (cognitive load zones)"
  must_be:
    - sensory OR trivial observation
    - noticed during stress/cognitive load
  must_not_be:
    - metaphorical
    - symbolic
    - explanatory
    - poetic
  hidden_function: "Reveals psychological state indirectly"
  examples_good:
    - '"The coffee on your desk went cold two hours ago. You didn''t notice."'
    - '"One of them has a pen that clicks. He clicks it seven times before he stops."'
    - '"The glass has fingerprints on it. You notice that."'
  examples_bad:
    - '"The glass looks dirty. Like everything is falling apart."'
    - '"The light flickers — as if the building knows."'

RULE_MOTIF_VARY:
  description: "Recurring motif must vary syntactic structure"
  check: "Same motif phrase never appears in identical sentence position 3x in a row"
  fix: "Move motif to end, fragment it, or embed in different clause"
  examples:
    before:
      - '"The name is still growing."'
      - '"The name is still the name."'
      - '"The name is still there."'
    after:
      - '"The name is still growing."'
      - '"Still the name. That''s all you need it to do."'
      - '"It holds. The name."'

RULE_COGNITIVE_FRICTION:
  description: "1-2 sentences that force viewer to process rather than absorb"
  frequency: "1-2 per episode (in addition to existing chiasmus)"
  must: "reflect real contradiction in the narrative"
  avoid:
    - perfect symmetry (= feels manufactured)
    - quote-like structure (= feels written for Instagram)
    - slogan-ready phrasing
  examples_good:
    - '"On paper, it all works. You keep looking at the paper."'
    - '"You move forward. Not because it works. Because stopping doesn''t."'
  examples_bad:
    - '"You don''t control the name. The name controls you."'
    - '"Success is the enemy. Failure is the teacher."'

RULE_CLIP_GROUNDING:
  description: "Clip-worthy dualities must be anchored in scene context"
  must_be: "tied to what''s happening in the narrative at that moment"
  must_not_be: "standalone philosophy that could appear anywhere"
  examples_good:
    - '"You don''t protect the buildings. You protect the name." (during bankruptcy negotiation)'
  examples_bad:
    - '"Names outlive men." (generic, unanchored)'

RULE_ELLIPSIS_CONTROL:
  max_per_episode: 1
  placement: "ONLY at narrator self-correction moment"
  forbidden:
    - inside WEIGHT_LINE or TEXT_OVERLAY
    - at sentence end as trailing thought
    - as substitute for Pause_After
```

---

## 13. LAYER P8 — RHYTHM & TENSION

> **Principle:** Uniform rhythm → listener autopilot → retention drop. Break rhythm with sentence length variation and uneven cognitive load. Emotional tension requires physical/sensory foreboding, not logical analysis.

### Rules

```yaml
RULE_SENTENCE_RHYTHM_BREAK:
  description: "Break sentence length uniformity in mid-section"
  minimum: "3 sentences >20 words per episode"
  placement: "PHASE_CONFLICT and PHASE_RESOLUTION (mid-sections)"
  must_have:
    - clause variation (parenthetical, em-dash insertion, triple-clause)
    - delayed meaning (payoff arrives at END of sentence)
  must_not_be:
    - simple compound (A and B and C)
    - linear narrative extension (just adding more words)
  test: "Does the listener need to HOLD information before understanding?"
  examples_good:
    - '"For a long time — longer than either of you will admit later — this is what the team looks like."'
    - '"Forward is the only direction — not because it works, but because you''ve never learned what standing still looks like."'
  examples_bad:
    - '"You went to the building and looked at the numbers and then went home."'

RULE_EMOTIONAL_SPIKE:
  description: "Physical foreboding signal before each CRISIS phase"
  frequency: "1 per episode"
  placement: "Last 3 lines before CRISIS phase begins"
  must_be:
    - physical/sensory (body sensation the character notices)
    - unnamed (character does NOT label the emotion)
    - temporally confused ("not sure when that started")
  must_not_be:
    - logic-based analysis ("Something didn't add up")
    - named emotion ("You felt afraid")
    - explicit foreshadowing ("Something bad was about to happen")
  principle: "Body knows before mind"
  examples_good:
    - '"Your jaw is tight — you''re not sure when that started."'
    - '"Your shoulders are up near your ears. You lower them. They go back up."'
  examples_bad:
    - '"A feeling of dread washed over you."'
    - '"You sensed trouble on the horizon."'

RULE_INFORMATION_DENSITY:
  description: "Long sentences must carry uneven cognitive load, not uniform extension"
  root_cause: "Sentence length alone doesn't fix rhythm — information density distribution does"
  must_have:
    - clause that delays meaning revelation
    - OR parenthetical that adds subtext
    - OR triple-clause that creates rhythmic pattern break
  examples:
    linear_bad: '"Your father always left early in the morning and came back late with blueprints and numbers."'
    layered_good: '"Your father comes back with something rolled under his arm — not blueprints this time, not numbers, but a photograph of a building that doesn''t have his name on it yet."'

RULE_AMBIENT_DREAD:
  description: "Tension between cognitive friction (logic) and emotional spike (body)"
  taxonomy:
    cognitive_friction: "Forces processing — logic-based"
    ambient_dread: "Creates unease — logic + slight emotion"
    emotional_spike: "Physical foreboding — body-based"
  usage_per_episode:
    cognitive_friction: "1-2 (placed in CONFLICT)"
    ambient_dread: "1 (transitional, CONFLICT→CRISIS)"
    emotional_spike: "1 (last lines before CRISIS)"
  examples:
    cognitive_friction: '"On paper, it all works. You keep looking at the paper."'
    ambient_dread: '"Something in them isn''t wrong yet. That''s what bothers you."'
    emotional_spike: '"Your jaw is tight — you''re not sure when that started."'
```

---

## 14. LAYER P9 — PRODUCTION DISCIPLINE

> **Principle:** Rules for HOW to edit, not WHAT to write. Learned from multi-pass optimization of PV_0002 (5 debate rounds, 4 passes).

### Rules

```yaml
RULE_WEIGHT_LINE_PATTERN_BREAK:
  description: "Anchor lines must BREAK the motif's syntactic pattern, not maintain it"
  rationale: "Viewer doesn't see VO_Type metadata — brain only sees word pattern repetition"
  risk: "If NARRATION lines before WEIGHT_LINE use same structure → anchor loses punch"
  must: "Use same motif word/concept but different sentence structure at anchor point"
  examples:
    weak: '"The name is still there. You make sure of it." (same "The name is still..." pattern)'
    strong: '"It never left. The name." (breaks prediction, motif at END not START)'

RULE_REFRAME_OVER_INSERT:
  description: "When script is mature (≥1 pass), prefer rewriting existing lines over inserting new ones"
  rationale: "Insertion inflates duration and risks pacing bloat; reframe preserves structure while adding depth"
  apply_when: "Script has already been through expansion or performance pass"
  technique: "Take existing flat/linear line → add delayed meaning, physical detail, or subtext"
  principle: '"Almost said — but not fully said"'
  examples:
    insert_wrong: "Adding a new line for tension when you could reframe an existing observation"
    reframe_right: '"You look at the numbers" → "You look at the numbers. Something in them isn''t wrong yet."'

RULE_PASS_ORDERING:
  description: "Optimization passes must follow this sequence"
  sequence:
    pass_1: "Duration expansion (hit target word count/speech time)"
    pass_2: "Narrator texture (self-correction, useless moments, motif vary)"
    pass_3: "Rhythm & tension (sentence length, emotional spike, information density)"
    pass_4: "Reframe polish (WEIGHT_LINE breaks, ambient dread, final grounding)"
  forbidden:
    - "Skipping pass_1 to do texture work (no foundation)"
    - "Doing rhythm pass before texture pass (optimize wrong layer)"
    - "More than 4 passes on same script (diminishing returns)"

RULE_HUMANIZATION_DENSITY:
  description: "Minimum texture point density for human perception"
  targets:
    noticeably_human: "1 texture point per 50 lines (score ~9.0-9.1)"
    consistently_human: "1 texture point per 30 lines (score ~9.3+)"
  texture_points:
    - narrator self-correction
    - useless human moment
    - physical sensation (unnamed)
    - cognitive friction
    - ambient dread
  note: "Micro-actions (tap desk, look up) count as 0.5 texture points — they're common, not unique"

RULE_VERSION_AWARE_EDITING:
  description: "Always verify which version you are editing/evaluating"
  checklist:
    - "Confirm line count matches expected version"
    - "Check if identified issues have already been fixed in current version"
    - "Track delta between versions explicitly"
  violation: "Evaluating pre-pass version as if it's current → wrong optimization direction"
```

---

## 15. LAYER P10 — SENTENCE RHYTHM DISTRIBUTION

> **Principle:** Uniform sentence length (6-14 words) creates "too clean" reading — listeners autopilot. Quantified distribution targets ensure breathing/surge waves are present regardless of character voice.
> **Learned from:** PV_0003 pass — initial draft had 0% surge sentences, felt controlled despite good content.

### Rules

```yaml
RULE_RHYTHM_DISTRIBUTION:
  description: "Quantified sentence length targets for every episode"
  targets:
    short_punch:
      range: "1-5 words"
      target_pct: "3-6%"
      purpose: "Punches, emotional hits, behavioral seals"
      placement: "After WEIGHT_LINEs, after revelations"
    base_rhythm:
      range: "6-14 words"
      target_pct: "65-78%"
      purpose: "Core narrative flow"
      note: "This is the default; no effort needed"
    long_standard:
      range: "15-19 words"
      target_pct: "12-18%"
      purpose: "Context, scene-setting, sensory detail"
    surge:
      range: "20-30 words"
      target_pct: "4-8%"
      purpose: "Breathing waves — forces listener to hold information"
      minimum: "4 per episode"
      maximum: "8 per episode"
  validation:
    check: "Count lines by word_count range after final pass"
    fail_condition: "surge < 4 OR surge > 8"
    fix: "Replace existing medium lines at emotional inflection points with surge rewrites"

RULE_SURGE_PLACEMENT:
  description: "Where surge sentences should appear"
  required_zones:
    - "1 in PHASE_CONFLICT (war/memory/accumulated experience)"
    - "1 in PHASE_CRISIS (leaked information / exposure moments)"
    - "1 in PHASE_RESOLUTION (consequence cascading)"
    - "1 in PHASE_PRESENT (if exists — active situation)"
  forbidden_zones:
    - HOOK (must be punchy, not flowing)
    - CALLBACK_CLOSE (must return to short rhythm)
  technique:
    - "Em-dash insertions (parenthetical clause)"
    - "Triple-clause with delayed payoff"
    - "Conditional/temporal embedding"
    - "NOT simple compound (A and B and C)"
  examples_good:
    - '"Everything you typed — every abbreviation, every typo, every word you thought was contained inside a closed system — is now public record, frozen on a server you don''t control."'
    - '"You know the war now — not from briefing papers or cable news panels, but from the dirt under your fingernails and the sleep you stopped trusting somewhere around month three."'
  examples_bad:
    - '"You went to the building and talked to the people and signed the papers and went home."'

RULE_SURGE_VS_BASE_CONTRAST:
  description: "Surge must be surrounded by short lines for maximum impact"
  pattern: "[base/short] → [SURGE] → [short punch]"
  rationale: "Long sentence after long sentence = no wave effect"
  check: "Surge line must have at least 1 line ≤ 10w within 2 lines before or after"
```

---

## 16. LAYER P11 — MICRO-CRACK ARCHITECTURE

> **Principle:** Characters with "no doubt, ever" are compelling but psychologically flat unless the conviction is shown to be ACTIVE (requires suppression) rather than PASSIVE (nothing to suppress). A micro-crack is NOT doubt — it's a body betrayal that the character immediately overrides.
> **Learned from:** PV_0003 — 51-50 vote moment needed visceral stakes beyond plot.

### Rules

```yaml
RULE_MICRO_CRACK_DEFINITION:
  description: "Brief involuntary response that character's will suppresses"
  what_it_is:
    - body doing something the mind hasn't authorized
    - sensory system revealing stress the persona hides
    - involuntary physical response immediately corrected
  what_it_is_NOT:
    - doubt (character questioning their beliefs)
    - weakness (character unable to cope)
    - internal monologue about uncertainty
    - narrator analyzing the crack

RULE_MICRO_CRACK_FREQUENCY:
  description: "1 per episode — never more"
  rationale: "Multiple cracks = character seems fragile; 1 crack = character seems human"
  mandatory: true
  minimum: 1
  maximum: 1

RULE_MICRO_CRACK_PLACEMENT:
  description: "At the single highest-stakes moment in the episode"
  required: "Inside PHASE_CRISIS — at the peak decision/outcome moment"
  forbidden:
    - HOOK (character not yet established)
    - PHASE_EARLY (stakes too low)
    - CALLBACK_CLOSE (resolution territory)
  ideal: "The 2-3 lines BEFORE or DURING the pivotal moment"

RULE_MICRO_CRACK_STRUCTURE:
  description: "3-beat suppression arc within 1-2 lines"
  pattern:
    beat_1: "Body acts ([hand/jaw/breath] does something)"
    beat_2: "Involuntary state (tremble/tighten/stutter)"
    beat_3: "Override (closes/sets/steadies — immediate)"
  seal: "Nobody sees it. / You don't mention it."
  total_duration: "≤ 0.5 seconds of narrative time"
  examples_good:
    - '"Your hand moves toward the armrest. For half a second your fingers don''t grip — they tremble. Then they close. Hard. Nobody sees it."'
    - '"Your breath catches — just once, in the middle of a sentence — and you keep talking. Nobody noticed. You''re almost sure."'
    - '"Something happens in your chest. Not pain. Not panic. Just a skip. And then it''s gone."'
  examples_bad:
    - '"You wonder if you''re really ready for this." (= doubt, not body)'
    - '"Your hands shake as you sign the document." (= sustained weakness, not momentary)'
    - '"For a moment, you question everything." (= internal monologue)'

RULE_MICRO_CRACK_CHARACTER_INTEGRITY:
  description: "Crack must NOT change character identity"
  check:
    - "Does character verbally acknowledge the crack? → FAIL"
    - "Does crack last more than 1 second narrative time? → FAIL"
    - "Does narrator analyze WHY the crack happened? → FAIL"
    - "Does character change behavior after crack? → FAIL"
  principle: "The crack EXISTS but changes NOTHING — that's what makes it powerful"
```

---

## 17. LAYER P12 — ESCALATION NON-LINEARITY

> **Principle:** Linear escalation (bad → worse → worst) creates predictable energy. Viewers disengage when they can predict the next beat. One "near-break" moment where the character's control field ALMOST fails — not from weakness, but from bandwidth overload — adds unpredictability.
> **Learned from:** PV_0003 — scandal → leak → war → fire generals escalated uniformly. Added system-overload blink to break pattern.

### Rules

```yaml
RULE_NEAR_BREAK_DEFINITION:
  description: "One moment where system capacity is exceeded briefly"
  what_it_is:
    - information overload (too many inputs at once)
    - sensory saturation (everything blurs)
    - bandwidth exceeded (thread lost, recovered)
  what_it_is_NOT:
    - emotional breakdown
    - loss of composure
    - character admitting failure
    - dramatic collapse

RULE_NEAR_BREAK_FREQUENCY:
  description: "1 per episode — in the late escalation section"
  minimum: 1
  maximum: 1
  placement: "PHASE_RESOLUTION or PHASE_PRESENT (during peak operational complexity)"
  forbidden:
    - PHASE_CRISIS (reserved for micro-crack)
    - CALLBACK_CLOSE (too late)

RULE_NEAR_BREAK_STRUCTURE:
  description: "4-beat overload-recovery pattern"
  pattern:
    beat_1: "Environment overwhelms (multiple simultaneous inputs)"
    beat_2: "Loss of thread (blur/fade/static)"
    beat_3: "Recovery (blink/breath/snap back)"
    beat_4: "Seal (doesn't mention it / keeps going)"
  duration: "1 line, 20-30 words"
  recovery_speed: "Instant — no lingering"
  examples_good:
    - '"For one moment — screens flashing, phones buzzing, three generals talking at once — you lose the thread. All of it blurs. Then you blink, and it''s back. You don''t mention it."'
    - '"For a second the numbers on the screen stop making sense — the columns blur, the totals swim — and then you refocus, and they''re just numbers again."'
  examples_bad:
    - '"You feel overwhelmed by the situation." (= named emotion)'
    - '"Everything is falling apart around you." (= dramatic collapse)'
    - '"You take a deep breath and try to center yourself." (= coping narrative)'

RULE_NEAR_BREAK_VS_MICRO_CRACK:
  description: "These are different tools — never confuse them"
  comparison:
    micro_crack:
      location: PHASE_CRISIS
      trigger: single pivotal moment
      mechanism: body betrayal
      target: character's physical control
      suppression: muscular (grip/set/close)
    near_break:
      location: PHASE_RESOLUTION/PRESENT
      trigger: accumulated complexity
      mechanism: sensory overload
      target: character's cognitive bandwidth
      suppression: perceptual (blink/refocus/snap)
  forbidden: "Both in same phase — they serve different escalation zones"
```

---

## 18. ANTI-PATTERNS (ABSOLUTE PROHIBITION)

```yaml
FORBIDDEN:
  # Content anti-patterns
  - Clickbait re-hooks: Making promises the script doesn't deliver
  - Forced spikes: Inserting emotion that doesn't fit the arc
  - Over-clipping: More than 2 clip moments = manufactured feel
  - Breaking humanize: Performance edits must not create new AI patterns
  - Double WEIGHT_LINE stacking (except clip duality)
  - Re-hooking inside CRISIS (already at peak — let it breathe)
  - Adding re-hooks that explain what's coming next (="narrator awareness")
  - Transition bridges longer than 2 lines (must be short punch)

  # Narrator anti-patterns (from PV_0002 debate)
  - Narrator matching subject tone exactly (both clean = flat)
  - Useless moments that are secretly metaphorical ("Like everything is falling apart")
  - Self-correction that sounds analytical ("Not exactly X, but rather Y")
  - Named emotions in 2nd-person declarative characters ("You felt scared")
  - Motif appearing in identical sentence position 3+ times consecutively
  - Standalone philosophical clip lines not grounded in scene context

  # Rhythm anti-patterns (from PV_0003 audit)
  - "Too clean" rhythm: >80% of lines in 6-14 word range
  - Zero surge sentences (20+ words) in episode
  - Surge sentences placed back-to-back (no contrast effect)
  - Surge that is simple compound ("A and B and C") instead of layered
  - Making sentences longer by adding words without adding cognitive load

  # Depth anti-patterns (from PV_0003 audit)
  - Micro-crack that is verbal doubt ("You wonder if...")
  - Micro-crack lasting more than 0.5s narrative time
  - Multiple micro-cracks per episode (= character seems fragile)
  - Near-break that is emotional breakdown instead of bandwidth overload
  - Near-break and micro-crack in same phase
  - Character acknowledging either crack or near-break aloud
  - Narrator analyzing WHY the crack/break happened

  # Escalation anti-patterns (from PV_0003 audit)
  - Perfectly linear escalation (each beat worse than last, no variation)
  - Control field never challenged (character seems omnipotent)
  - Resolution that feels "stable" when story is unresolved

  # Production anti-patterns
  - Evaluating pre-pass version as current (version mismatch)
  - More than 4 optimization passes on same script (diminishing returns)
  - Inserting new lines when reframing existing lines would work
  - Making sentences longer without adding cognitive load (linear extension)
  - Perfect symmetry in friction lines ("X is Y. Y is X." = AI signature)
```

