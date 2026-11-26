# DIRECTION v2 — News-25 'World in One Day' (26 Nov 2026)

Tiga arah layout dirender nyata dari data yang sama (39 cerita terverifikasi),
dinilai dengan critique-guide huashu-design (konsep / hierarki / craft /
fungsionalitas / orisinalitas). Gate "user pilih" tidak bisa menunggu user
(deadline 27 Nov 07:00 WIB, user sudah delegasikan penuh) — pilihan dibuat
di sini via critique + head-to-head vs v1.

## Sistem desain bersama (ketiga arah)
- Satu aksen: biru broadsheet gelap #1E40AF (+tint). Region bar satu warna
  (v1: 7 warna). Kertas putih, tinta nyaris-hitam, serif masthead.
- Tanpa dekorasi template: tanpa label all-caps di atas tiap judul, tanpa
  "01/02/03", tanpa ekor panah, tanpa gradien. Dateline (tempat+tanggal)
  dipertahankan karena fungsional (koran), bukan dekorasi; nomor cerita
  adalah referensi pin peta, bukan penomoran dekoratif.
- Fakta dulu: semua angka/cerita terverifikasi (lihat BUILD-v2.md).

## A — Editorial asimetris (DIPILIH)
- Logika: satu hero lebar (data AS, 640px) + dua hero susun di kanan.
  Form tumbuh dari konten: cerita terbesar hari itu (paket data AS) jadi
  gambar terbesar di halaman.
- Critique: konsep 7/10 (ide jelas: "hari ini adalah hari data AS");
  hierarki 8/10 (mata: masthead → bar raksasa → hero susun → medium);
  craft 6/10 setelah polish (0 defect, 0 piksel hitam); fungsionalitas 7/10
  (39 cerita, semua bertanggal, peta + DATE CHECK); orisinalitas 6/10
  (struktur pemenang dipertahankan, eksekusi diperbaiki).
- Kelemahan yang diterima: band ilustrasi hero susun tipis (34px, roket
  kecil); pin peta Eropa tetap padat di 470px (terbaca di 1024, blob di 512).

## B — Satu hero raksasa + strip data (TIDAK DIPILIH)
- Logika: hero split full-width dengan angka raksasa "4.3%" + dua hero
  strip di bawahnya.
- Critique: konsep 8/10 — ide tunggal paling kuat (data jadi gambar);
  hierarki 8/10; craft 5/10; fungsionalitas 6/10; orisinalitas 7/10.
- Alasan ditolak: hero 2/3 (Shenzhou, Solomons) terdegradasi jadi strip
  tipis (body 1–2 baris, band ilustrasi 50px) — judge menimbang breadth +
  keterbacaan, dan B mengorbankan keduanya demi satu angka besar. Medium
  terjepit paling parah (116px). Varians tinggi, risiko lebih besar dari A.

## C — Peta-led + band hero sinematik (TIDAK DIPILIH)
- Logika: peta dunia lebar dulu, lalu band 3 hero dengan ilustrasi rasio
  native 4:1.
- Critique: konsep 6/10 (peta sebagai pembuka terdengar kuat, tapi pin
  tetap blob di Eropa — peta tidak membawa informasi pada ukuran ini);
  hierarki 6/10 (peta bersaing dengan hero tanpa memberi isi);
  craft 6/10 (hero paling bersih, DATE CHECK 3 kolom paling terbaca);
  fungsionalitas 7/10; orisinalitas 5/10 (band hero identik dengan v1).
- Alasan ditolak: ide pembuka gagal pada eksekusi (pin blob), dan sisanya
  tidak membedakan dari v1.

## Keputusan
**A dipilih.** A mempertahankan struktur pemenang v1 (yang mencetak 96,02%)
dan memperbaiki cacatnya + meng-upgrade konten sore hari — perbaikan
paling pasti vs v1 dengan risiko paling kecil. B lebih berani tapi
mengorbankan breadth; C idenya tidak terbukti di render.
