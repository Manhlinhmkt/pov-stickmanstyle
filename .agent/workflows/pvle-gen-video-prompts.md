---
description: Generate Veo video prompts from image stills (PVLE P3.2)
skills_required:
  - pvle-engine
---

# WORKFLOW: /pvle-gen-video-prompts

> **Phase:** 3.2 - Video  
> **Input:** `illustration_strip_table.csv` + `image_prompts.csv` + `vo_script_table.csv`  
> **Output:** `pvle/episodes/{EP}/video_prompts.csv`  
> **Target tool:** Veo (Google video generation)

## EXECUTION_CHECKLIST

```yaml
total_steps: 7
steps:
  - step: 1
    name: "Read Inputs"
    type: AUTO
    output: "inline (data loaded)"

  - step: 2
    name: "Map Strips to Clips"
    type: AUTO
    output: "inline (clip mapping)"

  - step: 3
    name: "Select Camera Movement"
    type: AUTO
    output: "inline (camera selected)"

  - step: 4
    name: "Write Animation Notes"
    type: AUTO
    output: "inline (notes written)"

  - step: 5
    name: "Compose Veo Prompt"
    type: AUTO
    output: "inline (prompts composed)"

  - step: 6
    name: "Validate"
    type: AUTO
    output: "inline (validation report)"

  - step: 7
    name: "Output CSV"
    type: AUTO
    output: "pvle/episodes/{EP}/video_prompts.csv"

# On completion: verify all steps checked
# On skip: VIOLATION -> HALT_AND_REPORT
```

---

## STEP 1: Read Inputs

Load:
- `illustration_strip_table.csv` → Strip_ID, Start_VO_ID, End_VO_ID, Scene_Type, Duration_Sec
- `image_prompts.csv` → Slate (= Strip_ID), Image_Prompt
- `vo_script_table.csv` → VO_ID, Pause_After, Beat_Type, VO_Type

---

## STEP 2: Map Strips to Clips

Each strip = one clip (one still image animated into video).

```yaml
clip_mapping:
  rule: "1 Strip = 1 Clip"
  Clip_ID: "{Episode_ID}_C{NNN}" — 3-digit sequential
  Duration_Sec: from illustration_strip_table.csv (pre-calculated)
```

---

## STEP 3: Select Camera Movement

Based on Scene_Type from strip table:

```yaml
camera_selection:
  NARRATIVE_SCENE:
    default: SLOW_PAN_RIGHT
    alternatives:
      TENSION/DREAD: SLOW_ZOOM_IN
      WONDER: SLOW_ZOOM_OUT
      
  TIME_SKIP_SCENE:
    default: STATIC (left panel fades to right panel via dissolve)
    
  POV_SHOT:
    default: SLOW_ZOOM_IN (creeping perspective)
    DREAD: SLOW_PULL_BACK (reveal scale of situation)
    
  EMOTIONAL_CLOSEUP:
    default: SLOW_ZOOM_IN (emphasize isolation)
    BITTERSWEET: STATIC
    
  TEXT_OVERLAY:
    default: STATIC
    
  CONTRAST_SPLIT:
    default: STATIC
    
rule: "Movement is ALWAYS slow — no fast cuts, no shaky camera, no rapid zoom"
```

---

## STEP 4: Write Animation Notes

For each clip, write `Animation_Note` — describes stickman movement:

```yaml
NARRATIVE_SCENE:     "[Stickman walks / turns / sits / gestures — simple movement]"
TIME_SKIP_SCENE:     "Left panel fades, right panel fades in — crossfade transition"
POV_SHOT:            "Hands remain still / slightly shift weight — minimal movement"
EMOTIONAL_CLOSEUP:   "Stickman breathes slightly (micro-movement) — otherwise still"
TEXT_OVERLAY:        "Text fades in line by line — otherwise static"
CONTRAST_SPLIT:      "Both stickmen walk forward simultaneously — mirror movement"
```

---

## STEP 5: Compose Veo Prompt

```
Veo_Prompt formula:
"{Scene description from Image_Prompt — simplified, action-focused}. 
{Camera: CAMERA_MOVEMENT_DESCRIPTION}. 
{Animation_Note}. 
Minimalist stickman animation, flat illustration style, {background_type} background. 
Duration: {Duration_Sec} seconds. Slow, smooth movement throughout.
--no fast cuts, no realistic human faces, no photorealism, no shaky camera"
```

**Camera description mapping:**
```
STATIC           → "Fixed camera, no movement"
SLOW_ZOOM_IN     → "Slow, gentle zoom in toward subject, 10% zoom over full duration"
SLOW_ZOOM_OUT    → "Slow, gentle zoom out from subject, revealing wider environment"
SLOW_PAN_RIGHT   → "Slow horizontal pan right, steady pace"
SLOW_PAN_LEFT    → "Slow horizontal pan left, steady pace"
SLOW_PULL_BACK   → "Slow camera pull back (dolly out), revealing scale of environment"
```

---

## STEP 6: Validate

- [ ] Clip count == Strip count from illustration_strip_table.csv (1:1 parity)
- [ ] All Duration_Sec ≥ 3.0 seconds
- [ ] No clip > 15 seconds (split if needed)
- [ ] Camera movement matches Scene_Type rules
- [ ] All Veo_Prompts end with negative suffix
- [ ] Clip_ID sequential, no gaps

---

## STEP 7: Output

**RULE_SILENT_OUTPUT:** CSV only.

File: `pvle/episodes/{EP}/video_prompts.csv`

Columns: `Clip_ID,Source_Strip,Start_VO_ID,End_VO_ID,Duration_Sec,Camera_Movement,Animation_Note,Veo_Prompt`

> **Note:** `Source_Strip` replaces old `Source_Slate` — references Strip_ID from illustration_strip_table.csv.

---

## USER INPUT

> `Episode_ID`: {{Episode_ID}}
