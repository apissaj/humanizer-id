# Winarti dkk. (2009), *Kesalahan Berbahasa Indonesia dalam Terbitan Ilmiah Perguruan Tinggi di Kalimantan Timur* - pembentukan kata dan preposisi

**Sumber primer:** Winarti, Yudianti Herawati, Aminuddin Rifai, Diyan Kurniawati, Emiliana
Patiung, dan Erminawati. *Kesalahan Berbahasa Indonesia dalam Terbitan Ilmiah Perguruan
Tinggi di Kalimantan Timur*. Samarinda: Pusat Bahasa, Departemen Pendidikan Nasional, 2009.
xvi + 156 hlm. ISBN 978-602-95465-1-4.
Berkas: `books/kesalahan_berbahasa_terbitan_ilmiah_kaltim.pdf`, teks ekstraksi
`work/kaltim-text.txt`.

Cakupan catatan ini: subbab 2.1.1 (kesalahan pembentukan kata, Jurnal Budidaya Pertanian,
hlm. 7-10) dan 2.1.2 (kesalahan pemilihan kata, hlm. 11-14). Kualitas OCR buku ini rendah
(`1/miah` untuk *Ilmiah*, angka halaman kadang meleset); kutipan yang jelas salah baca
diberi penanda `[OCR]` dan tidak dijadikan dasar regex.

---

## 2.1.1 Kesalahan Pembentukan Kata `[hlm. 7-10]`

> Dalam bahasa Indonesia tidak ada subjek berkata depan. Dalam kalimat di atas, subjek
> diawali dengan kata pada.

`[telaah]` Subjek berkata depan tidak dipola: penandaannya menuntut analisis fungsi sintaksis
yang tidak mungkin regex. Tidak diaktifkan.

> (2) ... belum mampu mensuplai bahan organik yang banyak.

> Kata suplai bila mendapat imbuhan meng- akan menjadi menyuplai. Hal ini disebabkan fonem /s/
> luluh.

Kaidah aktif: `BDD-006` sudah menangkap `mensuplai`; contoh (2) terverifikasi tertangkap
mesin lama.

> (3) Data yang diperoleh dianalisa ...

> Penyerapan kata tersebut ke dalam bahasa Indonesia adalah analisis

Kaidah aktif: `BAK-005` (`analisa`) sudah dipasang pada siklus 15; bentuk `dianalisa`
terverifikasi tertangkap regex `analisa`.

> (4) ... yang mampu menstimulir pembelahan ...

> Bentuk yang lebih tepat dari kata mensdmulir adalah menstimulasi. `[OCR]` `mensdmulir` =
> `menstimulir`

Kaidah aktif: `TMS-037` - regex `\w*stimulir\w*` menangkap `menstimulir` dan turunannya;
bentuk baku `menstimulasi`, `stimulasi`, `stimulus` lolos.

> (5) Panili merupakan salah satu tanaman industri ...

> Penyerapannya ke dalam bahasa Indonesia adalah vanili, bukan panili

Kaidah aktif: `TMS-037` - `panili`.

> (6) Untuk meningkatkan produktifitas tanah-tanah ultisol ...

Kaidah aktif: `BPK-027` (`produktifitas`) sudah ada; contoh (6) terverifikasi tertangkap.

> (1) Program ... agar semua lahan-lahan disekitar lingkungan pengeboran ...

> baik penanda jamak maupun bentuk ulang digunakan secara bersamaan ... perlu dihilangkan
> salah satunya

Kaidah aktif: `SPB-001` (ganda jamak) sudah ada untuk pasangan penanda + reduplikasi;
`disekitar` serangkai masuk `TMS-037`.

---

## 2.1.2 Kesalahan Pemilihan Kata `[hlm. 11-14]`

> Bentuk mulai Maret sampai Mei 2001 mengandung unsur preposisi gabungan. Preposisi gabungan
> ini terdiri atas dua unsur yang dipakai berpasangan, tetapi terpisah oleh kata atau frasa
> lain. Bentuk preposisi gabungan itu antara lain adalah antara ... dengan ..., dari ...
> sampai dengan ..., sejak ... hingga ..., dan dari ... ke ...

> bentuk mulai Maret sampai Mei 2001 pada kalimat di atas kurang tepat. Bentuk tersebut
> sebaiknya dibetulkan menjadi mulai Maret sampai dengan Mei 2001.

Kaidah aktif: `TMS-038` - regex `(?:mulai|Mulai|MULAI)\s+(?:[A-Z][a-z]+\s+|\d)[^.!?;\n]{0,60}?\bsampai\b(?!\s+dengan\b)`.

Regex sengaja **tidak** memakai `(?i)`: huruf kapital pada nama bulan atau angka tahun
berfungsi sebagai penanda bahwa frasa di antara `mulai` dan `sampai` benar-benar rentang
waktu, sehingga kalimat semacam "Nilai ujian mulai naik setelah remedial sampai tuntas" -
yang bukan rentang waktu - tidak tertandai. Percobaan pertama dengan `(?i)` gagal kasus
negatif ini dan dipersempit.

> (2) Tiap bagian terdiri dari satu anakan (bibit).

> Bentuk terdiri dari merupakan bentuk yang rancu dengan bentuk terbuat dari.

Kaidah aktif: `TBB-004` (`terdiri dari`) sudah ada; contoh (2) terverifikasi tertangkap.

---

## Catatan verifikasi matcher

`work/test_tms37_38.py` 19/19: 5 positif + 5 negatif untuk `TMS-037`, 2 positif + 5 negatif
untuk `TMS-038`, 2 konteks bersih. Uji nol positif palsu `test_smoke.py` tetap 0 hit.
Regex `TMS-038` versi pertama memakai `(?i)` dan menandai "mulai naik ... sampai tuntas";
dipersempit dengan menghapus `(?i)` dan mewajibkan nama bulan berkapital atau angka setelah
`mulai`/`dari`.
