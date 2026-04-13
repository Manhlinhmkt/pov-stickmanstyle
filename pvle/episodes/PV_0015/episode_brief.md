# Episode Brief - PV_0015

## METADATA
| Field | Value |
|-------|-------|
| Episode_ID | PV_0015 |
| Episode_Title | Your Life as the Middleman in the Organ Trade |
| World_ID | WORLD_CRIMINAL_ORGAN_BROKER |
| Identity_Mode | GENERIC_ARCHETYPE |
| Structure_ID | LIFE_HIDDEN_POWER |
| Duration_Profile | EXTENDED |
| Target_Duration_Min | 15 |
| Word_Budget | 1755 - 2340 |
| Hook_Type | HOOK_WEIGHT_STATEMENT |
| Core_Tension | POWER_VS_ISOLATION |
| Secondary_Tensions | DUTY_VS_SELF, NORMAL_DESIRE_VS_IMPOSSIBLE_REALITY |
| Stickman_Accessory | disposable phone, cash envelope |

## WORLD CONTEXT
- **Domain:** CRIMINAL
- **Era:** MODERN_CONTEMPORARY
- **Veil Strictness:** N/A (GENERIC_ARCHETYPE - no named individuals)

### Key Facts Used
1. 5-10% of all organ transplants globally each year are illegal - roughly 5,000 to 12,000 illicit transplants annually (PHASE_EARLY: scale of the system you enter)
2. The illegal organ trade generates between $840 million and $1.7 billion in annual profits worldwide (PHASE_CONFLICT: the money that keeps you going)
3. Kidneys are the most trafficked organ - living donors, massive demand from chronic kidney disease (PHASE_CONFLICT: what you trade in)
4. The broker is the most critical role - connecting sellers with buyers, managing logistics, documents, travel, medical facilities (PHASE_CONFLICT: your exact function)
5. Recruiters target impoverished communities - promising large payments rarely delivered in full (PHASE_EARLY/CONFLICT: how you find "sellers")
6. Victims are told lies - kidneys regenerate, humans have three kidneys (PHASE_CONFLICT: the lies you let happen)
7. Operations require corrupt medical professionals working in private clinics or compromised hospitals (PHASE_CONFLICT: the network around you)
8. Donors are abandoned after surgery without follow-up care - lifelong health damage (PHASE_CRISIS/RESOLUTION: the aftermath you see)
9. A single kidney bought for $5,000 from seller, sold to recipient for $150,000+ (PHASE_CONFLICT: the margin you live on)
10. Wealthy patients engage in transplant tourism - bypassing legal waiting lists (PHASE_CONFLICT: who pays you)

### Key Locations
- LOC_RECRUITING_GROUND: Impoverished neighborhood where brokers find desperate sellers through local contacts and former victims turned recruiters
- LOC_BROKER_OFFICE: Nondescript room with a phone and a ledger - where deals are negotiated and payments promised but rarely honored
- LOC_PRIVATE_CLINIC: Unmarked medical facility where extractions happen behind closed doors - the one room you never enter
- LOC_TRANSPLANT_DESTINATION: Legitimate-looking hospital in a country with weak oversight where wealthy recipients receive their new organs
- LOC_ABANDONMENT_ROOM: Cheap hotel room where donors are left post-surgery with stitches, painkillers, and no aftercare

### Key Tensions
- **POWER_VS_ISOLATION**: You become indispensable to the network - everyone needs you, but no one can know you. The more powerful you become, the more alone you are.
- **DUTY_VS_SELF**: "I don't hurt anyone. I just connect people." - the self-rationalization that erodes your humanity one deal at a time.
- **NORMAL_DESIRE_VS_IMPOSSIBLE_REALITY**: You eat dinner, you walk home, you check your phone - but your normal life is built on other people's desperation.

## CONFIRMED OUTLINE

### HOOK
- Dien thoai reo luc 3 gio sang - mot "don hang" moi
- Weight line: "Ban khong cham vao ai. Ban chi goi dien."

### PHASE_EARLY: Khoi dau - Cach ban buoc vao
- Lon len trong khu o chuot - thay doi ngheo moi ngay
- Cong viec dau tien: chay viec vat cho mot "phong kham"
- Nguoi ta dua ban phong bi - ban chi can dua dia chi
- Time skip: tu ke chay viec thanh nguoi to chuc

### PHASE_CONFLICT: Leo thang - Ban tro thanh mat xich chinh
- Ban quan ly danh sach "nguoi ban" - tuyen tu khu ngheo
- Ban hua $5,000 - biet ho se chi nhan $1,500
- Ban sap xep chuyen bay cho "benh nhan" giau co
- Lan dau thay "nguoi ban" sau ca mo - nam trong khach san re tien
- Tu nhu: "Toi khong lam ai dau. Toi chi ket noi nguoi can voi nguoi co."
- So du tai khoan tang - vong tron ban be thu hep

### PHASE_CRISIS: Vu do vo
- Mot "nguoi ban" tre tuoi - khong tinh lai sau ca mo
- Bac si goi cho ban, khong phai canh sat
- Ban phai "xu ly" - don dep, phi tang, im lang
- Lan dau tien ban nhan ra: ban khong phai trung gian, ban la tong pham

### PHASE_RESOLUTION: Sau do
- Time skip: vai thang sau - ban van tiep tuc
- Dien thoai moi, danh sach moi, "nguoi ban" moi
- Nhung gio ban khong can tu thuyet phuc nua - ban da te liet
- Di an toi binh thuong - khong ai biet ban lam gi

### CALLBACK_CLOSE
- Dien thoai reo luc 3 gio sang - giong het HOOK
- Ban nhin man hinh. Ban biet do la gi.
- Weight line: "Ban co the dung. Ban biet dieu do. Nhung ban cung biet - ngay mai se co nguoi khac thay the."

## CHARACTER REGISTRY
> Source: `WORLD_CRIMINAL_ORGAN_BROKER.yaml`
> Approved: 2026-04-13. Used by `/pvle-gen-image-prompts`.

### Master Character Table
| Char_ID | Veil_Name | Visual_Summary | Face | Appears_In_Phases |
|---------|-----------|----------------|------|-------------------|
| CHAR_SUBJECT | "you" (SUBJECT) | Average build, plain dark clothes, disposable phone in hand, cheap briefcase. Clean-cut - looks like nobody. | dot eyes + simple mouth | ALL |
| CHAR_DOCTOR | "bac si" / "nguoi mo" | Male, surgical scrubs, rubber gloves, cold clinical posture | FACELESS | CONFLICT, CRISIS |
| CHAR_SELLERS | "nguoi ban" / "ho" | Poor, thin stickmen in worn clothes - different individuals across scenes | FACELESS | EARLY, CONFLICT, CRISIS |
| CHAR_BUYERS | "benh nhan" / "nguoi mua" | Wealthy-looking stickmen, expensive clothes, arriving at airport/hospital | FACELESS | CONFLICT |
| CHAR_RECRUITER_BOSS | "nguoi truoc ban" / "sep cu" | Male, older, heavier build, gold chain, expensive watch | FACELESS | EARLY |
| CHAR_YOUNG_SELLER | "nguoi ban tre" / "dua tre do" | Young, very thin, patched clothes - the one who doesn't wake up | FACELESS | CRISIS |

### SUBJECT Visual Traits by Phase
| Phase | Age_Range | Height | Hair | Clothing | Face | Distinguishing |
|-------|-----------|--------|------|----------|------|----------------|
| HOOK | 28-35 | AVERAGE | Short dark hair, unremarkable | Dark jacket, plain shirt, disposable phone glowing | dot eyes, awake/alert | Phone light in dark room |
| PHASE_EARLY | 16-22 | SHORT to AVERAGE | Short dark hair | Worn casual clothes, then plain button shirt | dot eyes, watchful | Thin, hungry look |
| PHASE_CONFLICT | 22-30 | AVERAGE | Short dark hair, neat | Dark jacket, plain clothes - deliberately forgettable | dot eyes, calculating then numb | Disposable phone + cash envelope |
| PHASE_CRISIS | 30-32 | AVERAGE | Same, slightly disheveled | Same dark jacket, now wrinkled | dot eyes, panicked then hollow | Blood-stained envelope (metaphor) |
| PHASE_RESOLUTION | 32-35 | AVERAGE | Same | Same clothes - nothing changed externally | dot eyes, flat/empty | New phone, same routine |
| CALLBACK | 35 | AVERAGE | Same | Same dark jacket, phone in hand | dot eyes, numb | Mirror of HOOK |

### Face Rule
- **SUBJECT (GENERIC_ARCHETYPE)**: dot eyes + simple mouth - expression evolves: watchful (EARLY) to calculating/numb (CONFLICT) to panicked (CRISIS) to flat/empty (RESOLUTION/CALLBACK)
- **ALL SUPPORTING CHARACTERS**: **FACELESS** - blank white circle head, no eyes, no mouth

### Injection Rules
- SUBJECT always has most visual detail among all characters in scene
- All supporting characters FACELESS - blank white circle head
- SUBJECT deliberately looks **ordinary, unremarkable** - visual metaphor for "the invisible middleman"
- **Signature visual**: disposable phone + cash envelope - phone changes but actions never do
- **Arc transition**: No major appearance change - horror is that **nothing changes externally while the person inside is already dead**
- Height does not scale dramatically - SUBJECT always AVERAGE, blends into crowd
- **Creative constraint**: NEVER show inside the operating room. All surgical aftermath shown through closed doors, bandages, hotel rooms.

## EPISODE NOTES
- **Duration**: 15 min target, 1755-2340 word budget
- **Beat count**: estimated 22-28 beats (EXTENDED profile)
- **Veil enforcement**: N/A (GENERIC_ARCHETYPE - no named individuals to veil)
- **Emotional arc**: WONDER (hook - the mundanity of evil) to TENSION (entering the system) to DREAD (escalation + first aftermath witnessed) to CLARITY (crisis - you ARE the system) to BITTERSWEET (moral paralysis) to DEEP_CONNECTION (callback - the cycle continues)
- **Callback structure**: Hook opens with phone ringing at 3am; Callback closes with same phone ringing at 3am - nothing changed, everything changed
- **Critical narrative device**: Self-rationalization as engine. Every action has an internal justification: "I just make calls", "They would do it without me", "I'm helping both sides." The viewer must feel HOW someone normalizes participation in organ trafficking.
- **Platform safety**: No graphic surgical content. No glorification. No power fantasy framing. Subject framed as logistics operator with moral distance from violence. Horror emerges from mundanity, not spectacle. Ending is moral paralysis, not coolness.
- **Creative constraint**: "NEVER_ENTER_OPERATING_ROOM" - entire narrative operates in the spaces between violence. Phone calls, addresses, envelopes, hotel rooms. The surgery happens behind a door you never open.
- **Forbidden**: Crime montage tone. Glorification. Cool villain framing. Graphic surgical imagery. Direct depiction of violence or organ extraction.
