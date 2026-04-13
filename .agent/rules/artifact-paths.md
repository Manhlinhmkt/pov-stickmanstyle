
---
trigger: always_on
---

# ARTIFACT IMAGE PATH RULE

### RULE_FORWARD_SLASH_PATHS

When embedding images or media in markdown artifacts using `![caption](path)` syntax:

- **ALWAYS** use forward slashes `/` in file paths
- **NEVER** use backslashes `\` — markdown renderers cannot resolve backslash paths
- This applies to ALL absolute paths in artifacts, including `![image](...)` and `[link](file:///...)`

```yaml
CORRECT:   "![caption](C:/Users/LinhDM/.gemini/antigravity/brain/id/image.png)"
FORBIDDEN: "![caption](C:\\Users\\LinhDM\\.gemini\\antigravity\\brain\\id\\image.png)"
```

- On violation: image will not render and user cannot review visual assets
