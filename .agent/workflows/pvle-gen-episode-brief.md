---
description: Generate PVLE episode brief from confirmed outline (P1.2)
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-gen-episode-brief

> **Phase:** 1.2 — Ideation  
> **Input:** Confirmed outline (from /pvle-gen-outline) + World_ID  
> **Output:** `pvle/episodes/{EP}/episode_brief.md`

---

## STEP 1: Assign Episode ID

Check `pvle/episodes/` for existing episodes. Assign next available `PV_xxxx`.

---

## STEP 2: Load References

- Load `pvle/worlds/{WORLD_ID}.yaml` → key_facts, key_tensions, key_locations, accessory_tags, **character_anchors**
- Load `phase-1/ideation-rules.md` → duration profile, phase emotional arcs
- Load `phase-2/scripting-rules.md` → WPM defaults

---

## STEP 3: Generate episode_brief.md Structure

Write content using the following structure:

```markdown
# Episode Brief — {Episode_ID}

## METADATA
| Field | Value |
|-------|-------|
| Episode_ID | PV_xxxx |
| Episode_Title | [Full English title] |
| World_ID | [WORLD_ID] |
| Identity_Mode | TRANSPARENT_VEIL |
| Structure_ID | [LIFE_PRIVILEGE / etc.] |
| Duration_Profile | STANDARD / EXTENDED |
| Target_Duration_Min | {{speech_time_config.target_minutes}} |
| Word_Budget | {{speech_time_config.word_budget_min}} - {{speech_time_config.word_budget_max}} |
| Hook_Type | [from phase-1/ideation-rules.md] |
| Core_Tension | [from world key_tensions — primary one] |
| Secondary_Tensions | [other tensions] |
| Stickman_Accessory | [primary accessory from world accessory_tags] |

## WORLD CONTEXT
- **Domain:** [from world yaml]
- **Era:** [from world yaml]
- **Veil Strictness:** [from world yaml]

### Key Facts Used
[Numbered list of specific facts and how they appear in narrative]

### Key Locations
[LOC_ID list with brief description per location]

### Key Tensions
[List with one-line description of how each tension manifests in episode]

## CONFIRMED OUTLINE
### HOOK
[2-3 bullet telegraphic beats]
### PHASE_EARLY
[3-4 bullet beats]
### PHASE_CONFLICT
[4-5 bullet beats]
### PHASE_CRISIS
[2-3 bullet beats]
### PHASE_RESOLUTION
[2-3 bullet beats]
### PHASE_PRESENT (if applicable)
[3-5 bullet beats]
### CALLBACK_CLOSE
[1-2 bullet beats]

## CHARACTER REGISTRY
> Source: `{WORLD_ID}.yaml → character_anchors`  
> Approved: [date]. Used by `/pvle-gen-image-prompts`.

### Master Character Table
| Char_ID | Veil_Name | Visual_Summary | Appears_In_Phases |

### SUBJECT Visual Traits by Phase
| Phase | Age_Range | Height | Hair | Clothing | Face | Distinguishing |

### Injection Rules
- SUBJECT always has most visual detail among all characters in scene
- AGENTS are always FACELESS — blank white circle head, no eyes, no mouth
- REAL NAMES FORBIDDEN in prompts — use veil_name only
- Height must scale — SUBJECT becomes progressively taller stickman across phases

## EPISODE NOTES
[Duration, beat count, veil enforcement notes, emotional arc, callback structure]
```

---

## STEP 3b: Extract CHARACTER REGISTRY

From `character_anchors` in `pvle/worlds/{WORLD_ID}.yaml`, extract and generate:

**Master Character Table:**
| Char_ID | Veil_Name | Visual_Summary | Appears_In_Phases |

**SUBJECT Visual Traits by Phase** (for all phases appearing in this episode):
| Phase | Age_Range | Height | Hair | Clothing | Face | Distinguishing |

Phase-to-age mapping:
```yaml
CHILD_0_6:    → HOOK, PHASE_EARLY (early, age 0-6)
CHILD_7_12:   → PHASE_EARLY (late, age 7-12)
TEEN_13_17:   → PHASE_CONFLICT (age 13-17)
ADULT_18_PLUS: → PHASE_CRISIS, PHASE_RESOLUTION, PHASE_PRESENT, CALLBACK_CLOSE
```

Injection Rules to always include:
- SUBJECT always has most visual detail among all characters
- AGENTS are always FACELESS — blank white circle head, no eyes, no mouth
- REAL NAMES FORBIDDEN in prompts — use veil_name only
- Height must scale — SUBJECT becomes progressively taller stickman across phases

---

## STEP 3c: ★ PAUSE — User Review of CHARACTER REGISTRY ★

Show the generated CHARACTER REGISTRY table to user BEFORE writing episode_brief.md.

Ask:
1. Confirm or adjust SUBJECT visual traits per phase
2. Confirm or remove supporting characters not used in this episode
3. Any phase-specific visual notes to add

**WAIT for explicit user approval before proceeding to STEP 4.**

---

## STEP 4: Save File

Save to: `pvle/episodes/{Episode_ID}/episode_brief.md`

Create directory if it doesn't exist.

Include the USER-APPROVED CHARACTER REGISTRY section in the file (between CONFIRMED OUTLINE and EPISODE NOTES).

---

## STEP 5: Update World Index

Add Episode_ID to `used_in_episodes` list in `pvle/worlds/{WORLD_ID}.yaml`.

---

## STEP 6: Confirm

```
✅ Episode brief created: pvle/episodes/{EP}/episode_brief.md
→ Ready for: /pvle-gen-breakdown {EP}
```

---

## USER INPUT

> `World_ID`: {{World_ID}}  
> `Outline`: {{confirmed_outline}}
