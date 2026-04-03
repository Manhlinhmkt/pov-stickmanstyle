# WORLD REGISTRY — Reference Guide

> **Scope:** How to locate, read, and use world data  
> **Load:** All workflows that need world context

---

## Registry Location

```
core/world-index.yaml          ← master index: all World_IDs + metadata
pvle/worlds/WORLD_*.yaml       ← individual world data files
```

---

## World YAML Schema (Quick Reference)

```yaml
WORLD_ID:                      # e.g. WORLD_US_PRESIDENT_FAMILY
display_name:                  # human-readable, safe for output
domain:                        # GOVERNMENT / CORPORATE / MILITARY / etc.
era:                           # HISTORICAL / MODERN_CONTEMPORARY / FUTURE
implied_identity_mode:         # GENERIC_ARCHETYPE / TRANSPARENT_VEIL / HISTORICAL_FIGURE
implied_person:                # [INTERNAL ONLY — NEVER output]

key_facts: []                  # verified facts → use in PHASE_EARLY/CONFLICT
key_locations: []              # location objects → use in image prompts
key_tensions: []               # tension IDs → determines Structure_ID
accessory_tags: []             # stickman accessories for this world

# TRANSPARENT_VEIL mode only:
era_anchors: []                # specific year + event pairs → inject as TIME_MARKERs
unique_circumstance_stack: []  # specific facts → inject in PHASE_EARLY/CONFLICT
public_perception_markers: []  # how public sees them → inject in PHASE_CONFLICT
forbidden_terms:               # names / companies / places → never appear in VO
  names: []
  companies: {}                # "brand name" → "replacement phrase"
  places: {}
```

---

## How to Load World Data

```yaml
step_1: "Read core/world-index.yaml → find World_ID entry → get file path"
step_2: "Read pvle/worlds/{WORLD_ID}.yaml"
step_3: "Check implied_identity_mode"

if GENERIC_ARCHETYPE:
  use: key_facts, key_locations, key_tensions, accessory_tags

if TRANSPARENT_VEIL:
  use_all_above + era_anchors + unique_circumstance_stack
             + public_perception_markers + forbidden_terms
  load: phase-2/veil-scan.md for VO generation step

if HISTORICAL_FIGURE:
  use: same as GENERIC_ARCHETYPE (no veil enforcement needed)
```

---

## World ID → Structure ID Mapping

```yaml
domain: GOVERNMENT / ROYALTY  + high privilege  → LIFE_PRIVILEGE
domain: CRIMINAL / INTELLIGENCE + secret        → LIFE_HIDDEN_POWER
domain: ANY + ADVERSITY context                 → LIFE_ADVERSITY
domain: ANY + impossible decision context       → LIFE_IMPOSSIBLE_CHOICE
domain: CELEBRITY / LEGACY + famous parent      → LIFE_LEGACY
```
