# TEMPLATE MASTER — POV Life Simulation Engine (PVLE)

> **Version:** v1.0  
> **Role:** Source of Truth for All PVLE Schema  
> **Scope:** Phase 1-3 (Ideation → Script → Illustration + Video)

---

## 0. METADATA

- **Engine:** PVLE (POV Life Simulation Engine)
- **Episode_ID_Pattern:** `PV_xxxx`
- **Editing Policy:**
  - Schema modifications ONLY in this file
  - Prompts cannot create new columns
  - All IDs/Enums must be defined here or in resource files

---

## 1. ID PATTERNS

```yaml
Episode_ID:  "PV_xxxx"           # e.g. PV_0001
Beat_ID:     "BEAT_xx_xx"        # e.g. BEAT_01_03
VO_ID:       integer              # continuous, no reset within episode
Slate:       "PV_xxxx_NNN"       # e.g. PV_0001_007
Clip_ID:     "PV_xxxx_CNNN"      # e.g. PV_0001_C007
World_ID:    "WORLD_{DOMAIN}"    # e.g. WORLD_US_PRESIDENT_FAMILY
```

---

## 2. TEMPLATE DEFINITIONS

---

## 2.1. TPL_EPISODE_METADATA

**Type:** Vertical Key-Value Table  
**File:** `pvle/episodes/{EP}/episode_brief.md`

| Field | Type | Description |
|-------|------|-------------|
| Episode_ID | ID | `PV_xxxx` |
| Episode_Title | Text | Full episode title (English) |
| World_ID | ID | Linked world from registry |
| Identity_Mode | Enum | GENERIC_ARCHETYPE / TRANSPARENT_VEIL / HISTORICAL_FIGURE |
| Structure_ID | Enum | LIFE_PRIVILEGE / LIFE_ADVERSITY / LIFE_HIDDEN_POWER / LIFE_IMPOSSIBLE_CHOICE / LIFE_LEGACY |
| Duration_Profile | Enum | STANDARD / EXTENDED |
| Target_Duration_Min | Number | Target minutes |
| Voice_Profile | Enum | VOICE_POV_DRAMATIST |
| Avg_WPM | Integer | Default 140 |
| Hook_Type | Enum | See §3.7 |
| Opening_Scene | Text | First visual/moment of the episode |
| Core_Tension | Enum | See §3.6 |
| Emotional_Arc | Text | Brief description of WONDER→CONFLICT→RESOLUTION arc |
| Stickman_Accessory | Text | Primary accessory for this episode's subject |
| Key_Locations | List | 3-5 locations used in episode |
| World_Key_Facts_Used | List | Specific facts from World_ID used in this episode |
| Episode_Notes | Text | Theme, tone notes, special instructions |

---

## 2.2. TPL_L2_BREAKDOWN_TABLE

**Type:** Horizontal Table  
**File:** `pvle/episodes/{EP}/l2_breakdown_table.csv`

| Column | Type | Description |
|--------|------|-------------|
| Beat_ID | ID | `BEAT_xx_xx` |
| Life_Phase | Enum | HOOK / PHASE_EARLY / PHASE_CONFLICT / PHASE_CRISIS / PHASE_RESOLUTION / CALLBACK_CLOSE |
| Beat_Type | Enum | See §3.5 |
| Content_Sketch | Text | Brief description of beat content |
| Mood_Tag | Enum | WONDER / TENSION / DREAD / LONGING / BITTERSWEET / CLARITY / PRIDE |
| Beat_Duration_Sec | Number | Estimated beat duration in seconds |
| Scene_Type | Enum | See §3.4 |
| Illustration_Note | Text | Visual note for this beat |

---

## 2.3. TPL_VO_DRAFT_TABLE

**Type:** Horizontal Table  
**File:** `pvle/episodes/{EP}/vo_draft_table.csv`

| Column | Type | Description |
|--------|------|-------------|
| Beat_ID | ID | Beat reference from L2 |
| Life_Phase | Enum | Phase reference |
| Beat_Type | Enum | Beat type reference |
| Mood_Tag | Enum | Mood reference |
| Content_Sketch | Text | From L2 (reference only) |
| VO_Draft_EN | Text | English narration draft for this beat |
| Word_Count | Integer | Word count of VO_Draft_EN |

---

## 2.4. TPL_VO_SCRIPT_TABLE

**Type:** Horizontal Table  
**File:** `pvle/episodes/{EP}/vo_script_table.csv`

| Column | Type | Description |
|--------|------|-------------|
| VO_ID | Integer | Sequential line number (1, 2, 3...) |
| Episode_ID | ID | Episode reference |
| Beat_ID | ID | Parent beat from L2 |
| Life_Phase | Enum | HOOK / PHASE_EARLY / PHASE_CONFLICT / PHASE_CRISIS / PHASE_RESOLUTION / CALLBACK_CLOSE |
| Beat_Type | Enum | Beat type |
| VO_Type | Enum | NARRATION / TIME_MARKER / WEIGHT_LINE / REFLECTION / CONTRAST_LINE |
| VO_EN | Text | English narration (clean, TTS-ready, no markers) |
| VO_JA | Text | Japanese translation (2nd person あなた, natural spoken style) |
| VO_VI | Text | Vietnamese translation (2nd person bạn, natural spoken style) |
| Word_Count_EN | Integer | Word count of VO_EN |
| Pause_After | Float | Seconds of silence after line (0 / 0.5 / 1.0 / 1.5 / 2.0) |

**Example row:**
```csv
1,PV_0001,BEAT_01,HOOK,ESTABLISH,NARRATION,"The moment you are born, the world already knows your name.","あなたが生まれた瞬間、世界はすでにあなたの名前を知っていた。","Khoảnh khắc bạn chào đời, thế giới đã biết tên bạn rồi.",11,0
```

---

## 2.5. TPL_IMAGE_PROMPTS

**Type:** Horizontal Table  
**File:** `pvle/episodes/{EP}/image_prompts.csv`  
**Target tool:** Nano Banana (Gemini Image Generation)

| Column | Type | Description |
|--------|------|-------------|
| Slate | ID | `PV_xxxx_NNN` (3-digit, sequential) |
| Start_VO_ID | Integer | VO_ID this image corresponds to |
| Life_Phase | Enum | Phase reference |
| Scene_Type | Enum | See §3.4 |
| Image_Prompt | Text | Complete Nano Banana prompt (STYLE_LOCK + CONTENT + NEG) |

---

## 2.6. TPL_VIDEO_PROMPTS

**Type:** Horizontal Table  
**File:** `pvle/episodes/{EP}/video_prompts.csv`  
**Target tool:** Veo

| Column | Type | Description |
|--------|------|-------------|
| Clip_ID | ID | `PV_xxxx_CNNN` (sequential) |
| Source_Slate | ID | Source still image Slate ID |
| Start_VO_ID | Integer | VO_ID where clip starts |
| End_VO_ID | Integer | VO_ID where clip ends |
| Duration_Sec | Float | Total clip duration (VO time + Pause_After sum) |
| Camera_Movement | Enum | STATIC / SLOW_ZOOM_IN / SLOW_ZOOM_OUT / SLOW_PAN_RIGHT / SLOW_PAN_LEFT / SLOW_PULL_BACK |
| Animation_Note | Text | Stickman movement description |
| Veo_Prompt | Text | Complete Veo prompt |

---

## 3. ENUMS & CONTROLLED VOCABULARIES

### 3.0. Identity_Mode (World-level)
```
GENERIC_ARCHETYPE     — No specific person implied. Generic world type.
TRANSPARENT_VEIL      — Specific real person implied but NEVER named in output.
HISTORICAL_FIGURE     — Deceased historical figure implied. Looser veil rules.
```

### 3.1. Structure_ID
```
LIFE_PRIVILEGE        — Born into extreme privilege, pays price in freedom
LIFE_ADVERSITY        — Extreme hardship that forges character
LIFE_HIDDEN_POWER     — Ordinary exterior concealing extraordinary secret
LIFE_IMPOSSIBLE_CHOICE — Life defined by impossible decisions
LIFE_LEGACY           — Lived under the shadow of a legend
```

### 3.2. Duration_Profile
```
STANDARD  (8-12 min)  — ~1100-1680 words EN at 140 WPM
EXTENDED  (12-15 min) — ~1680-2100 words EN at 140 WPM
```

### 3.3. Voice_Profile
```
VOICE_POV_DRAMATIST   — 140 WPM base, 2nd person "you", dramatic storyteller
```

### 3.4. Scene_Type (Visual)
```
NARRATIVE_SCENE       — Stickman action in detailed environment (default)
TIME_SKIP_SCENE       — Split panel: AGE X → AGE Y
POV_SHOT              — First-person view, stickman hands at frame bottom
EMOTIONAL_CLOSEUP     — Stickman isolated, background fades, posture-driven emotion
TEXT_OVERLAY          — Typography-only, key phrase / chapter title
CONTRAST_SPLIT        — Split screen: YOU vs EVERYONE ELSE
```

### 3.5. Beat_Type
```
ESTABLISH     — Set up world/context
TIME_MARKER   — Age/year jump signal
PRIVILEGE     — Demonstrate privilege moment
CONSTRAINT    — Demonstrate cost/restriction
CONFLICT      — Internal/external tension peak
CRISIS        — Point of no return moment
REFLECT       — Internal monologue, weight
RESOLVE       — Resolution or acceptance
CALLBACK      — Return to opening scene/image
CTA           — Closing call to action
```

### 3.6. Core_Tension (per World)
```
PRIVILEGE_VS_FREEDOM
IDENTITY_VS_LEGACY
FRIENDSHIP_VS_SURVEILLANCE
NORMAL_DESIRE_VS_IMPOSSIBLE_REALITY
POWER_VS_ISOLATION
DUTY_VS_SELF
PROTECTION_VS_CONTROL
```

### 3.7. Hook_Type
```
HOOK_BORN_DIFFERENT      — "The moment you are born, X is already different"
HOOK_FIRST_REALIZATION   — First moment you understand you are not normal
HOOK_CONTRAST_OPEN       — Open with what others have, pivot to what you have instead
HOOK_PRIVILEGE_REVEAL     — Reveal the extraordinary nature of your life in first 30s
HOOK_WEIGHT_STATEMENT    — Open with a single heavy line: "You never chose this."
```

### 3.8. VO_Type
```
NARRATION      — Standard narrative line
TIME_MARKER    — "You are [age]. And everything changes." pattern
WEIGHT_LINE    — Short high-impact anchor line (3-8 words)
REFLECTION     — Looking back / internal thought
CONTRAST_LINE  — "While others X, you Y." pattern
```

### 3.9. Mood_Tag
```
WONDER         — Awe, marvel at the extraordinary
TENSION        — Building unease, conflict approaching
DREAD          — Peak fear/impossibility
LONGING        — Desire for normalcy or lost things
BITTERSWEET    — Acceptance mixed with sadness
CLARITY        — Moment of understanding
PRIDE          — Earned, complex pride (not simple)
```

### 3.10. Camera_Movement (Veo)
```
STATIC             — Fixed camera
SLOW_ZOOM_IN       — Gradually closer to subject/scene
SLOW_ZOOM_OUT      — Gradually reveal wider shot
SLOW_PAN_RIGHT     — Horizontal pan right
SLOW_PAN_LEFT      — Horizontal pan left
SLOW_PULL_BACK     — Dolly back, reveal environment
```

---

## 4. COMPLIANCE RULES

| Rule | Description |
|------|-------------|
| `RULE_SCHEMA_LOCK` | Output ONLY defined columns, no additions |
| `RULE_ID_AUTHORITY` | All IDs/Enums must exist in this file or linked resources |
| `RULE_SILENT_OUTPUT` | Tables only, no commentary |
| `RULE_VO_TRILINGUAL` | Every VO_SCRIPT row must have VO_EN + VO_JA + VO_VI populated |
| `RULE_IMAGE_VIDEO_PARITY` | Every image_prompts row must have a matching video_prompts row |

---

## 5. WORKFLOW INTEGRATION

```
Phase 1: IDEATION
├── /analyze-seed          → match World_ID or generate new world
├── /pvle-ingest-world     → save WORLD_*.yaml to registry
├── /pvle-gen-outline      → telegraphic bullet outline
└── /pvle-gen-episode-brief → TPL_EPISODE_METADATA → episode_brief.md

Phase 2: SCRIPTING
├── /pvle-gen-breakdown    → TPL_L2_BREAKDOWN_TABLE → l2_breakdown_table.csv
└── /pvle-gen-vo           → TPL_VO_DRAFT_TABLE + TPL_VO_SCRIPT_TABLE (trilingual)

Phase 3: ILLUSTRATION + VIDEO
├── /pvle-gen-image-prompts → TPL_IMAGE_PROMPTS → image_prompts.csv
└── /pvle-gen-video-prompts → TPL_VIDEO_PROMPTS → video_prompts.csv
```
