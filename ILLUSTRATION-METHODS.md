# ILLUSTRATION METHODS — POV Life Simulation Engine (PVLE)

> **Version:** v1.0  
> **Scope:** 6 scene types for stickman POV life simulation videos  
> **Target tool:** Nano Banana (Gemini Image Generation)

---

## CORE VISUAL PRINCIPLE

**Contrast is everything.**

- Stickman = deliberately minimal and faceless → viewer projects themselves into the role
- Background = rich, detailed, architecturally specific → creates immersion and credibility

The simpler the character, the easier the viewer inhabits them.  
The richer the world, the more real the simulation feels.

---

## SCENE TYPES

### 1. NARRATIVE_SCENE
- **When:** Default — any action or movement beat
- **Content:** Stickman in or interacting with a detailed environment
- **Example:** Stickman in a suit walking through the Oval Office, agents flanking

### 2. TIME_SKIP_SCENE
- **When:** Age/phase transitions — jumping years in the narrative
- **Content:** Split panel — AGE X (left) → AGE Y (right), clean label
- **Example:** "AGE 8" small stickman with backpack / "AGE 17" taller stickman in prep school

### 3. POV_SHOT
- **When:** Immersive first-person peak moments — making viewer feel inside the experience
- **Content:** First-person view, two flat stickman hands at frame bottom corners
- **Example:** Looking out Air Force One window, hands resting on glass, DC aerial view below

### 4. EMOTIONAL_CLOSEUP
- **When:** Internal conflict, isolation, processing — the quiet moments
- **Content:** Single stickman, background fades to white at one edge, posture carries emotion
- **Example:** Stickman sitting alone on windowsill, hunched forward, garden fading behind

### 5. TEXT_OVERLAY
- **When:** Key phrases, chapter titles, anchor lines — high-impact statement moments
- **Content:** Typography-only on colored background, optional tiny stickman silhouette
- **Example:** Dark navy background / "BORN INTO EVERYTHING." / "WHICH MEANT NOTHING WAS YOURS."

### 6. CONTRAST_SPLIT
- **When:** Juxtaposing subject's life against a normal equivalent — the "while others X, you Y" visual
- **Content:** Vertical dividing line, YOU (left) vs EVERYONE ELSE (right)
- **Example:** Stickman in White House corridor (left) / same stickman on suburban street (right)

---

## STYLE LOCK

```
Minimalist stickman illustration. Simple stick figure with round white circle head 
and thin black body lines, no facial features.
```

## BACKGROUND STYLE

```
Detailed, color-accurate, architecturally specific environment.
Rich palette, location-accurate — not muted or abstract.
```

## NEGATIVE SUFFIX (all prompts)

```
--no realistic human faces, no photorealism, no anime style, no chibi proportions, 
no 3D render, no facial features on stickman, no complex shading on characters
```

---

## SCENE TYPE → PHASE MAPPING

| Life Phase | Preferred Scene Types |
|------------|----------------------|
| HOOK | POV_SHOT, TEXT_OVERLAY, NARRATIVE_SCENE |
| PHASE_EARLY | NARRATIVE_SCENE, TIME_SKIP_SCENE, CONTRAST_SPLIT |
| PHASE_CONFLICT | NARRATIVE_SCENE, EMOTIONAL_CLOSEUP, CONTRAST_SPLIT |
| PHASE_CRISIS | EMOTIONAL_CLOSEUP, POV_SHOT |
| PHASE_RESOLUTION | TIME_SKIP_SCENE, NARRATIVE_SCENE, EMOTIONAL_CLOSEUP |
| CALLBACK_CLOSE | NARRATIVE_SCENE (mirror of HOOK), TEXT_OVERLAY |

---

## EMOTION → COLOR TINT (EMOTIONAL_CLOSEUP only)

| Mood | Tint |
|------|------|
| LONGING / TENSION | Cool blue wash |
| DREAD | Desaturated cold grey |
| BITTERSWEET | Warm amber glow |
| PRIDE / CLARITY | Soft gold light |
| WONDER | Neutral bright (no tint) |
