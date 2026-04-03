# SYSTEM OVERVIEW — POV Life Simulation Engine (PVLE)

> **Version:** v1.0  
> **Type:** Illustrated Narrative + Video (VO + Stickman + Veo)

---

## What Is PVLE?

The POV Life Simulation Engine (PVLE) is an AI-assisted content production pipeline for creating "what if" life simulation videos. Each episode places the viewer inside an extraordinary life — narrated in second person ("you"), illustrated with minimalist stickman animation, and produced as trilingual content (English / Japanese / Vietnamese).

---

## Pipeline

```
Phase 1: IDEATION
  Seed → /analyze-seed → World Registry check → /pvle-gen-outline → episode_brief.md

Phase 2: SCRIPTING
  episode_brief.md → /pvle-gen-breakdown → /pvle-gen-vo
  Output: l2_breakdown_table.csv + vo_script_table.csv (EN | JA | VI)

Phase 3: ILLUSTRATION + VIDEO
  vo_script_table.csv → /pvle-gen-image-prompts → image_prompts.csv (Nano Banana)
                      → /pvle-gen-video-prompts → video_prompts.csv (Veo)
```

---

## What Makes PVLE Different

### World Registry
Every episode draws from a verified world data file (`pvle/worlds/WORLD_*.yaml`). When a seed is given, the engine checks whether this world already exists. If yes — reuse. If no — generate and ingest. The registry grows permanently with each new world.

### Trilingual VO
Every script line is produced simultaneously in English, Japanese, and Vietnamese. Translation follows meaning and emotional rhythm — not word-for-word.

### Stickman Style
The subject character is always an anonymous stickman — featureless so viewers can inhabit the role. Rich, detailed backgrounds create contrast and immersion.

### Nano Banana + Veo
Image still prompts feed Nano Banana (Gemini Image Generation). Video motion prompts feed Veo. Together they produce animated clips ready for assembly.

---

## Core Voice: VOICE_POV_DRAMATIST

- Always "you" — second person, no exceptions
- Short declarative sentences — max 15 words
- Controlled drama — let the situation carry the weight
- 140 WPM, heavy use of pauses
- Signature patterns: TIME_MARKER / CONTRAST / REVEAL / WEIGHT / REFLECTION

---

## Key Files

| Category | Files |
|----------|-------|
| Engine | `.agent/skills/pvle-engine/SKILL.md` |
| Resources | `template-master.md`, `story-structure.md`, `voice-lib.md`, `character-system.md`, `hook-lib.md`, `rhetorical-lib.md`, `validation-rules.md` |
| World Registry | `pvle/worlds/*.yaml`, `world-index.yaml` |
| Workflows (P1) | `analyze-seed`, `pvle-ingest-world`, `pvle-gen-outline`, `pvle-gen-episode-brief` |
| Workflows (P2) | `pvle-gen-breakdown`, `pvle-gen-vo` |
| Workflows (P3) | `pvle-gen-image-prompts`, `pvle-gen-video-prompts` |
| Macro | `pvle-run-full` |
