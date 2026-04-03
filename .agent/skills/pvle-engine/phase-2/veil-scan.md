# VEIL SCAN ENGINE — Phase 2 (Named Entity Mode)

> **Load:** /pvle-gen-vo ONLY when Identity_Mode = TRANSPARENT_VEIL  
> **Purpose:** Dedicated scan pass — enforce forbidden terms AFTER draft is complete  
> **Run as:** Isolated post-processing step (Step B5b), NOT during drafting

---

## HOW TO USE

```
1. Draft VO completely (scripting-rules.md)
2. THEN load this file
3. Run scan pass on completed vo_script_table.csv
4. Fix all violations
5. Re-run core validation checks
```

---

## STEP 1: Load Forbidden Terms

From `pvle/worlds/{WORLD_ID}.yaml`:

```yaml
load:
  forbidden_terms.names:     # person's real name + variants
  forbidden_terms.companies: # brand names + replacement phrases
  forbidden_terms.places:    # specific locations + replacement phrases
```

Build scan dictionary:
```
forbidden_token → replacement_phrase
"Tesla"        → "the electric car company"
"SpaceX"       → "the rocket company"
"Elon"         → [remove — replace with "you"] 
"Pretoria"     → "a city in South Africa"
```

---

## STEP 2: Scan All 3 Language Columns

**Scan order per row:** VO_EN → VO_JA → VO_VI

```yaml
VO_EN scan:
  - Exact match (case-insensitive)
  - Partial match (word boundary check: "Teslas" catches "Tesla")
  - Abbreviation check: "E.M." / "T." / initials
  - Nickname check: universally-tied nicknames

VO_JA scan:
  - Katakana equivalents (pre-built from names list)
    e.g. "テスラ", "イーロン", "スペースX"
  - Kanji if applicable
  - Romaji within Japanese text

VO_VI scan:
  - Direct transliterations
  - Common Vietnamese shorthand
  - Mixed-script occurrences (English name within Vietnamese sentence)
```

---

## STEP 3: Apply Replacements

```yaml
on_match_NAMES:
  if subject name: replace with "you" / "your" (context-appropriate)
  if other name:   remove or rephrase around it

on_match_COMPANIES:
  replace with approved_phrase from forbidden_terms.companies mapping
  ensure replacement phrase fits grammatically in all 3 languages

on_match_PLACES:
  replace with approved_phrase from forbidden_terms.places mapping

forbidden_bypass (ABORT if found):
  - Initials clearly identifying person: "E.M.", "B.O."
  - Nicknames universally tied to one individual
  - Company acronyms when company = primary identifier of person
  action: FLAG + REQUIRE_MANUAL_FIX
```

---

## STEP 4: Era Anchor Verification

```yaml
RULE_ERA_ANCHOR_INJECTION:
  required:
    - ≥ 2 era_anchors reflected in VO_EN (year + context from world YAML)
    - ≥ 3 unique_circumstance_stack items in PHASE_EARLY or PHASE_CONFLICT rows
    - ≥ 1 public_perception_marker echoed in PHASE_CONFLICT or PHASE_CRISIS rows
  
  method: "Inject as verified facts — viewer computes identity from data stack"
  
  if_missing:
    - era_anchor: Insert TIME_MARKER row in appropriate phase
    - circumstance: Insert NARRATION row after relevant beat
    - perception: Insert CONTRAST_LINE or REVEAL_LINE in PHASE_CONFLICT

  tone_check: "Injected rows must match Mood_Tag of surrounding beats"
```

---

## STEP 5: Language-Specific Replacement Guide

### Japanese replacements
```yaml
"テスラ"    → "電気自動車会社"
"スペースX" → "ロケット会社"
"ツイッター" → "そのプラットフォーム"
"[名前]"    → "あなた" (if referring to subject)
```

### Vietnamese replacements
```yaml
"Tesla"  → "công ty xe điện"
"SpaceX" → "công ty tên lửa"
"Twitter" → "nền tảng mạng xã hội"
"[tên]"  → "bạn" (if referring to subject)
```

---

## STEP 6: Post-Scan Validation

After all replacements applied:

- [ ] Re-run `RULE_TTS_COMPLIANCE` — replacements may have broken sentence flow
- [ ] Re-run `RULE_SENTENCE_MAX` — replacements may have made sentences longer
- [ ] Re-run `RULE_JA_PERSON_CONSISTENCY` — check あなた consistency post-replacement
- [ ] Re-run `RULE_VI_PERSON_CONSISTENCY` — check bạn consistency post-replacement
- [ ] Confirm era anchors present (Step 4 check)
- [ ] Confirm NO forbidden terms remain (full re-scan)

---

## WHAT VEIL DOES NOT DO

```yaml
forbidden_scope:
  - Does NOT change VO_Type or Beat_ID
  - Does NOT change Pause_After values
  - Does NOT alter World_ID or Episode_ID
  - Does NOT add new beats (except era anchor injection)
  - Does NOT change the emotional arc
```
