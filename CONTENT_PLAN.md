# CONTENT PLAN — POV Life Simulation Engine (PVLE)

> **Version:** v1.0  
> **Scope:** Channel identity, content pillars, episode types, season roadmap

---

## Channel Identity

- **Format:** "What if" POV life simulation — illustrated narrative
- **Tagline:** *Your life. Another world.*
- **Duration:** 8-12 min per episode (STANDARD) / 12-15 min (EXTENDED)
- **Cadence:** Weekly
- **Languages:** English narration (primary) + Japanese + Vietnamese subtitles/VO
- **Audience:** 16-35, curious, reflective — fans of documentary, psychology, "what if" content

---

## What This Channel Does

Each episode simulates a life the viewer has never lived — narrated in second person as if it is happening to them. The viewer is not watching a story. They are *inside* it.

Every episode answers: **"What would your life actually feel like if you were born into this?"**

Not the highlight reel. The full experience — the privilege, the cost, the isolation, the moments no one else sees.

---

## Content Pillars

1. **Privilege & Its Price** — Extraordinary power or wealth that comes at the cost of ordinary life
2. **Hidden Worlds** — Secret identities, protected lives, lives lived under cover
3. **Impossible Choices** — Lives defined by decisions no one should have to make
4. **Living the Legacy** — The weight of being born to someone legendary
5. **Adversity & Character** — Lives forged by difficulty into something extraordinary

---

## Episode Types (Structure Library)

| Structure ID | Description | Example |
|--------------|-------------|---------|
| `LIFE_PRIVILEGE` | Born into extreme privilege — power without freedom | Son of US President, Heir to billion-dollar empire |
| `LIFE_ADVERSITY` | Extreme hardship that forges character | Child in warzone, Refugee camp upbringing |
| `LIFE_HIDDEN_POWER` | Ordinary exterior hiding extraordinary secret | Child of CIA agent, Witness protection kid |
| `LIFE_IMPOSSIBLE_CHOICE` | Life defined by impossible decisions | Last doctor in warzone, Person who must end the AI |
| `LIFE_LEGACY` | Lived under the shadow of a legend | Child of Michael Jordan, Daughter of Einstein |

---

## Episode Flow (All Episodes)

```
HOOK               → Establish extraordinary world (30s)
PHASE_EARLY        → Childhood: innocence meets the extraordinary
PHASE_CONFLICT     → Adolescence: the cage starts to feel real
PHASE_CRISIS       → The defining moment — no turning back
PHASE_RESOLUTION   → Life after the choice: what was gained and lost
CALLBACK_CLOSE     → Return to opening — new meaning earned
```

---

## World Registry (Planned Growth)

| World_ID | Domain | Status |
|----------|--------|--------|
| `WORLD_US_PRESIDENT_FAMILY` | GOVERNMENT_PRIVILEGE | ✅ Active (PV_0001) |
| `WORLD_BILLION_HEIR` | CORPORATE_PRIVILEGE | Planned |
| `WORLD_CIA_AGENT_CHILD` | INTELLIGENCE_HIDDEN | Planned |
| `WORLD_BRITISH_ROYALTY` | ROYALTY_PRIVILEGE | Planned |
| `WORLD_REFUGEE_CAMP` | ADVERSITY | Planned |
| `WORLD_WITNESS_PROTECTION` | HIDDEN_POWER | Planned |

> New worlds are generated and ingested via `/analyze-seed` + `/pvle-ingest-world`.  
> The registry grows permanently — existing worlds are reused across episodes.

---

## Production Pipeline

```
/pvle-run-full → episode_brief.md
              → l2_breakdown_table.csv
              → vo_script_table.csv (EN | JA | VI)
              → image_prompts.csv (Nano Banana)
              → video_prompts.csv (Veo)
```
