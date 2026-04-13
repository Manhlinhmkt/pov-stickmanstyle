# Episode Brief - PV_0017

## METADATA
| Field | Value |
|-------|-------|
| Episode_ID | PV_0017 |
| Episode_Title | Your Life as the Person Who Didn't Ask |
| World_ID | WORLD_CRIMINAL_ORGAN_BUYER |
| Identity_Mode | GENERIC_ARCHETYPE |
| Structure_ID | LIFE_IMPOSSIBLE_CHOICE |
| Duration_Profile | EXTENDED |
| Target_Duration_Min | 15 |
| Word_Budget | 1755 - 2340 |
| Hook_Type | HOOK_CONTRAST_OPEN |
| Core_Tension | NORMAL_DESIRE_VS_IMPOSSIBLE_REALITY |
| Secondary_Tensions | DUTY_VS_SELF, POWER_VS_ISOLATION |
| Stickman_Accessory | medical wristband, pill bottle |

## WORLD CONTEXT
- **Domain:** CRIMINAL
- **Era:** MODERN_CONTEMPORARY
- **Veil Strictness:** N/A (GENERIC_ARCHETYPE - no named individuals)

### Key Facts Used
1. Organ waiting lists in developed countries average 3-5 years - during which 17 people die every day in the US alone waiting for a transplant (HOOK/PHASE_EARLY: the countdown that starts everything)
2. Transplant tourism packages cost $100,000-$200,000 - including travel, surgery, recovery, and documentation laundering (PHASE_CONFLICT: the price of survival)
3. Buyers typically receive a single phone call with a date and destination - they are told nothing about the donor (PHASE_CONFLICT/CRISIS: the void of knowledge)
4. Many buyers are ordinary people - teachers, engineers, parents - who were told they would die without a transplant within months (HOOK/PHASE_EARLY: you are not a criminal, you are a patient)
5. Post-transplant, buyers must take immunosuppressant drugs for life - a daily reminder of how the organ was obtained (PHASE_RESOLUTION: the pill you take every morning)
6. Brokers coach buyers to tell their home doctors the transplant happened through a generous family member abroad (PHASE_RESOLUTION: the cover story you rehearse)
7. Some buyers discover later that their donor was a kidnapping victim or a prisoner - by then the organ is already inside them (PHASE_RESOLUTION: the truth you cannot un-know)
8. A single kidney costs the buyer $100,000-$200,000 - while the donor receives $5,000 or less, often nothing (PHASE_CONFLICT: the margin built on desperation)
9. The Declaration of Istanbul (2008) explicitly condemns transplant tourism but enforcement remains weak (PHASE_CONFLICT: the system that lets you through)
10. Repeat buyers exist - once you enter the network, they know you will pay (PHASE_RESOLUTION: the call that comes back)

### Key Locations
- LOC_HOSPITAL_CORRIDOR: Where the diagnosis lands - the doctor's words that start the countdown and the desperation
- LOC_WAITING_LIST_OFFICE: Where you sit with a number that never moves - watching others called before you while your body fails
- LOC_BROKER_MEETING: Anonymous hotel lobby or parking garage where the broker offers the option you swore you would never consider
- LOC_FOREIGN_CLINIC: Clean enough to look legitimate - but the silence of the staff and the speed of the process tell you everything
- LOC_RECOVERY_HOME: Your own bed, your own house - with someone else's organ inside you and a cover story you rehearse daily

### Key Tensions
- **NORMAL_DESIRE_VS_IMPOSSIBLE_REALITY**: You want to live. That is the most normal desire in the world. But the only path to survival runs through someone else's body - and you are not allowed to ask whose.
- **DUTY_VS_SELF**: You have a family. Children. People who depend on you. Dying is selfish. But so is what you are about to do.
- **POWER_VS_ISOLATION**: You survive. You return home. You look healthy. But you carry a secret that separates you from every person who loves you - because they can never know what you did to stay alive.

## CONFIRMED OUTLINE

### HOOK
- Chan dung doi thuong - ban la nguoi binh thuong
- Chan doan: suy than giai doan cuoi
- "Ban khong chon dieu nay. Co the ban chon."

### PHASE_EARLY: Chan doan va danh sach cho
- Bac si noi: 3-5 nam cho, co the khong kip
- Dang ky waiting list - so cua ban la 847
- Tuan nao cung loc mau, tuan nao cung doi
- So di len 1, nghia la co nguoi vua chet
- Co the suy dan - met, phung, khong ngu duoc
- Gia dinh nhin ban nhu dang mat dan ban

### PHASE_CONFLICT: Loi de nghi
- Mot nguoi quen gioi thieu "mot cach khac"
- Cuoc gap dau tien - lobby khach san, nguoi la mat
- Broker noi: "Khong can biet chi tiet. Chi can san sang."
- Ban tu choi - lan dau
- Co the tiep tuc suy - nhap vien cap cuu
- Bac si noi: "Con khoang 6 thang neu khong duoc ghep"
- Ban goi lai so dien thoai do
- **IRREVERSIBLE MARKER #1:** Ban khong hoi "than cua ai"

### PHASE_CRISIS: Giao dich
- Ve may bay mot chieu den nuoc la
- Phong kham sach nhung im lang bat thuong
- Nhan vien khong nhin vao mat ban
- Ban nam tren giuong, nghe tieng may o phong ben
- Phau thuat xong - ban tinh day voi than moi
- **IRREVERSIBLE MARKER #2:** Ky giay khai bao y te gia
- Bay ve, ngoi canh cua so, cam nhan co gi la trong nguoi

### PHASE_RESOLUTION: Song voi no
- Ve nha - gia dinh mung, ban cuoi nhung mat khong cuoi
- **IRREVERSIBLE MARKER #3:** Vien thuoc uc che mien dich dau tien - moi ngay, suot doi
- Ai do hoi: "Tim duoc nguoi hien a?" - ban tra loi cau chuyen da tap
- Doc tin tuc ve nan buon ban noi tang - lat trang bao
- Mang luoi goi lai: "Co can gi khong? Gan? Giac mac?"
- Ban nhan ra: ban khong muon biet nua
- Co the khoe hon - nhung tam hon nang hon

### CALLBACK_CLOSE
- Quay lai hinh anh dau: con nguoi binh thuong, cuoc song binh thuong
- Bay gio ban song - nhung voi cau hoi khong bao gio duoc tra loi
- "Neu ban tu hoi cam giac song bang mot phan co the nguoi khac nhu the nao - bay gio ban biet."

## CHARACTER REGISTRY
> Source: `WORLD_CRIMINAL_ORGAN_BUYER.yaml`
> Approved: 2026-04-13. Used by `/pvle-gen-image-prompts`.

### Master Character Table
| Char_ID | Veil_Name | Visual_Summary | Face | Appears_In_Phases |
|---------|-----------|----------------|------|-------------------|
| CHAR_SUBJECT | "you" (SUBJECT) | Average build, business casual - khaki pants, button shirt. Medical wristband on left wrist. Pill bottle in pocket. Looks like any middle-class professional. | dot eyes + simple mouth | ALL |
| CHAR_DOCTOR | "bac si" / "nguoi bao tin" | Male, white coat, stethoscope, clipboard. Professional, clinical posture. | FACELESS | HOOK, EARLY |
| CHAR_FAMILY | "gia dinh" / "vo con" | 2-3 stickmen - wife + child. Clean casual clothes. Standing together, worried postures. | FACELESS | EARLY, RESOLUTION |
| CHAR_BROKER | "nguoi gioi thieu" / "nguoi la mat" | Male, nondescript dark jacket, disposable phone. Deliberately forgettable. | FACELESS | CONFLICT |
| CHAR_CLINIC_STAFF | "nhan vien" / "y ta" | Surgical scrubs, masks. Move quickly, avoid eye contact. | FACELESS | CRISIS |
| CHAR_OTHER_BUYER | "nguoi khac" / "nguoi giong ban" | Similar to SUBJECT - business casual, medical wristband. Mirror image. | FACELESS | RESOLUTION |

### SUBJECT Visual Traits by Phase
| Phase | Age_Range | Height | Hair | Clothing | Face | Distinguishing |
|-------|-----------|--------|------|----------|------|----------------|
| HOOK | 38-45 | AVERAGE | Dark hair, normal cut | Business casual - button shirt, khaki pants | dot eyes, normal/relaxed | Healthy appearance - ordinary life |
| PHASE_EARLY | 38-45 | AVERAGE | Same, slightly thinner | Same + hospital gown in dialysis scenes | dot eyes, worried then desperate | Medical wristband appears, skin paler |
| PHASE_CONFLICT | 38-45 | AVERAGE | Same, more unkempt | Same but wrinkled, loosened collar | dot eyes, conflicted then resigned | Phone with unknown number, envelope of cash |
| PHASE_CRISIS | 38-45 | AVERAGE | Same | Travel clothes - jacket, overnight bag | dot eyes, numb/disconnected | Airline ticket, foreign clinic setting |
| PHASE_RESOLUTION | 38-45 | AVERAGE | Same, healthier | Same business casual, better maintained | dot eyes, surface-calm but hollow | Pill bottle (daily), scar hidden under shirt |
| CALLBACK | 38-45 | AVERAGE | Same | Same as HOOK - button shirt, khaki pants | dot eyes, haunted | Mirror of HOOK but with pill bottle |

### Face Rule
- **SUBJECT (GENERIC_ARCHETYPE)**: dot eyes + simple mouth - expression evolves: normal (HOOK) to worried/desperate (EARLY) to conflicted (CONFLICT) to numb (CRISIS) to surface-calm but hollow (RESOLUTION/CALLBACK)
- **ALL SUPPORTING CHARACTERS**: **FACELESS** - blank white circle head, no eyes, no mouth

### Injection Rules
- SUBJECT always has most visual detail among all characters in scene
- All supporting characters FACELESS - blank white circle head
- SUBJECT looks **ordinary, middle-class** - visual metaphor for "the buyer could be anyone"
- **Signature visual**: medical wristband + pill bottle - wristband appears in EARLY, pill bottle replaces it in RESOLUTION as the permanent marker
- **Arc transition**: Minimal external change - horror is that **you look the same but carry someone else's organ inside you**
- Height does not scale - SUBJECT always AVERAGE
- **Creative constraint**: NEVER show the donor. All medical procedures shown from patient POV - waiting rooms, operating table from your perspective, recovery bed. The donor is a void.

## EPISODE NOTES
- **Duration**: 15 min target, 1755-2340 word budget
- **Beat count**: estimated 22-28 beats (EXTENDED profile)
- **Veil enforcement**: N/A (GENERIC_ARCHETYPE - no named individuals to veil)
- **Emotional arc**: WONDER (hook - the normalcy of your life before) to TENSION (diagnosis, waiting list, body failing) to DREAD (the offer, the refusal, the return to the offer) to CLARITY (the transaction - clinical, efficient, silent) to BITTERSWEET (living with it - alive but haunted) to DEEP_CONNECTION (callback - the question you will never answer)
- **Callback structure**: Hook opens with portrait of ordinary life; Callback closes with same portrait but now you carry a secret that changes everything - same shirt, same house, different person inside
- **Critical narrative device**: Willful blindness as engine. Every step has an unasked question: "Whose kidney?" "Where did they find them?" "Are they alive?" The viewer must feel HOW someone builds a wall of ignorance to survive - literally and morally.
- **Irreversible markers**: Three points of no return encoded in outline - (1) not asking whose kidney, (2) signing false medical declaration, (3) realizing you don't want to know anymore. Each marker deepens complicity.
- **Subject variant**: THE_RELUCTANT - delays decision until body forces the choice. Not eager, not thrill-seeking. Just dying.
- **Trilogy position**: Third perspective in organ trafficking trilogy (PV_0015: Broker, PV_0016: Surgeon, PV_0017: Buyer). Shared network, independent narrative. No cross-references in script.
- **Platform safety**: No graphic surgical content. No donor depiction. No glorification. Subject framed as desperate patient, not criminal. Horror emerges from complicity and willful ignorance, not violence. Ending is moral weight, not coolness.
- **Creative constraint**: "NEVER_SEE_THE_DONOR" - entire narrative operates from the buyer's limited, deliberately narrow perspective. You see waiting rooms, phones, clinics, pills. You never see who gave you their organ. The horror is the void.
- **Forbidden**: Graphic surgical imagery from external view. Donor suffering depicted directly. Framing purchase as clever solution. Criminal glorification. Power fantasy.
