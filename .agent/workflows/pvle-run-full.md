---
description: Full PVLE production pipeline — from seed to video prompts
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-run-full

> **Purpose:** Macro runner — executes all PVLE phases in sequence  
> **Use when:** Starting a new episode from scratch with a seed idea

---

## PIPELINE

```
Step 1:  /analyze-seed
         ├─ [Generic seed]      → world match or generate
         └─ [Named entity seed] → /pvle-extract-anchor
         ↓
Step 1c: Speech Time Input (user specifies target minutes → word budget calculated)
         ↓
Step 2:  /pvle-ingest-world (if new world)
Step 3:  /pvle-gen-outline
Step 4:  /pvle-gen-episode-brief  (includes Step 3b-VERIFY: research visual anchors)
Step 5:  /pvle-gen-breakdown
Step 6:  /pvle-gen-vo             (validates against speech_time_config: -10% / +20%)
Step 7:  /pvle-character-review   (generate visuals, user approve, save assets)
Step 8:  /pvle-gen-image-prompts  (prerequisite: Step 7 approved)
Step 9:  /pvle-gen-video-prompts
```

---

## EXECUTION RULES

```yaml
RULE_16_COMPLIANCE:
  - Execute steps in EXACT order as written
  - Do NOT skip steps
  - Do NOT combine steps
  - Report completion after EACH step

USER_CHECKPOINTS:
  - After Step 1 (/analyze-seed): WAIT for user to confirm world
  - After Step 3 (/pvle-gen-outline): WAIT for user to confirm outline
  - After Step 4 (/pvle-gen-episode-brief): WAIT for user to confirm CHARACTER REGISTRY
  - After Step 7 (/pvle-character-review): WAIT for user to approve character visuals
  - All other steps: AUTO-PROCEED (no wait required)

TURBO_MODE: DISABLED (default)
```

---

## STEP REPORTING FORMAT

After each step:

```
✅ Step [N] completed: [step name]
   Output: [file path if applicable]
→ Next: Step [N+1]: [description]
```

---

## ERROR HANDLING

```yaml
on_step_failure: HALT_AND_REPORT
skip_on_failure: FORBIDDEN
auto_recovery: DISABLED
message: "Report blocker, wait for user instruction"
```

---

## USER INPUT

> `Seed`: {{seed_text}}
