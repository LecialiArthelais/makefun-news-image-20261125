# BUILD v2 — News-25 'World in One Day' (26 Nov 2026)

Entri v1: 'World in One Day', submission `01a210ab-0aeb-763c-95dc-5e8318dbece3`,
commit `43b26a8`, skor **96,02%**, rank **4.495/9.291**. v2 dibangun oleh Builder v2
(Hire #2) dari `analysis-v2.md` (analis pesaing, 26 Nov ~16:30 WIB) + skill baru
huashu-design (31.015★) dan market-news-analyst (8.509★).

## Perubahan v2 vs v1 (P0-1 s.d. P0-10 — semua dikerjakan)
1. **Bar hitam hero (P0-1):** `illo_crop` ditulis ulang jadi cover-crop yang
   tidak pernah keluar batas (crop horizontal bila slot lebih sempit dari 4:1,
   crop vertikal bila lebih lebar). Verifikasi piksel: **0 piksel hitam** di
   zona hero (y 165–420) dan di tiap band hero H1/H2/H3.
2. **Hero 1 = data AS aktual (market-news-analyst):** "America runs hot: GDP
   jumps 4.3% as inflation sticks at 3.3%" — GDP Q3 +4,3% (est. pertama 3,4%,
   konsensus 3,5–3,6%), core PCE +0,3% MoM / +3,3% YoY (tertinggi sejak Nov
   2023), headline PCE 3,8% YoY, klaim pengangguran 189K, new home sales 701K
   (BEA/DOL/Census, 13:30 UTC 25 Nov). Panel DUE/FORECAST dihapus.
3. **Hero 2 = Shenzhou-24** (astronaut Pakistan pertama, docking 03:56 UTC),
   **Hero 3 = Solomons** (perjanjian dengan Australia). AU CPI turun ke strip
   angka saja.
4. **13 ilustrasi digambar ulang/diperbesar:** subjek ≥40% lebar frame via zoom
   1.3x (h2us 1.15x); scene baru h2us (bar data + gedung Fed), m14 (Kairo),
   m15 (Sandringham). Render `node render.mjs illos/<k>.svg illos/<k>.png
   --zoom 0,0,480,120` → 960×240.
5. **Afrika terisi:** Kairo (M14, 31 tewas 21 luka, tanker BBM Ring Road,
   25 Nov sore, CNN/The Times). **8 region, 39 cerita** (3 hero + 12 medium +
   24 brief). Tally dihitung programatik + assert (build gagal bila ≠ jumlah
   cerita): EAST ASIA 5, OCEANIA 3, SOUTH ASIA 2, EUROPE 8, AMERICAS 11,
   MIDDLE EAST 6, AFRICA 1, WORLD 3 = 39.
6. **SCHEDULED → hasil aktual:** KTT EU–Balkan (Montenegro 25/33 chapter,
   Serbia absen), Trump–Rutte (joint statement Mar-a-Lago), Gukesh Game 2
   (remis 20 langkah, 1–1); Cartagena B21 → CONFIRMED (1 penculik tewas,
   4 ditahan, ~20 sandera dibebaskan ~06:30 GMT).
7. **Peta ulang:** 30 pin (nomor 1–39; cerita global 20/38/39 tanpa pin),
   pin lebih besar (radius 450/550km), leader-line dijauhi untuk klaster
   Eropa/AS, warna pin biru aksen.
8. **Sumber terpotong diperbaiki:** tinggi band ilustrasi dihitung dari tinggi
   kartu minus blok teks; dateline kartu sempit pendek (nomor + tempat),
   tanggal pindah ke baris sumber. Brief format headline-dulu + cek wrap
   otomatis (defect bila wrap).
9. **Sandringham** jadi medium M15 (dakwaan 25 Nov, pembobolan Anmer Hall
   23 Nov); **Netanyahu** brief 36, **gempa Nepal** brief 37, **emas** brief 39.
10. **B28 & B31 TERVERIFIKASI (bukan dihapus):** Donald 85 off 32 (9 sixes,
    Inggris menang 8 wickets, T20I ke-2 Carrara 24 Nov); €17.12bn (presser
    Parlemen Eropa 25 Nov 11:00 CET, Ressler). 0 klaim ⚠️ VERIFY tersisa.
11. **Strip angka 8 statistik** (GDP 4,3% / core PCE 3,3% / klaim 189K /
    new-home 701K / AU CPI 4,9% / Kairo 31 tewas / docking 03:56 / Montenegro
    25/33). Timeline diperbarui dengan jam aktual.

## Ranking dampak hero (market-news-analyst)
Skor = (Price Impact × Breadth) × (1 + Forward Modifier).
- **(a) Paket data AS: (4 × 2) × 1.25 = 10.0 → Hero 1.** Price Impact
  Moderate (4): tutup pasar bergerak <1% tapi ayunan intraday parah
  (S&P −3,2%, Nasdaq −4,6% intraday). Breadth Cross-Asset (2x: saham +
  obligasi + USD + minyak). Forward Trend Confirmation (+25%: inflasi panas
  + pertumbuhan kuat memperkuat jalur kenaikan suku bunga).
- **(b) Shenzhou-24: 1 × 1 × 1.5 = 1.5 → Hero 2.** Dampak pasar negligible,
  forward +50% (astronaut asing pertama di Tiangong = pergeseran simbolik).
- **(d) Solomons: 1 × 1 × 1.5 = 1.5 → Hero 3** (tie-break vs Shenzhou:
  konsekuensi editorial — perjanjian mengubah peta keamanan Pasifik).
- (e) Trump–Rutte 1.25, (f) EU–Balkan 1.25, (c) Kairo 1.0 — Kairo dampak
  manusia tertinggi, dampak pasar terendah; ia memimpin kartu medium.
- **Reaksi pasar aktual 25 Nov (tutup, bukan intraday):** Dow +0,33%
  (50.182,95), S&P 500 −0,25% (7.182,78), Nasdaq −0,62% (23.585,80),
  Russell 2000 +0,71%; yield 10Y turun ke ~4,85% (−6bp); VIX ~28; Brent
  +3,51%; peluang kenaikan Fed 9 Des ~97% (CME FedWatch 97,2%). Reaksi
  didominasi aksi jual saham AI/teknologi (Nvidia −3,91%), BUKAN semata
  akibat data — korelasi ≠ kausalitas (prinsip skill).
- Jujur dicatat: framework ini mengukur dampak PASAR, bukan konsekuensi
  manusia. Kairo memimpin medium, bukan hero, karena itulah yang diukur
  framework — bukan karena nyawa 31 orang kurang penting.

## Tiga arah + pilihan (huashu-design) — lihat direction-v2.md
A editorial asimetris (DIPILIH) · B hero raksasa + strip data · C peta-led +
band hero sinematik. Critique lengkap + alasan di `direction-v2.md`.
Satu aksen biru broadsheet #1E40AF; tanpa dekorasi template (tanpa label
all-caps di atas judul, tanpa 01/02/03, tanpa ekor panah, tanpa gradien).
Polish loop 2 ronde — lihat `polish-log.md`.

## QA
- Render: 1024×1024, **298.031 byte (291 KiB)**, ≤1 MiB PASS; final y=1012,
  overflow PASS; **DEFECTS: 0**.
- Piksel hitam zona hero: **0** (H1 0, H2 0, H3 0).
- Determinisme: rebuild → byte-identik (cmp PASS).
- QA crop: `tmp-qa-a-512.png`, `tmp-qa-a-top.png`, `tmp-qa-a-bottom.png`
  (workdir, tidak di-commit). Dibaca di 1024 + 512: 0 teks terpotong;
  masthead/hero/strip angka/headline medium terbaca di 512; brief dan pin
  peta butuh ukuran penuh.
- Keterbatasan yang diakui jujur: pin peta Eropa masih padat di 470px
  (terbaca di 1024, blob di 512); body medium sengaja ringkas (kartu 156px);
  aturan "teks isi ≥36px" huashu tidak kompatibel dengan broadsheet 39
  cerita di 1024px — keterbacaan dimaksimalkan (brief 8.5→10/9px, body
  medium 9→10px, body hero 10→11px) dan diverifikasi di 512px.

## Local check (kit fresh, 26 Nov ~16:58 WIB)
- Kit fresh diunduh aman: `curl -o news25-kit-v2.tar.gz
  https://make.fun/c/news-image-20261125/kit?phase=dev` lalu `tar xzf`
  (tanpa pipe ke shell, tanpa git clone). Kit baru: CLI 44,5 MB, scorer
  `b4ff9a3e…`, bundle sha sama `946c3b76…` (bundle kompetisi tidak berubah).
- Perintah: `node <kit-fresh>/cli/makefun.mjs check --kit <kit-fresh>
  --repo . --worktree --json` (tanpa bundle transkrip).
- Hasil: **4 PASS** (competition_open, snapshot, license_osi, entrypoint),
  **1 FAIL** (`transcripts_present` — wajar: tanpa bundle; urusan finisher),
  **14 SKIP** (semua gate transkrip, tanpa sesi untuk dibaca),
  **5 SUBMISSION** (repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot — ini dicek situs saat submit, tidak
  bisa diverifikasi lokal; repo yang sama sudah menerima submit v1 dan
  mencetak skor, dan commit pertama 25 Nov 02:19 UTC — setelah kompetisi
  buka 00:00 UTC).

## Verdict head-to-head v1 vs v2 (jujur)
v2 **JELAS lebih baik** dari v1: (1) bar hitam di 3 hero hilang total
(cacat paling kasat mata v1); (2) Hero 1 kini peristiwa aktual terbesar hari
itu dengan 6 angka terverifikasi, bukan panel DUE/FORECAST; (3) 39 cerita
(dari 35) dengan Afrika terisi dan tally yang benar (v1: 34 vs klaim 35);
(4) dua klaim ⚠️ VERIFY kini terverifikasi; (5) ilustrasi lebih besar dan
dramatis; (6) peta lebih terbaca. Risiko: struktur dasar sama dengan v1
(sengaja — v1 mencetak 96,02%), jadi kenaikan skor mungkin moderat, bukan
lompatan. Tapi tidak ada regresi yang teridentifikasi: semua cacat v1 yang
terdaftar dianalisis sudah diperbaiki, konten ditambah, bukan diganti
sembarangan. **Rekomendasi: LAYAK RESUBMIT** — keputusan akhir di tangan
finisher (Force_Last: submit baru menggantikan v1).
