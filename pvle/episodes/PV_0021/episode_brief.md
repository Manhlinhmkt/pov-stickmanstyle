# Episode Brief - PV_0021

## METADATA
| Field | Value |
|-------|-------|
| Episode_ID | PV_0021 |
| Episode_Title | Your Life as the Person They Told It Would Grow Back |
| World_ID | WORLD_CRIMINAL_ORGAN_DONOR |
| Identity_Mode | GENERIC_ARCHETYPE |
| Structure_ID | LIFE_IMPOSSIBLE_CHOICE |
| Duration_Profile | EXTENDED |
| Target_Duration_Min | 15 |
| Word_Budget | 1755 - 2340 |
| Hook_Type | HOOK_WEIGHT_STATEMENT |
| Core_Tension | NORMAL_DESIRE_VS_IMPOSSIBLE_REALITY |
| Secondary_Tensions | DUTY_VS_SELF, PROTECTION_VS_CONTROL |
| Stickman_Accessory | lifted shirt showing scar, crumpled banknote, plastic bag |

## WORLD CONTEXT
- **Domain:** CRIMINAL
- **Era:** MODERN_CONTEMPORARY
- **Veil Strictness:** N/A (GENERIC_ARCHETYPE - no named individuals)

### Key Facts Used
1. Poverty is the primary driver - sellers are recruited from impoverished communities with promises of $5,000-$10,000 that are rarely paid in full (PHASE_EARLY: the desperation that makes the offer possible)
2. Brokers lie to sellers - claiming kidneys regenerate, or that humans have three kidneys (PHASE_EARLY: "it grows back" as community rumor / PHASE_CONFLICT: the question no one answers)
3. Sellers typically receive less than 10% of what the buyer pays - a kidney costs the buyer $100,000-$200,000 while the seller gets $5,000 or less, often nothing (PHASE_CRISIS: the envelope that is never enough)
4. Post-surgery, sellers are abandoned in cheap hotel rooms with stitches, painkillers, and zero follow-up medical care (PHASE_CRISIS: waking up lighter, alone)
5. Most sellers report their financial situation did NOT improve long-term - many end up in worse poverty because the surgery left them unable to do physical labor (PHASE_RESOLUTION: hands that tremble, back that won't straighten)
6. Regions where organ selling is prevalent are called Kidney Villages - entire communities where a significant portion of adults carry the same surgical scar (PHASE_RESOLUTION: seeing the scar on someone else)
7. Former sellers are sometimes recruited as recruiters themselves - bringing new victims into the network to earn small commissions (PHASE_RESOLUTION: the system loop - someone is always next)
8. The scar is permanent and visible - a mark that tells everyone in the community what you did, creating lifelong social stigma (HOOK/CALLBACK: the scar you hide under your shirt)
9. Sellers are often coerced through forged documents creating false family ties to make the procedure appear as legal altruistic donation (PHASE_CONFLICT: signing paper you cannot read)
10. Many sellers do not seek medical help for post-surgery complications out of fear of arrest, shame, or lack of legal recourse (PHASE_RESOLUTION: silence as survival)

### Key Locations
- LOC_HOME_VILLAGE: Where debt presses and the broker's man comes with a number written on a scrap of paper
- LOC_BROKER_MEETING_POINT: Bus station or roadside tea stall where the broker explains the deal in simple words
- LOC_TRANSIT: Overnight bus or van to the city - the last hours with your body still complete
- LOC_CLINIC_WAITING: Small room where you sit with other sellers - nobody talks, everyone knows why they are here
- LOC_RECOVERY_ROOM: Cheap hotel mattress where you wake with stitches, a half-dose of painkillers, and a phone number that stops answering

### Key Tensions
- **NORMAL_DESIRE_VS_IMPOSSIBLE_REALITY**: You want to feed your child. That is the most normal desire in the world. But the only path runs through your own body - and the price is permanent.
- **DUTY_VS_SELF**: Your family needs money. Your body is the only thing you own. Selling it is not a choice - it is what desperation looks like when all other options are gone.
- **PROTECTION_VS_CONTROL**: The system that recruits you promises protection - "it grows back," "it's safe," "others have done it." But the system controls you from the moment you sign the paper you cannot read.

## CONFIRMED OUTLINE

### HOOK
- Vet seo dai - ban keo ao xuong
- "They said it grows back. So you believed them."

### PHASE_EARLY: Truoc (static suffering)
- Ruong kho. Con ngoi bet nen dat.
- Nguoi dung ngoai san. Khong go cua. Chi dung.
- "No moc lai" - lan trong xom nhu su that.

### PHASE_CONFLICT: Vao he thong (system entry)
- Giay dat tren ban. Con so viet tay. Khong ai giai thich.
- Nguoi khac da nhan giay truoc ban. Ho di roi.
- Xe bus dem - gio cuoi cung voi co the nguyen ven.
- Phong cho im lang. Khong ai nhin ai.
- Anh den phong mo bat.
- Ban hoi: bao lau thi no moc lai?
- Khong ai tra loi. Dem nguoc tu 10.

### PHASE_CRISIS: Tinh day (internal fracture + physical loss)
- Tinh day nhe hon.
- Dung len - co the phan ung sai. Ban co nho "binh thuong" cam giac ra sao. Khong nho duoc.
- Phong bi tren ban. Ban khong dem lai lan thu hai.
- Tieng cua mo phong ben canh. Mot nguoi khac duoc dua vao.

### PHASE_RESOLUTION: Ve lang (system reveal qua quan sat)
- Ve nha. Vet seo giau duoi ao. Tien tra duoc nua no.
- Tay run khi ganh. Lung khong thang.
- Dung ngoai san. Mot nguoi keo ao - mep vet seo thoang hien.
- Xe dung gan nha ho. Im lang.

### CALLBACK_CLOSE
- Keo ao xuong. Vet seo van do.
- O dau do, luon co nguoi tiep theo.

## CHARACTER REGISTRY
> Source: `WORLD_CRIMINAL_ORGAN_DONOR.yaml`
> Approved: 2026-04-18. Used by `/pvle-gen-image-prompts`.

### Master Character Table
| Char_ID | Veil_Name | Visual_Summary | Face | Appears_In_Phases |
|---------|-----------|----------------|------|-------------------|
| CHAR_SUBJECT | "you" (SUBJECT) | Thin build, worn work clothes, bare feet or sandals, sun-darkened skin tone (stickman style). Lifted shirt showing scar in HOOK/CALLBACK. Plastic bag with belongings in CONFLICT. | dot eyes + simple mouth | ALL |
| CHAR_CHILD | "con" / "the child" | Small stickman, sitting on dirt floor, thin limbs | FACELESS | EARLY |
| CHAR_DEBT_COLLECTOR | "nguoi doi no" / "the figure at the gate" | Standing silhouette in yard, arms at sides, motionless | FACELESS | EARLY |
| CHAR_NEIGHBOR | "nguoi hang xom" / "the one who came back" | Same thin build as SUBJECT, shirt slightly lifted to show scar edge | FACELESS | EARLY, RESOLUTION |
| CHAR_OTHERS_WAITING | "nhung nguoi khac" / "the others" | 2-3 thin stickmen sitting in silence, same worn clothes, same posture | FACELESS | CONFLICT, CRISIS |
| CHAR_SYSTEM_HAND | "ban tay" / "the hand" | Disembodied hand placing paper on table - no body attached, just a hand and paper | N/A (partial) | CONFLICT |

### SUBJECT Visual Traits by Phase
| Phase | Age_Range | Height | Hair | Clothing | Face | Distinguishing |
|-------|-----------|--------|------|----------|------|----------------|
| HOOK | 25-35 | AVERAGE | Short dark hair | Worn shirt, pulling it down to hide scar | dot eyes, guarded | Scar visible momentarily on torso |
| PHASE_EARLY | 25-30 | AVERAGE | Short dark hair | Worn work clothes, bare feet, sun-darkened | dot eyes, tired/desperate | Thin, manual labor body |
| PHASE_CONFLICT | 25-30 | AVERAGE | Short dark hair | Same worn clothes, then hospital gown | dot eyes, resigned | Plastic bag with belongings, sitting in waiting room |
| PHASE_CRISIS | 25-30 | AVERAGE | Short dark hair | Hospital gown, then worn clothes again | dot eyes, disoriented | Bandage on torso, unsteady posture |
| PHASE_RESOLUTION | 25-35 | AVERAGE | Short dark hair | Same worn work clothes | dot eyes, hollow | Scar hidden under shirt, hands trembling |
| CALLBACK | 25-35 | AVERAGE | Short dark hair | Same shirt as HOOK | dot eyes, numb | Mirror of HOOK - pulling shirt down |

### Face Rule
- **SUBJECT (GENERIC_ARCHETYPE)**: dot eyes + simple mouth - expression evolves: tired/desperate (EARLY) to resigned (CONFLICT) to disoriented (CRISIS) to hollow/numb (RESOLUTION/CALLBACK)
- **ALL SUPPORTING CHARACTERS**: **FACELESS** - blank white circle head, no eyes, no mouth

### Injection Rules
- SUBJECT always has most visual detail among all characters in scene
- All supporting characters FACELESS - blank white circle head
- SUBJECT looks **poor, thin, worn** - visual metaphor for "the body at the bottom of the chain"
- **Signature visual**: scar on torso - hidden under shirt, revealed in HOOK and CALLBACK
- **Arc transition**: No height scaling (SUBJECT is an adult throughout). Visual change is posture: upright but desperate (EARLY) to unsteady/broken posture (CRISIS/RESOLUTION)
- **Creative constraint**: THE_BODY_IS_THE_PRICE - surgery is a gap (lights on -> lights off -> wake up lighter). No graphic surgical imagery. Horror is before and after, not during.
- **System visual**: The "hand placing paper" replaces broker as character. No face, no body. Just delivery mechanism.

## EPISODE NOTES
- **Duration**: 15 min target, 1755-2340 word budget
- **Beat count**: estimated 22-28 beats (EXTENDED profile)
- **Veil enforcement**: N/A (GENERIC_ARCHETYPE - no named individuals to veil)
- **Emotional arc**: TENSION (hook - scar + the lie) to DREAD (deepening desperation + system entry) to CLARITY (the question no one answers + surgery gap) to DREAD (waking up, internal fracture, the door) to BITTERSWEET (return home, body broken, seeing the system continue) to DEEP_CONNECTION (callback - scar + "someone is always next")
- **Callback structure**: Hook opens with pulling shirt down to hide scar + "They said it grows back"; Callback closes with same gesture + systemic inevitability ("someone is always next")
- **Critical narrative device**: The lie as engine. "It grows back" enters as community rumor (EARLY), is believed through desperation (CONFLICT), is questioned at the point of no return (surgery moment - no answer), and is permanently disproven by the body itself (RESOLUTION/CALLBACK). The viewer must feel HOW a lie becomes indistinguishable from hope when you have nothing else.
- **Emotional fracture point**: CRISIS contains a psychological break - "you try to remember what normal felt like. You can't." This is the moment the loss becomes irreversible not just physically but mentally.
- **Two-tier system reveal**: TIER 1 (CRISIS) = door opening, someone else being brought in (subtle: you are not the only one). TIER 2 (RESOLUTION) = seeing the scar on someone else, a vehicle stopping nearby (full: the system continues with or without you).
- **Series position**: Fourth perspective in organ trafficking series (PV_0015: Broker, PV_0016: Surgeon, PV_0017: Buyer, PV_0021: Donor). The victim's POV - the person at the bottom of the chain whose body funds everyone above. Shared network, independent narrative. No cross-references in script.
- **Platform safety**: No graphic surgical content. No body horror. No poverty porn or pity framing. Subject framed as person driven by desperation, not victim to be pitied. Horror emerges from transaction and system, not violence. Ending is systemic inevitability, not moralization.
- **Creative constraint**: "THE_BODY_IS_THE_PRICE" - narrative lives inside the body. Surgery is a gap - you go under, you wake up lighter. The real story is before (desperation) and after (emptiness). The body is both the product and the price.
- **Broker representation**: Broker is NOT a character. Broker is a "system signal" - represented by a disembodied hand placing paper with a number. No face, no dialogue, no human presence. The system recruits through absence, not persuasion.
- **Forbidden**: Graphic surgical imagery. Poverty porn. Pity framing. Heroic sacrifice narrative. Cool nihilism. Moralizing ending. Documentary-style CTA. Broker as speaking character.
