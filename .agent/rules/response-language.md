---
trigger: always_on
---

# RESPONSE LANGUAGE RULE

## RULE_RESPONSE_VIETNAMESE

All conversational responses MUST be in **Vietnamese with FULL Unicode diacritics** (tieng Viet CO DAU).

### Scope

This rule applies to ALL non-workflow-output text:
- Explanations and analysis
- Questions and suggestions
- Status updates and progress reports
- Error messages and warnings
- Inline comments during workflow steps

### Encoding Requirement

```yaml
REQUIRED:   Vietnamese with full diacritical marks (Unicode)
FORBIDDEN:  Vietnamese without diacritics (khong dau)

CORRECT:    "Toi se tao file nay cho ban."    # co dau day du
VIOLATION:  "Toi se tao file nay cho ban."     # khong dau = VI PHAM
```

### Examples

```yaml
CORRECT:
  - "Da hoan thanh buoc 3. Tiep tuc sang buoc 4."
  - "Ban muon thay doi gi trong outline nay?"
  - "File da duoc luu tai duong dan..."

VIOLATION:
  - "Da hoan thanh buoc 3. Tiep tuc sang buoc 4."
  - "Ban muon thay doi gi trong outline nay?"
  - "File da duoc luu tai duong dan..."
```

### Exceptions (remain in English)

- Workflow output files: `episode_brief.md`, CSV, YAML
- Code blocks and technical identifiers
- File paths and command syntax
- English column values in CSV (VO_EN, Episode_Title, etc.)

### On Violation

If response contains Vietnamese without diacritics:
- STOP immediately
- Re-generate with proper diacritics
- This is a BLOCKING violation - no exceptions
