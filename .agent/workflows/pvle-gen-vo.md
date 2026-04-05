---
description: Draft, finalize, humanize, and optimize trilingual VO script (PVLE P2.2 + P2.4 + P2.5 + P2.6)
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-gen-vo

> **Phase:** 2.2 + 2.4 + 2.5 + 2.6 — Scripting (Draft + Final + Humanize + Performance)  
> **Input:** `l2_breakdown_table.csv` + `episode_brief.md`  
> **Output:** `vo_draft_table.csv` + `vo_script_table.csv` (EN + JA + VI, humanized + optimized)

---

## PHASE A: DRAFT (vo_draft_table.csv)

### A1: Read Inputs

Load:
- `l2_breakdown_table.csv` → all beats with Life_Phase, Beat_Type, Mood_Tag, Content_Sketch
- `episode_brief.md` → Stickman_Accessory, Key_Locations, Core_Tension, Episode_Notes, **Identity_Mode**, **Word_Budget** (from speech_time_config)
- `phase-2/scripting-rules.md` → VOICE_POV_DRAMATIST patterns, sentence rules
- `phase-2/scripting-rules.md` → phase-level rhetorical strategies
- `phase-1/ideation-rules.md` → Hook_Type template for this episode

**If Identity_Mode = TRANSPARENT_VEIL:**
- Also load `pvle/worlds/{WORLD_ID}.yaml` → extract:
  - `forbidden_terms` (names, companies, places + replacement phrases)
  - `era_anchors` (inject into TIME_MARKER beats)
  - `unique_circumstance_stack` (inject into PHASE_EARLY + PHASE_CONFLICT beats)
  - `public_perception_markers` (inject into PHASE_CONFLICT beats)
- Store as `veil_config` for use in all subsequent steps

### A2: Draft VO per Beat

For each beat in l2_breakdown_table.csv:

1. Select rhetorical strategy from `phase-2/scripting-rules.md` based on `Beat_Type` + `Life_Phase`
2. Draft `VO_Draft_EN` following VOICE_POV_DRAMATIST rules:
   - Always "you"
   - Max 15 words per sentence
   - TIME_MARKER beats = "You are [age]." pattern
   - WEIGHT_LINE beats = 3-8 word anchor only
   - CONTRAST beats = "While others X, you Y." pattern
3. Calculate `Word_Count`

### A3: Output vo_draft_table.csv

**RULE_SILENT_OUTPUT:** CSV only.

File: `pvle/episodes/{EP}/vo_draft_table.csv`

Columns: `Beat_ID,Life_Phase,Beat_Type,Mood_Tag,Content_Sketch,VO_Draft_EN,Word_Count`

---

## PHASE B: FINAL SCRIPT (vo_script_table.csv)

### B1: Break Draft into Lines

For each beat's `VO_Draft_EN`:
1. Split at natural pause points (sentence boundaries, clause boundaries)
2. Each line = 1 spoken unit
3. TIME_MARKER and WEIGHT_LINE: always own row

### B2: Translate to Japanese (VO_JA)

Apply translation rules from `phase-2/scripting-rules.md §6 VO_JA`:
- Address: あなた (always)
- Natural spoken Japanese, not literal translation
- Short EN = short JA (match rhythm)
- US proper nouns keep English (White House → ホワイトハウス in katakana)
- Formality: neutral — plain form for dramatic lines

### B3: Translate to Vietnamese (VO_VI)

Apply translation rules from `phase-2/scripting-rules.md §6 VO_VI`:
- Address: bạn (always)
- Natural documentary-style Vietnamese
- Tighten aggressively (Vietnamese runs longer than EN)
- US proper nouns: keep English names
- Tone must match emotional energy of EN line

### B4: Assign Pause Values

Apply pause rules from `phase-2/scripting-rules.md §4`:
- After TIME_MARKER: 1.0
- After WEIGHT_LINE: 1.5
- At phase transitions (last line of each phase): 2.0
- Standard narration within beat: 0 or 0.5
- Before CALLBACK_CLOSE opening: 1.5

### B5: Validate

Before output:
- [ ] ALL rows have VO_EN + VO_JA + VO_VI populated (RULE_TRILINGUAL_COMPLETENESS)
- [ ] All rows ≥ 2 words in VO_EN (RULE_TTS_COMPLIANCE)
- [ ] Every "you"/"your" in VO_EN → あなた/あなたの in VO_JA → bạn/của bạn in VO_VI
- [ ] No inline pause markers in any VO column
- [ ] Pause_After at phase transitions ≥ required minimums (core/validation-core.md)
- [ ] Total Word_Count_EN within speech_time_config range (word_budget_min to word_budget_max, i.e. -10% to +20% of target)
- [ ] VO_ID is sequential with no gaps

### B5b: Veil Enforcement (TRANSPARENT_VEIL only)

**Only execute if Identity_Mode = TRANSPARENT_VEIL.**

For every row in vo_script_table.csv, scan VO_EN, VO_JA, VO_VI:

```yaml
scan_order:
  1. forbidden_terms.names    → on match: REMOVE or REPLACE with "you" context
  2. forbidden_terms.companies → on match: REPLACE with approved_phrase from mapping
  3. forbidden_terms.places   → on match: REPLACE with approved_phrase
  4. forbidden_bypass check   → initials, nicknames, partial names → FLAG + FIX

examples:
  "Tesla stock" → "the electric car company's stock"
  "At SpaceX"   → "At the rocket company"
  "テスラ"       → "電気自動車会社"
  "Tesla"       → "công ty xe điện"

era_anchor_check:
  - Verify ≥ 2 era_anchors appear somewhere in VO_EN rows (RULE_ERA_ANCHOR_INJECTION)
  - Verify ≥ 3 unique_circumstance_stack items appear in PHASE_EARLY/PHASE_CONFLICT rows
  - Verify ≥ 1 public_perception_marker echoed in PHASE_CONFLICT/PHASE_CRISIS rows
  - If missing: insert as additional NARRATION row in appropriate phase
```

Re-validate after veil enforcement: run B5 checks again on modified output.

### B6: Output vo_script_table.csv

**RULE_SILENT_OUTPUT:** CSV only.

File: `pvle/episodes/{EP}/vo_script_table.csv`

Columns: `VO_ID,Episode_ID,Beat_ID,Life_Phase,Beat_Type,VO_Type,VO_EN,VO_JA,VO_VI,Word_Count_EN,Pause_After`

---

## EXAMPLE OUTPUT ROW

```csv
1,PV_0001,BEAT_01_01,HOOK,ESTABLISH,NARRATION,"The moment you are born, the world already knows your name.","あなたが生まれた瞬間、世界はすでにあなたの名前を知っていた。","Khoảnh khắc bạn chào đời, thế giới đã biết tên bạn rồi.",11,0
2,PV_0001,BEAT_01_01,HOOK,ESTABLISH,NARRATION,"There are men outside the door.","扉の外には男たちがいる。","Có những người đàn ông đứng ngoài cửa.",6,0
3,PV_0001,BEAT_01_01,HOOK,ESTABLISH,WEIGHT_LINE,"There always will be.","これからもずっと。","Và họ luôn ở đó.",4,1.5
```

---

## PHASE C: HUMANIZE (vo_script_table.csv → humanized)

> **Rules file:** `phase-2/humanize-rules.md`  
> **Goal:** Transform AI cinematic narration into human memory narration

### C1: Load Humanize Rules

Load `phase-2/humanize-rules.md` — all 7 layers + density control + anti-patterns.

### C2: Apply Layer 1 — Rhythm Variation

Scan for uniform rhythm blocks (5+ consecutive lines of similar word count).
- Mix sentence lengths within each 5-line block
- PHASE_CRISIS: enforce short staccato (2-6 words)
- PHASE_PRESENT: alternate flowing/broken

### C3: Apply Layer 2 — Sensory Depth

Add 3-5 physical sensory details per episode:
- Prioritize touch, temperature, spatial awareness
- Each sensory detail on its own VO line
- No explanation of why it's noticed

### C4: Apply Layer 3 — Behavioral Detail

Add 4-6 behavioral details per episode:
- 3-4 micro-fidgets (meaningless physical actions)
- 1-2 social awkward moments
- Replace "feel X" with observable actions

### C5: Apply Layer 4 — Imperfect Thinking

Add 4-6 imperfections per episode:
- 2-3 false starts (thought cut off, restart simpler)
- 2-3 logic breaks (unrelated detail interrupts)
- 1-2 overlapping thoughts

### C6: Apply Layer 5 — Noise

Add 5-8 human artifacts per episode:
- 3-5 memory glitches (narrator unsure about own memory)
- 1-2 meaningless lines (zero narrative value)
- 1 micro confusion (narrator loses thread)
- 0-1 raw line (narrator comments on process of remembering)

### C7: Apply Layer 6 — Contraction Pass

Convert all formal grammar to contractions:
- "do not" → "don't", "it is" → "it's", etc.
- **EXCEPTIONS (keep formal):**
  - WEIGHT_LINE with declarative gravity
  - AGE_MARKER patterns ("You are [age].")
  - CALLBACK_CLOSE final weight lines

### C8: Apply Layer 7 — Pattern Audit

1. Count all uncertainty patterns ("You don't know", "You think", "Maybe", "Or —")
2. Cap each at max 3 instances — replace excess with behavioral equivalents
3. Break any 3-item symmetric lists (add trailing fragment)
4. Weaken any line that "sounds too good" (split into fragments)
5. Split compound ending lines into separate VO rows

### C9: Translate New Lines

For every new EN line added in C2-C8:
- Generate VO_JA following `scripting-rules.md §6 VO_JA`
- Generate VO_VI following `scripting-rules.md §6 VO_VI`
- Update Word_Count_EN
- Assign Pause_After

### C10: Renumber + Output

1. Renumber all VO_ID sequentially (no gaps)
2. Overwrite `vo_script_table.csv` with humanized version
3. Keep `vo_draft_table.csv` as original reference

---

## PHASE D: COMPLIANCE CHECK

> **Purpose:** Validate humanize rules compliance and notify user

### D1: Run Automated Checks

Execute the following checks on the final `vo_script_table.csv`:

```yaml
checks:
  PATTERN_COUNT:
    scan: Count instances of each uncertainty pattern
    patterns: ["You don't know", "You think", "Maybe", "Or —", "You're not sure"]
    threshold: max 3 per pattern
    
  CONTRACTION_AUDIT:
    scan: Find remaining formal grammar in NARRATION lines
    patterns: ["do not ", "does not ", "did not ", "is not ", "it is ", "You are "]
    exclude: WEIGHT_LINE, AGE_MARKER, CALLBACK_CLOSE weight lines
    threshold: 0 unintentional formal
    
  DENSITY_CHECK:
    scan: Verify no stacking of same type within 5 lines
    check_types: [sensory, behavioral, fidget, memory_glitch]
    
  LAYER_PRESENCE:
    scan: Verify minimum 1 of each type exists
    required:
      - fidget: ≥ 1
      - memory_glitch: ≥ 1
      - false_start: ≥ 1
      - sensory_standalone: ≥ 1
      - social_awkward: ≥ 1
    
  ENDING_CHECK:
    scan: Last 5 lines
    check: "Contains at least 1 fragment or unfinished thought"
    check2: "No compound multi-clause single lines"
    
  WORD_COUNT:
    total_en: calculate
    duration_estimate: total / 130 wpm
    target_check: within speech_time_config.word_budget_min to speech_time_config.word_budget_max (-10% / +20%)
```

### D2: Generate Compliance Report

Output a summary to user:

```
=== HUMANIZE COMPLIANCE REPORT ===

Episode: {EP}
VO lines: {count}
EN words: {count}
Est duration: ~{minutes} min

PATTERN AUDIT:
  "You think": {n} ✅/⚠️
  "You don't know": {n} ✅/⚠️
  "Maybe": {n} ✅/⚠️
  "Or —": {n} ✅/⚠️

LAYER PRESENCE:
  Fidget: {n} ✅/❌
  Memory glitch: {n} ✅/❌
  False start: {n} ✅/❌
  Sensory: {n} ✅/❌
  Social awkward: {n} ✅/❌

CONTRACTION:
  Remaining formal (unintentional): {n} ✅/⚠️

DENSITY:
  Stacking violations: {n} ✅/⚠️

ENDING:
  Imperfect: ✅/❌

OVERALL: {PASS / NEEDS_ADJUSTMENT}
```

### D3: User Decision Point

**If PASS:**
- Notify user: "Humanize compliance passed. Proceeding to Performance optimization."
- Continue to Phase E.

**If NEEDS_ADJUSTMENT:**
- List specific violations with suggested fixes
- Ask user: "Apply suggested fixes automatically, or adjust manually?"
- If user approves auto-fix → apply fixes, re-run D1-D2
- If user wants manual → stop and wait for instructions

---

## PHASE E: PERFORMANCE OPTIMIZATION (Viral + Retention)

> **Rules file:** `phase-2/performance-rules.md`  
> **Goal:** Maximize viral potential, retention, and shareability

### E1: Load Performance Rules

Load `phase-2/performance-rules.md` — all layers (P1–P9) + retention map + viral checklist + anti-patterns.

### E2: Map Retention Dip Zones

Scan script by phase and identify:
- Mid-CONFLICT zone (pattern fatigue, ~60 lines in)
- Post-CRISIS gap (energy drop after peak)
- Any phase transition without energy bridge

### E3: Apply Layer P1 — Re-Hook Moments

Insert 3-5 re-hook moments at dip zones:
- 1 before CONFLICT phase transition
- 1 at mid-CONFLICT (biggest retention risk)
- 1 at post-CRISIS (biggest energy drop)
- Pattern: 2-line promise-correction
- Each re-hook line_2 ≤ 6 words, Pause_After ≥ 1.5

### E4: Apply Layer P2 — Emotional Spike

Insert 1-2 emotional spikes in CONFLICT:
- 3-line try-fail-quit pattern
- Must pass relatability test ("Would a viewer with zero context feel this?")
- Failure must be mundane, resignation must be behavioral

### E5: Apply Layer P3 — Clip Moment

Insert 1-2 clip-worthy dualities:
- 2-line standalone (works out of context)
- Each line ≤ 6 words
- Must pass isolation test ("screenshot + share?")
- Usable as thumbnail text overlay

### E6: Apply Layer P4 — Phase Transitions

Check energy drops between phases:
- If CRISIS → RESOLUTION has no bridge → add short punch (max 2 lines)
- Bridge = max 2 lines, short punch

### E7: Apply Layer P5 — Roughen Clean Lines

Split 2-3 polished lines into fragments:
- Any line that sounds "quotable" → suspect
- Split into 3 beats (setup / middle / short punch)
- Add behavioral seals where appropriate

### E8: Apply Layer P6 — Cross-Audit

Re-check after all performance edits:
1. All uncertainty patterns still ≤ 3 each
2. No 2 consecutive WEIGHT_LINEs (except clip duality)
3. Total word count still within speech_time_config range (-10% / +20%)
4. New insertions don't create repetitive pattern

### E9: Apply Layer P7 — Narrator Texture

Apply narrator-layer rules from `performance-rules.md §12`:
- Add 1-2 narrator self-corrections (mid-sentence right-word-finding)
- Add 1-2 useless human moments (non-metaphorical sensory noise)
- Vary motif syntactic structure at anchor points
- Add 1 cognitive friction point (forces active processing)
- Verify ellipsis count ≤ 1 per episode (narrator correction only)

### E10: Apply Layer P8 — Rhythm & Tension

Apply rhythm rules from `performance-rules.md §13`:
- Verify ≥ 3 sentences >20 words with delayed meaning in mid-section
- Add 1 physical foreboding spike before CRISIS (body-based, not analytical)
- Add 1 ambient dread zone at CONFLICT→CRISIS transition
- Check information density: long sentences must carry uneven cognitive load

### E11: Apply Layer P9 — Production Discipline

Apply production discipline from `performance-rules.md §14`:
- WEIGHT_LINE pattern break: anchor lines must break motif's syntactic prediction
- Reframe over insert: prefer rewriting existing lines over adding new ones
- Humanization density check: ≥ 1 texture point per 50 lines minimum
- Version awareness: confirm current line count matches expected

### E12: Translate New Lines

For every new EN line added in E3-E11:
- Generate VO_JA + VO_VI
- Update Word_Count_EN + Pause_After

### E13: Renumber + Output

1. Renumber all VO_ID sequentially
2. Overwrite `vo_script_table.csv`

---

## PHASE F: FINAL COMPLIANCE CHECK

> **Purpose:** Combined humanize + performance validation. Report to user.

### F1: Run All Checks

Execute combined checks on final `vo_script_table.csv`:

```yaml
checks:
  # === HUMANIZE CHECKS ===
  PATTERN_COUNT:
    scan: Count uncertainty patterns
    patterns: ["You don't know", "You think", "Maybe", "Or ", "You're not sure"]
    threshold: max 3 per pattern
    
  CONTRACTION_AUDIT:
    scan: Remaining formal grammar (excluding intentional)
    threshold: 0 unintentional
    
  HUMANIZE_PRESENCE:
    required:
      fidget: ≥ 1
      memory_glitch: ≥ 1
      false_start: ≥ 1
      sensory_standalone: ≥ 1
      social_awkward: ≥ 1
      
  DENSITY:
    scan: No same-type stacking within 5 lines
    
  ENDING:
    scan: Last 5 lines contain fragment/unfinished thought

  # === PERFORMANCE CHECKS (P1-P6) ===
  REHOOK_COUNT:
    scan: Count re-hook patterns
    threshold: "≥ 3, ≤ 5"
    
  SPIKE_COUNT:
    scan: Emotional spike blocks
    threshold: ≥ 1
    
  CLIP_COUNT:
    scan: Clip-worthy dualities
    threshold: ≥ 1
    
  TRANSITION_BRIDGE:
    scan: Bridge at CRISIS→RESOLUTION
    threshold: ≥ 1

  # === NARRATOR TEXTURE CHECKS (P7-P9) ===
  NARRATOR_TEXTURE:
    self_correction: ≥ 1
    useless_moment: ≥ 1
    motif_vary: "no 3+ consecutive identical positions"
    ellipsis: ≤ 1

  RHYTHM_TENSION:
    long_sentences: "≥ 3 sentences >20w with delayed meaning"
    emotional_spike: ≥ 1 physical foreboding before CRISIS
    
  HUMANIZATION_DENSITY:
    scan: Count texture points per 50 lines
    threshold: ≥ 1 per 50 lines

  # === RHYTHM & DEPTH CHECKS (P10-P12) ===
  RHYTHM_DISTRIBUTION:
    scan: Count lines by word-count range
    targets:
      short_1_5: "3-6%"
      base_6_14: "65-78%"
      surge_20_30: "4-8% (minimum 4 lines)"
    fail_action: "Rewrite medium lines at inflection points as surges"

  MICRO_CRACK:
    scan: Identify body-betrayal suppression lines in CRISIS
    threshold: "= 1"
    test: "3-beat pattern (body act → involuntary → override)"
    integrity: "No verbal acknowledgment, no behavior change after"

  NEAR_BREAK:
    scan: Identify bandwidth-overload recovery lines in RESOLUTION/PRESENT
    threshold: "= 1"
    test: "4-beat pattern (overwhelm → blur → recover → seal)"
    placement: "Must NOT be in same phase as micro-crack"
    
  # === GENERAL CHECKS ===
  WORD_COUNT:
    total_en: calculate
    duration_estimate: total / 130 wpm
    target_check: within speech_time_config.word_budget_min to speech_time_config.word_budget_max (-10% / +20%)
    
  TRILINGUAL:
    scan: All rows have VO_EN + VO_JA + VO_VI
```

### F2: Generate Final Report

```
=== FINAL COMPLIANCE REPORT ===

Episode: {EP}
VO lines: {count}
EN words: {count}
Est duration: ~{minutes} min

─── HUMANIZE ───
Pattern audit:
  "You think": {n} ✅/⚠️
  "You don't know": {n} ✅/⚠️
  "Maybe": {n} ✅/⚠️
  "Or": {n} ✅/⚠️
  
Layer presence:
  Fidget: {n} ✅/❌
  Memory glitch: {n} ✅/❌
  False start: {n} ✅/❌
  Sensory: {n} ✅/❌
  Social awkward: {n} ✅/❌

Contraction: {n} remaining formal ✅/⚠️
Density: {n} violations ✅/⚠️
Ending: Imperfect ✅/❌

─── PERFORMANCE (P1-P6) ───
Re-hooks: {n} ✅/⚠️
Emotional spike: {n} ✅/❌
Clip moment: {n} ✅/❌
Transition bridge: {n} ✅/❌

─── NARRATOR TEXTURE (P7-P9) ───
Self-correction: {n} ✅/❌
Useless moment: {n} ✅/❌
Motif vary: ✅/❌
Rhythm break (>20w): {n} ✅/❌
Physical foreboding: {n} ✅/❌
Humanization density: {ratio} ✅/⚠️

─── RHYTHM & DEPTH (P10-P12) ───
Surge sentences (20-30w): {n} / 4-8 target ✅/❌
Short punches (1-5w): {n}% ✅/⚠️
Base rhythm (6-14w): {n}% ✅/⚠️
Micro-crack (CRISIS): {present/missing} ✅/❌
Near-break (RESOLUTION/PRESENT): {present/missing} ✅/❌
Crack/break phase separation: ✅/❌

─── OVERALL ───
Humanize: {PASS/NEEDS_FIX}
Performance: {PASS/NEEDS_FIX}
Rhythm & Depth: {PASS/NEEDS_FIX}
FINAL: {READY / NEEDS_ADJUSTMENT}
```

### F3: User Decision Point

**If READY:**
- Notify user: "Script passed all checks. Ready for Phase 3 (illustration)."
- Wait for user confirmation before proceeding.

**If NEEDS_ADJUSTMENT:**
- List specific violations with suggested fixes
- Ask user: "Apply suggested fixes, or adjust manually?"
- If approved → apply, re-run F1-F2
- If manual → stop and wait

---

## USER INPUT

> `Episode_ID`: {{Episode_ID}}
