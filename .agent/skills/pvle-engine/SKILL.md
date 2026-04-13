# SKILL: POV Life Simulation Engine (PVLE)

> **Engine:** POV Life Simulation Engine  
> **Version:** v2.1 (Phase Module Architecture)  
> **Type:** Illustrated narrative - VO + Stickman (Nano Banana) + Video (Veo)

---

## Philosophy

Place the viewer inside an extraordinary life they will never live.

Narrated entirely in second person ("you"). The stickman has no face — the face is theirs. The world around the stickman is rich, detailed, and real — because the simulation only works if the world feels true.

Every episode answers one question: **"What would this life actually feel like?"** Not the highlight reel. The full weight of it.

---

## Pipeline

```
Seed → /analyze-seed
          ├─ [Named entity] → /pvle-extract-anchor → world created
          └─ [Generic]      → world matched or created

World confirmed → /pvle-gen-outline → /pvle-gen-episode-brief

episode_brief.md → /pvle-gen-breakdown → /pvle-gen-vo
                                              ├─ [TRANSPARENT_VEIL] → veil-scan pass
                                              ├─ humanize pass (phase-2/humanize-rules.md)
                                              └─ performance pass (phase-2/performance-rules.md)

vo_script_table.csv → /pvle-gen-image-prompts → illustration_strip_table.csv
                                                  → image_prompts.csv → [Nano Banana]
                    → /pvle-gen-video-prompts  → video_prompts.csv → [Veo]
```

---

## File Map — What Each Workflow Loads

| Workflow | core/ | phase module | conditional |
|----------|-------|-------------|-------------|
| `/analyze-seed` | all 4 core files | — | — |
| `/pvle-extract-anchor` | all 4 core files | phase-1/ideation-rules.md | — |
| `/pvle-gen-outline` | all 4 core files | phase-1/ideation-rules.md | — |
| `/pvle-gen-episode-brief` | all 4 core files | phase-1/ideation-rules.md | — |
| `/pvle-gen-breakdown` | all 4 core files | phase-1/ideation-rules.md | — |
| `/pvle-gen-vo` | all 4 core files | phase-2/scripting-rules.md, phase-2/humanize-rules.md, phase-2/performance-rules.md | [VEIL] phase-2/veil-scan.md |
| `/pvle-gen-image-prompts` | all 4 core files | phase-3/visual-rules.md, phase-3/illustration-mapping-rules.md | — |
| `/pvle-gen-video-prompts` | all 4 core files | phase-3/visual-rules.md | — |

**Core files (always load):**
- `core/template-master.md` — all schemas and IDs
- `core/world-registry.md` — how to read world YAML
- `core/validation-core.md` — cross-phase rules
- `core/world-index.yaml` — master world list

---

## Key Rules (see source files for detail)

| Rule | File | Summary |
|------|------|---------|
| RULE_POV_CONSISTENCY | core/validation-core.md | Always "you" — never 3rd person |
| RULE_ACCURACY | core/validation-core.md | Facts must be verifiable |
| RULE_PRIORITY_ORDER | core/validation-core.md | Conflict resolution order |
| RULE_EMOTION_PER_PHASE | phase-1/ideation-rules.md | Required emotion per phase |
| RULE_EARNED_RESOLUTION | phase-1/ideation-rules.md | Resolution must mirror crisis |
| RULE_SENTENCE_MAX | phase-2/scripting-rules.md | 15 words max per VO line |
| RULE_TTS_COMPLIANCE | phase-2/scripting-rules.md | TTS-ready output |
| RULE_BILINGUAL_COMPLETENESS | phase-2/scripting-rules.md | All 2 langs (EN + VI) populated |
| RULE_VEIL_ENFORCEMENT | phase-2/veil-scan.md | No forbidden terms in output |
| RULE_ERA_ANCHOR_INJECTION | phase-2/veil-scan.md | Anchor facts must appear |
| RULE_CONTRACTION_DEFAULT | phase-2/humanize-rules.md | Use contractions, keep formal for weight lines |
| RULE_MAX_PATTERN_3 | phase-2/humanize-rules.md | No uncertainty phrase > 3 per episode |
| RULE_MICRO_FIDGET | phase-2/humanize-rules.md | 1 meaningless action per ~30 lines |
| RULE_MEMORY_GLITCH | phase-2/humanize-rules.md | 1 memory uncertainty per ~40 lines |
| RULE_REHOOK_FREQUENCY | phase-2/performance-rules.md | 1 re-hook per ~60 lines (3-5/episode) |
| RULE_SPIKE_STRUCTURE | phase-2/performance-rules.md | 3-line try-fail-quit emotional spike |
| RULE_CLIP_STRUCTURE | phase-2/performance-rules.md | 2-line duality for shorts/thumbnails |
| RULE_PHASE_SPLIT | phase-3/illustration-mapping-rules.md | Never cross phase boundaries in strips |
| RULE_DURATION_SPLIT | phase-3/illustration-mapping-rules.md | Max 12s per strip |
| RULE_STRIP_COVERAGE | phase-3/illustration-mapping-rules.md | Every VO line covered by exactly 1 strip |
| RULE_PROMPT_COMPONENTS | phase-3/visual-rules.md | Style lock + negative suffix |
| RULE_VIDEO_PARITY | phase-3/visual-rules.md | Every image has video prompt |

---

## Output Files Per Episode

```
pvle/episodes/{PV_xxxx}/
  episode_brief.md          ← P1 - single source of truth
  l2_breakdown_table.csv    ← P2 - beat table
  vo_draft_table.csv        ← P2 - EN draft per beat
  vo_enhanced_table.csv     ← P2 - EN humanized per line
  vo_finalize_table.csv     ← P2 - EN performance-optimized per line
  vo_script_table.csv       ← P2 - final EN + VI
  illustration_strip_table.csv ← P3 - strip grouping (VO to visual mapping)
  image_prompts.csv         ← P3 - Nano Banana
  video_prompts.csv         ← P3 - Veo
```

---

## Identity Modes

```
GENERIC_ARCHETYPE   → standard pipeline
TRANSPARENT_VEIL    → standard pipeline + veil-scan.md at VO step
HISTORICAL_FIGURE   → standard pipeline (no veil enforcement needed)
```
