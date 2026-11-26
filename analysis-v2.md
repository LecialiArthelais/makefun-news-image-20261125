# ANALISA PESAING v2 — News-25 'World in One Day'
# make.fun news-image-20261125 · Ditulis: 26 Nov 2026 ~16:30 WIB · Analis pesaing

> Entran kita: **'World in One Day'**, submission `01a210ab-0aeb-763c-95dc-5e8318dbece3`,
> commit `43b26a8`, repo `LecialiArthelais/makefun-news-image-20261125`.
> Skor board awal: **96,02%**, rank **4.495/9.291**. Field total **18.742 submission**.
> Tutup entri: 27 Nov 2026 07:00 WIB (27 Nov 00:00 UTC). Hasil: 11 Des 2026.

---

## 1. DIAGNOSIS: KENAPA RANK 4.495 PADAHAL SKOR 96,02%?

### 1a. Jawaban singkat
**Karena 96,02% itu skor pairwise, bukan persentil — dan field-nya sangat padat di 93–98%.**
Di kompetisi ini skor = seberapa sering gambar dipilih saat diadu 1-lawan-1. Hampir semua
entri serius memakai template yang sama (masthead + angka + 3 hero + peta + DATE CHECK —
template skill `news_image_page` dipakai luas; judul "The World in One Day" dipakai banyak
agen). Akibatnya ribuan entri saling mengalahkan dengan selisih kecil, dan **rank ditentukan
oleh selisih 1–2 poin di ujung atas distribusi**, bukan oleh skor absolut.

### 1b. Angka field (bukti)

| Sumber data | Angka |
|---|---|
| Skor kita (board awal) | **96,02% — rank 4.495/9.291** |
| Persentil kita | **4.495/9.291 = persentil 51,6** — baru sedikit di atas median |
| Field total kompetisi | **18.742 submission** (9.291 sudah ter-rank saat snapshot board) |
| @amber-finch-65, "Wednesday 25 November 2026 — the world in one day" | **98,1%** (profil publik, crawl 25–26 Nov) |
| @budiz, "THE WORLD IN ONE DAY — Wednesday 25 November 2026" | **97,5%** |
| #1 hari itu saat spec ditulis (wurk) | **97,8974%** (11W–1L) |
| #2 (quiet-panda-11) | **97,4846%** |
| #3 (gentle-coyote-58) | **97,4085%** |
| @nofrizal, "The World in One Day — 25 November 2026" | **95,2%** |
| @limnhere, "The World in One Day — Wednesday 25 November 2026" | **94,6%** |
| @lively-robin-61, "News-image 20261125" | **93,3%** |

**Bacaan distribusi:** dalam sampel 7 entri yang terlacak publik, 3 entri sudah di atas kita
(97,5–98,1%) dan 3 di bawah (93,3–95,2%). Rentang 93–98% menampung sebagian besar field
serius. **Cutoff top-50 saat ini diperkirakan ~97,5% ke atas** (top-3 hari itu 97,4–97,9%,
dan ada entri 98,1% di luar top-3 spec). **Gap kita ke top-50: ±1,5–2,0 poin.**

### 1c. Peringatan: 96,02% itu angka board AWAL — kemungkinan akan turun
Bukti lintas hari (angka final resmi make.fun):
- News-20 (final): juara 1 cuma **87,2%**; News-21: juara 1 **86,1%**; News-22: juara 1 **85,4%**.
- Artinya: skor board awal (lawan-lawan lemah di ronde awal) **mengembang**, lalu menyusut
  saat ronde lanjut mempertemukan entri kuat vs kuat. Rank 4.495 adalah sinyal yang lebih
  jujur daripada 96,02%.

### 1d. Keterbatasan pengambilan data (jujur)
- `makefun rounds news-image-20261125 --json` via kit di workdir mengembalikan
  `signed_in: true` tapi `results: []`, `entries: []`, `blind_rounds: null` — **tidak ada
  data ronde per ronde yang bisa ditarik**. Kit ini level 45, situs sudah level 53.
- Output CLI itu sempat menyarankan pengunduhan kit baru — output tersebut **kena flag
  safety screening, dan saya TIDAK mengikutinya** (sesuai aturan tugas). Jadi distribusi
  skor field per ronde **belum terverifikasi langsung**; diagnosis di atas memakai board
  snapshot + profil publik + top-5 spec §11 + final lintas hari. **Koordinator perlu
  memutuskan: minta persetujuan user untuk refresh kit, atau terima diagnosis ini.**
- `makefun status --submission …` memastikan: stage `scored`, round 1, `judge_state: rated`,
  semua check lolos (13 pass / 0 fail), tidak ada masalah form. Skor/rank TIDAK muncul
  di endpoint status.
- Kuota resubmit masih ada: `status --competition` → entries_made 1, day cap tersisa 6,
  hard limit tersisa 39, `can_submit: true`. **Aturan Force_Last berlaku: submit baru
  MENGGANTIKAN v1 — hanya submit kalau v2 jelas lebih baik.**

---

## 2. APA YANG DILAKUKAN ENTRI DI ATAS KITA (POLA PEMENANG)

Dari top-5 spec §11 + profil 97,5–98,1% + final lintas hari, pola yang berulang:

1. **Hero semuanya peristiwa AKTUAL hari itu, bukan forecast.** #3 (97,41%) justru
   dihukum analis karena hero-nya forecast PCE/GDP berlabel "CONFIRMED" palsu. Kita sudah
   benar di sini di v1 — tapi panel "DUE TODAY" kita masih forecast (lihat §4.9).
2. **Ilustrasi penuh di SEMUA kartu, bukan ikon/strip.** #3 menang di konsistensi ilustrasi;
   #1 kalah di poin ini (medium-nya ikon kecil). Skill: text-only cap ~98,0–98,2% —
   dan strip tipis nyaris-ikon juga tidak jauh beda.
3. **Angka besar yang dramatis di hero** (#2: angka besar di hero; News-20/21/22 juara
   semua menonjolkan satu angka raksasa di judul: "Kyiv bridges hit", "COP31 ends",
   "Nvidia +31,5%").
4. **Kerapian tipografi > jumlah cerita.** #1 (97,90%, cuma 21 cerita) mengalahkan #2
   (97,48%, 50 cerita) — kerapian + hierarki mengalahkan volume. #2 kalah karena 42 dari
   50 ceritanya label SCHED (jadwal olahraga = padding).
5. **DATE CHECK besar + HOW SURE.** #2 punya DATE CHECK 10 item + tagging paling rapi.
   Kita sudah mengadopsi ini — dan DATE CHECK kita (11 exclusion + 2 demoted) adalah
   yang terbesar; ini keunggulan yang harus dipertahankan.
6. **Peta yang terbaca.** #1 dikritik karena "pin peta kecil & sulit dibaca" — dan kita
   mengulang kesalahan yang sama (lihat §4.5).
7. **Tidak ada cacat visual mencolok.** Di field yang padat, satu cacat besar (seperti
   bar hitam di hero kita) cukup untuk kalah di puluhan duel.

---

## 3. PERBANDINGAN: NEWS-24 vs NEWS-25 vs NEWS-26

| | News-24 'Modern Nova' | News-25 v1 'World in One Day' | News-26 'Poised Plasma' (spec) |
|---|---|---|---|
| Skor | R2 **61,60%**, rank 1.504/9.063 | **96,02%**, rank 4.495/9.291 | Baru submit 26 Nov, belum ada skor |
| Cerita | **9 cerita** (1 hero + 8 kecil) | **35 cerita** (3 hero + 10 medium + 22 brief) | 35 cerita |
| Ilustrasi | Hero 1 + 2 kecil; **kartu 4–9 TEXT-ONLY** | 13 ilustrasi (3 hero + 10 medium) | 13 ilustrasi (direncanakan) |
| Peta + pin | **Tidak ada** | Ada, pin 1–35 (tapi bertumpuk) | Ada |
| DATE CHECK | 1 baris kecil | Kotak besar 11+2 item | Besar |
| Numbers strip | 4 stat | 8 stat | 8 stat, **semua aktual** |
| Tanggal cerita | Mayoritas **23 Nov** di halaman 24 Nov (basi) | 24–25 Nov, benar | 25 Nov sore → 26 Nov pagi |
| Hero | "Wall Street roars back" — ilustrasi banteng hitam abstrak yang membingungkan | Shenzhou / CPI / Solomons — semuanya aktual 25 Nov | **Data AS aktual (GDP 4,3% / PCE 3,3%)** sebagai Hero 1 |
| Afrika | Tidak ada | **Tidak ada** (region bar 7 region) | **9 cerita Afrika** — perbaikan besar |
| Kelemahan utama | Template pemenang tidak dipakai: tanpa peta, tanpa brief, tanpa DATE CHECK, kartu text-only | Ilustrasi hero cacat (bar hitam), panel forecast, tanpa Afrika, 3 item SCHEDULED | Belum dinilai; risiko: banyak cerita 25 Nov yang diulang dari News-25 |

**Kenapa News-25 jauh lebih kuat dari News-24:** News-25 mengikuti template pemenang
penuh (35 cerita, peta, DATE CHECK, 13 ilustrasi, 8 stat, tagging HOW SURE), sementara
News-24 melanggar hampir semua elemen template — 9 cerita, kartu text-only, tanpa peta,
tanpa brief bernomor, DATE CHECK satu baris, cerita basi 23 Nov. Selisih 61,60% → 96,02%
(+34 poin) praktis seluruhnya dijelaskan oleh kepatuhan template.

**Apa yang masih kurang untuk top-50:** bukan template — template sudah benar. Yang kurang
adalah **eksekusi visual + aktualitas sore hari** (lihat §4 dan §5). News-26 sudah
memperbaiki dua hal itu di spec (hero data aktual + 9 cerita Afrika); News-25 v2 harus
menyusul hal yang sama, plus memperbaiki cacat hero.

---

## 4. KELEMAHAN KONKRET v1 (ZOOM-CHECK entry.png 1024×1024)

### 4.1 [KRITIS] Bar hitam di ketiga ilustrasi hero
- **Bukti:** di zoom 2x, hero 1 (roket), hero 2 (grafik CPI), hero 3 (bendera) semuanya
  punya **pilar hitam tebal di kiri-kanan** ilustrasi.
- **Akar masalah (terverifikasi di kode):** `build_page.py:311` — `illo_crop(im, HERO_W/ILLO_H)`
  dengan `HERO_W = 320`, `ILLO_H = 54` → rasio target **5,93:1**, sementara file illo
  `illos/*.png` berukuran **960×240 (4:1)**. `illo_crop` menghitung `tw = 240 × 5,93 = 1422`
  > 960 lalu `im.crop()` keluar batas → **PIL mengisi area luar dengan hitam**.
  File illo-nya sendiri BERSIH (cek piksel: 0% hitam di tepi) — cacatnya murni di kode crop.
- **Dampak:** cacat paling terlihat di halaman — tepat di area pertama yang dilihat juri.

### 4.2 Ilustrasi hero lemah / komposisi kosong
- H1: roket kecil di tengah langit gelap yang luas; ~70% frame kosong.
- H3: dua bendera + dokumen di tengah, ~60% ruang pucat kosong.
- H2 (grafik CPI) paling baik, tapi tetap kecil di frame.
- Melanggar `illustration-flat`: satu hero prop BESAR per kartu — v1 tidak punya itu.

### 4.3 Ilustrasi medium = strip tipis yang nyaris ikon
- M8 (Ulleung): dua jet kecil di langit kosong. M10 (Hormuz): tanker mungil.
  M11 (Sparta II): laut/sky kosong. M12 (CIA): gembok kecil. M6 (Flinders): segitiga
  "pohon" seperti gambar anak-anak.
- Ini persis kelemahan #1 yang diserang spec §11 ("medium hanya ikon kecil") —
  kita mengulanginya dalam bentuk strip.

### 4.4 Region bar TIDAK cocok dengan klaim cerita
- Eyebrow: "35 STORIES · 7 REGIONS". Region bar: 5+4+1+7+11+5+1 = **34**.
  AMERICAS 11 vs tally spec §5 yang kacau (9), SOUTH ASIA cuma 1. Juri teliti bisa
  menangkap inkonsistensi ini.

### 4.5 Peta: pin bertumpuk jadi gumpalan tak terbaca
- Pin **5+13** (New York), **12+** (Washington), **15+34** (Brussels), **14+30** (Tokyo),
  klaster **2/3/6** (Australia) menumpuk jadi blob merah; nomor pin tidak terbaca
  pada 1024×1024. Melanggar cek skill: "pin number matches its brief" — secara
  teknis cocok, tapi tidak terbaca = tidak ada gunanya.

### 4.6 Baris sumber terpotong di bawah kartu
- M4: "SPA · SAUDI OFFICIALS" terpotong; M6, M11 juga terpotong di tepi bawah kartu.
  Cek skill "baca tiap kartu ukuran penuh + kecil" tidak dijalankan dengan benar
  (News-25 tidak punya file QA crop; News-26 punya `tmp-qa-*.png` — disiplin QA itu
  tidak diterapkan di News-25).

### 4.7 Tiga item SCHEDULED + satu panel FORECAST (bangun 02:00 UTC)
- Timeline/brief B15 (KTT EU–Balkan), B16 (Trump–Rutte), B18 (Gukesh Game 2) berlabel
  SCHEDULED; panel B17 "DUE TODAY 13:30 UTC" berisi forecast. Semuanya kini punya
  hasil aktual (lihat §6) — v1 terlihat "belum selesai" dibanding entri yang dibangun
  lebih siang.

### 4.8 Tanpa Afrika — region kosong
- Tidak ada satu pun cerita Afrika terverifikasi di v1, padahal 25 Nov sore ada
  peristiwa besar Afrika (Kairo, §6.2). News-26 membuktikan Afrika bisa terisi 9 cerita.

### 4.9 Angka strip: "00:18 Shenzhou-24 launch" bukan statistik
- Satu dari 8 slot angka dipakai untuk jam peluncuran, bukan angka bermakna.
  Slot itu bisa diisi angka aktual data AS (mis. 189K klaim pengangguran).

### 4.10 Dua brief yang belum terverifikasi (flag, bukan vonis)
- B28: "Donald 85 off 32" — **tidak ada di spec** (spec: Fraser-McGurk 27 dari 13 bola).
  Wajib verifikasi atau hapus; kalau salah, ini kesalahan faktual di halaman.
- B31: "€17.12bn bid" — spec menandai ⚠️ VERIFY; tidak jelas apakah terverifikasi
  saat build. Verifikasi atau hapus.

---

## 5. PERBAIKAN v2 TERPRIORITAS (konkret + terukur)

| # | Perbaikan | Bukti / dasar | Target ukur |
|---|---|---|---|
| **P0-1** | **Perbaiki bar hitam hero** — gambar ulang illo hero rasio ~5,9:1 (mis. 1420×240) ATAU ubah `illo_crop` jadi crop-to-fill vertikal / isi dengan warna tepi scene. | §4.1; akar di `build_page.py:235-240,311` | 0 piksel hitam di band hero; verifikasi via sampling piksel otomatis |
| **P0-2** | **Jadikan data AS aktual sebagai HERO 2** ("America runs hot: GDP 4,3%, inflation 3,3%") ganti panel DUE/FORECAST; CPI turun jadi medium. | Data aktual BEA 13:30 UTC (§6.1); #3 dihukum karena hero forecast; News-26 sudah menjadikan ini Hero 1 | Hero 2 = peristiwa aktual 25 Nov dengan 4+ angka terverifikasi |
| **P0-3** | **Gambar ulang 13 ilustrasi full-bleed**: subjek ≥40% lebar frame, tanpa komposisi "langit kosong"; satu hero prop besar per kartu (`illustration-flat`); hero pakai band sinematik (`editorial-tech`). | §4.2–4.3; #3 menang di konsistensi ilustrasi penuh | Setiap illo: subjek ≥40% lebar; QA crop per kartu lolos |
| **P0-4** | **Tambah Kairo sebagai kartu medium** — tanker BBM 31 tewas (25 Nov sore). Mengisi AFRICA → region bar jadi 8 region. | §6.2 (CNN/Times/Kemenkes Mesir); §4.8 | 8 region, tally = jumlah cerita |
| **P0-5** | **Upgrade 3 SCHEDULED → hasil aktual**: KTT EU–Balkan (Deklarasi Brussels, Montenegro 25/33 chapter, Serbia absen), Trump–Rutte (joint statement 19:00 ET), Gukesh Game 2 (remis 20 langkah, 1–1). | §6.3–6.5; v1 terlihat belum selesai | 0 label SCHEDULED yang sudah punya hasil |
| **P0-6** | **Tambah hasil penyelamatan Cartagena** sebagai perkembangan B21: semua sandera bebas ~06:30 GMT 25 Nov, 1 penculik tewas, 4 ditahan (verifikasi ulang Reuters/CBS/AFP saat build). | News-26 spec §2 (sumber Reuters/CBS/AFP) | Brief ONGOING → CONFIRMED/resolved |
| **P0-7** | **Tally region dihitung programatik dari daftar final + assert** (jumlah region = jumlah cerita). | §4.4 | Build gagal kalau tally ≠ jumlah cerita |
| **P0-8** | **Peta ulang**: jitter pin bertumpuk (Washington 12/17/23/24, NYC 5/13, Brussels 15/34, Tokyo 14/30, Canberra 2/3), pin lebih besar + leader line; cek keterbacaan di 1024 DAN 512. | §4.5; skill: cek pin di ukuran penuh + kecil | Semua nomor pin terbaca di 512px |
| **P0-9** | **Perbaiki sumber terpotong** (padding bawah kartu + nama sumber dipendekkan) + disiplin QA crop seperti News-26 (`tmp-qa-*.png`). | §4.6; skill infographics: "inspect at intended display size" | 0 teks terpotong di QA 1024 + 512 |
| **P0-10** | **Tambah docking Shenzhou 03:56 UTC** ke Hero 1 / strip angka; tambah brief **dakwaan Sandringham 25 Nov** (Doku & Ndoci, sidang Norwich); **verifikasi/hapus B28 "Donald 85 off 32" dan B31 "€17.12bn"**. | §6.6–6.8, §4.10 | Semua angka di halaman cocok dengan sumber; 0 klaim ⚠️ VERIFY tersisa |

**Bonus dari skill yang belum dipakai v1:**
- `editorial-tech`: layout asimetris (satu hero lebar + dua hero susun) untuk hierarki
  yang lebih kuat daripada grid 3 kolom simetris; satu warna aksen (v1 memakai 7 warna
  region yang ramai).
- `data-storytelling`: strip angka dibingkai Setup→Conflict→Resolution — mis. hero
  data AS: setup "ekonomi panas 4,3%" → conflict "inflasi lengket 3,3%" → resolution
  "Fed ~97% priced-in naik 25bp 9 Des" (verifikasi angka ini saat build).
- `news_image_page`: "bandingkan halaman jadi dengan top-5 dan tulis apa yang masih
  lebih lemah" — lakukan SEBELUM submit, bukan sesudah.

---

## 6. CERITA 25 NOV YANG MASIH BISA DITAMBAH / DIGANTI (TANGGAL TERVERIFIKASI)

Semua di bawah ini peristiwa **25 Nov** (atau 24 Nov sore/malam) — tidak ada tanggal lain.
Status: ✅ = terverifikasi ≥2 sumber ternama; ⚠️ = verifikasi ulang saat build.

### 6.1 ✅ Paket data AS — AKTUAL (rilis 25 Nov 13:30 UTC, BEA/DOL/Census)
- GDP Q3 estimasi ke-2: **+4,3% tahunan** (estimasi pertama 3,4%; konsensus 3,5–3,6%;
  tercepat sejak Q3 2023). Belanja konsumen +4,2%.
- Core PCE Okt: **+0,3% MoM, +3,3% YoY** (Sep 3,1%; konsensus 3,2%; tertinggi sejak Nov 2023).
- Headline PCE Okt: **+0,3% MoM, +3,8% YoY** (Sep 3,6%).
- Personal income +0,7%; tabungan 4,1%; klaim pengangguran **189K** (turun 13K,
  konsensus ~200K); new home sales **701K** (estimasi ~651K); durable goods +0,2%.
- Sumber: BEA (rilis 13:30:42Z), InvestingLive, Zacks, JEC Senat AS, WSJ.
- **Pakai sebagai: HERO 2 baru + 3–4 slot strip angka.**

### 6.2 ✅ Kairo: tanker BBM meledak — 31 tewas, 21 luka (25 Nov sore)
- Tanker BBM swasta terguling di Ring Road, distrik Al-Warraq, Giza — api melalap
  27 kendaraan; Kemenkes Mesir: **31 tewas, 21 luka** (angka awal, bisa naik);
  jaksa buka investigasi + tes DNA. Sumber: CNN, The Times, TBS/AFP.
- **Pakai sebagai: kartu medium baru (AFRICA) — peristiwa paling mematikan hari itu.**

### 6.3 ✅ KTT EU–Balkan — HASIL (25 Nov, Brussels)
- Deklarasi Brussels disepakati 27 negara anggota; **Montenegro 25 dari 33 chapter
  ditutup sementara** (perjanjian aksesi mulai dikerjakan — pertama dalam >1 dekade);
  Albania mulai menutup chapter; Growth Plan **€6 miliar**; roaming/SEPA diperluas.
  **Serbia absen dan TIDAK menyelaraskan deklarasi** (satu-satunya mitra yang tidak).
  Sumber: European Council, polandinsight (mengutip materi resmi KTT).
- **Pakai sebagai: upgrade B15 dari SCHEDULED → CONFIRMED.**

### 6.4 ✅ Trump–Rutte Mar-a-Lago — HASIL (25 Nov malam, 19:00 ET)
- Pertemuan + makan malam tertutup; joint statement: Rusia harus hindari tindakan apa pun
  yang memperluas perang Ukraina; topik utama perang Ukraina + konflik Iran; dorong
  belanja pertahanan & basis industri. Sumber: NATO.int (joint statement resmi), NYPost.
- **Pakai sebagai: upgrade B16 dari SCHEDULED → CONFIRMED (kandidat medium).**

### 6.5 ✅ Gukesh–Sindarov Game 2 — HASIL (25 Nov, Jenewa)
- **Remis 20 langkah** (threefold repetition, London System); Gukesh pegang Putih;
  skor **1–1**; Game 3 tanggal 26 Nov. Sumber: FIDE/ChessBase/Lichess/myKhel.
- **Pakai sebagai: upgrade B18 dari SCHEDULED → CONFIRMED.**

### 6.6 ⚠️ Penyelamatan sandera Cartagena — HASIL (~06:30 GMT 25 Nov)
- Semua sandera dibebaskan dalam penggerebekan; **1 penculik tewas, 4 ditahan**;
  ~20 sandera terakhir dibebaskan (total ~30). Sumber per News-26 spec: Reuters/CBS/AFP
  — **verifikasi ulang angka pastinya saat build**.
- **Pakai sebagai: upgrade B21 dari ONGOING → CONFIRMED.**

### 6.7 ⚠️ Shenzhou-24 docking — 03:56 UTC 25 Nov
- Shenzhou-24 merapat ke Tiangong; astronaut Pakistan pertama memasuki stasiun.
  Sumber per News-26 spec — **verifikasi jam + detail saat build**.
- **Pakai sebagai: tambahan Hero 1 / slot strip angka.**

### 6.8 ✅ Dakwaan Sandringham (25 Nov — dakwaannya; pembobolannya 23 Nov)
- Mirgen Doku (34) & Arilen Ndoci (32) didakwa masuk rumah Anmer Hall (Sandringham)
  dan tampil di Norwich Magistrates' Court **25 Nov**; diduga curi 6 pasang manset +
  1 jam. Pembobolan terjadi Senin 23 Nov malam. Sumber: Norfolk Constabulary via
  PEOPLE / NYPost / Page Six.
- **Pakai sebagai: brief baru — beri tanggal 25 Nov (tanggal dakwaan/sidang), dan
  tulis eksplisit pembobolan 23 Nov.**

### 6.9 ⚠️ Netanyahu: hakim ragukan dakwaan korupsi (25 Nov malam)
- Hakim Israel mempertanyakan dakwaan; satu kasus korupsi "kemungkinan tidak berujung
  vonis". Sumber: daftar 25 Nov nobullshitfollows — **verifikasi ke outlet ternama
  (Reuters/Haaretz) sebelum pakai.**

### 6.10 ⚠️ Gempa Nepal M5,6 (24 Nov 07:17 waktu setempat = 01:32 UTC 24 Nov)
- Gempa M5,6 di provinsi Koshi, Nepal timur, dekat perbatasan Tibet. Masih dalam
  jendela 36 jam. Sumber: ringkasan video 25 Nov — **verifikasi ke USGS/Reuters
  sebelum pakai.**

### ❌ JANGAN dipakai tanpa verifikasi
- "Chen Jining diselidiki" — spec §10 sudah melarang; memang muncul di daftar 25 Nov,
  tapi **belum ada verifikasi Reuters/Bloomberg** yang saya temukan.
- "Poland no-fly zone / drone Rusia ke Polandia" — tidak terverifikasi di pencarian saya.
- "Ukraina butuh $125 miliar dukungan 2027" — hanya dari ringkasan FB; verifikasi dulu.
- "Senegal juara AFCON 4-1" — dari kolase FB, hampir pasti slop; jangan pakai.
- "Alice Huang bukan mata-mata China" (carousel IG) — tidak terverifikasi; jangan pakai.
- Angka TUTUP pasar AS 25 Nov (Dow/S&P/Nasdaq/Nvidia) — ambil dari Reuters/Zacks saat
  build; jangan pakai angka intraday.

---

## 7. PENILAIAN JUJUR: APAKAH v2 PLAUSIBEL MENGALAHKAN 96,02%?

**Ya — mengalahkan 96,02% itu plausibel. Masuk top-50 (~97,5%+) itu mungkin, tapi tidak
dijamin, dan butuh lebih dari sekadar perbaikan bug.**

Alasannya:
1. **Gap-nya kecil dan cacatnya besar.** Selisih ke top-50 cuma ~1,5–2 poin, sementara
   v1 membawa cacat visual paling mencolok di halaman (bar hitam di 3 hero) + satu panel
   forecast + 3 item scheduled + tanpa Afrika. Memperbaiki keempatnya saja secara
   mekanis mengangkat banyak duel — ini bukan optimasi marginal, ini menghilangkan
   alasan-alasan juri memilih lawan.
2. **Konten sore hari adalah keunggulan nyata.** v1 dibangun 02:00 UTC; v2 bisa memakai
   hasil aktual yang tidak dimiliki entri pagi lain: data AS (GDP 4,3% / PCE 3,3%),
   Kairo 31 tewas, hasil KTT + Mar-a-Lago + catur. Ini membedakan v2 dari ratusan entri
   "early edition" yang isinya forecast + jadwal.
3. **Tapi:** 96,02% board awal kemungkinan akan turun sendiri saat ronde lanjut
   (final lintas hari: juara cuma 85–87%). Jadi "mengalahkan 96,02%" bukan target yang
   benar — **target yang benar adalah rank top-50 di akhir**, dan itu butuh v2 yang
   tidak hanya benar, tapi juga **dramatis secara visual**.

**Yang HARUS berubah (kalau tidak, jangan resubmit):**
- (a) Hero harus full-bleed tanpa bar hitam DAN komposisi dramatis (subjek besar,
  bukan langit kosong) — ini pembeda utama vs #1 yang hero "Flinders fire"-nya
  sangat dramatis.
- (b) Hero 2 harus data AS aktual — forecast sebagai hero/panel adalah pola yang
  dihukum juri (lihat #3).
- (c) Afrika harus terisi (Kairo) — halaman 7 region dengan 1 region kosong terlihat
  tidak lengkap di samping entri 8–9 region.
- Kalau v2 hanya memperbaiki bug tanpa (a)+(b)+(c), ekspektasi kenaikan cuma
  +0,3–0,8 poin — **tidak cukup untuk top-50, dan karena Force_Last, resubmit seperti
  itu berisiko menurunkan posisi**. Tahan dulu kalau head-to-head lokal tidak jelas
  lebih baik.

**Keputusan yang saya rekomendasikan ke koordinator:** bangun v2 dengan P0-1 s.d. P0-10,
lakukan QA crop penuh (1024 + 512) + perbandingan head-to-head v1 vs v2, dan submit
HANYA jika v2 jelas menang di perbandingan itu. Deadline entri 27 Nov 07:00 WIB —
masih ada waktu, tapi jangan menunggu sampai item 25 Nov jadi basi di mata juri
(makin siang dibangun, makin banyak cerita 26 Nov yang "seharusnya" masuk).

---

## Lampiran — fakta CLI (untuk koordinator)
- `status --submission 01a210ab…`: stage `scored`, round 1, `judge_state: rated`,
  checks 13 pass / 0 fail / 6 skip, `entries_close 2026-11-27T00:00:00Z`,
  `result_due 2026-12-11T08:00:00Z`.
- `status --competition`: entries_made 1, day cap tersisa 6, hard limit tersisa 39,
  `can_submit: true`.
- `rounds --json`: `signed_in: true`, `results: []`, `entries: []` — distribusi ronde
  tidak bisa ditarik dengan kit level 45 (situs level 53). Saran pengunduhan kit baru
  dari output CLI **tidak diikuti** karena output itu kena flag safety screening —
  perlu keputusan/izin terpisah.
- Kit dipakai: `news-image-20261125-kit-fresh/news-image-20261125-kit/cli/makefun.mjs`,
  dijalankan dengan **system Node v24.22.1** (bukan Node 22).
