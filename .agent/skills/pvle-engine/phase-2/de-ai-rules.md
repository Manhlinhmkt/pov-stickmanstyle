thê# DE-AI RULES — Phase 2 Post-Processing

> **Load:** After humanize + performance passes complete  
> **Purpose:** Detect and correct AI writing signatures that survived earlier passes  
> **Output:** Applied directly to `vo_script_table.csv`  
> **Trigger:** Mandatory scan after finalize. Fix only if hotspots detected.

---

## 0. CORE PHILOSOPHY

```
Nguoi that khong "co viet giong nguoi that".
Ho chi... khong kiem soat hoan toan cach ho noi.

Neu mot cau nghe "dung qua" — lam no hoi sai di mot chut.

AI chon chi tiet vi no dung.
AI nang cao chon chi tiet vi no "trong random".
Nguoi that chon chi tiet... roi tu nghi ngo no.
```

---

## 1. AI SIGNATURE DETECTION

Scan script for the following 10 patterns. Each is an AI generation fingerprint:

```yaml
SIG_01_FRAGMENT_STACCATO:
  description: "3+ consecutive single-word or ultra-short fragments as stylistic device"
  example_bad: '"Present." / "Yes." / "But containable."'
  why_AI: "AI uses this cadence to simulate poetic rhythm"
  human_reality: "People either say it as one sentence or trail off"

SIG_02_MORAL_HAMMER:
  description: "3-line setup/conflict/loop contradiction"
  example_bad: '"You are relieved." / "You hate yourself for that." / "You are still relieved."'
  why_AI: "AI stacks emotional contradiction in clean 3-beat structure"
  human_reality: "People don't articulate moral contradictions this cleanly"

SIG_03_META_AWARENESS:
  description: "Narrator analyzing own emotional state in real-time"
  example_bad: '"You are trying to locate what you feel but the feelings arrive in the wrong order"'
  why_AI: "AI has perfect introspective access — humans don't"
  human_reality: "People show emotion through behavior, not analysis"

SIG_04_NEGATIVE_DEFINITION_LOOP:
  description: '"You don''t [X]" repeated 5+ times across script'
  example_bad: '"You don''t shake." / "You don''t think." / "You don''t sleep." / "You don''t turn it off."'
  why_AI: "AI defaults to negative definition as character tool"
  threshold: "Standalone 'You don''t' > 3 per episode = pattern"
  note: "'You don''t' embedded in longer sentences does not count"

SIG_05_PERFECT_SYMMETRY:
  description: "Contrast lines with balanced/mirrored structure"
  example_bad: '"His body learned something yours can''t unlearn."'
  why_AI: "AI optimizes for elegant opposition"
  human_reality: "People don't construct perfect antithesis naturally"

SIG_06_ZERO_WASTE:
  description: "Every single line serves the narrative arc"
  why_AI: "AI optimizes signal-to-noise ratio to 100%"
  human_reality: "Real stories always have noise — details that don't payoff"

SIG_07_CLEAN_MOTIF_ARC:
  description: "Motif follows textbook introduce/reinforce/transform/resolve"
  example_bad: '"Ninety seconds felt like forever" -> "feels like nothing" -> "stopped counting"'
  why_AI: "AI tracks motif trajectory too perfectly"
  human_reality: "Motifs drift, get forgotten, come back imperfectly"

SIG_08_MINI_CONCLUSIONS:
  description: "Lines that neatly close a thought/observation"
  example_bad: '"Then it doesn''t." / "Everyone carrying something they can''t put down."'
  why_AI: "AI wraps every observation with a bow"
  human_reality: "People leave thoughts open, unresolved, trailing"

SIG_09_DESIGNED_RANDOMNESS:
  description: "Detail chosen to appear random but is secretly meaningful"
  example_bad: '"A stain on the wall" (stain = moral stain, symbolic)'
  why_AI: "AI selects random details that still serve theme"
  test: "Could this detail appear in a poem? If YES = too symbolic"

SIG_10_CLEAN_TRANSITIONS:
  description: "Every phase flows into the next with perfect logical order"
  why_AI: "AI maintains coherent timeline and causal chain"
  human_reality: "People recall events with temporal blur and repetition"
```

---

## 2. CORRECTION TECHNIQUES

When a signature is detected, apply the appropriate technique:

```yaml
TECH_01_HALF_ARTICULATION:
  description: "Say enough to show feeling, not enough to name it"
  sweet_spot: "Between too-explicit and too-vague"
  example:
    too_explicit: '"That detail destroys you more than any explosion."'
    too_vague: '"You sit with that for a while."'
    half_articulation: '"You don''t know what to do with that."'
  principle: "Narrator reaches for the word but doesn't quite get there"

TECH_02_BEHAVIOR_ONLY_MORAL:
  description: "Show moral reaction through action, not self-knowledge"
  example:
    AI_self_aware: '"You know what that makes you."'
    human_behavior: '"You don''t look at your wife."'
  rule: "Narrator must NOT label their own moral state"

TECH_03_TRULY_MUNDANE_FOCUS:
  description: "Wrong focus detail must have zero symbolic value"
  good: ["cable behind TV", "tape on corner", "glass on counter", "pen cap"]
  bad: ["stain on wall", "crack in mirror", "wilted flower", "flickering light"]
  test: "Remove this object from a poem. Does the poem lose meaning? If NO = mundane enough."

TECH_04_IMPERFECT_CALLBACK:
  description: "Callback without commentary or labeling"
  example:
    AI_commented: '"You step on a LEGO piece. Same spot as always."'
    AI_designed: '"You step on a LEGO piece. Might be the same one."'
    human: '"You step on a LEGO piece in the hallway that night."'
  rule: "Action only. No observation. No nostalgia. Stop."

TECH_05_INLINE_SELF_CORRECTION:
  description: "Narrator corrects own memory inside the flow"
  example:
    good: '"It was already closed. You keep forgetting that."'
    good: '"Or you think you do."'
    bad: '"Actually, now that you think about it..."'
  must: "Sound like brain glitching, not narrator performing awareness"

TECH_06_END_EARLY:
  description: "Remove the final conclusive line — let absence speak"
  example:
    AI_complete: |
      You drink it.
      It tastes the same.
      That should be comforting.
      It isn't.
    human_early: |
      You drink it anyway.
  principle: "The ABSENCE of conclusion IS the human signal"

TECH_07_BREAK_SYMMETRY:
  description: "Degrade perfect contrast by 10%"
  example:
    AI_symmetric: '"His body learned something yours can''t unlearn."'
    human_broken: |
      His body learned something.
      Yours didn't.
  technique: "Split into 2 lines, use simpler/shorter second half"

TECH_08_ATTENTION_DRIFT:
  description: "Perception without explanation — just notice and move on"
  example:
    good: |
      You notice it.
      You look at it for a second.
      You look away.
    over_designed: |
      It bothers you for a second.
      Then something else does.
  rule: "Simple perception verbs only. No analysis of WHY attention drifted."
```

---

## 3. HOTSPOT DETECTION

```yaml
DETECTION_METHOD:
  approach: "Hotspot-based, NOT quota-based"
  
  scan_process:
    step_1: "Read entire script"
    step_2: "Mark every line matching any SIG_01-10"
    step_3: "Identify clusters: 3+ signatures within 10 consecutive lines = HOTSPOT"
    step_4: "Fix only hotspots. Isolated signatures in natural flow = ignore."

  FORBIDDEN:
    - "Counting total interventions needed"
    - "Setting quota per technique type"
    - "Distributing fixes evenly across script"
    - "Creating checklist of 'signals to include'"
    
  PRINCIPLE: |
    Fix WHERE the density is high.
    Leave WHERE the writing already breathes.
    Over-fixing creates "AI pretending to be human" — which is worse than original.
```

---

## 3.5. STRUCTURAL SCAN

> Texture signatures (SIG_01-10) detect **cach viet**.
> Structural scan detects **tu duy cua narrator** — ap dung cho MOI episode, MOI chu de.

```yaml
STRUCTURAL_QUESTION_1:
  ask: "Narrator dang O TRONG hay DUNG NGOAI trai nghiem?"
  
  signals_outside:
    - Phan loai entities bang "There are [X]... And there are [Y]"
    - Dung framing words: "On the other side", "The system", "What you don't know is"
    - Giai thich context/backstory thay vi cho viewer thay qua scene
    - Documentary tone: narrator tong hop thong tin nhu dang quay phim tai lieu
    - Mo ta he thong bang logic thay vi bang trai nghiem
  
  fix_principle: "Thay EXPLANATION bang SCENE"
  fix_method:
    - Thay category list bang specific moments: "A man arrives. He pays. He doesn't ask."
    - Thay system overview bang narrator's daily actions
    - Thay backstory paragraphs bang sensory details from that time
  
  test: "Neu bo doan nay, viewer co biet dieu gi dang xay ra tu nhung scene xung quanh khong?"
  if_yes: "Bo doan giai thich. Scene du roi."
  if_no: "Giu lai - nhung viet lai nhu trai nghiem, khong nhu bao cao."

STRUCTURAL_QUESTION_2:
  ask: "Nhan vat co TU BIET minh dang nghi gi khong?"
  
  signals_self_aware:
    - Inner debate co cau truc: claim / phu dinh / rephrase / phu dinh
    - Self-labeling: "You know what that makes you", "You're the reason"
    - Emotional analysis: "trying to locate what you feel", "feelings arrive in wrong order"
    - Narrator giai thich dong co cua chinh minh
    - Moral self-identification: nhan vat tu ket an hoac tu tha
  
  fix_principle: "Thay SELF-KNOWLEDGE bang BEHAVIOR hoac SILENCE"
  fix_method:
    - Inner debate -> im lang + environment (kinh mo, ngoi trong xe, khong nho duong ve)
    - Self-labeling -> hanh dong (khong nhin vo, khong tra loi, di ra khoi phong)
    - Emotional analysis -> physical sensation (ham cang, tay run, tho nong)
  
  test: "Neu nguoi ngoai quan sat nhan vat, ho co THAY duoc dieu nay khong?"
  if_yes: "Oke - day la behavior, giu lai."
  if_no: "Day la internal narration. Thay bang behavior hoac xoa."

STRUCTURAL_QUESTION_3:
  ask: "Cau nay nghe 'dung qua' khong?"
  
  signals_too_right:
    - In len poster/thumbnail duoc
    - Ket thuc mot y qua gon, qua sach
    - Conclusion sau mot scene = narrator dong goi y nghia
    - Cau co the dung doc lap nhu quote
    - Ending 3-beat hoan chinh
  
  fix_principle: "BO 1 BEAT hoac LAM LECH NHE"
  fix_method:
    - Xoa cau conclusion cuoi cung (TECH_06 end early)
    - Thay declarative bang hesitation: "That is everything" -> chi giu "That is all you do."
    - Thay comparison bang simple statement: "What replaced them is worse" -> "After that it gets quieter"
  
  test: "Doc cau nay mot minh. No co nghe nhu 1 nguoi that dang nghi khong, hay giong 1 writer dang ket bai?"
```

---

## 4. META-RULES

```yaml
# === GIU TU BAN GOC ===

RULE_NO_DESIGN_NATURALNESS:
  description: "Do not design imperfections - let them emerge from hotspot fixes"
  test: "Am I adding this because the script NEEDS it, or because my checklist says so?"
  if_checklist: "STOP. Remove it."

RULE_PROOF_QUESTION:
  description: "For every edit, ask: is this line proving something?"
  test: '"Is this line trying to DEMONSTRATE that a human wrote it?"'
  if_yes: "Remove or weaken. Human writing doesn't prove itself."

RULE_DIMINISHING_RETURNS:
  description: "Stop editing when further changes make script feel MORE designed"
  signal: "When you're choosing between two equally good options = you've gone too far"
  action: "Keep whichever is simpler. Stop editing this section."

RULE_PRESERVATION:
  description: "Many lines in a humanized script are already fine"
  estimate: "Typically 75-85% of script needs NO de-AI changes"
  forbidden: "Touching lines that don't trigger any SIG or structural question"

# === THEM MOI: PROCESS RULES ===

RULE_THREE_PASS_LIMIT:
  description: "De-AI chi duoc chay toi da 3 passes tren cung 1 script"
  sequence:
    pass_1: "Texture - scan SIG_01-10, fix hotspots"
    pass_2: "Structural - ask 3 questions, fix blocks"
    pass_3: "Meta - check for over-control, then STOP"
  after_pass_3: "DONE. Khong sua them du van thay van de."
  rationale: "Pass 4+ tao pattern moi cua anti-pattern. Better 95% human than 100% designed."

RULE_STOP_EARLY:
  description: "Dung sua khi tiep tuc sua = designed imperfection"
  signal_1: "Dang chon giua 2 options deu tot"
  signal_2: "Dang them 'noise' de pha pattern ban vua tao"
  signal_3: "Dang sua lai cai vua sua"
  action: "Giu option don gian hon. Ngung sua section do. Chuyen sang section khac."

RULE_KEEP_IMPERFECT:
  description: "1-2 cho hoi 'clean' con sot lai = feature, khong phai bug"
  rationale: "Neu MOI THU deu imperfect = perfect imperfection = AI moi"
  action: "Khong co gang fix 100%. 95% la diem dung."
  paradox: "KHONG CHON cho nao de giu clean - chi don gian la DUNG SUA SOM HON."
```

---

## 5. EXECUTION WORKFLOW

```yaml
de_ai_workflow:
  input: vo_script_table.csv (post-finalize, post-translate)
  output: vo_script_table.csv (overwritten if changes made)

  steps:
    # === TIER 1: TEXTURE ===
    1_TEXTURE_SCAN:
      action: "Read script, flag SIG_01 through SIG_10"
      output: "Annotated signature list with VO_ID ranges"

    2_HOTSPOT_MAP:
      action: "Identify clusters (3+ sigs per 10 lines)"
      output: "List of hotspot ranges"
      decision: "If zero hotspots = proceed to Tier 2"

    3_TEXTURE_FIX:
      action: "Apply TECH_01-08 to each hotspot"
      rule: "Only hotspots. Do not touch clean sections."

    # === TIER 2: STRUCTURAL ===
    4_STRUCTURAL_SCAN:
      action: "Re-read entire script. Ask 3 structural questions per section."
      question_1: "Narrator dang o trong hay dung ngoai?"
      question_2: "Nhan vat co tu biet minh dang nghi gi khong?"
      question_3: "Cau nay nghe dung qua khong?"
      output: "List of structural issues (if any)"
      decision: "If zero structural issues = proceed to Tier 3"

    5_STRUCTURAL_FIX:
      action: "Rewrite structural problem blocks"
      techniques:
        - "Scene replaces explanation"
        - "Behavior/silence replaces inner debate"
        - "Underplay replaces structured emptiness"
        - "Truncated callback replaces designed callback"
      rule: "Full rewrite of block, not line-level tweaks"

    # === TIER 3: META ===
    6_META_CHECK:
      action: "Re-read all changes from Tier 1 + 2"
      check_1: "Does any fix feel like it's PROVING something?"
      check_2: "Am I choosing between two equally good options? (= over-optimizing)"
      check_3: "Do all fixes look similar? (= new pattern)"
      action_on_yes: "Simplify or remove the fix"

    7_RE_TRANSLATE:
      action: "Update VO_VI for changed lines only"

    8_WORD_COUNT:
      action: "Verify total still within budget"

  validation:
    - "No remaining SIG_03 (meta-awareness)"
    - "Standalone 'You don''t' pattern <= 3"
    - "No SIG_02 (3-line moral hammer)"
    - "Structural Q1: no explanation blocks remaining"
    - "Structural Q2: no clean inner debates"
    - "No fix feels 'designed to be imperfect'"
    - "Total passes on this script <= 3"
```

---

## 6. ANTI-PATTERNS (De-AI pass itself)

```yaml
FORBIDDEN_IN_DE_AI:
  # Texture anti-patterns
  - "Adding imperfections on a schedule/quota"
  - "Distributing techniques evenly (= AI distribution)"
  - "Choosing 'random' details that are secretly meaningful"
  - "Self-explaining wrong focus ('You don't know why you watched')"
  - "Using 'though' to fake conversational tone"
  - "Over-correcting: making EVERY emotional line behavioral"
  - "Creating anti-pattern of anti-patterns (all fixes look the same)"
  - "More than 1 messy section per script"
  - "Commenting on callbacks ('Same spot as always', 'Might be the same one')"
  - "Setup/Punch cliche: 'That should be [X]. / It isn't.'"

  # Structural anti-patterns
  - "Narrator stepping out to explain system/context/backstory"
  - "Clean inner debate structure (claim / No / rephrase / No)"
  - "Documentary framing words to introduce new entities"
  - "Designed callback: identify -> recall -> project -> conclude"
  - "Semantic negative cluster: 3+ 'You don't' same meaning group in 20 lines"
  - "Writer sentences: quotable, poster-ready, sounds like tagline"

  # Process anti-patterns
  - "More than 3 passes on same script"
  - "Fixing something that was already fine before last edit"
  - "Choosing to keep specific lines 'clean' on purpose (= designing imperfection)"
  - "Continuing to edit after reaching 95% human level"
```
