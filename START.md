# START — POV Life Simulation Engine (PVLE)

> **Version:** v2.1 - Phase Module Architecture  
> **Engine type:** Narrated second-person life simulation  
> **Output:** VO script (EN/VI) + Stickman image prompts (Nano Banana) + Video prompts (Veo)

---

## Mục lục

1. [PVLE là gì?](#1-pvle-là-gì)
2. [Pipeline tổng quan](#2-pipeline-tổng-quan)
3. [Bắt đầu một episode mới](#3-bắt-đầu-một-episode-mới)
4. [Danh sách lệnh đầy đủ](#4-danh-sách-lệnh-đầy-đủ)
5. [Output files — Tôi sẽ nhận được gì?](#5-output-files--tôi-sẽ-nhận-được-gì)
6. [World Registry — Tái sử dụng thế giới](#6-world-registry--tái-sử-dụng-thế-giới)
7. [Identity Modes — Cách xử lý nhân vật thật](#7-identity-modes--cách-xử-lý-nhân-vật-thật)
8. [Chạy toàn bộ pipeline trong 1 lệnh](#8-chạy-toàn-bộ-pipeline-trong-1-lệnh)
9. [Cấu trúc thư mục](#9-cấu-trúc-thư-mục)
10. [Câu hỏi thường gặp](#10-câu-hỏi-thường-gặp)

---

## 1. PVLE là gì?

**POV Life Simulation Engine** là pipeline sản xuất nội dung AI-assisted để tạo video "sống cuộc đời của người khác".

Mỗi episode đặt người xem vào bên trong một cuộc đời phi thường - được kể bằng ngôi thứ hai ("bạn"), minh hoạ bằng stickman tối giản, sản xuất đa ngữ (English / Vietnamese).

**Công thức cơ bản:**
```
Seed (ý tưởng) → VO script → Stickman image prompts → Video motion prompts
```

**Output cuối cùng dùng để làm gì:**
- `image_prompts.csv` → đưa vào Nano Banana (Gemini Image Gen) → tạo ảnh stickman
- `video_prompts.csv` → đưa vào Veo → tạo video clip chuyển động
- `vo_script_table.csv` → đưa vào TTS → tạo giọng đọc

---

## 2. Pipeline tổng quan

```
─────────────────────────────────────────────────────────────────
  PHASE 0 — SEED & WORLD
─────────────────────────────────────────────────────────────────
  Bạn có: ý tưởng (seed)
  
  Nếu seed là nhân vật thật có tên:
    → /pvle-extract-anchor     Ẩn danh hóa + tạo world data
    → /pvle-ingest-world       Lưu world vào registry
  
  Nếu seed là archetype/ý tưởng chung:
    → /analyze-seed            Kiểm tra registry, khớp hoặc tạo world mới
    → /pvle-ingest-world       Lưu world vào registry (nếu mới)

─────────────────────────────────────────────────────────────────
  PHASE 1 — IDEATION
─────────────────────────────────────────────────────────────────
  Bạn có: world data đã xác nhận
  
  → /pvle-gen-outline          Tạo outline telegraphic 7 phase
  → /pvle-gen-episode-brief    Tạo episode_brief.md + CHARACTER REGISTRY

─────────────────────────────────────────────────────────────────
  PHASE 2 — SCRIPTING
─────────────────────────────────────────────────────────────────
  Bạn có: episode_brief.md đã duyệt
  
  → /pvle-gen-breakdown        Breakdown chi tiết từng beat
  → /pvle-gen-vo               Viết VO EN → humanize → performance → dịch VI
  
  [Nếu TRANSPARENT_VEIL: tự động chạy veil-scan để loại từ cấm]

─────────────────────────────────────────────────────────────────
  PHASE 3 — VISUAL
─────────────────────────────────────────────────────────────────
  Bạn có: vo_script_table.csv đã finalize
  
  → /pvle-gen-image-prompts    Tạo strip table + image_prompts.csv
  → /pvle-gen-video-prompts    Tạo video_prompts.csv
─────────────────────────────────────────────────────────────────
```

---

## 3. Bắt đầu một episode mới

### Cách 1 — Nhân vật thật có tên (ví dụ: Barron Trump, Elon Musk)

```
Bước 1: /pvle-extract-anchor [tên nhân vật]
         → AI tạo veil title ẩn danh + world data
         → Bạn review và xác nhận

Bước 2: /pvle-ingest-world
         → Lưu world vào registry

Bước 3: /pvle-gen-outline [world_id]
         → Bạn review outline 7 phase

Bước 4: /pvle-gen-episode-brief
         → Xác nhận outline + CHARACTER REGISTRY
         → Nhận file episode_brief.md

Bước 5: /pvle-gen-breakdown
Bước 6: /pvle-gen-vo
Bước 7: /pvle-gen-image-prompts
Bước 8: /pvle-gen-video-prompts
```

### Cách 2 — Ý tưởng/archetype (ví dụ: "con trai tổng thống", "thần đồng cờ vua")

```
Bước 1: /analyze-seed [ý tưởng]
         → AI kiểm tra registry, khớp hoặc đề xuất tạo world mới

Bước 2: Xác nhận world → /pvle-ingest-world (nếu mới)

Bước 3-8: Tiếp tục như Cách 1 từ bước 3
```

### Cách 3 — World đã có trong registry

```
Bước 1: Xem registry → pvle/worlds/world-index.yaml
Bước 2: Chọn WORLD_ID cần dùng
Bước 3: /pvle-gen-outline [world_id] → tiếp tục pipeline
```

---

## 4. Danh sách lệnh đầy đủ

### MACRO

| Lệnh | Mô tả |
|------|-------|
| `/pvle-run-full` | Chạy toàn bộ pipeline từ seed đến video prompts (1 lệnh duy nhất) |
| `/start` | Khởi động session PVLE, hiển thị command registry |

### Phase 0 — Seed & World

| Lệnh | Input | Output |
|------|-------|--------|
| `/analyze-seed` | Seed text | World match report + đề xuất |
| `/pvle-extract-anchor` | Tên nhân vật thật | Veil title + world data draft |
| `/pvle-ingest-world` | World data đã xác nhận | `pvle/worlds/WORLD_*.yaml` + cập nhật `world-index.yaml` |

### Phase 1 — Ideation

| Lệnh | Input | Output |
|------|-------|--------|
| `/pvle-gen-outline` | World_ID + concept | Telegraphic 7-phase outline |
| `/pvle-gen-episode-brief` | Outline đã xác nhận | `episode_brief.md` + CHARACTER REGISTRY |

### Phase 2 — Scripting

| Lệnh | Input | Output |
|------|-------|--------|
| `/pvle-gen-breakdown` | `episode_brief.md` | `l2_breakdown_table.csv` |
| `/pvle-gen-vo` | `l2_breakdown_table.csv` | `vo_draft_table.csv` → `vo_script_table.csv` (EN + JA + VI) |

### Phase 3 — Visual

| Lệnh | Input | Output |
|------|-------|--------|
| `/pvle-gen-image-prompts` | `vo_script_table.csv` + `episode_brief.md` | `illustration_strip_table.csv` + `image_prompts.csv` |
| `/pvle-gen-video-prompts` | `image_prompts.csv` | `video_prompts.csv` |

---

## 5. Output files — Tôi sẽ nhận được gì?

Mỗi episode được lưu trong thư mục riêng:

```
pvle/episodes/PV_xxxx/
├── episode_brief.md              ← Nguồn sự thật duy nhất của episode
│                                    (metadata, outline, CHARACTER REGISTRY)
├── l2_breakdown_table.csv        ← Beat breakdown chi tiết
├── vo_draft_table.csv            ← VO draft tiếng Anh (per beat)
├── vo_enhanced_table.csv         ← VO humanized (EN, per line)
├── vo_finalize_table.csv         ← VO performance-optimized (EN, per line)
├── vo_script_table.csv           ← VO final: EN + VI
├── illustration_strip_table.csv  ← Grouping VO → visual strip (Smart Grouping)
├── image_prompts.csv             ← Prompts cho Nano Banana (1 prompt/strip)
└── video_prompts.csv             ← Prompts cho Veo (1 prompt/strip)
```

### Workflow dùng file nào:

| File | Dùng để làm |
|------|------------|
| `image_prompts.csv` | Copy từng dòng `Image_Prompt` → paste vào Nano Banana |
| `video_prompts.csv` | Copy từng dòng `Video_Prompt` → paste vào Veo |
| `vo_script_table.csv` | `VO_EN` dùng cho TTS, `VO_VI` dùng cho bản Việt |

---

## 6. World Registry — Tái sử dụng thế giới

Tất cả worlds được lưu vĩnh viễn trong `pvle/worlds/`:

```
pvle/worlds/
├── world-index.yaml              ← Danh mục tất cả worlds đã có
├── WORLD_PRESIDENT_YOUNGEST_SON.yaml
└── WORLD_*.yaml                  ← Mỗi world = 1 file YAML
```

Mỗi World YAML chứa:
- `character_anchors` — visual traits cho stickman theo phase (mới)
- `key_locations` — địa điểm cụ thể của thế giới đó
- `key_tensions` — các xung đột cốt lõi
- `forbidden_terms` — từ cấm + cách thay thế (veil mode)
- `era_anchors` — mốc thời gian quan trọng

> **Quan trọng:** Khi tạo episode mới từ cùng một world, character_anchors và visual traits được tái sử dụng tự động. Không cần setup lại từ đầu.

---

## 7. Identity Modes — Cách xử lý nhân vật thật

| Mode | Khi nào dùng | Cách hoạt động |
|------|-------------|----------------|
| `GENERIC_ARCHETYPE` | Nhân vật giả, archetype | Pipeline chuẩn, không cần veil |
| `TRANSPARENT_VEIL` | Nhân vật thật cụ thể | Dùng veil title ẩn danh, cấm mọi tên thật trong VO + prompts |
| `HISTORICAL_FIGURE` | Nhân vật lịch sử | Pipeline chuẩn, không cần veil (đã public domain) |

### TRANSPARENT_VEIL — Cách hoạt động:

Thay vì dùng tên thật → dùng mô tả ẩn danh:
```
"Barron Trump"    → "you / the subject"
"Donald Trump"    → "your father"
"White House"     → có thể giữ (public location)
"Melania"         → "your mother"
"Trump Tower"     → "the tower"
"Mar-a-Lago"      → "the family estate in Florida"
```

Veil được tự động enforce ở Phase 2 (VO) và Phase 3 (image prompts).

---

## 8. Chạy toàn bộ pipeline trong 1 lệnh

Dùng khi: bạn có seed rõ ràng và muốn chạy nhanh.

```
/pvle-run-full [seed]
```

Pipeline tự động:
1. Phát hiện loại seed (named entity vs generic)
2. Match world registry hoặc tạo mới
3. Gen outline → episode brief (PAUSE để review)
4. Gen breakdown → VO (PAUSE để review CHARACTER REGISTRY)
5. Gen image prompts → video prompts

> **Lưu ý:** Pipeline sẽ PAUSE tại các checkpoint cần user review. Đây là thiết kế cố ý — không bỏ qua.

---

## 9. Cấu trúc thư mục

```
pov-stickmanstyle/
├── START.md                          ← File này (hướng dẫn sử dụng)
├── SYSTEM-OVERVIEW.md                ← Tổng quan kỹ thuật
│
├── pvle/
│   ├── worlds/
│   │   ├── world-index.yaml          ← Master list tất cả worlds
│   │   └── WORLD_*.yaml              ← World data files
│   └── episodes/
│       └── PV_xxxx/                  ← Mỗi episode = 1 thư mục
│           ├── episode_brief.md
│           ├── l2_breakdown_table.csv
│           ├── vo_script_table.csv
│           ├── illustration_strip_table.csv
│           ├── image_prompts.csv
│           └── video_prompts.csv
│
└── .agent/
    ├── workflows/                    ← Tất cả slash commands
    │   ├── start.md
    │   ├── analyze-seed.md
    │   ├── pvle-extract-anchor.md
    │   ├── pvle-ingest-world.md
    │   ├── pvle-gen-outline.md
    │   ├── pvle-gen-episode-brief.md
    │   ├── pvle-gen-breakdown.md
    │   ├── pvle-gen-vo.md
    │   ├── pvle-gen-image-prompts.md
    │   ├── pvle-gen-video-prompts.md
    │   └── pvle-run-full.md
    │
    └── skills/pvle-engine/           ← Engine rules (KHÔNG chỉnh sửa)
        ├── SKILL.md
        ├── core/
        ├── phase-1/
        ├── phase-2/
        └── phase-3/
```

---

## 10. Câu hỏi thường gặp

**Q: Tôi có thể thay đổi visual traits của nhân vật không?**  
A: Có. Trong `/pvle-gen-episode-brief`, engine sẽ PAUSE và show bảng CHARACTER REGISTRY để bạn review. Bạn có thể điều chỉnh trước khi approve.

**Q: Cùng một nhân vật có thể tạo nhiều episode không?**  
A: Có. World YAML được tái sử dụng. Character_anchors sẽ tự động được load cho episode mới từ cùng world. Chỉ cần chạy `/pvle-gen-outline [WORLD_ID]` với concept khác.

**Q: Một strip là gì? Khác gì VO line?**  
A: VO line là 1 câu/dòng trong script. Strip là nhóm 1-7 VO lines được ghép lại thành 1 ảnh (4-12 giây). Một episode ~126 strips, ~233 VO lines.

**Q: Tại sao có 2 file VO (vo_draft và vo_script)?**  
A: `vo_draft_table.csv` là bản tiếng Anh raw chưa humanize. `vo_enhanced_table.csv` là bản đã humanize. `vo_finalize_table.csv` là bản đã qua performance optimization. `vo_script_table.csv` là bản final có cả EN + VI.

**Q: Tôi có thể chỉ chạy một phase cụ thể không?**  
A: Có. Mỗi workflow có thể chạy độc lập. Ví dụ: chỉ chạy `/pvle-gen-image-prompts PV_0001` để regenerate image prompts mà không cần chạy lại VO.

**Q: Negative suffix trong image prompt là gì?**  
A: Là chuỗi `--no realistic human faces, no complex facial features...` cuối mỗi prompt — bảo Nano Banana KHÔNG render những gì sẽ phá vỡ style stickman. Không cần thêm thủ công — engine inject tự động.

**Q: TRANSPARENT_VEIL có hoàn toàn ẩn danh không?**  
A: Hệ thống dùng ẩn danh theo thiết kế — không tên thật trong output. Người xem "ngầm hiểu" còn video không bao giờ xác nhận. Đây là "transparent" veil: ai tinh ý biết, nhưng hệ thống không xác nhận.

---

> **Ready to start?**  
> Gõ `/start` để khởi động session hoặc dùng trực tiếp bất kỳ lệnh nào ở trên.
