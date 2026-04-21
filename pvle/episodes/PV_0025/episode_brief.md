# Episode Brief - PV_0025

## METADATA
| Field | Value |
|-------|-------|
| Episode_ID | PV_0025 |
| Episode_Title | Your Life as the Person Who Doesn't Catch Criminals. You Make Them. |
| World_ID | WORLD_CRIMINAL_CORRUPT_COP |
| Identity_Mode | GENERIC_ARCHETYPE |
| Structure_ID | LIFE_HIDDEN_POWER |
| Duration_Profile | EXTENDED |
| Target_Duration_Min | 15 |
| Word_Budget | 1755 - 2340 |
| Hook_Type | HOOK_WEIGHT_STATEMENT |
| Core_Tension | PROTECTION_VS_CONTROL |
| Secondary_Tensions | DUTY_VS_SELF, POWER_VS_ISOLATION |
| Stickman_Accessory | badge on belt, body camera with red light off, small bag in vest pocket |
| Signature_Line | You don't find evidence. You place it. |

## WORLD CONTEXT
- **Domain:** CRIMINAL
- **Era:** MODERN_CONTEMPORARY
- **Identity Mode:** GENERIC_ARCHETYPE (no veil enforcement needed)

### Key Facts Used
1. "You have seventeen seconds when the camera goes dark. That's all you need." - used in HOOK, PHASE_CONFLICT, CALLBACK
2. "The report is already written. You just need someone to fit it." - used in PHASE_CONFLICT as paperwork horror
3. "You don't pick criminals. You pick people no one will defend." - used in PHASE_CONFLICT target logic
4. "Your partner saw it. That's why they'll never say it." - used in PHASE_CONFLICT blue wall
5. "You say 'stop resisting' before they move. The audio is evidence." - used in PHASE_CONFLICT micro-behavior
6. "Paperwork is the cleanest part of the crime. If it's written, it happened." - used in PHASE_CONFLICT beat
7. "You say 'in plain view' because those three words close every question." - used in PHASE_CONFLICT courtroom
8. LAPD Rampart scandal: CRASH unit, 100+ convictions reversed, $125M+ settlements - writer reference
9. Chicago Sgt. Ronald Watts: planted drugs, extorted dealers, hundreds of dismissals - writer reference
10. Baltimore 2017: body camera caught Officer Pinheiro fabricating evidence - writer reference
11. "Flaking" = planting contraband. "Testilying" = perjury on stand. Both coined inside departments - writer reference
12. Innocence Project: official misconduct in ~54% of wrongful convictions overturned by DNA - writer reference

### Key Locations
- LOC_PATROL_CAR: Where the second bag lives and the camera has a story for why it turned off
- LOC_ALLEY: Where arrests happen without witnesses and evidence appears in seventeen seconds
- LOC_PRECINCT_DESK: Where ink makes it real. Report matches arrest matches plant
- LOC_COURTROOM: Where you say "in plain view" and the judge nods because you are in uniform
- LOC_LOCKER_ROOM: Where stories are aligned and silences are confirmed
- LOC_TARGET_NEIGHBORHOOD: Where no one files complaints because complaints go to the same precinct

### Key Tensions
- **PROTECTION_VS_CONTROL (primary):** The badge means protection - but the cop uses it as permission. The system designed to protect creates the crimes it claims to solve.
- **DUTY_VS_SELF:** The cop started with duty. Duty became routine. Routine became profit. The self that believed in justice is gone.
- **POWER_VS_ISOLATION:** The power to manufacture cases isolates. The partner who sees everything becomes the biggest threat. Trust is a liability.

## CONFIRMED OUTLINE

### HOOK
- The camera turns off. You have seventeen seconds. That's when you make the crime.
- 1-2 lines of action (tap bag, reach in)
- Signature drop (reveal): "You don't find evidence. You place it."

### PHASE_EARLY (The Badge - fast, cold, enough)
- Graduate academy. Believe the badge means something.
- First week: watch a guilty man walk free. Not enough evidence.
- Partner says: "This isn't how it works."
- First time witnessing partner "help" evidence - shocked, silent

### PHASE_CONFLICT (Noble Cause - erosion + second cold beat)
- First plant: suspect IS guilty. Just missing evidence. You "help."
- First success = no consequence: no questions, no report flagged. That's how you know it works.
- System REWARDS: commendation letter. Sergeant praises. System doesn't just stay silent - it encourages.
- Second time easier. Third time no thinking.
- Standalone beat: You write it down. Ink makes it real.
- Body camera off = reflex. Seventeen seconds is enough.
- Quota rises. Sergeant asks why numbers are low.
- 4-beat loop emerges: choose, prepare, place, swear
- Target logic: You don't pick criminals. You pick people no one will defend.
- System failure cluster: Partner saw it - that's why they'll never say it. Public defender doesn't fight. System too tired to check.
- Name on promotion list. Every arrest on it is manufactured.
- Teach rookie: "this is how it works."

### PHASE_CRISIS (The Snap - point of no return)
- Bridge line: "You stop checking first."
- SNAP MOMENT: Tonight, it's different. You know they're innocent. Not maybe. You know.
- Signature line #2: "You don't find evidence. You place it." - same words, different weight.
- Internal Affairs calls. Partner calls first.
- Drive through neighborhood. Person you arrested stands there. They don't run. They just look at you.

### PHASE_RESOLUTION (Dissolution)
- Not caught. Not punished. System protects itself.
- Training officer now. Rookies learn the method. Method is department.
- Final blow: You try to remember one real arrest. You can't.

### CALLBACK_CLOSE
- The camera turns off. Seventeen seconds. That's all it ever took.
- Signature line #3: "You don't find evidence. You place it." - now not what you do. What you are.
- "You can't tell which ones were real. You're not sure there were any."

## CHARACTER REGISTRY
> Source: `WORLD_CRIMINAL_CORRUPT_COP.yaml`
> Approved: 2026-04-20. Used by `/pvle-gen-image-prompts`.

### Master Character Table
| Char_ID | Veil_Name | Visual_Summary | Face | Appears_In_Phases |
|---------|-----------|----------------|------|-------------------|
| CHAR_SUBJECT | The Cop | Stickman with badge on belt, body camera on chest, small bag in vest pocket. Progressively taller across phases. | dot eyes + simple mouth (neutral to cold) | ALL |
| CHAR_PARTNER | The Partner | Stickman in same police uniform, slightly shorter than SUBJECT | FACELESS | PHASE_EARLY, PHASE_CONFLICT, PHASE_CRISIS |
| CHAR_SERGEANT | The Sergeant | Stickman in police uniform with desk, slightly wider build | FACELESS | PHASE_CONFLICT |
| CHAR_ROOKIE | The Rookie | Stickman in new police uniform, shorter, thinner than SUBJECT | FACELESS | PHASE_RESOLUTION |
| CHAR_TARGET | The Target | Stickman in civilian clothes (hoodie, jeans), handcuffed | FACELESS | PHASE_CONFLICT, PHASE_CRISIS |
| CHAR_PUBLIC_DEFENDER | The Public Defender | Stickman in wrinkled suit with stack of files | FACELESS | PHASE_CONFLICT |
| CHAR_JUDGE | The Judge | Stickman in black robe behind bench | FACELESS | PHASE_CONFLICT |

### SUBJECT Visual Traits by Phase
| Phase | Age_Range | Height | Hair | Clothing | Face | Distinguishing |
|-------|-----------|--------|------|----------|------|----------------|
| HOOK | 30-35 | Medium-tall | Short dark buzz cut | Dark navy police uniform, badge on belt, body camera on chest, small bag visible in vest pocket | dot eyes + simple mouth (cold, neutral) | Camera red light OFF |
| PHASE_EARLY | 22-25 | Medium | Short dark buzz cut | Fresh police uniform, shiny badge, body camera ON (red light visible) | dot eyes + simple mouth (eager, alert) | Clean uniform, camera light ON |
| PHASE_CONFLICT | 26-30 | Medium-tall | Short dark buzz cut | Worn police uniform, badge duller, body camera present but light OFF | dot eyes + simple mouth (neutral, hardening) | Camera light OFF, posture confident |
| PHASE_CRISIS | 30-35 | Tall | Short dark buzz cut | Dark navy uniform, badge worn, body camera OFF, vest pocket slight bulge | dot eyes + simple mouth (cold, flat) | Hands steady, no hesitation |
| PHASE_RESOLUTION | 35-40 | Tallest | Short dark with slight grey at temples | Same uniform but with training officer insignia | dot eyes + simple mouth (blank, unreadable) | Standing over rookie, demonstrating |
| CALLBACK_CLOSE | 35-40 | Tallest | Short dark with grey | Same as HOOK - full circle | dot eyes + simple mouth (empty) | Camera OFF. Same posture as HOOK. |

### Face Rule
- **SUBJECT (CHAR_SUBJECT):** dot eyes + simple mouth - expression progression: eager to neutral to cold to empty
- **ALL OTHERS:** FACELESS - blank white circle head, no eyes, no mouth

### Injection Rules
- SUBJECT always has most visual detail among all characters in scene
- ALL supporting characters are FACELESS - blank white circle head, no eyes, no mouth
- Height must scale - SUBJECT becomes progressively taller stickman across phases
- Body camera red light status (ON/OFF) is a key visual indicator per phase
- REAL NAMES FORBIDDEN in prompts - use Veil_Name only

## EPISODE NOTES
- **Duration:** 15 min target, 1755-2340 words
- **Emotional Arc:** WONDER (idealism) to TENSION (noble cause) to DREAD (snap moment) to CLARITY (dissolution)
- **Signature Line Loop:** "You don't find evidence. You place it." - appears 3x with escalating weight
- **17 Seconds Motif:** Recurring operational detail - time camera is off. Appears in HOOK, PHASE_CONFLICT, CALLBACK.
- **Paperwork Horror:** "Ink makes it real" - the crime becomes real through documentation, not action
- **Snap Moment:** Late PHASE_CRISIS - planting on known innocent person. Shift from system horror to personal horror.
- **4-Beat Loop:** choose to prepare to place to swear - visible in PHASE_CONFLICT structure
- **Top 3 Micro-Behaviors:** (1) camera check - red light off - 17 seconds (2) tap bag through pocket before reaching in (3) say "stop resisting" before they move
- **Callback Structure:** Mirror HOOK exactly - camera turns off, seventeen seconds, signature line returns as identity not action
- **Ending:** "You can't tell which ones were real. You're not sure there were any."
- **No Veil Enforcement:** GENERIC_ARCHETYPE mode - no real person referenced
