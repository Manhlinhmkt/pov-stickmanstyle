---
trigger: always_on
---

# WORKFLOW STRICT MODE - ENGINE METHODOLOGY

> **Version:** v2025-Engine  
> **Scope:** Workflow Execution Compliance  
> **Principle:** Strict Sequential Execution

---

## 1. WORKFLOW EXECUTION RULES

### RULE_16: Workflow Step Compliance (MANDATORY)

When executing any workflow from `.agent/workflows/`:

```yaml
execution_mode: STRICT
step_order: SEQUENTIAL
optimization: FORBIDDEN
```

**Requirements:**
- Execute steps in EXACT order as written in workflow file
- Do NOT skip steps for perceived efficiency
- Do NOT combine multiple steps into one
- Do NOT optimize or reorder steps
- Report completion after EACH major step

---

### RULE_17: File Operations During Workflow

When inside an active workflow execution:

```yaml
file_read: AUTO_APPROVE
file_write: AUTO_APPROVE
ask_permission: DISABLED
```

**Behavior:**
- Do NOT ask for user permission to read files referenced in workflow
- Do NOT ask for user permission to write output files specified in workflow
- Only ask permission for operations OUTSIDE workflow scope
- Treat workflow file references as pre-approved by user

---

### RULE_18: Turbo Mode Control

```yaml
turbo_default: DISABLED
turbo_activation: EXPLICIT_ANNOTATION_ONLY
```

**Behavior:**
- Do NOT auto-run steps unless explicitly annotated with `// turbo`
- Do NOT set `SafeToAutoRun: true` unless step has `// turbo` annotation
- Exception: `// turbo-all` annotation enables turbo for entire workflow

---

### RULE_19: Execution Checklist Verification (MANDATORY)

Every workflow file contains an `EXECUTION_CHECKLIST` at the top.

```yaml
behavior:
  on_workflow_start: "Read EXECUTION_CHECKLIST first"
  on_each_step: "Mentally check off completed step"
  on_workflow_end: "Verify ALL steps in checklist are completed"
  on_missing_step: "HALT_AND_REPORT - do NOT skip"

verification:
  before_reporting_completion:
    - "Count completed steps vs total_steps in checklist"
    - "If count mismatch: ABORT completion, find skipped step"
    - "If all match: report completion with step summary"
```

**On Violation:**
- If a step is found skipped after completion report: REOPEN workflow
- Execute skipped step before final confirmation

---

### RULE_20: Gate Enforcement (MANDATORY)

Steps marked `type: BLOCKING` in EXECUTION_CHECKLIST require explicit user response.

```yaml
BLOCKING_behavior:
  action: "Display output, then STOP and WAIT"
  forbidden:
    - "Assuming user approved based on silence"
    - "Auto-proceeding after displaying output"
    - "Inferring approval from context"
    - "Combining BLOCKING step output with next step"
  
  valid_user_responses:
    - Explicit confirmation: "ok", "proceed", "approved", "confirmed"
    - Edit request: any modification instruction
    - Rejection: "no", "change", "redo"

AUTO_behavior:
  action: "Execute immediately, report inline, continue to next step"
  no_wait: true
```

---

## 2. WORKFLOW STEP REPORTING

After each major step:
- [ ] Confirm step completed
- [ ] Show output file created (if any)
- [ ] State next step before executing

**Format:**
```
Step [N] completed: [description]
   Output: [file path]
-> Next: Step [N+1]: [description]
```

---

## 3. VIOLATION HANDLING

If unable to complete a step:
- Do NOT skip to next step
- Report blocker to user
- Wait for user instruction before proceeding

```yaml
on_step_failure: HALT_AND_REPORT
skip_step: FORBIDDEN
auto_recovery: DISABLED
```
