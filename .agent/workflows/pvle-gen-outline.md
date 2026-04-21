---
description: Generate telegraphic phase outline from confirmed world and episode concept (PVLE P1.1)
skills_required:
  - pvle-engine
  - skill-ideation
---

# WORKFLOW: /pvle-gen-outline

> **Phase:** 1.1 - Ideation  
> **Input:** Confirmed World_ID + episode concept (from /analyze-seed)  
> **Output:** Approved Episode Title + Telegraphic bullet outline per life phase (inline, Vietnamese)

## EXECUTION_CHECKLIST

```yaml
total_steps: 6
steps:
  - step: 1
    name: "Read World Data"
    type: AUTO
    output: "inline (world context loaded)"

  - step: 2
    name: "Determine Structure"
    type: AUTO
    output: "inline (Structure_ID selected)"

  - step: 3
    name: "Generate Episode Title Options"
    type: BLOCKING
    gate: "Wait for user to select title A/B/C or provide custom"
    output: "inline (3 title options displayed)"

  - step: 4
    name: "Generate Phase Outline"
    type: AUTO
    output: "inline (telegraphic outline)"

  - step: 5
    name: "Display + Wait for User"
    type: BLOCKING
    gate: "Wait for user to confirm or edit outline"
    output: "inline display"

  - step: 6
    name: "Proceed"
    type: AUTO
    output: "inline (confirmation message)"

# On completion: verify all steps checked
# On skip: VIOLATION -> HALT_AND_REPORT
```

---

## STEP 1: Read World Data

Load `pvle/worlds/{WORLD_ID}.yaml`:
- Extract: key_facts, key_tensions, key_locations, accessory_tags

---

## STEP 2: Determine Structure

Based on world domain and privilege_type, select Structure_ID:
- GOVERNMENT / ROYALTY + HIGH privilege -> `LIFE_PRIVILEGE`
- Any domain + ADVERSITY -> `LIFE_ADVERSITY`
- CRIMINAL / INTELLIGENCE + secret -> `LIFE_HIDDEN_POWER`
- IMPOSSIBLE_CHOICE context -> `LIFE_IMPOSSIBLE_CHOICE`
- LEGACY of famous person -> `LIFE_LEGACY`

---

## STEP 3: Generate Episode Title Options (BLOCKING)

> **Purpose:** Ensure user selects the best title BEFORE outline is generated.
> **Applies to ALL flows** - both Generic seed and Named Entity seed.

Generate **3 title options** in the format: `"Your Life as [ANCHOR]"`

```yaml
title_option_rules:
  - Anchor must uniquely capture the emotional CORE of this episode
  - Anchor must be factually grounded in world data
  - Try one per angle: status/role / emotional hook / cultural impact
  - For TRANSPARENT_VEIL: anchor must NOT reveal real name
  - For GENERIC_ARCHETYPE: anchor describes the role/situation

format: "Your Life as [ANCHOR]"
```

**Output (display to user):**

```
🎬 3 title options cho episode nay:

A: "Your Life as [ANCHOR_A]"
   -> [1-line description of angle/focus]

B: "Your Life as [ANCHOR_B]"
   -> [1-line description of angle/focus]

C: "Your Life as [ANCHOR_C]"
   -> [1-line description of angle/focus]

-> Chon A / B / C / hoac de xuat title rieng?
```

**WAIT for user selection. Do NOT proceed to Step 4 until title is confirmed.**

---

## STEP 4: Generate Phase Outline

Generate a **telegraphic bullet outline** - short phrases only (3-8 words each), NO full sentences.

Format per phase:

```
## [HOOK]
- [key moment / opening image - 3-8 words]
- [weight line - 3-6 words]

## [PHASE_EARLY: Childhood]
- [key childhood contrast/event 1]
- [key childhood contrast/event 2]
- [key childhood contrast/event 3]
- [time skip marker: age X -> age Y]

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

Output language: **Vietnamese** (tom tat y, khong phai VO)

---

## STEP 5: Display + Wait for User

Display outline inline. Ask:
- "Chot outline nay?" OR
- "Muon thay doi gi?"

Wait for confirmation or edits.

---

## STEP 6: Proceed

On user confirmation:
```
✅ Outline confirmed
   Title: "[approved title]"
-> Ready for: /pvle-gen-episode-brief
```

---

## USER INPUT

> `World_ID`: {{World_ID}}  
> `Episode_Concept`: {{episode_concept_note}}
