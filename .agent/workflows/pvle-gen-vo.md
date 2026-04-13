---
description: Draft, enhance, finalize, and translate VO script (PVLE P2.2 - P2.6)
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-gen-vo

> **Phase:** 2.2 + 2.4 + 2.5 + 2.6 - Scripting (Draft + Enhance + Finalize + Translate)
> **Input:** `l2_breakdown_table.csv` + `episode_brief.md`
> **Output:** 4 files in sequence:
>   1. `vo_draft_table.csv` (EN draft per beat)
>   2. `vo_enhanced_table.csv` (EN humanized per line)
>   3. `vo_finalize_table.csv` (EN performance-optimized per line)
>   4. `vo_script_table.csv` (EN + VI final)

---

## STEP 1: DRAFT (vo_draft_table.csv)

### 1.1: Read Inputs

Load:
- `l2_breakdown_table.csv` - all beats with Life_Phase, Beat_Type, Mood_Tag, Content_Sketch
- `episode_brief.md` - Stickman_Accessory, Key_Locations, Core_Tension, Episode_Notes, Identity_Mode, Word_Budget
- `phase-2/scripting-rules.md` - VOICE_POV_DRAMATIST patterns, sentence rules
- `phase-1/ideation-rules.md` - Hook_Type template for this episode

**If Identity_Mode = TRANSPARENT_VEIL:**
- Also load `pvle/worlds/{WORLD_ID}.yaml` - extract forbidden_terms, era_anchors, unique_circumstance_stack, public_perception_markers
- Store as `veil_config`

### 1.2: Draft VO per Beat

For each beat in l2_breakdown_table.csv:
1. Select rhetorical strategy from `scripting-rules.md` based on Beat_Type + Life_Phase
2. Draft VO_Draft_EN following VOICE_POV_DRAMATIST rules:
   - Always "you"
   - Max 15 words per sentence
   - TIME_MARKER beats = "You are [age]." pattern
   - WEIGHT_LINE beats = 3-8 word anchor only
   - CONTRAST beats = "While others X, you Y." pattern
3. Calculate Word_Count

### 1.3: Output

**RULE_SILENT_OUTPUT:** CSV only.

File: `pvle/episodes/{EP}/vo_draft_table.csv`

Columns: `Beat_ID,Life_Phase,Beat_Type,Mood_Tag,Content_Sketch,VO_Draft_EN,Word_Count`

### 1.4: *** PAUSE - User Review ***

Display:
```
Step 1 complete: vo_draft_table.csv
VO lines: {beat_count}
EN words: {total_word_count}

Review the draft and confirm before proceeding to Step 2 (Humanize).
```

Wait for explicit user confirmation.

---

## STEP 2: ENHANCE (vo_enhanced_table.csv)

> **Rules file:** `phase-2/humanize-rules.md`
> **Goal:** Transform AI narration into human memory narration

### 2.1: Read Inputs

Load:
- `vo_draft_table.csv` - all beats
- `phase-2/humanize-rules.md` - all 7 layers + density control + anti-patterns

### 2.2: Break Draft into Lines

For each beat's VO_Draft_EN:
1. Split at natural pause points (sentence boundaries, clause boundaries)
2. Each line = 1 spoken unit
3. TIME_MARKER and WEIGHT_LINE: always own row
4. Assign VO_ID sequentially
5. Assign VO_Type (NARRATION / TIME_MARKER / WEIGHT_LINE / REFLECTION / CONTRAST_LINE)
6. Assign Pause_After per scripting-rules.md section 4

### 2.3: Duration Expansion (MANDATORY)

> **Purpose:** Ensure word count reaches target BEFORE humanize layers are applied.
> **Principle:** Expansion = real content (detail, context, scene depth). NOT padding.

Calculate gap:
```yaml
current_words: sum(Word_Count) from broken lines
target_words: episode_brief.Word_Budget midpoint
gap: target_words - current_words

if gap > 10%_of_target:
  expansion_required: true
  expansion_target: target_words * 0.90  # humanize will add remaining ~10%
```

**If expansion_required = true:**

For each phase, identify expansion opportunities (in priority order):

1. **Scene Detail Expansion** - Add environmental, temporal, spatial details to thin scenes
   - "The parking lot is half empty" → context that grounds the moment
   - Add 1-2 new NARRATION lines per under-developed beat

2. **Internal State Expansion** - Add behavioral observations that reveal psychology
   - Physical reactions, things noticed, things ignored
   - Must be SHOW not TELL

3. **Transitional Beats** - Add connective tissue between major beats
   - "The next morning..." / "Two weeks later..." moments
   - Small scenes that build the routine/pattern

4. **Dialogue Echo** - Expand existing dialogue beats with aftermath
   - What happens AFTER the conversation ends
   - The silence that follows a question

**Expansion Rules:**
```yaml
RULE_EXPAND_EVENLY:
  description: "Don't inflate only one phase"
  target: "Each phase within +/- 5% of its allocated word budget percentage"

RULE_EXPAND_NOT_PAD:
  description: "Every added line must serve scene or psychology"
  test: "Remove this line - does the scene feel thinner? If YES, keep."
  forbidden: "Filler observations with no grounding in narrative"

RULE_EXPAND_BEFORE_HUMANIZE:
  description: "All expansion happens BEFORE humanize layers"
  rationale: "Humanize depends on line count and rhythm - changing content after breaks texture"
```

**After expansion, verify:**
- [ ] Total word count >= 90% of word_budget_min
- [ ] Phase distribution within allocation percentages
- [ ] No phase exceeds 50 lines

---

### 2.4: Apply Humanize Layer 1 - Rhythm Variation

Scan for uniform rhythm blocks (5+ consecutive lines of similar word count).
- Mix sentence lengths within each 5-line block
- PHASE_CRISIS: enforce short staccato (2-6 words)

### 2.5: Apply Humanize Layer 2 - Sensory Depth

Add 3-5 physical sensory details per episode:
- Prioritize touch, temperature, spatial awareness
- Each sensory detail on its own VO line

### 2.6: Apply Humanize Layer 3 - Behavioral Detail

Add 4-6 behavioral details per episode:
- 3-4 micro-fidgets (meaningless physical actions)
- 1-2 social awkward moments
- Replace "feel X" with observable actions

### 2.7: Apply Humanize Layer 4 - Imperfect Thinking

Add 4-6 imperfections per episode:
- 2-3 false starts
- 2-3 logic breaks
- 1-2 overlapping thoughts

### 2.8: Apply Humanize Layer 5 - Noise

Add 5-8 human artifacts per episode:
- 3-5 memory glitches
- 1-2 meaningless lines
- 1 micro confusion
- 0-1 raw line

### 2.9: Apply Humanize Layer 6 - Contraction Pass

Convert formal grammar to contractions.
- EXCEPTIONS: WEIGHT_LINE with gravity, AGE_MARKER, CALLBACK_CLOSE weight lines

### 2.10: Apply Humanize Layer 7 - Pattern Audit

1. Count all uncertainty patterns - cap each at max 3
2. Break any 3-item symmetric lists
3. Weaken lines that sound "too good"
4. Split compound ending lines

### 2.11: Humanize Compliance Check

Run automated checks:
```yaml
checks:
  PATTERN_COUNT: max 3 per pattern
  CONTRACTION_AUDIT: 0 unintentional formal
  DENSITY_CHECK: no stacking within 5 lines
  LAYER_PRESENCE:
    fidget: >= 1
    memory_glitch: >= 1
    false_start: >= 1
    sensory_standalone: >= 1
    social_awkward: >= 1
  ENDING_CHECK: last 5 lines contain fragment
  WORD_COUNT: within word_budget range
```

### 2.12: Renumber + Output

1. Renumber all VO_ID sequentially (no gaps)
2. Output to `vo_enhanced_table.csv`

File: `pvle/episodes/{EP}/vo_enhanced_table.csv`

Columns: `VO_ID,Episode_ID,Beat_ID,Life_Phase,Beat_Type,VO_Type,VO_EN,Word_Count_EN,Pause_After`

### 2.13: *** PAUSE - User Review ***

Display humanize compliance report, then:
```
Step 2 complete: vo_enhanced_table.csv
VO lines: {count}
EN words: {count}
Est duration: ~{minutes} min

Humanize compliance: {PASS/NEEDS_FIX}

Review the humanized script and confirm before proceeding to Step 3 (Performance).
```

Wait for explicit user confirmation.

---

## STEP 3: FINALIZE (vo_finalize_table.csv)

> **Rules file:** `phase-2/performance-rules.md`
> **Goal:** Maximize viral potential, retention, and shareability

### 3.1: Read Inputs

Load:
- `vo_enhanced_table.csv` - humanized EN script
- `phase-2/performance-rules.md` - all layers P1-P12

### 3.2: Map Retention Dip Zones

Scan script by phase and identify:
- Mid-CONFLICT zone (pattern fatigue)
- Post-CRISIS gap (energy drop after peak)
- Any phase transition without energy bridge

### 3.3: Apply Layer P1 - Re-Hook Moments

Insert 3-5 re-hook moments at dip zones.
- Pattern: 2-line promise-correction
- line_2 <= 6 words, Pause_After >= 1.5

### 3.4: Apply Layer P2 - Emotional Spike

Insert 1-2 emotional spikes in CONFLICT.
- 3-line try-fail-quit pattern
- Must pass relatability test

### 3.5: Apply Layer P3 - Clip Moment

Insert 1-2 clip-worthy dualities.
- 2-line standalone, each <= 6 words
- Must pass isolation test

### 3.6: Apply Layer P4 - Phase Transitions

Check energy drops between phases.
- Add bridge at CRISIS to RESOLUTION if needed

### 3.7: Apply Layer P5 - Roughen Clean Lines

Split 2-3 polished lines into fragments.

### 3.8: Apply Layer P6 - Cross-Audit

Re-check all patterns from humanize pass.
- Patterns still <= 3 each
- No double WEIGHT_LINEs
- Word count still in budget

### 3.9: Apply Layer P7 - Narrator Texture

- 1-2 narrator self-corrections
- 1-2 useless human moments
- Vary motif syntactic structure
- 1 cognitive friction point
- Ellipsis count <= 1

### 3.10: Apply Layer P8 - Rhythm and Tension

- Verify >= 3 sentences >20 words with delayed meaning
- 1 physical foreboding spike before CRISIS
- 1 ambient dread zone at CONFLICT to CRISIS transition
- Information density: long sentences carry uneven cognitive load

### 3.11: Apply Layer P9 - Production Discipline

- WEIGHT_LINE pattern break
- Reframe over insert
- Humanization density check >= 1 per 50 lines

### 3.12: Apply Layers P10-P12

- P10: Sentence rhythm distribution (surge 4-8%, short 3-6%, base 65-78%)
- P11: Micro-crack architecture (1 in CRISIS)
- P12: Near-break escalation (1 in RESOLUTION)

### 3.13: Performance Compliance Check

Run automated checks:
```yaml
checks:
  REHOOK_COUNT: >= 3, <= 5
  SPIKE_COUNT: >= 1
  CLIP_COUNT: >= 1
  TRANSITION_BRIDGE: >= 1
  RHYTHM_DISTRIBUTION: surge 4-8%, short 3-6%
  MICRO_CRACK: = 1 (CRISIS only)
  NEAR_BREAK: = 1 (RESOLUTION only)
  NARRATOR_TEXTURE: self_correction >= 1, useless_moment >= 1
  WORD_COUNT: within word_budget range
```

### 3.14: Renumber + Output

1. Renumber all VO_ID sequentially
2. Output to `vo_finalize_table.csv`

File: `pvle/episodes/{EP}/vo_finalize_table.csv`

Columns: `VO_ID,Episode_ID,Beat_ID,Life_Phase,Beat_Type,VO_Type,VO_EN,Word_Count_EN,Pause_After`

### 3.15: *** PAUSE - User Review ***

Display performance compliance report, then:
```
Step 3 complete: vo_finalize_table.csv
VO lines: {count}
EN words: {count}
Est duration: ~{minutes} min

Performance compliance: {PASS/NEEDS_FIX}

Review the finalized script and confirm before proceeding to Step 4 (Translation).
```

Wait for explicit user confirmation.

---

## STEP 4: SCRIPT (vo_script_table.csv)

> **Goal:** Translate to Vietnamese + final compliance

### 4.1: Read Inputs

Load:
- `vo_finalize_table.csv` - finalized EN script (DO NOT modify VO_EN)
- `phase-2/scripting-rules.md` - section 6 VO_VI translation rules

**If Identity_Mode = TRANSPARENT_VEIL:**
- Load `veil_config` from world YAML
- Load `phase-2/veil-scan.md`

### 4.2: Translate to Vietnamese (VO_VI)

For every VO_EN line, generate VO_VI:
- Address: ban (always 2nd person)
- Natural documentary-style Vietnamese
- Tighten aggressively (Vietnamese runs longer than EN)
- US proper nouns: keep English names
- Tone must match emotional energy of EN line
- TIME_MARKER: "Ban [so tuoi] tuoi."
- CONTRAST_LINE: "Trong khi nhung dua tre khac [X], ban [Y]."

### 4.3: Veil Enforcement (TRANSPARENT_VEIL only)

**Only execute if Identity_Mode = TRANSPARENT_VEIL.**

Scan VO_EN and VO_VI for forbidden terms:
1. forbidden_terms.names - REMOVE or REPLACE
2. forbidden_terms.companies - REPLACE with approved phrase
3. forbidden_terms.places - REPLACE with approved phrase
4. Bypass check - initials, nicknames, partial names

Verify era_anchors and unique_circumstance_stack injection.

### 4.4: Final Compliance Check

Run combined checks:
```yaml
checks:
  # BILINGUAL
  BILINGUAL_COMPLETENESS: All rows have VO_EN + VO_VI
  VI_PERSON_CONSISTENCY: All VO_VI use "ban" for subject

  # HUMANIZE (recheck)
  PATTERN_COUNT: max 3 per pattern
  CONTRACTION_AUDIT: 0 unintentional formal
  LAYER_PRESENCE: fidget, memory_glitch, false_start, sensory, social_awkward

  # PERFORMANCE (recheck)
  REHOOK_COUNT: >= 3, <= 5
  SPIKE_COUNT: >= 1
  CLIP_COUNT: >= 1
  MICRO_CRACK: = 1
  NEAR_BREAK: = 1

  # RHYTHM
  SURGE_SENTENCES: 4-8
  SHORT_PUNCHES: 3-6%
  BASE_RHYTHM: 65-78%

  # GENERAL
  WORD_COUNT: within word_budget range
  VO_ID: sequential, no gaps
```

### 4.5: Output

File: `pvle/episodes/{EP}/vo_script_table.csv`

Columns: `VO_ID,Episode_ID,Beat_ID,Life_Phase,Beat_Type,VO_Type,VO_EN,VO_VI,Word_Count_EN,Pause_After`

### 4.6: Final Report

```
=== FINAL VO REPORT ===

Episode: {EP}
VO lines: {count}
EN words: {count}
Est duration: ~{minutes} min

Pipeline: vo_draft -> vo_enhanced -> vo_finalize -> vo_script_table
Languages: EN + VI

Compliance: {PASS/NEEDS_FIX}

Ready for: /pvle-gen-image-prompts {EP}
```

---

## EXAMPLE OUTPUT ROW (vo_script_table.csv)

```csv
1,PV_0011,BEAT_01_01,HOOK,ESTABLISH,NARRATION,"The screen glows blue in the dark.","Man hinh phat sang xanh trong bong toi.",7,0
```

---

## USER INPUT

> `Episode_ID`: {{Episode_ID}}
