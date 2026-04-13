# Episode Brief - PV_0016

## METADATA
| Field | Value |
|-------|-------|
| Episode_ID | PV_0016 |
| Episode_Title | Your Life as the Surgeon Who Cuts for the Wrong Side |
| World_ID | WORLD_CRIMINAL_ORGAN_SURGEON |
| Identity_Mode | GENERIC_ARCHETYPE |
| Structure_ID | LIFE_IMPOSSIBLE_CHOICE |
| Duration_Profile | EXTENDED |
| Target_Duration_Min | 15 |
| Word_Budget | 1755 - 2340 |
| Hook_Type | HOOK_WEIGHT_STATEMENT |
| Core_Tension | DUTY_VS_SELF |
| Secondary_Tensions | NORMAL_DESIRE_VS_IMPOSSIBLE_REALITY, POWER_VS_ISOLATION |
| Stickman_Accessory | surgical gloves, stethoscope, scrub cap |

## WORLD CONTEXT
- **Domain:** CRIMINAL
- **Era:** MODERN_CONTEMPORARY
- **Veil Strictness:** N/A (GENERIC_ARCHETYPE - no named individuals)

### Key Facts Used
1. Surgeons in trafficking networks are the scarcest and most protected asset - without them, the entire operation collapses (PHASE_CONFLICT: why the network needs you and won't let you leave)
2. Many trafficking surgeons were once legitimate doctors who lost licenses, accumulated debt, or were coerced into the network (PHASE_EARLY/CONFLICT: your path into the system)
3. A single kidney extraction takes 2-4 hours - the surgeon works in silence knowing the donor may not have consented (PHASE_CONFLICT: the reality of what you do)
4. Trafficking networks pay surgeons $20,000-$50,000 per operation - ten times what they earned legally in their home country (PHASE_CONFLICT: the money that traps you)
5. Some victims are kidnapped and wake up in unfamiliar rooms with fresh surgical scars and no memory of what happened (PHASE_CRISIS: the truth you can no longer deny)
6. Surgeons must perform without full medical teams - often with minimal anesthesia, improvised equipment, and no post-operative care plan for donors (PHASE_CONFLICT: the conditions you work in)
7. The Hippocratic Oath - 'First, do no harm' - is the oldest ethical code in medicine, dating back to ancient Greece (HOOK/CALLBACK: the oath that defines and condemns you)
8. Trafficking surgeons rationalize by telling themselves the recipient will die without the organ - reframing extraction as saving a life (PHASE_CONFLICT: your internal justification engine)
9. Once inside the network, surgeons cannot leave - they know too much about locations, patients, and the organization (PHASE_RESOLUTION: why you are trapped)
10. Medical boards in multiple countries have documented cases of licensed surgeons moonlighting in illegal transplant operations (PHASE_EARLY: the real-world bridge between legitimate and illegal)

### Key Locations
- LOC_FORMER_HOSPITAL: Where you once worked legally - clean halls, proper teams, patients who thanked you - the life you lost
- LOC_UNDERGROUND_CLINIC: Converted basement or back-room facility with surgical equipment - sterile enough to operate but far from any standard
- LOC_PREP_ROOM: Where donors are sedated before surgery - the last room where you can still pretend you do not know what comes next
- LOC_OPERATING_TABLE: The center of everything - where your hands do what your mind has learned to disconnect from
- LOC_RECOVERY_NOWHERE: Donors are moved here briefly then abandoned - you never see what happens after you close the wound

### Key Tensions
- **DUTY_VS_SELF**: The Hippocratic Oath says 'First, do no harm.' Your hands say otherwise. Every operation is a betrayal of the person you trained to be.
- **NORMAL_DESIRE_VS_IMPOSSIBLE_REALITY**: You wanted to be a doctor. You wanted to save lives. Now you extract organs from people who may not have chosen to be here.
- **POWER_VS_ISOLATION**: You are the most valuable person in the network - no one can replace you. But that value is your prison. You know too much to leave.

## CONFIRMED OUTLINE

### HOOK
- Ban tay ban run. Nhung dao mo van chinh xac.
- "Ban khong chon nghe nay. Nghe nay chon ban."

### PHASE_EARLY: Truong Y / Su nghiep hop phap
- Truong y - 7 nam hoc, ngu 4 tieng/ngay
- Ca phau thuat dau tien - ban cuu mot mang nguoi
- Benh nhan cam on ban, gia dinh ho khoc vi mung
- Luong thap, no chong chat, nhung ban tu hao
- Thua nhan thanh cong - bac si phau thuat tai benh vien lon

### PHASE_CONFLICT: Su sa nga
- No hoc tang - vo/chong muon ly di - ap luc tai chinh nghet tho
- Mot dong nghiep cu gioi thieu "ca mo phu" - tra gap 10 lan
- Ca dau tien: nguoi hien tang "tu nguyen" - ban tu thuyet phuc
- Ca thu hai: nguoi hien tre hon, mat so hai hon
- Ban bat dau tu hoi nhung khong dung lai - tien da tra het no
- Dinh nghia "tu nguyen" ngay cang mo nhat

### PHASE_CRISIS: Diem khong the quay lai
- Nan nhan tren ban mo - co ve bi bat coc, khong tu nguyen
- Ban nhan ra: day khong phai nguoi hien - day la nan nhan
- Ong trum de nghi: "Mo di, hoac ban la nguoi tiep theo"
- Ban mo. Ban tay van chinh xac. Dau oc thi khong.

### PHASE_RESOLUTION: Bi mac ket
- Khong the bo - ban biet qua nhieu
- Moi ca mo, ban tu dong disconnect - lam sang thuan tuy
- Ban nhin ban tay minh moi sang - cung ban tay do
- Khong benh vien nao nhan ban lai - su nghiep hop phap chet

### CALLBACK_CLOSE
- Ban tay van run. Dao mo van chinh xac.
- "Ban la bac si. Ban tung la bac si."

## CHARACTER REGISTRY
> Source: `WORLD_CRIMINAL_ORGAN_SURGEON.yaml`
> Approved: 2026-04-13. Used by `/pvle-gen-image-prompts`.

### Master Character Table
| Char_ID | Veil_Name | Visual_Summary | Face | Appears_In_Phases |
|---------|-----------|----------------|------|-------------------|
| CHAR_SUBJECT | "you" (SUBJECT) | Average build, surgical scrubs under a worn jacket, stethoscope around neck, scrub cap. Hands always visible - the central motif. | dot eyes + simple mouth | ALL |
| CHAR_COLLEAGUE | "dong nghiep cu" / "nguoi gioi thieu" | Male, older surgeon, expensive watch peeking from scrub sleeve, confident posture | FACELESS | CONFLICT |
| CHAR_BOSS | "ong trum" / "nguoi dieu hanh" | Male, heavy build, dark suit, gold rings, never in medical clothes - businessman | FACELESS | CONFLICT, CRISIS, RESOLUTION |
| CHAR_DONORS | "nguoi hien" / "nan nhan" | Various - thin, poor, some sedated on gurney. Different individuals across scenes | FACELESS | CONFLICT, CRISIS |
| CHAR_KIDNAP_VICTIM | "nan nhan bi bat coc" | Young, bound wrists marks visible, terrified body language on operating table | FACELESS | CRISIS |
| CHAR_MEDICAL_STAFF | "y ta" / "nguoi phu mo" | Thin stickmen in scrubs, masked, anonymous assistants | FACELESS | CONFLICT, CRISIS |
| CHAR_FAMILY | "vo/chong" | Average build, civilian clothes, increasingly distant posture across phases | FACELESS | EARLY, CONFLICT |
| CHAR_PATIENTS_LEGAL | "benh nhan hop phap" | Various patients in hospital gowns - the people you once saved | FACELESS | EARLY |

### SUBJECT Visual Traits by Phase
| Phase | Age_Range | Height | Hair | Clothing | Face | Distinguishing |
|-------|-----------|--------|------|----------|------|----------------|
| HOOK | 35-40 | AVERAGE | Short dark hair, slightly graying | Surgical scrubs, gloves on, scrub cap, under harsh lamp | dot eyes, hands trembling but steady on instrument | Hands in surgical gloves - central frame |
| PHASE_EARLY | 22-30 | SHORT to AVERAGE | Short dark hair, neat | Medical student white coat, then surgeon scrubs with hospital badge | dot eyes, eager then proud | Stethoscope, clean white coat |
| PHASE_CONFLICT | 30-36 | AVERAGE | Short dark hair, less neat | Scrubs without hospital badge, jacket over scrubs, disposable gloves | dot eyes, calculating then conflicted | No badge, underground clinic setting |
| PHASE_CRISIS | 36-38 | AVERAGE | Disheveled | Blood-flecked scrubs, gloves, harsh overhead light | dot eyes, wide with horror then hollow | Hands frozen mid-surgery |
| PHASE_RESOLUTION | 38-40 | AVERAGE | Graying | Same scrubs, no badge, mechanical posture | dot eyes, flat/dead | Hands move automatically |
| CALLBACK | 40 | AVERAGE | Graying | Same scrubs, same gloves | dot eyes, numb | Mirror of HOOK - hands still precise |

### Face Rule
- **SUBJECT (GENERIC_ARCHETYPE)**: dot eyes + simple mouth - expression evolves: proud (EARLY) to calculating/conflicted (CONFLICT) to horrified (CRISIS) to flat/dead (RESOLUTION/CALLBACK)
- **ALL SUPPORTING CHARACTERS**: **FACELESS** - blank white circle head, no eyes, no mouth

### Injection Rules
- SUBJECT always has most visual detail among all characters in scene
- All supporting characters FACELESS - blank white circle head
- **Central motif**: HANDS - always visible, always focal point of frame
- **Signature visual**: Surgical gloves + stethoscope - symbols of medicine weaponized
- **Arc transition**: Clean white coat with badge (EARLY) to scrubs without badge (CONFLICT) to blood-flecked scrubs under harsh light (CRISIS) to same scrubs, mechanical hands (RESOLUTION)
- Height does not scale dramatically - SUBJECT always AVERAGE
- **Creative constraint**: INSIDE_THE_OPERATING_ROOM - unlike PV_0015, this episode lives INSIDE the surgery. The horror is clinical precision applied to monstrous purpose.
- **Forbidden**: Gratuitous gore, surgical fetishism, power fantasy, cool-surgeon trope

## EPISODE NOTES
- **Duration**: 15 min target, 1755-2340 word budget
- **Beat count**: estimated 22-28 beats (EXTENDED profile)
- **Veil enforcement**: N/A (GENERIC_ARCHETYPE - no named individuals to veil)
- **Emotional arc**: WONDER (hook - hands that heal) to TENSION (financial pressure, first illegal operation) to DREAD (escalation, donors getting younger and more scared) to CLARITY (crisis - victim is kidnapped, not voluntary) to BITTERSWEET (trapped, cannot return to legitimate medicine) to DEEP_CONNECTION (callback - same hands, different meaning)
- **Callback structure**: Hook opens with trembling hands holding a scalpel; Callback closes with same trembling hands - precision unchanged, person inside destroyed
- **Critical narrative device**: The Hippocratic corruption. Every phase is measured against the oath: 'First, do no harm.' EARLY = honoring it. CONFLICT = bending it ('the recipient needs this'). CRISIS = shattering it (operating on a kidnap victim). RESOLUTION = the oath is dead but the hands still work.
- **Companion piece**: PV_0015 (The Middleman) shows the same ecosystem from OUTSIDE the operating room. PV_0016 shows it from INSIDE. Together they form a diptych of moral decay in organ trafficking.
- **Platform safety**: No gratuitous surgical gore. Horror emerges from clinical detachment, not spectacle. Subject framed as corrupted healer, not villain. Ending is moral death, not coolness.
- **Creative constraint**: "INSIDE_THE_OPERATING_ROOM" - narrative lives in the hands. The same hands that once saved now extract. The horror is precision, not violence.
- **Forbidden**: Surgical fetishism. Gore montage. Cool villain framing. Power fantasy. Victim dehumanization.
