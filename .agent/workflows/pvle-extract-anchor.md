---
description: Extract anonymized anchor title and build world data from a named real person (PVLE Named Entity Mode)
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-extract-anchor

> **Phase:** Pre-ideation (triggered from /analyze-seed when named entity detected)  
> **Purpose:** Named person -> anonymized title options -> TRANSPARENT_VEIL world data  
> **Output:** Confirmed title + world YAML ready for /pvle-ingest-world

## EXECUTION_CHECKLIST

```yaml
total_steps: 6
steps:
  - step: 1
    name: "Entity Classification"
    type: AUTO
    output: "inline (entity type + veil strictness)"

  - step: 2
    name: "Research Real Person's Public Profile"
    type: AUTO
    output: "inline (extraction schema)"

  - step: 3
    name: "Generate Anonymized Title Options"
    type: BLOCKING
    gate: "Wait for user to select title A/B/C or custom"
    output: "inline (3 title options displayed)"

  - step: 4
    name: "Confirm World ID"
    type: BLOCKING
    gate: "Wait for user to confirm World_ID"
    output: "inline (WORLD_ID displayed)"

  - step: 5
    name: "Assemble World YAML"
    type: AUTO
    output: "inline (YAML assembled)"

  - step: 6
    name: "Pass to /pvle-ingest-world"
    type: AUTO
    output: "pvle/worlds/{WORLD_ID}.yaml"

# On completion: verify all steps checked
# On skip: VIOLATION -> HALT_AND_REPORT
```

---

## STEP 1: Entity Classification

Identify the type of named entity from seed:

```yaml
LIVING_PUBLIC_FIGURE:
  examples: "Elon Musk, Jeff Bezos, Tim Cook, Taylor Swift"
  veil_strictness: MAXIMUM
  rules: "No name, no company names, no direct quotes, no private events"

POLITICAL_FIGURE:
  examples: "Obama, Trump, Macron, Xi Jinping"
  veil_strictness: MAXIMUM
  rules: "No name, no party, no policy positions attributed — only life circumstances"

HISTORICAL_FIGURE:
  examples: "Einstein, Da Vinci, Marie Curie, Napoleon"
  veil_strictness: MODERATE
  rules: "No name in VO, but era + field of work can be stated directly"
  note: "Deceased figures have looser defamation exposure"

FICTIONAL_ARCHETYPE:
  examples: "a billionaire, a president, a spy"
  veil_strictness: NONE
  action: "Redirect to standard /analyze-seed generic flow"
```

→ For "Elon Musk": `LIVING_PUBLIC_FIGURE`, veil_strictness = MAXIMUM

---

## STEP 2: Research Real Person's Public Profile

**Using only verified public information**, extract:

```yaml
extraction_schema:

  defining_roles:
    primary:    "[Most universally recognized role without name]"
    secondary:  "[Additional role / achievement]"
    tertiary:   "[Cultural moment / defining action]"

  era_anchors:
    birth:         "[Year + country — no city unless major]"
    key_milestone: "[Year + public event, no name required]"
    current_era:   "[Year range of peak public presence]"

  unique_circumstance_stack:
    - "[Specific verifiable fact about their life — not from name]"
    - "[Fact 2]"
    - "[Fact 3...]"
    (minimum 5, maximum 10 facts)

  public_perception_markers:
    - "[How public views them — polarizing / celebrated / controversial]"
    - "[Cultural conversation they are permanently part of]"

  forbidden_terms:
    names:     ["[first name]", "[last name]", "[nickname]"]
    companies: ["[Company 1]" → "replacement phrase", ...]
    places:    ["[Too-specific location]" → "replacement phrase"]
    titles:    ["[Official title if unique identifier]" → "replacement phrase"]
```

**Example extraction for "Elon Musk":**

```yaml
defining_roles:
  primary:    "the richest person on earth"
  secondary:  "the man who built rockets and electric cars simultaneously"
  tertiary:   "the man who bought the internet's most powerful town square"

era_anchors:
  - year: 1971, event: "Born in South Africa"
  - year: 1988, event: "Left for North America at 17 with almost nothing"
  - year: 2002, event: "Founded rocket company after selling first venture for $300M+"
  - year: 2021, event: "Became confirmed richest person alive"
  - year: 2022, event: "Purchased major global social media platform for $44B"

unique_circumstance_stack:
  - "Father owned mining operations in southern Africa — wealth that shaped and scarred"
  - "Taught himself programming, sold a video game at age 12 for $500"
  - "Arrived in North America with almost no money, slept on friend's couches"
  - "Invested entire personal fortune from first exit into rocket and car companies"
  - "Company nearly bankrupt three times — personally funded final launch"
  - "Sleeps on factory floor during production crises rather than going home"
  - "Has publicly stated he intends to die on Mars, not Earth"
  - "More than ten children with multiple partners across different decades"
  - "Works 80-120 hours weekly — describes it as a physical compulsion"

public_perception_markers:
  - "One of the most divisive figures of the 21st century — worshipped by some, despised by others"
  - "Every major decision analyzed by millions in real time"
  - "Name alone triggers strong reaction — no neutrality possible"

forbidden_terms:
  names:
    - "Elon" → "you"
    - "Musk" → [omit entirely]
  companies:
    - "Tesla" → "the electric car company"
    - "SpaceX" → "the rocket company" / "the Mars project"
    - "Twitter" → "the platform" / "the town square"
    - "X" → "the platform" (context-dependent)
    - "PayPal" → "the first company you built"
    - "Neuralink" → "the brain interface company"
    - "The Boring Company" → "the tunneling project"
  people:
    - "Grimes" → "the musician you shared a life with"
    - "Vivek" → [avoid entirely if possible]
  places:
    - "Pretoria" → "a city in South Africa"
    - "Hawthorne" → [avoid — too specific]
```

---

## STEP 3: Generate Anonymized Title Options

Generate **3 title options** in the format: `"Your Life as [ANCHOR]"`

```yaml
title_option_rules:
  - Anchor must uniquely identify the implied person WITHOUT naming them
  - Anchor must be true (factually accurate)
  - Anchor should reflect the emotional CORE of the episode, not just status
  - Try one per: wealth/status angle / ambition angle / cultural impact angle

format: "Your Life as [ANCHOR]"
```

**Output (display to user):**

```
Based on your seed, 3 title options:

A: "Your Life as the Richest Person Alive"
   → Anchor: wealth + status. Immediately recognizable. Episodes focuses on cost of wealth.

B: "Your Life as the Man Who Bet Everything on Mars"
   → Anchor: ambition + obsession. Focuses on the compulsion beneath the achievement.

C: "Your Life as the Man Who Built the Future and Couldn't Stop"
   → Anchor: compulsion + creation. Focuses on the psychological engine behind the empire.

→ Which title do you want? (A / B / C / custom)
```

Wait for user selection.

---

## STEP 4: Confirm World ID

Generate `WORLD_ID` from approved anchor:

```yaml
WORLD_ID_format: "WORLD_{DOMAIN}_{KEY_ANCHOR}"
example: "WORLD_TECH_RICHEST_ALIVE" or "WORLD_TECH_MARS_VISIONARY"
```

Display to user for quick confirmation.

---

## STEP 5: Assemble World YAML

Assemble full world YAML using extracted data + `implied_identity_mode: TRANSPARENT_VEIL`:

```yaml
WORLD_ID: [confirmed_id]
display_name: "[approved title without 'Your Life as']"
domain: [detected from entity type]
era: MODERN_CONTEMPORARY
implied_identity_mode: TRANSPARENT_VEIL
implied_person: "[full real name — INTERNAL ONLY, never appears in any output]"
veil_strictness: MAXIMUM

tags: [...]

seed_keywords:
  - "[real person's name]" ← for future match detection only
  - "[anchor phrase]"
  - "[role descriptor]"

era_anchors: [from Step 2]
unique_circumstance_stack: [from Step 2]
public_perception_markers: [from Step 2]
forbidden_terms: [from Step 2]

key_tensions:
  - [auto-derived from circumstance stack]

accessory_tags:
  - [derived from world — e.g., "rocket model" for space founder]

used_in_episodes: []
created: "[today]"
```

---

## STEP 6: Pass to /pvle-ingest-world

Auto-trigger `/pvle-ingest-world` with assembled YAML.

```
✅ Named Entity Mode complete
   Implied identity: [real name] (INTERNAL ONLY)
   World ID: [WORLD_ID]
   Title: "[approved title]"
   Veil: TRANSPARENT_VEIL / MAXIMUM
→ Next: /analyze-seed Step 1c (speech time input) → then /pvle-gen-outline [WORLD_ID]
```

---

## USER INPUT

> `Named_Entity_Seed`: {{seed_with_real_person_name}}
