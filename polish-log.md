# POLISH LOG — News-25 v2, arah A (huashu-design polish-loop)

## Ronde 0 — tiga arah, 1 ronde tiap arah (26 Nov ~16:30 WIB)
Render A/B/C, baca ketiganya di 1024.
3 hal terburuk (semua arah): (1) dateline medium bertabrakan dengan tag
("6 · FLINDERS ISLAND · TUE 25 NOV" menimpa "OFFICIAL"); (2) baris sumber
menabrak baris terakhir body di kartu medium; (3) brief line1 terpotong
("17 · BRUSSELS — EU–Balkans deal; Serbia" — "stays away" hilang).
Perbaikan: draw_card menghitung tinggi band ilustrasi dari tinggi kartu
minus blok teks (sumber tidak pernah bertabrakan lagi); kartu sempit pakai
dateline pendek (nomor + tempat), tanggal pindah ke baris sumber; brief
ditulis ulang format headline-dulu + cek wrap otomatis (defect kalau wrap).
Hasil: A/B/C 0 defect (sebelumnya 21 defect tiap arah).

## Ronde 1 — arah A, baca top/bottom 1024 (26 Nov ~16:45 WIB)
3 hal terburuk: (1) label strip "US GDP, Q3 annualised" wrap 2 baris dan
baris ke-2 terpotong tepi band; (2) klaster pin Eropa di peta masih padat
(Geneva/Strasbourg/Paris bertumpuk); (3) verifikasi piksel hitam band hero
belum dilakukan.
Perbaikan: label jadi "US GDP, Q3 ann." (1 baris); offset pin Geneva/
Strasbourg/Paris/Jerusalem dijauhi lagi; sampling piksel otomatis zona hero
(165–420px): **0 piksel hitam** (H1 0, H2 0, H3 0).
Hasil: A 0 defect, final y=1012, 298.653 byte.

## Ronde 2 — arah A, baca 512px + full (26 Nov ~16:55 WIB)
3 hal terburuk: (1) di 512px peta jadi blob pin (Eropa tak terbaca — tapi
masthead, hero, strip angka, dan headline medium tetap terbaca);
(2) band ilustrasi hero susun (Shenzhou) tipis, roket kecil;
(3) bangunan Fed di ilustrasi H1 sempat terpotong tepi (sudah diperbaiki
di ronde 0 dengan skala 1.15 + gedung digeser).
Perbaikan: radius pin peta 550/450km (declutter, marginal); poin (1) dan
(2) diterima sebagai trade-off arah A yang sudah dipilih — dicatat jujur,
bukan dipoles paksa. Cek determinisme: rebuild byte-identik.
Hasil: A 0 defect, final y=1012, 298.031 byte, 0 piksel hitam, deterministik.
Tidak ada lagi 3 hal yang layak diperbaiki tanpa mengganti arah — polish
berhenti di ronde 2.
