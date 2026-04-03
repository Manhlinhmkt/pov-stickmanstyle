# VALIDATION CORE — POV Life Simulation Engine (PVLE)

> **Scope:** Cross-phase rules — apply in ALL phases  
> **Load:** Every workflow loads this file  
> **Note:** Phase-specific rules live in phase-1/, phase-2/, phase-3/ modules

---

## RULE_POV_CONSISTENCY
```yaml
description: "Subject must always be 'you' — never switch to 3rd person"
check: "Scan every VO_EN/JA/VI line for 'he', 'she', 'they' referring to subject"
forbidden:
  - "He walked into the room."    # → "You walked into the room."
  - "She realized that day..."    # → "You realized that day..."
on_violation: FIX_BEFORE_OUTPUT
applies_to: [phase-2, phase-3]
```

## RULE_TIMELINE_CONTINUITY
```yaml
description: "Ages and events must progress forward — no regression"
check: "TIME_MARKER ages must always increase within episode"
forbidden:
  - Age going backwards without explicit flashback marker
  - Events from PHASE_RESOLUTION referenced in PHASE_CONFLICT as future
on_violation: FIX_BEFORE_OUTPUT
applies_to: [phase-1, phase-2]
```

## RULE_ACCURACY
```yaml
description: "All world facts must be accurate and verifiable"
check: "Facts must come from World_ID key_facts or unique_circumstance_stack"
forbidden: "Pure fantasy without real-world anchor"
allowed: "Extrapolation clearly framed as interpretive"
on_violation: REMOVE_OR_VERIFY
applies_to: [all]
```

## RULE_NO_PREACHING
```yaml
description: "Moral lessons shown via narrative — never stated"
forbidden:
  - "This teaches us that..."
  - "The lesson here is..."
  - Direct moral instruction of any kind
required: "Let viewer draw their own conclusion"
on_violation: REPHRASE_AS_EXPERIENCE
applies_to: [phase-2]
```

## RULE_WORLD_EXISTS
```yaml
check: "World_ID in episode_brief.md must exist in core/world-index.yaml"
if_not_found: "Run /analyze-seed → confirm → /pvle-ingest-world → then proceed"
applies_to: [all]
```

## RULE_FACTS_FROM_WORLD
```yaml
check: "World_Key_Facts_Used must be subset of key_facts in WORLD_*.yaml"
forbidden: "Adding facts in episode that contradict WORLD_*.yaml"
allowed: "Episode can use FEWER facts than world has"
applies_to: [phase-1, phase-2]
```

## RULE_PRIORITY_ORDER
```yaml
description: "When two rules conflict, resolve in this order"
priority:
  1: RULE_POV_CONSISTENCY       # always wins
  2: RULE_ACCURACY              # facts cannot be changed for style
  3: RULE_TIMELINE_CONTINUITY   # structure is fixed
  4: RULE_NO_PREACHING          # tone is adjusted last
applies_to: [all]
```
