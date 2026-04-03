---
description: Generate telegraphic phase outline from confirmed world and episode concept (PVLE P1.1)
skills_required:
  - pvle-engine
  - skill-ideation
---

# WORKFLOW: /pvle-gen-outline

> **Phase:** 1.1 — Ideation  
> **Input:** Confirmed World_ID + episode concept (from /analyze-seed)  
> **Output:** Telegraphic bullet outline per life phase (inline, Vietnamese)

---

## STEP 1: Read World Data

Load `pvle/worlds/{WORLD_ID}.yaml`:
- Extract: key_facts, key_tensions, key_locations, accessory_tags

---

## STEP 2: Determine Structure

Based on world domain and privilege_type, select Structure_ID:
- GOVERNMENT / ROYALTY + HIGH privilege → `LIFE_PRIVILEGE`
- Any domain + ADVERSITY → `LIFE_ADVERSITY`
- CRIMINAL / INTELLIGENCE + secret → `LIFE_HIDDEN_POWER`
- IMPOSSIBLE_CHOICE context → `LIFE_IMPOSSIBLE_CHOICE`
- LEGACY of famous person → `LIFE_LEGACY`

---

## STEP 3: Generate Phase Outline

Generate a **telegraphic bullet outline** — short phrases only (3-8 words each), NO full sentences.

Format per phase:

```
## [HOOK]
- [key moment / opening image — 3-8 words]
- [weight line — 3-6 words]

## [PHASE_EARLY: Childhood]
- [key childhood contrast/event 1]
- [key childhood contrast/event 2]
- [key childhood contrast/event 3]
- [time skip marker: age X → age Y]

## [PHASE_CONFLICT: Adolescence / Rising tension]
- [conflict catalyst 1]
- [conflict catalyst 2]
- [internal conflict moment]

## [PHASE_CRISIS: The defining moment]
- [crisis trigger]
- [impossible situation]
- [stakes stated]

## [PHASE_RESOLUTION: After]
- [time skip to resolution age]
- [what was gained]
- [what was permanently lost]

## [CALLBACK_CLOSE]
- [mirror of hook image]
- [final weight line]
```

Output language: **Vietnamese** (tóm tắt ý, không phải VO)

---

## STEP 4: Display + Wait for User

Display outline inline. Ask:
- "Chốt outline này?" OR
- "Muốn thay đổi gì?"

Wait for confirmation or edits.

---

## STEP 5: Proceed

On user confirmation:
```
✅ Outline confirmed
→ Ready for: /pvle-gen-episode-brief
```

---

## USER INPUT

> `World_ID`: {{World_ID}}  
> `Episode_Concept`: {{episode_concept_note}}
