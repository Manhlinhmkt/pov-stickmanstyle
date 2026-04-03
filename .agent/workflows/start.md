---
description: Initialize POV Life Simulation Engine (PVLE) session and display command registry
---

# /start — PVLE Session Init

// turbo
Load skill: `.agent/skills/pvle-engine/SKILL.md`
Load core: `core/template-master.md`, `core/world-registry.md`, `core/validation-core.md`, `core/world-index.yaml`

Display command registry and await user command.

## Command Registry

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  POV LIFE SIMULATION ENGINE — PVLE v2.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MACRO
  /pvle-run-full       Full pipeline: seed → video prompts
                       (auto-detects named entity vs generic)

PHASE 0 — SEED
  /analyze-seed        Parse seed, match or create world
  /pvle-extract-anchor Named entity mode: extract anchor title
  /pvle-ingest-world   Save confirmed world to registry

PHASE 1 — IDEATION
  /pvle-gen-outline        Build telegraphic phase outline
  /pvle-gen-episode-brief  Produce episode_brief.md

PHASE 2 — SCRIPTING
  /pvle-gen-breakdown  Generate l2_breakdown_table.csv
  /pvle-gen-vo         Draft + finalize vo_script_table.csv
                       (EN | JA | VI + veil enforcement if needed)

PHASE 3 — VISUAL
  /pvle-gen-image-prompts  Generate image_prompts.csv (Nano Banana)
  /pvle-gen-video-prompts  Generate video_prompts.csv (Veo)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Worlds registered: [count from world-index.yaml]
  Episodes produced: [count from pvle/episodes/]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Await user command or seed input.
