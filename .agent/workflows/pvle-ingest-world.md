---
description: Save confirmed world data to PVLE World Registry
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-ingest-world

> **Phase:** Pre-ideation utility  
> **Purpose:** Write confirmed WORLD_*.yaml to registry and update world-index.yaml

---

## STEP 1: Receive World Data

Input: Confirmed world YAML from `/analyze-seed` Step 3b.

Validate:
- [ ] WORLD_ID follows pattern `WORLD_{DOMAIN}_{IDENTIFIER}` (all caps, underscores)
- [ ] `key_facts` has 5-8 entries
- [ ] `key_locations` has 3-5 entries
- [ ] `key_tensions` has 2-4 entries
- [ ] `seed_keywords` has ≥ 2 entries
- [ ] `accessory_tags` has ≥ 1 entry

---

## STEP 2: Write World File

Write to: `pvle/worlds/{WORLD_ID}.yaml`

---

## STEP 3: Update World Index

Read `pvle/engines/core/world-index.yaml`.

Append new entry:

```yaml
  {WORLD_ID}:
    file: "pvle/worlds/{WORLD_ID}.yaml"
    display_name: "[display_name]"
    domain: [domain]
    identity_mode: [identity_mode]
    tags: [tags list]
    episodes: []
    created: "[today's date]"
```

Write updated world-index.yaml.

---

## STEP 4: Confirm

```
✅ World ingested: [WORLD_ID]
   File: pvle/worlds/{WORLD_ID}.yaml
   Index updated: pvle/engines/core/world-index.yaml
→ Ready for: /pvle-gen-outline [WORLD_ID]
```
