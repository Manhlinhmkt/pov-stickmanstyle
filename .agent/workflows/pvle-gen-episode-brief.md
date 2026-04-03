---
description: Generate PVLE episode brief from confirmed outline (P1.2)
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-gen-episode-brief

> **Phase:** 1.2 â€” Ideation  
> **Input:** Confirmed outline (from /pvle-gen-outline) + World_ID  
> **Output:** `pvle/episodes/{EP}/episode_brief.md`

---

## STEP 1: Assign Episode ID

Check `pvle/episodes/` for existing episodes. Assign next available `PV_xxxx`.

---

## STEP 2: Load References

- Load `pvle/worlds/{WORLD_ID}.yaml` â†’ key_facts, key_tensions, key_locations, accessory_tags
- Load `phase-1/ideation-rules.md` â†’ duration profile, phase emotional arcs
- Load `phase-2/scripting-rules.md` â†’ WPM defaults

---

## STEP 3: Generate episode_brief.md

Write file using TPL_EPISODE_METADATA schema from `core/template-master.md`.

Structure:
```markdown
# Episode Brief â€” {Episode_ID}

## Metadata
| Field | Value |
|-------|-------|
| Episode_ID | PV_xxxx |
| Episode_Title | [Full English title] |
| World_ID | [WORLD_ID] |
| Structure_ID | [LIFE_PRIVILEGE / etc.] |
| Duration_Profile | STANDARD / EXTENDED |
| Target_Duration_Min | [number] |
| Voice_Profile | VOICE_POV_DRAMATIST |
| Avg_WPM | 140 |
| Hook_Type | [from phase-1/ideation-rules.md] |
| Core_Tension | [from world key_tensions â€” primary one] |
| Stickman_Accessory | [primary accessory from world accessory_tags] |

## Emotional Arc
[One paragraph describing the WONDERâ†’[middle]â†’BITTERSWEET arc of this specific episode]

## Opening Scene
[Description of first visual â€” what viewer sees in first 10 seconds]

## Key Locations Used
- [LOC_ID]: [location name + how used in episode]
- [LOC_ID]: ...

## World Key Facts Used
- [Specific fact from WORLD_*.yaml and how it appears in narrative]
- ...

## Phase Outline
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

### CALLBACK_CLOSE
[1-2 bullet beats]

## Episode Notes
[Any special tone, pacing, or thematic notes for this specific episode]
```

---

## STEP 4: Save File

Save to: `pvle/episodes/{Episode_ID}/episode_brief.md`

Create directory if it doesn't exist.

---

## STEP 5: Update World Index

Add Episode_ID to `used_in_episodes` list in `pvle/worlds/{WORLD_ID}.yaml`.

---

## STEP 6: Confirm

```
âœ… Episode brief created: pvle/episodes/{EP}/episode_brief.md
â†’ Ready for: /pvle-gen-breakdown {EP}
```

---

## USER INPUT

> `World_ID`: {{World_ID}}  
> `Outline`: {{confirmed_outline}}

