---
description: Generate L2 breakdown table from episode brief (PVLE P2.0)
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-gen-breakdown

> **Phase:** 2.0 â€” Scripting  
> **Input:** `pvle/episodes/{EP}/episode_brief.md`  
> **Output:** `pvle/episodes/{EP}/l2_breakdown_table.csv`

---

## STEP 1: Read Episode Brief

Load `episode_brief.md`:
- Extract: Structure_ID, Duration_Profile, Phase Outline, Key Locations, Stickman_Accessory
- Load `phase-1/ideation-rules.md` â†’ phase beat_types, duration profile word targets

---

## STEP 2: Calculate Beat Budget

From Duration_Profile:
```yaml
STANDARD:  word_target â‰ˆ 784-1176 (8-12 min Ã— 70% Ã— 140 WPM)
EXTENDED:  word_target â‰ˆ 1176-1470 (12-15 min Ã— 70% Ã— 140 WPM)

beat_budget per phase (STANDARD as example):
  HOOK:              10-15% of total â†’ 2-3 beats
  PHASE_EARLY:       20-25% â†’ 3-4 beats
  PHASE_CONFLICT:    25-30% â†’ 4-5 beats
  PHASE_CRISIS:      10-15% â†’ 2-3 beats
  PHASE_RESOLUTION:  15-20% â†’ 2-3 beats
  CALLBACK_CLOSE:    5-10%  â†’ 1-2 beats
```

---

## STEP 3: Expand Outline Bullets â†’ Beats

For each bullet in Phase Outline from episode_brief.md, create 1 beat row.

Per beat, assign:
- `Beat_ID`: `BEAT_[phase_num]_[beat_num]` (e.g. BEAT_01_01)
- `Life_Phase`: from phase
- `Beat_Type`: most appropriate from Enum (ESTABLISH/TIME_MARKER/PRIVILEGE/CONSTRAINT/CONFLICT/CRISIS/REFLECT/RESOLVE/CALLBACK/CTA)
- `Content_Sketch`: 1-sentence summary of beat
- `Mood_Tag`: from phase-1/ideation-rules.md phase emotional arc
- `Beat_Duration_Sec`: calculated from word budget / 140 WPM
- `Scene_Type`: based on RULE_SCENE_TYPE_PER_PHASE from core/validation-core.md
- `Illustration_Note`: 1-line visual description

---

## STEP 4: Validate

Before output:
- [ ] Total Beat_Duration_Sec sum â‰ˆ Target_Duration_Min Ã— 60 Ã— 0.7 (Â±10%)
- [ ] All 6 phases represented
- [ ] HOOK has â‰¥ 2 beats
- [ ] PHASE_CRISIS has â‰¥ 2 beats
- [ ] CALLBACK_CLOSE has â‰¥ 1 CALLBACK + 1 CTA beat
- [ ] Scene_Type distribution follows core/validation-core.md RULE_SCENE_TYPE_PER_PHASE

---

## STEP 5: Output

**RULE_SILENT_OUTPUT:** CSV only, no commentary.

File: `pvle/episodes/{EP}/l2_breakdown_table.csv`

Columns: `Beat_ID,Life_Phase,Beat_Type,Content_Sketch,Mood_Tag,Beat_Duration_Sec,Scene_Type,Illustration_Note`

---

## USER INPUT

> `Episode_ID`: {{Episode_ID}}

