# SKILL DIAGRAM — POV Life Simulation Engine (PVLE)

> Architecture overview: skills, workflows, resources, and data flow

---

## Layer Architecture

```
RULES (Always-On)
  hard-rules.md
  naming-conventions.md
  response-language.md
  workflow-strict-mode.md

ENGINE (Domain Knowledge)
  pvle-engine/SKILL.md          ← Core philosophy, pipeline, key rules

RESOURCES (Reference Data)
  template-master.md            ← All output schemas (the law)
  story-structure.md            ← 5 structure types + phase flow
  voice-lib.md                  ← VOICE_POV_DRAMATIST + translation rules
  character-system.md           ← Stickman design + visual style lock
  hook-lib.md                   ← Hook patterns + CTA templates
  rhetorical-lib.md             ← Sentence devices + phase strategies
  validation-rules.md           ← All quality and consistency rules
  world-index.yaml              ← Master world registry index

WORLD REGISTRY (Persistent Knowledge)
  pvle/worlds/WORLD_*.yaml      ← Per-world facts, locations, tensions

WORKFLOWS (Executable Pipelines)
  Phase 0 (Seed):   analyze-seed, pvle-ingest-world
  Phase 1 (Ideas):  pvle-gen-outline, pvle-gen-episode-brief
  Phase 2 (Script): pvle-gen-breakdown, pvle-gen-vo
  Phase 3 (Visual): pvle-gen-image-prompts, pvle-gen-video-prompts
  Macro:            pvle-run-full
```

---

## Data Flow

```
[User Seed]
    │
    ▼
/analyze-seed ──► world-index.yaml ──► WORLD_*.yaml
    │                                      │
    │                    ┌─────────────────┘
    ▼                    ▼
/pvle-gen-outline  (world facts injected)
    │
    ▼
/pvle-gen-episode-brief ──► episode_brief.md
    │
    ▼
/pvle-gen-breakdown ──► l2_breakdown_table.csv
    │
    ▼
/pvle-gen-vo ──► vo_draft_table.csv
             └── vo_script_table.csv
                   ├── VO_EN
                   └── VO_VI
    │
    ▼
/pvle-gen-image-prompts ──► image_prompts.csv  ──► [Nano Banana]
    │
    ▼
/pvle-gen-video-prompts ──► video_prompts.csv  ──► [Veo]
```

---

## Episode Output Structure

```
pvle/episodes/{PV_xxxx}/
  ├── episode_brief.md          P1 — single source of truth
  ├── l2_breakdown_table.csv    P2 — beat table with phases + scene types
  ├── vo_draft_table.csv        P2 — draft narration (EN only)
  ├── vo_script_table.csv       P2 - final bilingual script
  ├── image_prompts.csv         P3 — Nano Banana prompts (1 per VO line)
  └── video_prompts.csv         P3 — Veo prompts (1 per still image)
```

---

## ID Map

| Object | Pattern | Example |
|--------|---------|---------|
| Episode | `PV_xxxx` | `PV_0001` |
| World | `WORLD_{DOMAIN}_{KEY}` | `WORLD_US_PRESIDENT_FAMILY` |
| Beat | `BEAT_xx_xx` | `BEAT_02_03` |
| VO Line | Integer | `1, 2, 3...` |
| Image Slate | `{EP}_{NNN}` | `PV_0001_007` |
| Video Clip | `{EP}_C{NNN}` | `PV_0001_C007` |

---

## World Registry Growth Model

```
Episode 1: WORLD_US_PRESIDENT_FAMILY  ← created
Episode 2: WORLD_BILLION_HEIR         ← created
Episode 3: "son of a president again" → MATCH WORLD_US_PRESIDENT_FAMILY → reuse
Episode 4: WORLD_CIA_AGENT_CHILD      ← created
...
Registry grows. Reuse accelerates. World-building compounds over time.
```
