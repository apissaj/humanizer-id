# Winarti dkk. (2009), *Kesalahan Berbahasa Indonesia dalam Terbitan Ilmiah ...* - penyusunan kalimat Budidaya Pertanian dan jurnal Ekonomi Pertanian

**Sumber primer:** Winarti, Yudianti Herawati, Aminuddin Rifai, Diyan Kurniawati, Emiliana
Patiung, dan Erminawati. *Kesalahan Berbahasa Indonesia dalam Terbitan Ilmiah Perguruan
Tinggi di Kalimantan Timur*. Samarinda: Pusat Bahasa, Departemen Pendidikan Nasional, 2009.
Berkas: `books/kesalahan_berbahasa_terbitan_ilmiah_kaltim.pdf`, teks ekstraksi
`work/kaltim-text.txt`.

Catatan ini melanjutkan dua berkas saudaranya (`kaltim-2009-terbitan-ilmiah-pembentukan-kata.md`
hlm. 7-14; `kaltim-2009-terbitan-ilmiah-kalimat-jurnal-agrifor.md` hlm. 24-32) dan mencakup
subbab 2.1.3-2.1.4 (hlm. 14-23) serta 2.3.1-2.3.2 (hlm. 32-37).

---

## 2.1.3 Kesalahan Penyusunan Kalimat - Jurnal Budidaya Pertanian `[hlm. 14-19]`

> (2) Menurut Kim H. Tan (1991), bahwa Al yang dilepaskan kemudian dijerap oieh kompleks
> liat akan membentuk suatu kompleks -Al-H dengan cepat, ....

> subjek dalam Bahasa Indonesia tidak didahuiui dengan kata penghubung seperti bahwa dalam
> kalimat di atas. Jadi, kata penghubung bahwa harus dihilangkan

Kaidah aktif: `SPK-012` (baru) - regex `\bmenurut\s+[^,]{3,60},\s*bahwa\b`. Jendela
`[^,]` sengaja memperbolehkan titik agar singkatan nama (Kim H. Tan (1991)) tidak memutus
pencocokan; versi pertama `[^,.]` gagal kasus positif itu.

> (3) apabila Al bereaksi dengan air maka dari reaksi tersebut akan terlepas Kation H.

> dalam kalimat majemuk tidak dibenarkan hadir dua kata penghubung secara bersamaan

Kaidah aktif: `SPK-001` sudah ada, tetapi daftar konjungsinnya diperluas dari
`jika|kalau|apabila` menjadi `jika|kalau|apabila|bila` - buku contoh (5) dan (9) memakai
`bila ... maka` dan `bila ... namun ... maka`. Kalimat tanpa `maka` seperti "Pengujian
dilakukan bila cuaca mendukung." tetap lolos (terverifikasi negatif).

> (11) Hal ini disebabkan karena fosfor merupakan bagian dari inti sei, ...

Kaidah aktif: `UIN-001` + `BDD-001` sudah ada; contoh (11) terverifikasi tertangkap.

> (15) Berdasarkan hasil penelitian menunjukkan bahwa perlakuan pemberian pupuk organik
> Super Toshan berbeda nyata ...

> Frasa yang mengawali kalimat, yaitu Berdasarkan hasil penelitian, bukanlah subjek,
> melainkan keterangan. Frasa tersebut dapat menjadi subjek kalimat dengan syarat kata
> berdasarkan harus dihilangkan.

Kaidah aktif: `SPK-013` (baru) - regex `\bberdasarkan\s+[^,.]{3,60}\s+menunjukkan\b`.
Varian dengan koma ("Berdasarkan hasil penelitian, tingkat erosi tergolong rendah.") lolos
karena frasa keterangan itu sah; yang ditandai hanya ketika frasa `Berdasarkan X` langsung
disambung verba `menunjukkan` tanpa subjek.

> (16) Oleh Sri Setyad Haryadi (1979) menguatkan, bahwa ...

Kaidah aktif: subjek preposisional `Oleh X + verba aktif` sudah dicatat `[telaah]` pada
siklus 18 (`kaltim-2009-terbitan-ilmiah-kalimat-jurnal-agrifor.md`); tidak diubah.

> (1) Pada Jokasi pen elitian mempunyai vegetasi yang beragam ... `[OCR]`
> (12) Pada analisis tanah awal menunjukkan bahwa ... `[OCR]`

`[telaah]` Subjek berkata depan dengan awalan `Pada` tidak dipola: `Pada analisis tanah awal
menunjukkan` secara bentuk mirip kasus (15), tetapi buku meresepkan penghapusan `Pada`,
bukan `Berdasarkan`; penandaiannya butuh pembedaan fungsi sintaksis. Tidak diaktifkan.

## 2.1.4 Kesalahan Penataan Penalaran `[hlm. 20-23]`

> (1) Badak 107 kejenuhan basa rendah disebabkan terjadi pencucian yang intensif ...

Kaidah aktif: `SPK-011` (`disebabkan terjadinya`) dan `BDD-001` sudah ada; varian
`disebabkan terjadi` tidak dibuat kaidah baru karena pola `disebabkan + verba kedua`
menuntut analisis batas klausa (kalimat pasif ganda yang sah akan tertandai). `[telaah]`

> (3) Dengan memanfaatkan limbah pertanian sebagai pupuk, maka dapat mengurangi
> pencemaran lingkungan ...

Kaidah aktif: `SPK-001` menandai `... maka` hanya bila ada konjungsi syarat di depan;
konstruksi `Dengan X, maka ...` tanpa konjungsi syarat tidak dipola karena butuh analisis
fungsi frasa `Dengan X`. `[telaah]`

> (4) Di Kalimantan Timur pemanfaatan limbah pertanian belum banyak dimanfaatkan ...

`[telaah]` Redundans `pemanfaatan ... dimanfaatkan` tidak dipola: penandaiannya menuntut
pencocokan akar leksikal lintas afiks (memanfaatkan/pemanfaatan) yang regex murni akan
membuat bising pada pasangan sah. Tidak diaktifkan.

> (6) Berdasarkan Tabel 2 pada lahan profil 1 memiliki kelerengan 10-15% mempunyai kelas
> kesesuaian lahan yang cukup sesuai. `[OCR]` (kelerengan = kelereng/lereng)

`[telaah]` Subjek berkata depan ganda + redundans `memiliki/mempunyai`; tidak dipola.

## 2.3.1 Kesalahan Pembentukan Kata - Jurnal Ekonomi Pertanian dan Pembangunan `[hlm. 32-36]`

Kaidah aktif:

| Buku | Bentuk | Perbaikan | Kaidah |
|---|---|---|---|
| (1) | `mensosialisasi` | `menyosialisasi` | `KK-001` (sudah; terverifikasi) |
| (2), (6) | `teoritis` | `teoretis` | `TMS-042` (baru) |
| (3) | `komoditi` | `komoditas` | `TMS-001` (sudah; terverifikasi) |
| (4) | `sekedar` | `sekadar` | `TMS-042` (baru) |
| (7) | `menunjukan` | `menunjukkan` | `BPK-032` (sudah; terverifikasi) |
| (8) | `pasca BPPC` | `Pasca-BPPC` | `BAK-011` + `TMS-003` (sudah; terverifikasi) |
| (9) | `mempengaruhi` | `memengaruhi` | `BAK-001` (sudah; terverifikasi) |
| (10) | `keefektivan` | `keefektifan` | `KK-003` (sudah; terverifikasi) |
| (5) | `analisa` | `analisis` | `BAK-005` (sudah; terverifikasi) |

## 2.3.2 Kesalahan Pemilihan Kata `[hlm. 36-37]`

> (1) ... mengalami perkembangan yang lebih lambat dari perkembangan produksi nasional.

Kaidah aktif: `TMS-029` (adjektiva pembanding + `dari`) sudah ada pada siklus 13.

> (2) Hipotesis daripenelitian ini tercfiri dari: ... `[OCR]` (daripenelitian = dari penelitian)

Kaidah aktif: `TBB-004`/`TBB-005` (`terdiri dari`) sudah ada; frasa `hipotesis dari
penelitian` tidak dipola karena preposisi `dari` milik frasa nominal yang sah (bukan
pembanding). `[telaah]`

---

## Catatan verifikasi matcher

`work/test_tms42_spk012_013.py` 18/18: 2 positif + 2 negatif untuk `TMS-042`, 3 positif +
1 negatif untuk `SPK-012`, 2 positif + 1 negatif untuk `SPK-013`, 3 positif + 1 negatif
untuk perluasan `SPK-001`, 2 konteks bersih. Uji nol positif palsu `test_smoke.py` tetap
0 hit (45 passed).
