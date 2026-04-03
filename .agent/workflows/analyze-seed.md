---
description: Analyze seed topic, match World Registry, suggest or create new world data
skills_required:
  - pvle-engine
---

# WORKFLOW: /analyze-seed

> **Phase:** Pre-ideation  
> **Purpose:** Parse user seed â†’ detect named entity OR match world â†’ confirm before proceeding

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

Scan seed for known public figures â€” living, historical, or widely recognized:
- Format patterns: `"as [Name]"`, `"of [Name]"`, `"[Name]'s life"`, `"[Name]'s child"`
- Entity types: business figures, political figures, scientists, artists, athletes, historical leaders

```yaml
examples:
  "your life as Elon Musk"       â†’ NAMED_ENTITY: "Elon Musk"   â†’ LIVING_PUBLIC_FIGURE
  "son of Obama"                 â†’ NAMED_ENTITY: "Obama"       â†’ POLITICAL_FIGURE
  "your life as Einstein"        â†’ NAMED_ENTITY: "Einstein"    â†’ HISTORICAL_FIGURE
  "your life as a billionaire"   â†’ NO named entity â†’ continue Step 2
  "child of the US president"    â†’ NO named entity â†’ continue Step 2
```

**If NAMED_ENTITY detected:**
```
â†’ STOP standard flow
â†’ Run /pvle-extract-anchor with detected entity name + entity_type
â†’ /pvle-extract-anchor handles: classification, anchor extraction, title options, world build, ingest
â†’ Rejoin at Step 6 (Proceed) after /pvle-extract-anchor completes
```

**If NO named entity detected:**
```
â†’ Continue to Step 2 (standard generic flow below)
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
  EXACT_MATCH:    "seed_keywords overlap â‰¥ 3 AND domain matches"
  PARTIAL_MATCH:  "domain matches AND â‰¥ 1 seed_keyword OR privilege_type matches"
  NO_MATCH:       "no overlap found"
```

---

## STEP 3a: If EXACT_MATCH or PARTIAL_MATCH

Display to user:

```
âœ… World found: [WORLD_ID]
   Display name: [display_name]
   Domain: [domain]
   Mode: [implied_identity_mode]
   Previously used in: [episodes]

   Key facts available:
   - [fact 1]
   - [fact 2]
   - [fact 3]
   ...

â†’ Proceed with this world? (yes / create variation / create new)
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
  - "[Stickman accessory for this world â€” e.g. earpiece, crown, lab coat]"

used_in_episodes: []
created: "[today's date]"
```

Display to user for review and edits.

---

## STEP 4: User Confirms

Wait for explicit user confirmation:
- "OK" / "proceed" / "looks good" â†’ go to Step 5
- Edits â†’ apply, redisplay, wait for re-confirmation

---

## STEP 5: Ingest (if new world)

If world is NEW (Step 3b confirmed):
â†’ Run `/pvle-ingest-world` automatically

If world is EXISTING (Step 3a confirmed):
â†’ Skip ingest, proceed directly to `/pvle-gen-outline`

---

## STEP 6: Proceed

Report:
```
âœ… World confirmed: [WORLD_ID]
   Mode: [implied_identity_mode]
â†’ Ready for: /pvle-gen-outline [WORLD_ID]
```

---

## USER INPUT

> `Seed`: {{user_seed_text}}

