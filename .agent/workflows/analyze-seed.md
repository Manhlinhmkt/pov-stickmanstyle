---
description: Analyze seed topic, match World Registry, suggest or create new world data
skills_required:
  - pvle-engine
---

# WORKFLOW: /analyze-seed

> **Phase:** Pre-ideation  
> **Purpose:** Parse user seed -> detect named entity OR match world -> confirm before proceeding

## EXECUTION_CHECKLIST

```yaml
total_steps: 6
steps:
  - step: 1
    name: "Parse Seed"
    type: AUTO
    output: "inline (parsed_seed)"

  - step: 1b
    name: "Named Entity Detection"
    type: AUTO
    output: "inline (entity detected or not)"
    note: "If NAMED_ENTITY -> triggers /pvle-extract-anchor (separate workflow)"

  - step: 1c
    name: "Speech Time Input"
    type: BLOCKING
    gate: "Wait for user to specify target minutes"
    output: "inline (speech_time_config)"

  - step: 2
    name: "Match World Registry"
    type: AUTO
    output: "inline (match result)"

  - step: 3
    name: "Display World (match or new)"
    type: BLOCKING
    gate: "Wait for user to confirm world"
    output: "inline (world data displayed)"

  - step: 4
    name: "Ingest + Proceed"
    type: AUTO
    output: "World_ID confirmed"

# On completion: verify all steps checked
# On skip: VIOLATION -> HALT_AND_REPORT
```

---

## STEP 1: Parse Seed

Read user seed input. Extract:

```yaml
parsed_seed:
  subject_role:   "Who is the subject?" (e.g. "son of US President", "child of a mafia boss")
  domain:         "What domain?" (GOVERNMENT / CRIMINAL / CORPORATE / MILITARY / CELEBRITY / SCIENCE / ROYALTY / OTHER)
  era:            "When?" (HISTORICAL / MODERN_CONTEMPORARY / FUTURE / TIMELESS)
  privilege_type: "PRIVILEGE / ADVERSITY / HIDDEN_POWER / IMPOSSIBLE_CHOICE / LEGACY"
  seed_keywords:  "[list of key phrases from seed]"
```

---

## STEP 1b: Named Entity Detection

**Before any world matching, check if seed contains a real person's name.**

Scan seed for known public figures — living, historical, or widely recognized:
- Format patterns: `"as [Name]"`, `"of [Name]"`, `"[Name]'s life"`, `"[Name]'s child"`
- Entity types: business figures, political figures, scientists, artists, athletes, historical leaders

```yaml
examples:
  "your life as Elon Musk"       → NAMED_ENTITY: "Elon Musk"   → LIVING_PUBLIC_FIGURE
  "son of Obama"                 → NAMED_ENTITY: "Obama"       → POLITICAL_FIGURE
  "your life as Einstein"        → NAMED_ENTITY: "Einstein"    → HISTORICAL_FIGURE
  "your life as a billionaire"   → NO named entity → continue Step 1c
  "child of the US president"    → NO named entity → continue Step 1c
```

**If NAMED_ENTITY detected:**
```
→ STOP standard flow
→ Run /pvle-extract-anchor with detected entity name + entity_type
→ /pvle-extract-anchor handles: classification, anchor extraction, title options, world build, ingest
→ After /pvle-extract-anchor completes → continue to Step 1c (speech time)
```

**If NO named entity detected:**
```
→ Continue to Step 1c (speech time input)
```

---

## STEP 1c: Speech Time Input

**Ask user:**

```
🎤 Target speech time cho episode này là bao nhiêu phút?
   (Ví dụ: 10, 15, 20)
```

**Wait for user input.**

Once received, compute:

```yaml
speech_time_config:
  target_minutes: {{user_input}}                    # e.g. 15
  wpm: 130                                          # constant: PVLE narration speed
  
  # Core calculation
  target_words: target_minutes * 130                # e.g. 15 * 130 = 1950
  
  # Tolerance band: -10% to +20%
  word_budget_min: target_words * 0.90              # e.g. 1755
  word_budget_max: target_words * 1.20              # e.g. 2340
  word_budget_display: "{word_budget_min} - {word_budget_max}"
  
  # Duration equivalents
  duration_min_minutes: word_budget_min / 130       # e.g. 13.5
  duration_max_minutes: word_budget_max / 130       # e.g. 18.0

# Reference table:
#   10 min → 1170 - 1560 words →  9.0 - 12.0 min
#   15 min → 1755 - 2340 words → 13.5 - 18.0 min  
#   20 min → 2340 - 3120 words → 18.0 - 24.0 min
```

Store `speech_time_config` — passed to all downstream steps:
- `/pvle-gen-episode-brief` → `Word_Budget` + `Target_Duration_Min`
- `/pvle-gen-vo` → validation target (replaces hardcoded ±15%)

Display:
```
✅ Speech time config:
   Target: {{target_minutes}} min
   Word budget: {{word_budget_min}} - {{word_budget_max}} words
   Tolerance: -10% / +20%
→ Proceeding to world matching...
```

---

## STEP 2: Match World Registry

Read `pvle/engines/core/world-index.yaml`.

For each world in registry:
- Compare `parsed_seed.seed_keywords` against world's `seed_keywords`
- Compare `parsed_seed.domain` against world's `domain`
- Compare `parsed_seed.privilege_type` against world's structure type

```yaml
match_result:
  EXACT_MATCH:    "seed_keywords overlap >= 3 AND domain matches"
  PARTIAL_MATCH:  "domain matches AND >= 1 seed_keyword OR privilege_type matches"
  NO_MATCH:       "no overlap found"
```

---

## STEP 3a: If EXACT_MATCH or PARTIAL_MATCH

Display to user:

```
✅ World found: [WORLD_ID]
   Display name: [display_name]
   Domain: [domain]
   Mode: [implied_identity_mode]
   Previously used in: [episodes]

   Key facts available:
   - [fact 1]
   - [fact 2]
   - [fact 3]
   ...

→ Proceed with this world? (yes / create variation / create new)
```

Wait for user confirmation.

If user selects **create variation**: go to Step 3b, but pre-fill from existing world.

---

## STEP 3b: If NO_MATCH (or user requests new world)

Generate new world brief with `implied_identity_mode: GENERIC_ARCHETYPE`:

```yaml
WORLD_ID: WORLD_{DOMAIN}_{KEY_IDENTIFIER}
display_name: "[Human-readable name]"
domain: [DOMAIN]
era: [ERA]
implied_identity_mode: GENERIC_ARCHETYPE
tags: [list of 4-6 thematic tags]

seed_keywords:
  - "[main seed phrase]"
  - "[variations]"

key_facts:
  - "[Verified fact 1 about this world]"
  - "[Verified fact 2]"
  - "[Verified fact 3]"
  - "[Verified fact 4]"
  - "[Verified fact 5]"
  (5-8 facts, all verifiable)

key_locations:
  - id: LOC_{NAME}
    name: "[Location name]"
    description: "[1-line description]"
  (3-5 locations)

key_tensions:
  - [TENSION_TYPE_1]
  - [TENSION_TYPE_2]
  (2-4 from: PRIVILEGE_VS_FREEDOM / IDENTITY_VS_LEGACY / FRIENDSHIP_VS_SURVEILLANCE / 
   NORMAL_DESIRE_VS_IMPOSSIBLE_REALITY / POWER_VS_ISOLATION / DUTY_VS_SELF / PROTECTION_VS_CONTROL)

accessory_tags:
  - "[Stickman accessory for this world — e.g. earpiece, crown, lab coat]"

used_in_episodes: []
created: "[today's date]"
```

Display to user for review and edits.

---

## STEP 4: User Confirms

Wait for explicit user confirmation:
- "OK" / "proceed" / "looks good" → go to Step 5
- Edits → apply, redisplay, wait for re-confirmation

---

## STEP 5: Ingest (if new world)

If world is NEW (Step 3b confirmed):
→ Run `/pvle-ingest-world` automatically

If world is EXISTING (Step 3a confirmed):
→ Skip ingest, proceed directly to `/pvle-gen-outline`

---

## STEP 6: Proceed

Report:
```
✅ World confirmed: [WORLD_ID]
   Mode: [implied_identity_mode]
   Speech time: {{target_minutes}} min ({{word_budget_min}}-{{word_budget_max}} words)
→ Ready for: /pvle-gen-outline [WORLD_ID]
```

---

## USER INPUT

> `Seed`: {{user_seed_text}}
