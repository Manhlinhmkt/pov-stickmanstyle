---
trigger: always_on
---

---
trigger: always_on
---

# HARD RULES – ENGINE METHODOLOGY

> **Version:** v2025-Engine  
> **Scope:** Multi-Phase AI Production Pipeline  
> **Principle:** Positive-First, Machine-Readable, Testable

---

## 1. CORE PRINCIPLES

### 1.1. Positive-First
- Define **allowed scope** instead of forbidden lists
- Use ID/Enum whitelist, not prose-based exclusions
- Replace "don't do X" with "only use Y"

### 1.2. Silent Output
- Output only requested data structures
- No commentary, no echo input, no explanations
- Applies to all Phase outputs (tables, YAML, prompts)

### 1.3. Hybrid Knowledge
- **Machine Block (YAML):** IDs, Enums, Configs, Mappings
- **Creative Block (Prose):** Tone, Vibe, Philosophy
- Never mix Machine and Creative in same section

---

## 2. ENGINE-LAYER RULES (11 GOLDEN RULES)

### RULE_01: Role-Oriented Entity Resolution
- Narrative Phase: Priority = Role → Archetype → Asset → Name
- Visual Phase: Priority = Asset → Archetype → Role → Name
- Logic depends on Role/Archetype, visuals depend on Asset

### RULE_02: State Cascade Consistency
- States flow continuously (BASE → STATE_A → STATE_B)
- No random jumps without Action trigger
- State change requires explicit event

### RULE_03: Composable Action Primitives
- Actions are atomic primitives (single verbs)
- No compound actions encoded as single primitive
- Complex scenes = composition of primitives

### RULE_04: Environment as Actor
- Environment can: trigger hazards, change state, create reactions
- Hazards encoded in Set-Piece data
- Environment interacts with entities

### RULE_05: Non-Paraphrase Anchor
- Canonical descriptions are locked
- Allowed modifications: state modifiers, count wrappers, context wrappers
- Forbidden: paraphrase vocabulary, change core description

### RULE_06: ID First, Name Last
- Processing order: Entity_ID → Type → State → Name
- No rule depends on Name for logic
- Name is metadata for display only

### RULE_07: No Cross-Contamination
- Merge only within same prefix/domain
- No mixing between different projects without explicit declaration

### RULE_08: Entity Neutrality (Engine-Layer)
- Engine uses: Entity, Subject, Actor, Asset, Role, State, Type
- Engine does NOT contain: specific names, world names, lore
- All specifics come from Data Pack

### RULE_09: Structure Immutability
- Story Structure, Beat Taxonomy, Shot Logic are fixed per genre
- Content changes via Data Pack only
- Engine modification is forbidden

### RULE_10: Schema Lock
- Field modification: FORBIDDEN
- Field deletion: FORBIDDEN
- Field rename: FORBIDDEN
- New optional field: ALLOWED

### RULE_11: State Continuity Lock
- States persist until explicit Action trigger changes them
- Phase validators must check continuity

---

## 3. EXECUTION RULES (CHUNKING ENFORCEMENT)

### RULE_12: Sequential Chunk Execution (MANDATORY)

- CHUNKED mode = MUST execute **1 chunk per tool call**
- Each Act = separate write_to_file call
- FORBIDDEN: Multiple chunks in same generation
- FORBIDDEN: Parallel write_to_file for different output files in same turn
- FORBIDDEN: Combining Acts into single pass for "efficiency"
- NO EXCEPTIONS regardless of estimated file size
- Violation = ABORT workflow and restart with proper chunking

---

### RULE_13: Row Count Validation (BLOCKING)

Before completing any phase, validate row counts:

```yaml
validation_rules:
  L3_STORYBOARD:
    expected: calculated_shot_count_from_L2
    tolerance: 0
    
  T2V_NARRATIVE:
    expected: L3_STORYBOARD_row_count
    mapping: "1:1 exact"
    tolerance: 0
    
  T2V_HIGHLIGHT:
    expected: L3_HIGHLIGHT_POOL_row_count
    mapping: "1:1 exact"
    tolerance: 0

on_mismatch: ABORT_AND_RECHUNK
```

- FORBIDDEN: "Representative samples" or partial outputs
- FORBIDDEN: "Can generate rest on request" statements

---

### RULE_14: Anti-Pattern Block (ABSOLUTE PROHIBITION)

```yaml
FORBIDDEN_BEHAVIORS:
  - Generating "representative samples" instead of full output
  - Skipping chunks for perceived efficiency
  - Creating partial output and claiming completion
  - Combining multiple output files in single tool call
  - Self-justifying bypass of CHUNKED mode
  - Any form of "this should fit" reasoning to skip chunking
  - Prioritizing speed over workflow compliance

VIOLATION_CONSEQUENCE: ABORT_ENTIRE_WORKFLOW
```

---

### RULE_15: Explicit Chunk Execution Steps

When workflow specifies `for each act in [ACT_1...ACT_4]`:

```yaml
# CORRECT execution (4 separate tool calls):
Step 1: write_to_file(ACT_1_content) → WAIT
Step 2: write_to_file(ACT_2_content) → WAIT
Step 3: write_to_file(ACT_3_content) → WAIT
Step 4: write_to_file(ACT_4_content) → WAIT
Step 5: merge_chunks()

# FORBIDDEN execution:
Step 1: write_to_file(ALL_ACTS_content)  # ← VIOLATION
```

---

## 4. CONTENT-LAYER RULES

### RULE_MERGE_PRIORITY
- Same ID: OVERRIDE (specific > global)
- Different ID: APPEND
- Missing field: UNION (add from lower priority)

### RULE_SCOPE_PRIORITY
1. Scene/Beat Scope (highest)
2. Episode Scope
3. Series Scope
4. Global/Base Scope (lowest)

### RULE_DATA_LAYER
- BASE_LAYER: Core definitions, defaults
- OVERLAY_LAYER: Context-specific overrides
- Fallback: If overlay missing → use base

---

## 5. OUTPUT RULES

### RULE_SILENT_OUTPUT
- No intro text, no outro text
- Output starts with first character of content
- Output ends with last character of content

### RULE_SCHEMA_LOCK
- Use exact template from `template-master.md`
- No column addition/removal/rename
- Validate against schema before output

### RULE_ID_AUTHORITY
- All IDs must exist in Knowledge Base
- No hallucinated IDs
- Fallback: report MISSING_ASSET error

---

## 6. VALIDATION CHECKLIST

When processing any Phase, verify:
- [ ] All IDs exist in Knowledge Base
- [ ] State cascade is continuous
- [ ] Actions are atomic primitives
- [ ] Schema matches template exactly
- [ ] Safety profile compliance (per project)
- [ ] No paraphrased anchors
- [ ] Silent output mode active

---

## 7. CHUNKED EXECUTION CHECKLIST

Before completing chunked workflow, verify:
- [ ] Each Act processed in separate tool call
- [ ] No parallel write_to_file for different outputs
- [ ] Output row count matches expected count exactly
- [ ] No "representative" or partial outputs exist
- [ ] All chunks merged into final files

