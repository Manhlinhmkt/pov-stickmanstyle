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
Step 1: /analyze-seed
        ├─ [Generic seed]      → world match or generate → Steps 2-8
        └─ [Named entity seed] → /pvle-extract-anchor → Steps 3-8

Step 2: /pvle-ingest-world (if new world)
Step 3: /pvle-gen-outline
Step 4: /pvle-gen-episode-brief
Step 5: /pvle-gen-breakdown
Step 6: /pvle-gen-vo               (includes Veil Enforcement if TRANSPARENT_VEIL)
Step 7: /pvle-gen-image-prompts
Step 8: /pvle-gen-video-prompts
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
