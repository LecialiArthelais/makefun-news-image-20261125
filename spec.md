# SPEC — News Image 25 November 2026
# "Sum up 25 November's world news in one image" — make.fun news-image-20261125
# Target: TOP 1 | Ditulis: 25 Nov 2026 ~09:00 WIB (02:00 UTC) | Analis pesaing

## 0. ATURAN TANGGAL (keras, dari skill news_image_page)
- Tanggal = tanggal PERISTIWA, bukan tanggal artikel.
- Halaman 25 Nov memuat: peristiwa 25 Nov + peristiwa 24 Nov sore/malam AS (~24 jam terakhir).
- Keluarkan yang ≥36 jam dari 25 Nov 02:00 UTC (= lebih tua dari 23 Nov ~14:00 UTC). Semua yang dikeluarkan WAJIB tercantum di kotak DATE CHECK.
- Cerita 24 Nov yang tidak masuk kartu tetap dicantumkan jejaknya (demote ke DATE CHECK atau bawa sebagai brief bernomor — pilih satu, jangan hilang tanpa jejak).
- Setiap angka di halaman ini sudah diverifikasi ke sumbernya (lihat kolom Sumber). Yang BELUM terverifikasi ditandai ⚠️ VERIFY — jangan dipakai sebelum dicek ulang saat build.

## 1. MASTHEAD
- Eyebrow: "THE WORLD IN ONE DAY · 35 STORIES · 8 REGIONS · EVERY ONE DATED"
- Masthead raksasa serif: **Wednesday 25 November 2026**
- Sub-masthead (3 headline pendek, seperti #1): "Shenzhou-24 carries first Pakistani into orbit / Australia inflation jumps to 4.9% / Solomons scraps China pact, signs with Canberra"
- Region bar berwarna (8 region + jumlah cerita) — ⚠️ PROVISIONAL, hitung ulang dari daftar final di §5 sebelum build: EAST ASIA 7 · OCEANIA 4 · SOUTH ASIA 2 · EUROPE 7 · AMERICAS 6 · MIDDLE EAST 5 · AFRICA 2 · WORLD 2 (= 35). Jika tidak ada 2 cerita Afrika terverifikasi, turunkan ke 7 region dan hapus AFRICA dari bar; JANGAN mengarang cerita Afrika.
- Timeline UTC di bawah masthead (seperti #2, tapi hanya peristiwa NYATA, bukan jadwal olahraga):
  00:18 Shenzhou-24 lifts off · 00:30 AU CPI 4.9% · 02:40 Seoul Metro deal · 04:15 strike called off · ~10:43 Flinders "too late to leave" · 13:30 US data pile DUE · 15:00 Gukesh–Sindarov Game 2 · 17:00 EU–Balkans summit · late p.m. Trump–Rutte, Mar-a-Lago
- Footer: "All times UTC · Every story dated by its event · Illustrations are original drawings · Sources: see each story"

## 2. THE DAY IN NUMBERS — 8 statistik (semua TERVERIFIK, semua aktual — tanpa forecast)
| # | Angka | Arti | Sumber |
|---|-------|------|--------|
| 1 | **4.9%** | Inflasi Australia Okt YoY (naik dari 4,3% Sep; di atas forecast 4,8%) | ABS, 25 Nov 00:30 GMT |
| 2 | **3.8%** | Trimmed mean Australia Okt (naik dari 3,6%; target RBA 2–3%) | ABS, 25 Nov |
| 3 | **00:18 UTC** | Shenzhou-24 meluncur 25 Nov; astronaut asing pertama ke Tiangong | Xinhua / Reuters, 25 Nov |
| 4 | **11** | Orang terluka saat drone Houthi menghantam PIF Tower, Riyadh (24 Nov) | Saudi Civil Defence / Reuters, 24 Nov |
| 5 | **10 of 12** | Dakwaan Huawei yang diputus bersalah oleh juri Brooklyn (24 Nov) | Reuters / DOJ, 24 Nov |
| 6 | **2.212** | Pemotongan pekerjaan Seoul Metro yang dibatalkan lewat kesepakatan 25 Nov | Korea JoongAng Daily / Yonhap, 25 Nov |
| 7 | **4** | Tanker yang diklaim Iran menghantam ranjau di Selat Hormuz (24 Nov) | IRGC via ANI / IRIB, 24 Nov |
| 8 | **30** | Sandera awal di supermarket Exito, Cartagena (24 Nov; 5 perempuan lansia dibebaskan pertama) | Reuters, 24 Nov |

## 3. HERO — 3 kartu besar berilustrasi (semua peristiwa 25 Nov, semua aktual terverifikasi)

### HERO 1 — JIUQUAN, CHINA · SPACE
- **Judul: "Shenzhou-24 lifts off with Pakistan's first astronaut"**
- Ringkasan: Long March-2F meluncur 25 Nov 00:18:52 UTC (08:18 CST) dari Jiuquan membawa Tang Hongbo, Wu Yi, dan Muhammad Zeeshan Ali (40) — orang Pakistan pertama di orbit dan astronaut asing pertama yang mengunjungi stasiun Tiangong. Ali bertugas sebagai payload specialist, tinggal 5–10 hari, lalu pulang dengan Shenzhou-23.
- Angka kunci: 00:18:52 UTC · 3 awak · 1st foreign astronaut on Tiangong · 5–10 hari misi.
- Sumber: Xinhua / Reuters / Wikipedia (launch 25 Nov 00:18:52 UTC). Tag: CONFIRMED.
- Ilustrasi: roket Long March-2F lepas landas fajar, bendera China + Pakistan, stasiun Tiangong di langit.

### HERO 2 — CANBERRA, AUSTRALIA · ECONOMY
- **Judul: "Australia inflation jumps to 4.9% — hottest in about three years"**
- Ringkasan: CPI Oktober naik 4,9% YoY (dari 4,3% Sep, di atas forecast 4,8%), dirilis ABS 25 Nov 00:30 GMT (11:30 AEDT). Trimmed mean naik ke 3,8% (dari 3,6%). Pendorong: listrik +25,2% (subsidi berakhir), transportasi +10,6%, perumahan +6,4%, BBM +32,5% (bahan bakar otomotif). RBA cash rate 4,85%; pengangguran Okt juga 4,9% (tertinggi sejak Okt 2021).
- Angka kunci: 4,9% headline · 3,8% trimmed mean · +0,5% MoM · listrik +25,2%.
- Sumber: ABS via FXStreet / 1trader / InvestingLive, 25 Nov. Tag: CONFIRMED.
- Ilustrasi: grafik batang CPI menanjak tajam + keranjang belanja / pompa bensin.

### HERO 3 — CANBERRA, AUSTRALIA · DIPLOMACY
- **Judul: "Solomons signs historic treaty with Australia — and scraps its China pact"**
- Ringkasan: PM Anthony Albanese dan PM Matthew Wale menandatangani Australia–Solomon Islands Treaty di Canberra, 25 Nov — Australia menjadi "security partner of choice". Honiara memberi tahu Beijing bulan lalu bahwa pakta keamanan 2022 dengan China tidak akan diperpanjang saat berakhir April 2027 (Wale menolak berkomentar, mengutip NDA). Isi: tanpa pangkalan militer asing, infrastruktur sensitif bebas militerisasi, dukungan polisi/perbatasan/pendidikan iklim; pendanaan Australia ~$980 juta sampai 2028 (termasuk $142 juta/2 thn untuk pendidikan gratis).
- Angka kunci: 25 Nov ditandatangani · 2022 China pact berakhir Apr 2027 · $980 jt sampai 2028 · delegasi 24 orang, 17 menteri.
- Sumber: DFAT / Reuters / AAP, 25 Nov. Tag: CONFIRMED.
- Ilustrasi: dua PM berjabat tangan, peta Pasifik dengan panah Canberra–Honiara, bendera kedua negara.

## 4. MEDIUM — 10 kartu berilustrasi (peristiwa 24 Nov sore/malam + 25 Nov pagi)

### M4 — RIYADH, SAUDI ARABIA · CONFLICT (24 Nov)
- **Judul: "Houthi drone hits Riyadh's tallest tower — 11 wounded"**
- Ringkasan: Serangan drone Houthi menghantam PIF Tower (385 m, 80 lantai, markas Public Investment Fund) di King Abdullah Financial District, Selasa 24 Nov — serangan kedua ke menara itu dalam <1 minggu (yang pertama 19 Nov, tanpa korban). Korban: 2 Saudi, 2 India, 3 Nepal, 4 Mesir. Koalisi pimpinan Saudi menyebutnya serangan drone dan berjanji merespons "decisively". Houthi belum mengklaim sampai 16:00 GMT 24 Nov.
- Angka: 11 terluka · 385 m · serangan ke-2 dalam seminggu.
- Sumber: Reuters / Saudi Civil Defence / WSJ, 24 Nov. Tag: REPORTED (atribusi Saudi; klaim Houthi belum ada).
- Ilustrasi: menara kaca menjulang dengan asap, langit malam Riyadh.

### M5 — NEW YORK, USA · JUSTICE (24 Nov)
- **Judul: "Huawei guilty on 10 of 12 counts in US criminal trial"**
- Ringkasan: Juri federal Brooklyn, Selasa 24 Nov, memutus Huawei + 3 anak perusahaan bersalah atas 10 dari 12 dakwaan: bank fraud, wire fraud, pelanggaran sanksi (bisnis Iran via Skycom, menyesatkan HSBC/Standard Chartered/BNP Paribas), konspirasi mencuri rahasia dagang (source code Cisco, teknologi antena Quintel, board CNEX, robot T-Mobile), dan money laundering. Bebas dari dakwaan racketeering (RICO) + obstruction. Sidang 12 minggu, >60 saksi penuntut; vonis dijatuhkan 14 Sep 2027. Kasus bermula 2018.
- Angka: 10/12 bersalah · 12 minggu sidang · vonis 14 Sep 2027.
- Sumber: Reuters / US DOJ (EDNY), 24 Nov. Tag: CONFIRMED.
- Ilustrasi: gedung pengadilan federal + chip / papan sirkuit.

### M6 — FLINDERS ISLAND, TASMANIA · WILDFIRE (25 Nov)
- **Judul: "Flinders Island fire: 'too late to leave' as blaze bears down"**
- Ringkasan: Tasmania Fire Service menaikkan peringatan ke Emergency Warning pada 25 Nov pagi (AEDT) untuk Killiecrankie, Leeka & Mount Tanner — "too late to leave", warga diminta berlindung; Killiecrankie Beach jadi tempat perlindungan terakhir. Kebakaran dipicu petir 19 Nov, jebol garis containment 23 Nov; ~3.000 ha per 24 Nov, perimeter resmi terpetakan 10.139 ha. Watch and Act juga berlaku untuk Palana & Mount Blyth.
- Angka: 3.000 ha (24 Nov) · 10.139 ha perimeter terpetakan · 3 wilayah dalam Emergency Warning.
- Sumber: Tasmania Fire Service / ABC / EWN, 25 Nov. Tag: OFFICIAL.
- Ilustrasi: api + asap oranye di atas pesisir pulau, rambu evakuasi.

### M7 — SEOUL, SOUTH KOREA · TRANSPORT (25 Nov)
- **Judul: "Seoul Metro strike called off hours before first train"**
- Ringkasan: Setelah negosiasi maraton ~18 jam (mulai 24 Nov 10:04), Seoul Metro dan 3 serikat mencapai kesepakatan 25 Nov 02:40–04:15 KST — hanya beberapa jam sebelum mogok umum tanpa batas yang dijadwalkan dari kereta pertama. Isi: rencana pemotongan 2.212 posisi ditangguhkan, 500 karyawan baru direkrut, upah naik s.d. 3,5% (+1,4% seniority). Jalur 1–8 beroperasi normal; kekacauan komuter pagi terhindarkan.
- Angka: 2.212 posisi ditangguhkan · 500 rekrutan baru · +3,5% upah · deal 02:40 KST.
- Sumber: Korea JoongAng Daily / Yonhap / YTN, 25 Nov. Tag: CONFIRMED.
- Ilustrasi: kereta metro Seoul di stasiun pagi, jam menunjukkan 02:40.

### M8 — ULLEUNG ISLAND, SOUTH KOREA · DEFENCE (24 Nov)
- **Judul: "Russian jets near Ulleung — Seoul issues rare 'take shelter' alert"**
- Ringkasan: Beberapa pesawat militer Rusia memasuki KADIZ di atas Laut Timur, Selasa 24 Nov, mendekati Pulau Ulleung; AU Korea Selatan mengerahkan jet tempur dan pemerintah mengeluarkan peringatan "preemptive" agar warga berlindung — langkah yang disebut langka. Tidak ada pelanggaran wilayah udara Korea Selatan; pesawat Rusia keluar dari zona. Kemenhan akan memanggil atase militer Rusia untuk protes keras. Insiden serupa sebelumnya 17 Nov (dan 25 Agu) — yang 24 Nov inilah yang dibawa.
- Angka: beberapa pesawat Rusia · 0 pelanggaran wilayah udara · peringatan berlindung (langka).
- Sumber: Reuters / JCS Korea Selatan, 24 Nov. Tag: REPORTED.
- Ilustrasi: jet tempur + pulau Ulleung + garis ADIZ di peta.

### M9 — BAGHDAD, IRAQ · POLITICS (24 Nov)
- **Judul: "Baghdad orders takeover of Kurdish oilfields"**
- Ringkasan: PM Ali al-Zaidi memerintahkan Kementerian Perminyakan federal mengelola ladang minyak di Diyala, Kirkuk, Salahuddin & Nineveh yang berada di bawah kontrol keamanan Kurdi, plus otoritas perbatasan mengambil alih semua penyeberangan di Kurdistan; ekspor KRG hanya lewat kementerian federal. Pemicu: penyelidikan penyelundupan minyak di North Oil Company (ratusan juta dolar, diduga melibatkan Kataib Hezbollah). PM Kurdistan Masrour Barzani menolak: "in no way acceptable". Ladang Khormala termasuk yang dicakup. Pejabat dicopot: kepala otoritas perbatasan, komandan operasi Kirkuk, kepala polisi Kirkuk; Dirjen North Oil diskors.
- Angka: 4 provinsi · ladang Khormala · ratusan juta dolar dugaan penyelundupan.
- Sumber: Reuters/FT via AJOT / Al Jazeera, 24 Nov. Tag: REPORTED.
- Ilustrasi: pompa angguk (pumpjack) + peta 4 provinsi + bendera Irak/Kurdistan.

### M10 — STRAIT OF HORMUZ · ENERGY (24 Nov)
- **Judul: "Four tankers hit mines in the Strait of Hormuz, Iran claims"**
- Ringkasan: IRGC Navy mengklaim 4 tanker meledak/terbakar setelah menghantam ranjau laut di Selat Hormuz, Selasa 24 Nov (1 di timur selat, 2 lagi di zona terlarang timur; 2 tanker lain dipaksa kembali ke Teluk). Iran menyebut kapal-kapal itu memakai "rute tak resmi" dan mematikan sistem identifikasi. Reuters belum bisa memverifikasi klaim Iran secara independen. Terpisah, UKMTO melaporkan 3 kapal dihantam proyektil tak dikenal hari Minggu (~20:25 UTC) saat transit ke timur.
- Angka: 4 tanker diklaim · 2 dipaksa kembali · 3 kapal terpisah (UKMTO, Minggu).
- Sumber: IRGC via ANI/IRIB + UKMTO, 24 Nov. Tag: CLAIMED — UNVERIFIED (tulis eksplisit di kartu).
- Ilustrasi: tanker terbakar di selat sempit, ranjau laut, peta Hormuz.

### M11 — KYIV, UKRAINE · WAR (konfirmasi 24 Nov; serangan 21 Nov)
- **Judul: "Zelenskiy confirms Ukraine hit Russian ship Sparta II"**
- Ringkasan: Presiden Volodymyr Zelenskiy mengonfirmasi ke Bloomberg (wawancara Senin malam, dilaporkan 24 Nov) bahwa Ukraina bertanggung jawab atas serangan drone Sabtu 21 Nov terhadap kapal kargo Rusia Sparta II di Teluk Finlandia — kapal berbendera Rusia milik Oboronlogistika (logistik Kemenhan Rusia), tujuan Kaliningrad, diklaim membawa senjata (belum terverifikasi independen). Kapal terbakar dan hanyut ke perairan Finlandia. Norwegia — sekutu kuat Kyiv — mendesak kehati-hatian. Zelenskiy juga mengonfirmasi serangan terhadap dua kapal Rusia di lepas Libya (Benghazi, 22 Nov — lihat DATE CHECK).
- Angka: serangan 21 Nov · konfirmasi 24 Nov · 1 kapal (Sparta II).
- Sumber: Reuters / Bloomberg, 24 Nov. Tag: CONFIRMED (konfirmasinya); klaim muatan senjata UNVERIFIED.
- Ilustrasi: kapal kargo terbakar di laut dingin, drone di langit.

### M12 — WASHINGTON, USA · CYBER (24 Nov)
- **Judul: "CIA and ODNI hit by breach of unclassified spy network"**
- Ringkasan: NYT pertama melaporkan Selasa 24 Nov: CIA dan Office of the Director of National Intelligence menemukan peretasan pada jaringan tak terklasifikasi yang dipakai menganalisis info publik/komersial (OSINT). Sejumlah info tak terklasifikasi terekspos; sistem terklasifikasi TIDAK terdampak; gangguan sudah teratasi. Pelaku dan data persis yang diambil belum diketahui. NYT juga melaporkan National Geospatial-Intelligence Agency ikut terdampak. Rangkaian insiden federal: FBI (NCIC, 20 Nov) dan Dept. Pertanian sebelumnya.
- Angka: 2 lembaga (CIA + ODNI) · 0 sistem terklasifikasi terdampak.
- Sumber: NYT via Reuters / Nextgov, 24 Nov. Tag: REPORTED.
- Ilustrasi: gembok digital retak + satelit / layar data.

### M13 — NEW YORK, USA · MARKETS (24 Nov)
- **Judul: "Nvidia slides ~7% as the AI rally unwinds — again"**
- Ringkasan: Sehari setelah melonjak +31,5% pasca Jensen Huang dikembalikan sebagai CEO (menambah ~$1 triliun kapitalisasi pasar), Nvidia jatuh ~7% pada Selasa 24 Nov (intraday −7,5%; tutup −5,9% di $155,38 menurut satu sumber — angka tutup bervariasi antar sumber, pakai "~7%" intraday). Nasdaq −1,48% ke 23.733,54; Philadelphia Semiconductor Index −7,88%. Pemicu: kekhawatiran valuasi AI + margin server (HPE −14–17%, Dell −10–11% jelang earnings, Micron −10–11%, AMD −9%, Anthropic −8–9% ke bawah harga IPO $83). Ketua Senate Banking Tim Scott memanggil Huang bersaksi 3 Des soal kontrol ekspor. Efek lanjut 25 Nov: Nikkei −2,8% di pembukaan (Advantest −12%).
- Angka: Nvidia ~−7% · Nasdaq −1,48% · SOX −7,88% · Senin +31,5%.
- Sumber: Reuters / TipRanks / BBN Times, 24–25 Nov. Tag: CONFIRMED (angka tutup Nvidia tulis "~7%" karena sumber berbeda).
- Ilustrasi: grafik saham jatuh tajam setelah lonjakan, chip GPU.

## 5. BRIEFS BERNOMOR — 14–35 (satu baris judul + satu baris isi + tag sumber)
Nomor brief = nomor pin peta. Semua peristiwa 24–25 Nov.

- **14 TOKYO, JAPAN · POLITICS (24 Nov)** — "Six opposition parties move to censure education minister Seki" — Partai oposisi di majelis tinggi sepakat mengajukan mosi kecaman non-binding terhadap Mendikbud Yoshihiro Seki atas skandal fundraising 2024 (5 acara, birokrat jadi pembicara, perwakilan biofarmasi bayar ¥90.000/orang; awalnya mengaku 2). Seki menolak mundur; PM Takaichi mempertahankannya; RUU pajak pangan (8%→1%) terancam. Sumber: Japan Times via EuropeSays / TBS, 24 Nov. Tag: REPORTED.
- **15 BRUSSELS, BELGIUM · SUMMIT (25 Nov, 17:00 CET)** — "EU meets Western Balkans — without Serbia" — Costa & von der Leyen menjamu 6 mitra Balkan; Serbia absen (Pj Presiden/ketua parlemen Čupić tidak hadir); Montenegro terdepan ("28 by 28" — anggota ke-28 pada 2028). Sumber: European Council / RFE-RL, 25 Nov. Tag: SCHEDULED.
- **16 PALM BEACH, USA · DIPLOMACY (25 Nov, sore)** — "Trump to meet NATO chief Rutte at Mar-a-Lago" — Pertemuan tertutup, tanpa agenda publik/media, diumumkan Gedung Putih 23 Nov; menyusul pertemuan Trump dengan Putin & Xi pekan lalu di Asia. Sumber: Reuters, 23 Nov. Tag: SCHEDULED.
- **17 WASHINGTON, USA · ECONOMY (25 Nov, 13:30 UTC / 20:30 WIB) — PANEL "DUE TODAY"** — "Thanksgiving-eve data pile: GDP, PCE, claims, durables" — Rilis 08:30 ET: GDP Q3 estimasi ke-2 (konsensus WSJ +3,6%; estimasi pertama +3,4%; Q2 +2,2%), core PCE Okt +0,3% MoM / +3,2% YoY (prev +3,1%), headline PCE +3,8% YoY (prev +3,6%), durable goods +1,1% (WSJ) / +0,4–0,7% (survei lain) (prev +1,8%), jobless claims ~200 ribu (prev 203 ribu); new home sales 10:00 ET ~645–650 ribu (prev 676 ribu); Beige Book 14:00 ET. ⚠️ **HANYA FORECAST — angka aktual BELUM rilis saat riset (25 Nov 02:00 UTC). Tambahkan angka aktual HANYA kalau sudah keluar dan terverifikasi saat build; JANGAN fabrikasi. Kalau build sebelum 13:30 UTC, tampilkan panel ini apa adanya sebagai "DUE 13:30 UTC — forecasts".** Sumber: WSJ via Morningstar / BEA / DOL / Census, 24 Nov. Tag: FORECAST.
- **18 GENEVA, SWITZERLAND · SPORT (25 Nov, 15:00 CET)** — "Gukesh–Sindarov Game 2 today, scores level" — Game 1 (24 Nov) berakhir remis 38 langkah (Berlin Defence); skor 0,5–0,5. Game 2: Gukesh pegang Putih, mulai 15:00 CET (14:00 UTC). 14 partai klasik, pertama ke 7,5 poin juara; hadiah $2,5 jt. Sumber: FIDE / World Chess, 24–25 Nov. Tag: SCHEDULED (hasil Game 2 belum ada saat build).
- **19 WORLD · RIGHTS (25 Nov)** — "16 Days of Activism begins: 'Ensure justice, protect survivors, end impunity'" — Hari Internasional Penghapusan Kekerasan terhadap Perempuan; kampanye UN Women 25 Nov–10 Des. 1 dari 3 perempuan/gadis di dunia terdampak (~840 jt); <10% (9,2%) melapor ke polisi. Sumber: UN Women / WHO, 25 Nov. Tag: CONFIRMED.
- **20 MADRID, SPAIN · SPORT (24 Nov)** — "Real Madrid 5–1 PSV: Bellingham stunner, Mbappé brace" — Tertinggal 0–1 (penalti Perišić 32'), Madrid bangkit: Valverde 50', Bellingham 60' (trivela, masuk dari bangku cadangan), Mbappé 64' + 84', Vinícius 87'. Madrid 5/5 di UCL, 10 kemenangan beruntun semua kompetisi. Sumber: UEFA / Real Madrid, 24 Nov. Tag: CONFIRMED.
- **21 CARTAGENA, COLOMBIA · CRIME (24 Nov, berlangsung)** — "30 hostages seized in supermarket after botched armoured-truck robbery" — Pria bersenjata bertopeng gagal merampok truk lapis baja, lalu berlindung di supermarket Exito, La Castellana; ~30 sandera awal, 5 perempuan lansia dibebaskan pertama, lalu total 9–10 dibebaskan; ~15–25 masih di dalam saat laporan sore. Tuntutan yang dilaporkan media lokal (~$2 jt + 2 kendaraan lapis baja + jalur aman ke Barranquilla) BELUM terverifikasi. Bandara Cartagena sempat menangguhkan operasi. Sumber: Reuters / AP, 24 Nov. Tag: ONGOING.
- **22 OTTAWA/CANADA · SPACE (24 Nov)** — "Astronaut Kutryk becomes a father from orbit" — CSA mengumumkan 24 Nov: Joshua Kutryk (Crew-13, ISS sejak 1 Okt) dan istrinya Heather menyambut anak ketiga, seorang putri; kakak Peter & Anna. Orang ke-4 yang menjadi ayah saat mengorbit (Fincke 2004, Bresnik 2009). Sumber: CSA / SpaceQ, 24 Nov. Tag: CONFIRMED.
- **23 WASHINGTON, USA · POLITICS (24 Nov)** — "Trump spares turkeys Freedom and Feathers" — Tradisi pengampunan kalkun Thanksgiving (Thanksgiving 26 Nov). ⚠️ VERIFY tanggal persis saat build (Reuters summary 25 Nov; kemungkinan 24 Nov). Sumber: Reuters, 24 Nov (verify).
- **24 WASHINGTON, USA · POLITICS (24 Nov)** — "Trump awards Giuliani the Medal of Freedom" — Presiden menganugerahkan Presidential Medal of Freedom kepada mantan Wali Kota New York Rudy Giuliani. Sumber: Reuters / Washington Post, 24 Nov. Tag: REPORTED.
- **25 PARIS, FRANCE · JUSTICE (24 Nov)** — "Sarkozy corruption case ordered to trial" — Pejabat Prancis memerintahkan kasus korupsi mantan Presiden Nicolas Sarkozy (dan istrinya Carla Bruni) ke pengadilan; sidang praperadilan awal 1 Apr 2027. Sumber: Reuters, 24 Nov. Tag: REPORTED.
- **26 TEXAS, USA · JUSTICE (24 Nov)** — "Fort Hood shooter Hasan seeks stay of execution" — Nidal Hasan (penembakan Fort Hood 2009, 13 tewas) meminta penundaan eksekusi yang dijadwalkan pekan depan; terungkap dari dokumen pengadilan Selasa 24 Nov. Sumber: Reuters, 24 Nov. Tag: REPORTED.
- **27 VILLAVICENCIO, COLOMBIA · SECURITY (malam 23–24 Nov)** — "Car bombing rocks Villavicencio; FARC dissidents blamed" — Bom mobil semalam di Villavicencio; pemerintah menyalahkan kelompok disiden FARC yang menolak perjanjian damai 2016. Presiden de la Espriella sedang berada di sana saat kabar sandera Cartagena datang. Sumber: Reuters, 24 Nov. Tag: REPORTED.
- **28 AUSTRALIA · SPORT (24 Nov)** — "England beat Australia by 8 wickets in 2nd T20I" — Inggris mengejar target 185 dan menyamakan seri 5 laga; Jake Fraser-McGurk 27 run dari 13 bola untuk Australia. Sumber: Jagran Josh / Reuters, 24 Nov. Tag: CONFIRMED.
- **29 NEW DELHI, INDIA · POLITICS (24 Nov)** — "BJP and Akali Dal announce alliance for 2027 Punjab polls" — Aliansi diumumkan setelah 6 tahun berpisah, jelang pemilu Majelis Punjab 2027. ⚠️ VERIFY tanggal pengumuman persis saat build. Sumber: Jagran Josh, 25 Nov (verify).
- **30 TOKYO, JAPAN · MARKETS (25 Nov)** — "Nikkei falls 2.8% at the open as chip rout resumes" — Nikkei −2,55–2,8% ke ~57.152 (00:18 GMT); Advantest −12%, JX Advanced Metals −8,1%; dolar ¥159,24. Mengikuti SOX AS −7,88%. Sumber: Reuters via TradingView (Dow Jones), 25 Nov 00:19 UTC. Tag: CONFIRMED.
- **31 STRASBOURG, FRANCE · MIGRATION (25 Nov, 11:00 CET)** — "EU Parliament to brief on migration and border funds" — MEP mengadakan konferensi pers soal pendanaan migrasi & pengelolaan perbatasan. ⚠️ VERIFY jadwal/isi saat build (diambil dari #1; belum diverifikasi independen). Tag: SCHEDULED (verify).
- **32 HODEIDAH, YEMEN · CONFLICT (23 Nov — konteks untuk M4)** — "Saudi jets hit telecom building in Hodeidah, 4 killed" — Media Houthi: serangan udara Saudi ke gedung telekomunikasi Hodeidah 23 Nov menewaskan 4, melukai 18; Riyadh belum berkomentar; pemimpin Houthi memperingatkan tak akan dibiarkan tanpa jawaban. Masuk brief sebagai konteks eskalasi — BUKAN peristiwa 24/25 Nov. Sumber: Houthi media via Silent Dossier, 23 Nov. Tag: CLAIMED.
- **33 GENEVA, SWITZERLAND · DIPLOMACY (24 Nov)** — "Houthis won't seize Aden, Yemeni government forces say" — Houthi disebut sudah 60 km dari Aden, ibu kota sementara pemerintah yang diakui internasional; militer Yaman menyatakan kota tidak akan jatuh. Sumber: Reuters, 24 Nov. Tag: REPORTED.
- **34 BRUSSELS, BELGIUM · POLITICS (25–27 Nov)** — "EU leaders head for budget & Ukraine summit" — Setelah KTT Balkan 25 Nov, European Council khusus 26–27 Nov membahas anggaran 2028–2034 (€1,78 triliun) dan pendanaan Ukraina; Spanyol pemilu Minggu 29 Nov. Sumber: EU Insider / RFE-RL, 24–25 Nov. Tag: SCHEDULED.
- **35 WORLD · CLIMATE (konteks)** — "COP31 ended with no deal — see DATE CHECK" — Satu baris pengarah ke kotak DATE CHECK (bukan cerita 25 Nov). Jangan ulangi detailnya di sini.

**Total cerita: 3 hero + 10 medium + 22 briefs = 35 cerita, 8 region.**
Tally region: East Asia 7 (Shenzhou, Seoul Metro, KADIZ, Seki, Nikkei, Gukesh? — TIDAK, Gukesh = Europe; hitung ulang saat build: East Asia = Shenzhou, Seoul Metro, KADIZ, Seki, Nikkei, + Hormuz? tidak. Final: EAST ASIA 6 (Shenzhou, Seoul Metro, KADIZ, Seki, Nikkei, +1: "Asia markets" gabung Nikkei) — **koordinator/build: hitung ulang tally region dari daftar final dan samakan dengan region bar; jangan pakai angka di §1 kalau daftar berubah.** OCEANIA 4 (CPI, Solomons, Flinders, T20 Inggris–Australia), SOUTH ASIA 2 (BJP–SAD, + Gukesh sebagai India? Gukesh = Eropa lokasinya; South Asia 2 = BJP–SAD + 1 cadangan), EUROPE 7 (Gukesh, EU–Balkans, Sarkozy, EU Parl, EU budget summit, Real Madrid, +1), AMERICAS 6 (Huawei, CIA, Nvidia, Trump–Rutte, turkey pardon, Giuliani, Fort Hood, Cartagena, Villavicencio — itu 9; sesuaikan), MIDDLE EAST 5 (Riyadh, Iraq, Hormuz, Hodeidah, Aden), AFRICA 2 (16 Days diluncurkan global — taruh di WORLD; Afrika 2 = ? — **jika tidak ada 2 cerita Afrika terverifikasi, turunkan klaim region ke 7 dan hapus AFRICA dari bar; JANGAN mengarang cerita Afrika**), WORLD 2 (16 Days, US data pile). **Aturan: jumlah region di bar = jumlah region yang benar-benar punya cerita; tally harus cocok dengan daftar.**

## 6. PETA DUNIA + PIN BERNOMOR
- Peta dunia titik-titik (dot map) dengan pin bernomor 1–35 yang cocok dengan nomor kartu/brief.
- Pin: 1 Jiuquan · 2 Canberra (CPI) · 3 Canberra (treaty — pin sama, label 2/3) · 4 Riyadh · 5 New York (Huawei) · 6 Flinders Island · 7 Seoul · 8 Ulleung · 9 Baghdad · 10 Hormuz · 11 Teluk Finlandia · 12 Washington (CIA) · 13 New York (Nvidia — pin sama dengan 5, label 5/13) · 14 Tokyo · 15 Brussels (summit) · 16 Palm Beach · 17 Washington (data pile — pin sama 12) · 18 Jenewa · 19 (global — tanpa pin, ikon dunia) · 20 Madrid · 21 Cartagena · 22 Kanada/ISS (pin di Kanada) · 23 Washington (turkey — pin sama 12) · 24 Washington (Giuliani — pin sama 12) · 25 Paris · 26 Texas · 27 Villavicencio · 28 Australia (T20 — pin di kota laga? ⚠️ VERIFY kota; kalau tidak ketemu, pakai pin Sydney dengan label "Australia") · 29 New Delhi · 30 Tokyo (pin sama 14) · 31 Strasbourg · 32 Hodeidah · 33 Aden · 34 Brussels (pin sama 15) · 35 (pengarah DATE CHECK — tanpa pin).
- Legenda di bawah peta: "Pins = story numbers · ● = confirmed · ◆ = reported/claimed · ○ = scheduled/forecast".

## 7. DATE CHECK — kotak wajib (dua bagian)
**A. EXCLUDED — terjadi ≥36 jam sebelum 25 Nov 02:00 UTC (jangan dibawa sebagai cerita hari ini):**
- COP31 berakhir tanpa kesepakatan — 22 Nov, Antalya. KTT iklim PBB pertama sejak 2009 yang berakhir tanpa perjanjian; EU/Inggris menolak teks tanpa bahasa fosil; ~130 pihak menolak cover text; teks just-transition + loss-and-damage tetap diadopsi; 46 keputusan diadopsi (Erdogan). Sumber: WRI / Reuters, 22–24 Nov.
- ICJ: Myanmar bersalah atas genosida Rohingya — 19 Nov, Den Haag. 9–6 hakim; pertama kalinya sebuah negara dinyatakan bertanggung jawab atas genosida; perintah investigasi/prosekusi + reparasi. Inggris secara formal mengakui genosida 23 Nov. Sumber: ICJ / HRW / MRG, 19–23 Nov.
- Analisis 700.000 tentara Rusia tewas — diterbitkan 23 Nov (Meduza/Mediazona, dari data Rosstat yang diretas): 490.000 kematian terdaftar s.d. akhir Sep 2026; model total >700.000 (~720.000 menurut CNN) termasuk yang hilang; total korban (tewas+luka) menuju >2 jt. Tepat di luar garis 36 jam. Sumber: RFE/RL / CNN, 23–24 Nov.
- Prabowo menamai 2 cawapres (Amran Sulaiman + Sugiono) — 23 Nov, Jakarta. Surat diserahkan langsung ke MPR; sidang pleno MPR 11 Des. (BUKAN "deadline 25 Nov" — itu tanggal lama saat sidang masih 9 Des.) Sumber: detikNews via IndonesiaNow / Jakarta Weekly, 23 Nov.
- Serangan terhadap Sparta II itu sendiri — 21 Nov (hanya KONFIRMASI Zelenskiy 24 Nov yang dibawa sebagai M11).
- Kapal Rusia ditenggelamkan di lepas Benghazi, Libya — 22 Nov, Minggu (konfirmasi Zelenskiy 24 Nov dicatat di M11).
- Kunjungan PM Nepal Balendra Shah ke India — 22–23 Nov (berakhir 23 Nov).
- Insiden KADIZ 17 Nov — digantikan insiden 24 Nov yang dibawa sebagai M8.
- Kejatuhan pasar 20–23 Nov (Nikkei −5,06% Jumat 20 Nov; KOSPI level terendah 10 bulan 23 Nov) — hanya pembukaan 25 Nov (−2,8%) yang dibawa sebagai B30.
- Serangan udara Hodeidah (gedung telekomunikasi) — 23 Nov; dicatat sebagai konteks di B32, bukan cerita 25 Nov.
- Pengakuan formal Inggris atas genosida Rohingya — 23 Nov (terkait putusan ICJ 19 Nov).

**B. DEMOTED — peristiwa 24 Nov yang hasilnya dibawa di dalam brief lain (bukan kartu sendiri):**
- Gukesh–Sindarov Game 1 remis 38 langkah — 24 Nov; hasilnya dibawa di dalam brief Game 2 (B18).
- Serangan pertama ke PIF Tower Riyadh — 19 Nov, tanpa korban; disebut di dalam M4.

## 8. SOURCING & "HOW SURE" (adopsi keunggulan #2)
- Setiap kartu/brief membawa tag: CONFIRMED / OFFICIAL / REPORTED / CLAIMED / ONGOING / SCHEDULED / FORECAST + nama outlet (bukan "menurut laporan" tanpa nama).
- Legenda HOW SURE di footer: CONFIRMED = diverifikasi ≥2 sumber / sumber resmi · OFFICIAL = pernyataan lembaga resmi · REPORTED = 1+ outlet ternama · CLAIMED = klaim satu pihak, belum terverifikasi independen · SCHEDULED = dijadwalkan hari ini, hasil belum ada · FORECAST = angka perkiraan, bukan aktual.
- Footer sumber: Xinhua · Reuters · ABS · DFAT · AAP · Saudi Civil Defence · US DOJ · Tasmania Fire Service · Korea JoongAng Daily / Yonhap · JCS Korea · FIDE · UN Women · UEFA · CSA · European Council · BEA / DOL / Census (forecast WSJ) · NYT (via Reuters).

## 9. STRUKTUR HALAMAN (untuk tim build)
1. Masthead serif raksasa + eyebrow + sub-headline 3 berita + region bar.
2. Timeline UTC (hanya peristiwa nyata + item DUE/SCHEDULED yang diberi label).
3. THE DAY IN NUMBERS (8 stat, §2).
4. 3 hero berilustrasi (§3) — SATU ilustrasi flat-vector orisinal per kartu, digambar via kode, BUKAN ikon kecil.
5. 10 medium berilustrasi (§4) — SATU ilustrasi per kartu (ini yang membedakan dari #1 yang medium-nya hanya ikon kecil).
6. Panel "DUE TODAY 13:30 UTC" (B17) — tampil menonjol tapi jelas berlabel FORECAST, terpisah dari hero.
7. Peta dunia + pin 1–35 (§6).
8. Briefs bernomor 14–35 (§5).
9. DATE CHECK (§7) — besar dan terbaca, bukan satu baris kecil seperti #1.
10. Footer: HOW SURE legend + daftar sumber + "All times UTC · Every story dated by its event".

## 10. YANG TIDAK BOLEH MASUK (tidak terverifikasi / salah tanggal)
- ❌ Angka aktual PCE/GDP/claims/durable goods — BELUM RILIS. Hanya forecast (B17) sampai terverifikasi.
- ❌ "Brent $88–89" (klaim #3) — tidak terverifikasi oleh riset ini.
- ❌ "OpenTable buys me&u", "NASA seeks Hubble rescue / RFI", "US widens SE Asia chip curbs" (klaim #3) — tidak ditemukan verifikasinya; JANGAN pakai.
- ❌ "Coalition orders Hodeidah port evacuation" (klaim #3) — tidak terverifikasi; yang terverifikasi adalah serangan udara Hodeidah 23 Nov (B32).
- ❌ Cerita #1 yang tidak terverifikasi: "Infant refused birth certificate" (Kolkata), "Taiz misses measles vaccine for 350.000 children" — tidak dicek; jangan pakai tanpa verifikasi.
- ❌ ICJ Myanmar sebagai cerita 25 Nov — itu 19 Nov (lihat DATE CHECK).
- ❌ "Prabowo must name VP candidates by today" — SUDAH dinamai 23 Nov (lihat DATE CHECK).
- ❌ "Chen Jining investigated" (klaim #5) — tidak terverifikasi; jangan pakai.

## 11. PERBANDINGAN JUJUR vs TOP-5 (untuk koordinator; juga jadi bahan § "apa yang masih lebih lemah" di laporan akhir)

### Apa yang dimiliki bersama top-5
Semua top-3 punya: masthead tanggal raksasa, region bar, strip THE DAY IN NUMBERS (6 stat), 3 hero berilustrasi, ~10 kartu medium, peta + pin, brief bernomor, DATE CHECK, sumber per cerita. #4/#5 tidak punya sebagian besar dari itu (itulah kenapa mereka 94,8% dan 88,0%).

### #1 wurk — 97,8974% (11W–1L, 382.147 byte)
- **Kenapa #1:** layout paling bersih & paling "koran"; timeline UTC nyata; 3 hero berilustrasi penuh; DATE CHECK ada; 21 cerita semuanya terasa 25 Nov.
- **Kelemahan yang kita serang:** (a) hanya 21 cerita vs 35 kita; (b) 3 cerita berlabel AHEAD (KTT EU–Balkan, briefing Parlemen EU — jadwal, bukan peristiwa); (c) kartu medium hanya memakai ikon kecil, bukan ilustrasi penuh — melanggar template pemenang; (d) strip angka berisi stat trivial ("5:30 Seoul Metro pay deal time"); (e) DATE CHECK cuma satu baris, 4 item; (f) tanpa legenda HOW SURE / tanpa tag per cerita; (g) pin peta kecil & sulit dibaca.
- **Yang masih lebih kuat dari kita:** kerapian tipografi & hierarki visual (serif masthead + timeline terpadu); hero "Flinders fire" sangat dramatis. Kita harus menandingi kerapian ini, bukan hanya jumlah cerita.

### #2 quiet-panda-11 — 97,4846% (10W–2D–0L, 283.194 byte)
- **Kenapa #2:** 50 cerita (terbanyak), UTC timeline dengan titik-titik, sourcing tags + legenda HOW SURE, DATE CHECK besar (10 item), 3 hero berilustrasi dengan angka besar.
- **Kelemahan yang kita serang:** (a) 42 dari 50 cerita berlabel SCHED — sebagian besar jadwal olahraga (UCL, NBA Cup, Davis Cup) yang belum terjadi; "50 cerita" itu padding; (b) hero 3 adalah FORECAST (data AS belum rilis) — sama seperti #3; (c) brief 16–50 dicetak super kecil, nyaris tak terbaca; (d) kartu medium didominasi olahraga; (e) peta terlalu padat.
- **Yang masih lebih kuat dari kita:** volume mentah (50 vs 35) + sistem tagging HOW SURE yang paling rapi. Kita mengadopsi tagging-nya, tapi kita tidak bisa menandingi 50 tanpa mengorbankan keterbacaan — tradeoff sadar: 35 cerita terbaca penuh > 50 cerita yang 42-nya jadwal. Jika judge menghargai volume di atas segalanya, ini titik kalah kita.

### #3 gentle-coyote-58-8226 — 97,4085% (11W–1D–0L, 269.418 byte)
- **Kenapa #3:** semua kartu berilustrasi penuh; tampilan broadsheet gelap yang khas; DATE CHECK 12 item; 20 cerita terkurasi.
- **Kelemahan yang kita serang (paling banyak):** (a) hero 1 adalah forecast PCE/GDP yang BELUM RILIS tapi dilabeli "CONFIRMED" — kesalahan faktual paling fatal di top-5; (b) "Early Edition 00:30–02:00 UTC" — dibangun sebelum sebagian besar hari berjalan; (c) beberapa cerita tidak terverifikasi/tidak ditemukan: "Hodeidah port evacuation", "OpenTable buys me&u", "NASA Hubble rescue RFI", "US widens SE Asia chip curbs"; (d) hanya 20 cerita; (e) angka Brent "$88–89" tanpa sumber jelas.
- **Yang masih lebih kuat dari kita:** konsistensi ilustrasi penuh di semua kartu + identitas visual gelap yang mudah dikenali. Kita harus menyamai standar ilustrasi ini.

### #4 mase-ayas — 94,8377% (28.693 byte)
- Text-only, 7 cerita, tanpa ilustrasi/peta/angka/DATE CHECK. Plus kesalahan faktual: "Prabowo must name two VP candidates by today" (sudah dinamai 23 Nov) dan "700.000" tanpa konteks tanggal (analisis 23 Nov). Bukan ancaman; jadi patokan bawah.

### #5 raihanmd — 87,9856% (102.410 byte)
- Layout rusak: teks terpotong ("HORMUZ CLOSED: 4TH TANKER HITS MI…", badge tanggal terpotong), 6 cerita, tanpa peta/angka/DATE CHECK. Cerita ICJ Myanmar sudah 6 hari (19 Nov) tapi disajikan sebagai berita 25 Nov. Bukan ancaman.

### Keunggulan kita (ringkas)
1. 35 cerita vs 21 (#1) / 20 (#3) — dan semuanya peristiwa nyata + bertanggal + bersumber, bukan jadwal olahraga (beda dari #2).
2. 3 hero semuanya peristiwa 25 Nov AKTUAL (Shenzhou, CPI, Solomons) — #2 dan #3 memakai forecast sebagai hero.
3. Panel data AS sebagai FORECAST yang jujur (label DUE 13:30 UTC) — bukan "CONFIRMED" palsu seperti #3.
4. DATE CHECK terbesar & paling jujur (11 exclusion + 2 demoted, lengkap dengan tanggal dan alasan) — termasuk koreksi atas kesalahan #4/#5 (Prabowo, ICJ).
5. Tag HOW SURE + sumber di setiap cerita (adopsi keunggulan #2) + ilustrasi penuh di SEMUA 13 kartu (adopsi keunggulan #3, perbaiki kelemahan #1).
6. 8 statistik terverifikasi (vs 6 di #1/#3).

### Yang masih lebih lemah dari top-5 (jujur)
1. Volume mentah: 35 < 50 (#2). Kalau judge menimbang jumlah cerita di atas segalanya, kita kalah di sini.
2. Drama visual hero: Shenzhou/CPI/treaty kurang dramatis dibanding trio #1 (AI crash + krisis kabinet + kebakaran). Houthi Riyadh (M4) adalah kartu paling dramatis kita tapi hanya medium.
3. Kedalaman olahraga: hanya Real Madrid + catur + T20; #2 punya dinding jadwal olahraga yang mungkin disukai judge.
4. Build lebih siang (data 02:00 UTC) — kita melewatkan peristiwa sore 25 Nov (KTT Balkan 17:00, Trump–Rutte, Game 2 catur, data AS 13:30 UTC) sebagai hasil; kita hanya bisa melabelinya SCHEDULED/DUE. #1/#3 "mengisi" slot itu dengan AHEAD — tidak jujur, tapi terlihat lengkap.
5. Afrika: tidak ada cerita Afrika terverifikasi dalam jendela ini — region bar kita mungkin hanya 7 region (lihat catatan §5), sementara #1 mengklaim 8.

## 12. CATATAN BUILD (untuk tim build — BUKAN untuk halaman)
- Verifikasi ulang saat build (paling lambat sebelum submit): B23 (tanggal turkey pardon), B29 (tanggal pengumuman BJP–SAD), B31 (jadwal briefing Parlemen EU), B28 (kota laga T20), angka tutup Nvidia (sumber berbeda: −5,9% vs −7,2% — pakai "~7%" intraday atau pilih satu sumber dan tulis sumbernya), tally region (§5), dan — jika build melewati 13:30 UTC — angka AKTUAL data AS (B17) dari BEA/DOL/Census.
- Jangan tambahkan cerita baru yang tidak ada di spec ini tanpa verifikasi tanggal + sumber.
- Ilustrasi: 13 ilustrasi flat-vector orisinal (3 hero + 10 medium), satu per kartu. Tanpa ilustrasi = plafon ~98,0–98,2% (text-only) — jangan ulangi kesalahan #4.
- Cek sebelum submit (skill): baca tiap kartu ukuran penuh + kecil; cocokkan nomor pin peta dengan brief; cocokkan tiap angka dengan sumber; DATE CHECK lengkap; bandingkan dengan top-5 dan tulis apa yang masih lebih lemah.
