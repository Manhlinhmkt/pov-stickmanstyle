# SCRIPTING RULES — Phase 2

> **Load:** /pvle-gen-breakdown, /pvle-gen-vo  
> **Contains:** Voice profile + Sentence patterns + Translation rules + VO validation

---

## 1. VOICE PROFILE: VOICE_POV_DRAMATIST

| Attribute | Value |
|-----------|-------|
| Tone | Calm authority + controlled drama |
| Base WPM | 140 |
| Address | Always "you" — never "he/she/they" for subject |
| Emotion | Controlled — let situation carry weight, never over-emote |
| Max sentence | 15 words |

---

## 2. SIGNATURE SENTENCE PATTERNS

```yaml
TIME_MARKER:
  pattern: "You are [age]." OR "You are [age]. [One-line consequence]."
  rule: "Always own VO row. Pause_After: 1.0"

CONTRAST_LINE:
  pattern: "While [others] [X], you [Y]."
  rule: "Max 2 per phase"
  examples:
    - "While your classmates trade notes, yours are reviewed."
    - "While other teenagers worry about curfews, yours is enforced by agents."

REVEAL_LINE:
  pattern: "What [you/no one] [doesn't] [know/say] is..."
  use: "Best at phase transitions — reveals hidden cost or gift"

WEIGHT_LINE:
  pattern: "[3-8 words. Declarative. Final.]"
  rule: "Own VO row. Pause_After: 1.5. Max 2 per phase."
  examples:
    - "This is not a home."
    - "You never chose this."
    - "He is always the President first."

REFLECTION_LINE:
  pattern: "Looking back, you [understand/see/know]..."
  use: "PHASE_RESOLUTION and CALLBACK_CLOSE primarily"

ACCUMULATION:
  pattern: "[Item 1]. [Item 2]. [Item 3]. [All of this is X.]"
  rule: "Max once per phase"

NEGATE_REVEAL:
  pattern: "It's not [surface assumption]. It's [deeper truth]."
  rule: "Max once per episode — reserve for PHASE_CONFLICT or PHASE_CRISIS"
```

---

## 3. EMOTIONAL ENERGY vs. PACE

```yaml
WONDER:        pace=140, sentences=8-14 words, pause=0.5 after reveals
TENSION:       pace=130-140, mixed short/long, pause=1.0 at transitions
DREAD:         pace=120-130, short 4-8 words, pause=1.5-2.0 after crisis
LONGING:       pace=130-140, longer sentences, pause=0.5-1.0
BITTERSWEET:   pace=120-130, variable, pause=1.0-1.5
CLARITY:       pace=140, short declarations, pause=1.5 before CALLBACK
```

---

## 4. PAUSE SYSTEM

```yaml
0:    "No pause — continuation"
0.5:  "Breath pause — within beat"
1.0:  "Beat pause — after TIME_MARKER, between ideas"
1.5:  "Section pause — after WEIGHT_LINE, phase transition"
2.0:  "Dramatic pause — after CRISIS, before CALLBACK_CLOSE"

required_minimums:
  Last line of HOOK:              Pause_After ≥ 2.0
  PHASE_EARLY → PHASE_CONFLICT:  Pause_After ≥ 1.5
  PHASE_CONFLICT → PHASE_CRISIS: Pause_After ≥ 2.0
  PHASE_CRISIS → PHASE_RESOLUTION: Pause_After ≥ 2.0
  PHASE_RESOLUTION → CALLBACK:   Pause_After ≥ 1.5
  After any WEIGHT_LINE:          Pause_After ≥ 1.5
  After any TIME_MARKER:          Pause_After ≥ 1.0
```

---

## 5. VO VALIDATION RULES

```yaml
RULE_SENTENCE_MAX:
  max_words: 15
  check: "Word_Count_EN > 15 → split into 2 rows"
  exception: "ACCUMULATION lists may use up to 20 words"

RULE_WEIGHT_LINE_ISOLATION:
  check: "VO_Type = WEIGHT_LINE → single row, nothing combined"
  forbidden: "Combining WEIGHT_LINE with following NARRATION"

RULE_TTS_COMPLIANCE:
  - Minimum 2 words per VO line
  - Numbers written as words ("thirty-two" not "32")
  - No inline pause markers in VO text ("[pause]", "..." forbidden in cells)
  - All pauses in Pause_After column as numeric float
  - No brackets in VO text

RULE_EMOTION_MATCH:
  check: "VO tone must match Mood_Tag of its beat"
  WONDER_beat + DREAD_tone = violation
  on_violation: REVISE_TONE
```

---

## 6. TRANSLATION RULES

### VO_JA (Japanese)
```yaml
address: "あなた (anata) — always 2nd person"
formality: "Neutral — plain form for dramatic lines"
rhythm: "Match EN rhythm — short EN = short JA"
forbidden:
  - Overly formal keigo
  - Literal word-for-word translation breaking rhythm
adaptation:
  - US proper nouns: keep English (White House → ホワイトハウス katakana)
  - Emotional idioms: adapt to Japanese equivalents
  - TIME_MARKER: "あなたは[年齢]歳だ。"
  - CONTRAST_LINE: "他の[子供]が[X]している間、あなたは[Y]。"
  - WEIGHT_LINE: plain form declarative
```

### VO_VI (Vietnamese)
```yaml
address: "bạn — always 2nd person"
formality: "Neutral conversational — documentary narration style"
rhythm: "Vietnamese runs longer — tighten aggressively"
forbidden:
  - "Mày/tao" (too informal)
  - Academic or formal register
  - Over-literal translation sounding unnatural
adaptation:
  - US institutions: keep English names
  - Emotional register must match — DREAD in EN = heavy tone in VI
  - Numbers translated accurately (no rounding)
  - TIME_MARKER: "Bạn [số tuổi] tuổi."
  - CONTRAST_LINE: "Trong khi những đứa trẻ khác [X], bạn [Y]."
```

### Trilingual Validation
```yaml
RULE_TRILINGUAL_COMPLETENESS:
  check: "Every vo_script_table.csv row must have VO_EN + VO_JA + VO_VI populated"
  forbidden: ["Empty cells", "'TBD'", "placeholder text"]
  on_violation: GENERATE_MISSING_TRANSLATION

RULE_JA_PERSON_CONSISTENCY:
  check: "All VO_JA use あなた for subject — never 彼/彼女"

RULE_VI_PERSON_CONSISTENCY:
  check: "All VO_VI use 'bạn' for subject — never 'anh/chị/họ'"

RULE_NO_LITERAL_TRANSLATION:
  test: "Read aloud — sounds like natural narration or translated text?"
  if_fail: "Rephrase to preserve meaning + emotion, not word order"
```

---

## 7. RHETORICAL STRATEGY BY PHASE

```yaml
HOOK:
  primary: WEIGHT_LINE (open strong)
  secondary: REVEAL_LINE (unexpected truth)
  avoid: REFLECTION_LINE

PHASE_EARLY:
  primary: CONTRAST_LINE
  secondary: TIME_MARKER
  avoid: NEGATE_REVEAL (save for later)

PHASE_CONFLICT:
  primary: CONTRAST_LINE + REVEAL_LINE
  secondary: ACCUMULATION (build constraint weight)
  avoid: REFLECTION_LINE

PHASE_CRISIS:
  primary: WEIGHT_LINE (anchor the stakes)
  secondary: NEGATE_REVEAL (peak truth)
  sentence_length: "SHORT — 4-8 words max"

PHASE_RESOLUTION:
  primary: REFLECTION_LINE
  secondary: TIME_MARKER
  tone: "Acceptance — not happiness, not despair"

CALLBACK_CLOSE:
  primary: REFLECTION_LINE + WEIGHT_LINE
  secondary: None — let silence close
```

---

## 8. RHYTHM TEMPLATES

```yaml
DRAMATIC_DROP:
  "[Long context — 10-14 words]"
  "[Short punch — 4-6 words]"
  "[Even shorter — 2-4 words]"

BUILD:
  "[Short — 4-6 words]"
  "[Medium — 8-10 words]"
  "[Full conclusion — 12-15 words]"

PARALLEL:
  "No [X]."
  "No [Y]."
  "No [Z]."
  "[Resolution or weight line]"
```
