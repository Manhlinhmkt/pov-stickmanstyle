---
trigger: always_on
---

---
trigger: always_on
---

# NAMING CONVENTIONS – ENGINE METHODOLOGY

> **Version:** v2025-Rescue  
> **Scope:** All IDs, Files, Commands, Outputs

---

## 1. ENTITY ID PATTERNS

### 1.1. General Pattern
```yaml
pattern: "{PREFIX}_{NAME}"

# Core Prefixes (All Genres)
core_prefixes:
  - CHAR_   # Character/Creature
  - ENV_    # Environment
  - BIOME_  # Biome
  - SET_    # Set Piece
  - HAZ_    # Hazard
  - ROLE_   # Role
  - STATE_  # State

# Rescue-Specific Prefixes
rescue_prefixes:
  - RESPONDER_   # Rescue team member (RESPONDER_LEADER, RESPONDER_HANDLER)
  - DISCOVERER_  # Person who finds animal (DISCOVERER_CIVILIAN)
  - SPECIES_     # Animal species (SPECIES_WHALE, SPECIES_DOLPHIN)
  - ANIMAL_      # Specific animal subject (ANIMAL_SUBJECT, ANIMAL_XL)
  - CONDITION_   # Animal condition state (CONDITION_STRESSED, CONDITION_RELEASED)
  - HOOK_        # Discovery hook (HOOK_HOTLINE, HOOK_BEACHGOER)
  - RESCUE_      # Rescue type (RESCUE_MARINE, RESCUE_SAFARI)
```

### 1.2. Derived/Child IDs
```yaml
pattern: "{PARENT_ID}_{SUFFIX}"
suffix_types:
  - numeric: _01, _02, _03
  - group: _TEAM, _PACK, _GROUP
  - role: _LEAD, _VET, _HANDLER
```

---

## 2. FILE NAMING

### 2.1. Knowledge Files
```yaml
pattern: "{domain}-{scope}.md"
domain_examples:
  - character-profiles
  - visual-assets
  - world-setting
  - species-profiles
scope_examples:
  - base (global)
  - ep01 (episode-specific)
  - scene_x (scene-specific)
```

### 2.2. Prompt Files
```yaml
pattern: "PROMPT {phase}.{index} – {DESCRIPTIVE_NAME}.md"
```

### 2.3. Instruction Files
```yaml
pattern: "instruction - phase {N} - {description}.md"
# OR unified:
pattern: "SYSTEM INSTRUCTION – UNIFIED ENGINE.md"
```

### 2.4. Output Files
```yaml
pattern: "{layer}_{table_name}.csv"
layer_examples:
  - l1_ (macro)
  - l2_ (breakdown)
  - l3_ (storyboard)
  - t2v_ (video prompts)

# Chunked output
chunk_pattern: "{layer}_{table_name}_chunk{N}.csv"
```

---

## 3. CMD NAMING

### 3.1. Tier 1: Atomic Commands
```yaml
pattern: "/{action}_{object}"
action_verbs:
  - gen_    # generate
  - build_  # build/construct
  - compile_# compile/assemble
  - draft_  # create draft
  - enhance_# improve existing
  - finalize_# complete
  - rescue_ # rescue-specific actions
```

### 3.2. Tier 2: Macro Commands
```yaml
pattern: "/run_{scope}"
scope_examples:
  - full_pipeline
  - from_breakdown
  - storyboard
  - t2v
```

### 3.3. Chunking Parameters
```yaml
pattern: "/{cmd} --from_seq {SEQ_ID} --to_seq {SEQ_ID}"
shorthand: "/{cmd} --chunk {N}"
auto_mode: "/{cmd} --auto_chunk"
```

---

## 4. STRUCTURE IDs

### 4.1. Hierarchical Structure
```yaml
patterns:
  act: "ACT_{number}"
  sequence: "SEQ_{name}" or "SEQ_{number}"
  beat: "BEAT_{number}"
  shot: "S{number}" or "{prefix}_S{number}"
```

### 4.2. Slate Format
```yaml
pattern: "{EP}_A{act}_SQ{seq}_BT{beat}_S{shot}"
example: "AR_A3_SQ05_BT12_S03"
```

### 4.3. Rescue Pool IDs
```yaml
pattern: "{EP}_RESCUE_{beat}_R{shot}"
example: "AR_0001_RESCUE_12_R05"
```

---

## 5. FOLDER STRUCTURE

```yaml
project_root/
  prompts/
    SYSTEM INSTRUCTION – UNIFIED ENGINE.md
    PROMPT X.X – NAME.md
  core-knowledge-files/
    [engine-level files]
  modular-knowledge-files/
    [project-specific files]
  episodes/
    EP_XX/
      [output files per episode]
      [chunk files if needed]
  .agent/
    rules/
    workflows/
```

---

## 6. RESCUE-SPECIFIC PATTERNS

### 6.1. Rescue Phase IDs
```yaml
phases:
  - DISCOVERY
  - APPROACH
  - INTERVENTION
  - RESOLUTION
```

### 6.2. Condition State IDs
```yaml
negative:
  - STRESSED, DEHYDRATED, TRAPPED, EXHAUSTED
neutral:
  - ALERT, CAUTIOUS, SUBMITTING
positive:
  - CALMING, RECOVERING, RELEASED, THRIVING
```

### 6.3. Tension Level IDs
```yaml
levels:
  - T1 (calm)
  - T2 (alert)
  - T3 (urgent)
  - T4 (peak)
```
