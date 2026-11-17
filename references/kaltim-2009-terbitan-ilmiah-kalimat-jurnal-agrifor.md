# Winarti dkk. (2009), *Kesalahan Berbahasa Indonesia dalam Terbitan Ilmiah ...* - Jurnal Agrifor (pembentukan kata dan kalimat)

**Sumber primer:** Winarti, Yudianti Herawati, Aminuddin Rifai, Diyan Kurniawati, Emiliana
Patiung, dan Erminawati. *Kesalahan Berbahasa Indonesia dalam Terbitan Ilmiah Perguruan
Tinggi di Kalimantan Timur*. Samarinda: Pusat Bahasa, Departemen Pendidikan Nasional, 2009.
Berkas: `books/kesalahan_berbahasa_terbitan_ilmiah_kaltim.pdf`, teks ekstraksi
`work/kaltim-text.txt`.

Catatan ini melanjutkan `kaltim-2009-terbitan-ilmiah-pembentukan-kata.md` (subbab
2.1.1-2.1.2, hlm. 7-14) dan mencakup subbab 2.2.1-2.2.3, Jurnal Agrifor (hlm. 24-32).
Penanda `[OCR]` dan `[telaah]` mengikuti konvensi berkas saudaranya.

---

## 2.2.1 Kesalahan Pembentukan Kata - Jurnal Agrifor `[hlm. 24-27]`

Kaidah aktif:

| Buku | Bentuk | Perbaikan | Kaidah |
|---|---|---|---|
| (1) | `memposisikan` | `memosisikan` | `TMS-039` (baru) |
| (1b) | `marjinal` | `marginal` | `TMS-039` (baru) |
| (2) | `hektar` | `hektare` | `TMS-039` (baru) |
| (4) | `diprioritas` | `diprioritaskan` | `KK-004` (sudah; terverifikasi) |
| (6) | `menghasil` | `menghasilkan` | `TMS-040` (baru) |
| (8) | `mempengaruhi` | `memengaruhi` | `BAK-001` (sudah; terverifikasi) |

> (5) Multiplier adalah pengukuran suatu respon ...

> Bentuk respon berasal dari serapan kata bahasa Inggris, yaitu response. Penyerapannya ke
> dalam bahasa Indonesia adalah respons.

Kaidah aktif: `TMS-041` (baru) - regex `\brespon\b` yang sengaja **tidak** memakai `\w*`
di awal agar turunan sah `responden` dan `responden` tidak tertandai; turunan baku
`responsif`, `responsivitas` juga lolos.

> (9) Data yang diperoleh dianalisa ... `[OCR]`

Kaidah aktif: `BAK-005` sudah ada.

> (3) Kepmenhut ini kemudian dirubah ...

Kaidah aktif: `BAK-002` dan `BPK-019` sudah ada; contoh (3) terverifikasi tertangkap.

> (7) ... waktu dan tehnik aplikasi ...

Kaidah aktif: `BPK-030` (`tehnik`) sudah ada.

---

## 2.2.2 Kesalahan Pemilihan Kata `[hlm. 28-29]`

> (1) ... walaupun sudah lebih partisipasif dari istilah "mengikutsertakan" ...

> kata dari tidak digunakan untuk menyatakan perbandingan dalam ragam bahasa baku. Kata yang
> tepat untuk menyatakan perbandingan adalah daripada

Kaidah aktif: `TMS-029` (adjektiva pembanding + `dari`) sudah ada pada siklus 13.

> (2) Tiap bagian terdiri dari satu anakan (bibit).

Kaidah aktif: `TBB-004` sudah ada.

---

## 2.2.3 Kesalahan Penyusunan Kalimat `[hlm. 29-32]`

> (1) Pola pemanfaatan hutan kemasyarakatan adalah ... dalam memanfaatkan kawasan,
> pemanfaatan jasa lingkungan, ...

> di samping kata memanfaatkan juga digunakan kata pemanfaatan. Sebaiknya digunakan satu
> bentuk saja

`[telaah]` Kesejajaran bentuk deret perincian tidak dipola: penandaiannya menuntut analisis
struktur deret frasa; regex murni akan menandai deret yang sah. Tidak diaktifkan.

> (2) Oleh Sri Setyati Haryadi (1979) menguatkan, bahwa ...

> predikat kalimat tersebut seharusnya berbentuk pasif, yaitu berawalan di-

`[telaah]` Subjek preposisional `Oleh X + predikat aktif` tidak dipola: penandaiannya butuh
pembedaan nama orang dan konstruksi pasif fokus pelaku yang sah. Selain itu, buku menuntut
penghapusan koma sebelum `bahwa` - koma antara predikat dan objek juga tidak dipola karena
`SPE-001`/`KJK-005` sudah mengelola pasangan koma-konjungsi kausal yang mirip. Tidak
diaktifkan.

> (3) Untuk pengamatan berat kering tunas batang (Tabel 3) menunjukkan bahwa ...

> subjek berkata depan ... dapat dilakukan dengan cara menghilangkan kata untuk

`[telaah]` Subjek berkata depan tidak dipola (butuh analisis fungsi). Tidak diaktifkan.

> (4) Topografi berombak ini juga didukung adanya bahan organik di atas tanah mengakibatkan ...

> harus dihadirkan kata penghubung yang sebelum kata mengakibatkan

`[telaah]` Verba kedua tanpa penghubung tidak dipola: penandaiannya menuntut analisis batas
klausa; regex murni menandai deret verba yang sah (mis. `berjalan mengejar`). Tidak
diaktifkan.

> (5) Berdasarkan hasil penelitian menunjukkan bahwa ...

`[telaah]` Frasa `Berdasarkan X menunjukkan` tidak dipola pada siklus ini; kasusnya menunggu
penajaman apakah koma penghubung atau pengubahan predikat yang diresepkan buku. Tidak
diaktifkan.

---

## Catatan verifikasi matcher

`work/test_tms39_41.py` 15/15: 3 positif + 3 negatif untuk `TMS-039`, 1 positif + 2 negatif
untuk `TMS-040`, 1 positif + 3 negatif untuk `TMS-041`, 2 konteks bersih. Regex `TMS-039`
memakai `\b\w*posisikan\b|\bmemposisi\b` agar turunan `memposisikan` tertangkap, tetapi
nomina `posisi` dan frasa `data posisi` tidak. Uji nol positif palsu `test_smoke.py` tetap
0 hit.
