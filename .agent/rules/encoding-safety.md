---
trigger: always_on
---

# ENCODING SAFETY RULE

> **Version:** v1.0
> **Scope:** All generated output files (CSV, MD, TXT, YAML)
> **Root cause:** Em dash (U+2014) and en dash (U+2013) cause mojibake when files transit through Windows cp1252 editors

---

## RULE_NO_UNICODE_DASH

**In ALL output data fields (CSV cells, markdown body text, YAML values):**

```yaml
FORBIDDEN_CHARACTERS:
  - "\u2014"   # em dash (—)
  - "\u2013"   # en dash (–)
  - "\u2018"   # left single quote (')
  - "\u2019"   # right single quote (')
  - "\u201C"   # left double quote ("")
  - "\u201D"   # right double quote ("")
  - "\u2026"   # horizontal ellipsis (…)

REPLACEMENT_MAP:
  em_dash:     " - "     # space-hyphen-space
  en_dash:     " - "     # space-hyphen-space
  left_quote:  "'"       # ASCII apostrophe (U+0027)
  right_quote: "'"       # ASCII apostrophe (U+0027)
  left_dquote: '"'       # ASCII double quote (U+0022)
  right_dquote: '"'      # ASCII double quote (U+0022)
  ellipsis:    "..."     # three ASCII dots
```

**Applies to:**
- `vo_script_table.csv` (VO_EN, VO_JA, VO_VI columns)
- `vo_draft_table.csv` (VO_Draft_EN column)
- `illustration_strip_table.csv` (Strip_Summary column)
- `image_prompts.csv` (Image_Prompt column)
- `video_prompts.csv` (Veo3_Prompt, Animation_Note columns)
- `l2_breakdown_table.csv` (Content_Sketch column)
- `episode_brief.md` (all body text)

**Does NOT apply to:**
- Workflow instruction files (`.agent/workflows/*.md`) - these are read-only instructions
- Rule files (`.agent/rules/*.md`) - these are engine config
- Skill files (`.agent/skills/**/*.md`) - these are reference docs

---

## RULE_CSV_ENCODING

All CSV output files MUST be written as **UTF-8 with BOM** (`utf-8-sig`):

```yaml
encoding: "utf-8-sig"
newline: ""          # empty string for csv.writer (OS-independent)
```

This ensures Excel, Google Sheets, and Windows tools read the file correctly.

---

## RULE_SANITIZE_ON_WRITE

Before writing ANY output file, apply character sanitization:

```
Step 1: Replace all FORBIDDEN_CHARACTERS with their ASCII equivalents
Step 2: Verify no remaining non-ASCII punctuation (except Vietnamese/Japanese content)
Step 3: Write with utf-8-sig encoding
```

---

## VALIDATION

After generating any output file, verify:
- [ ] Zero em dashes (U+2014) in file
- [ ] Zero en dashes (U+2013) in file
- [ ] Zero smart quotes (U+2018, U+2019, U+201C, U+201D) in file
- [ ] File starts with UTF-8 BOM (EF BB BF)

On violation: FIX immediately before presenting output to user.
