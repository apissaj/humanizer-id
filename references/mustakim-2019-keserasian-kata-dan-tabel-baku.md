# Mustakim (2019), *Bentuk dan Pilihan Kata* - keserasian kata dan tabel bentuk baku

**Sumber primer:** Mustakim. *Bentuk dan Pilihan Kata: Seri Penyuluhan Bahasa Indonesia*.
Jakarta: Badan Pengembangan Bahasa dan Perbukuan, Kementerian Pendidikan dan Kebudayaan, 2019.
Berkas: `books/buku_seri_penyuluhan_bentuk_dan_pilihan_kata_2019.pdf`, teks ekstraksi
`work/bpik-text.txt`.

Catatan ini melengkapi `mustakim-2019-bentuk-pilihan-kata-mantan-bekas-dari-daripada.md`
(subbab 3.3 c-h, hlm. 76-82) dan mencakup subbab 3.1.3 bagian keserasian (hlm. 60-72) serta
tabel baku-tidak baku pada hlm. 67-68. Anotasi `[telaah]` adalah penilaian penyusun kaidah.

---

## 3.1.3 Keserasian - faktor kebahasaan `[hlm. 60-66]`

> (2) Penggunaan bentuk gramatikal

> Jika digunakan di dalam komunikasi yang resmi, bentuk kata kumpul pada kalimat (34) dan
> jumpa pada kalimat (35) dianggap tidak gramatikal karena strukturnya tidak lengkap. Agar
> gramatikal, bentuk kedua kata tersebut harus dilengkapi, yaitu dengan menambahkan imbuhan
> ber- sehingga menjadi berkumpul dan berjumpa

> (34) Para peserta upacara sudah kumpul di lapangan.
> (35) Sampai jumpa lagi pada kesempatan yang lain.

Kaidah aktif: `TMS-035` - `sudah kumpul`, `telah kumpul`, `akan kumpul`, `baru jumpa`, dan
`sampai jumpa` ditandai; bentuk berimbuhan (`berkumpul`, `berjumpa`, `mengumpulkan`) lolos.

> (4) Penggunaan Ungkapan Idiomatis

> Beberapa ungkapan idiomatis dalam bahasa Indonesia adalah sebagai berikut.
> sesuai dengan / sehubungan dengan / berkaitan dengan / bergantung pada / tergantung pada /
> terdiri atas

> kata kedua dari ungkapan idiomatis tersebut, yaitu dengan, atas, dan pada, sering
> ditanggalkan oleh pemakai bahasa karena dianggap tidak mendukung makna ... Meskipun tidak
> mendukung makna, kata kedua dari ungkapan itu tidak seharusnya ditanggalkan karena keduanya
> sudah merupakan satu kesatuan.

Kaidah aktif: `BPK-005` sudah ada dan pada siklus ini daftar nominanya diperluas sehingga
`tergantung cuaca`, `bergantung anggaran`, dan `tergantung penilaian` ikut tertandai, tidak
lagi terbatas pada `hasil`, `kondisi`, `keputusan`, `situasi`, `tingkat`.

`[telaah]` `sesuai undang-undang` dan `sesuai jadwal` sengaja tidak ditandai. Praktik
penyuntingan resmi masih menerima `sesuai` tanpa `dengan` pada frasa pendek yang lazim, dan
menandainya akan menghasilkan tuduhan palsu pada naskah hukum yang memilih ragam ringkas.
Hanya konteks yang secara eksplisit menanggalkan preposisi wajib (`sesuai konteks`,
`berkaitan hal`) yang dijaga mesin.

> (1) Penggunaan Kata yang Sesuai dengan Konteks Kalimat ... penggunaan kata di mana dan yang
> mana ... tidak serasi karena kata tanya itu seharusnya digunakan untuk mengungkapkan
> pertanyaan

`[telaah]` Sudah terjaga kaidah lama (`CX11-001`, `UIN-009`, `BDD-007`, `BDD-009`); tidak ada
entri baru.

## 3.1.3 Tabel baku - tidak baku `[hlm. 67-68]`

> Kata-kata yang termasuk dalam daftar baku (lajur kiri) itulah yang harus dipilih dalam
> pemakaian bahasa yang resmi.

Isi tabel (lajur baku -> bentuk tidak baku) dan status mesin:

| Baku | Tidak baku | Kaidah |
|---|---|---|
| akta | akte | `TMS-036` (baru) |
| aktivitas | aktifitas | `TIQ-003` (sudah) |
| analisis | analisa | `BAK-005` |
| biaya | beaya | `TMS-036` (baru) |
| diagnosis | diagnosa | `BPK-017` |
| efektif | effektif, efektip | `TMS-036` (baru) |
| efisien | effisien | `TMS-036` (baru) |
| Februari | Pebruari | `BPK-028` |
| foto | photo | `BPK-031` |
| fotokopi | photo copi, foto copy | `BPK-031` |
| hipotesis | hipotesa | `BPK-017` |
| jadwal | jadual | `BPK-015` |
| Jumat | Jum'at | `BPK-029` |
| kualitas | kwalitas | `BPK-015` |
| kuantitas | kwantitas | `BPK-015` |
| kuesioner | questioner | `BPK-016` |
| kuitansi | kwitansi | `BPK-015` |
| metode | methode, metoda | `BPK-017` |
| November | Nopember | `BPK-028` |
| objek | obyek | `BPK-018` |
| persen | prosen | `BPK-016` |
| persentase | prosentase | `BPK-016` |
| produktivitas | produktifitas | `BPK-027` |
| Rabu | Rabo, Rebo | `BPK-029` |
| risiko | resiko | `BAK-008` |
| sistem | sistim | `BPK-017` |
| teknik | tehnik, technik | `BPK-030` |

Regex `TMS-036` memakai alternasi eksplisit `efektip|effektif|effisien`, bukan pola
`eff?ekti[pf]`, karena pola longgar semacam itu akan ikut menandai bentuk baku `efektif`.

## 3.1.4 Pilihan kata yang tidak tepat `[hlm. 73-82]`

Sudah dibedah pada siklus sebelumnya (`kita` untuk `saya`, `kami` untuk penulis tunggal,
`kebijakan`/`kebijaksanaan`, `mantan`/`bekas`, `jam`/`pukul`, `dari`/`daripada`,
`yaitu`/`yakni`/`adalah`/`ialah`, `antara lain`/`misalnya`). Statusnya:

- Bermesin: `BPK-007` (jam/pukul), `BPK-008` (yaitu), `BPK-009` (bekas), `BPK-006` dan
  `TMS-029` (dari/daripada), `BPK-024` (kebijaksanaan).
- `[telaah]` sengaja tidak dipola: `BPK-013` (`kita` untuk penulis tunggal) dan `BPK-014`
  (`kami` untuk penulis tunggal), karena keduanya hanya dapat diputuskan dengan mengetahui
  jumlah penulis naskah.
- `[telaah]` `antara lain` vs `misalnya` (kalimat 57-58) tetap tidak dipola: pembedaan
  "seluruhnya" vs "sebagian" bergantung pada pengetahuan tentang populasi yang dirujuk.

## Catatan verifikasi matcher

`work/test_tms35_36.py` 16/16 (6 positif, 6 negatif, 3 konteks bersih); uji nol positif palsu
`test_smoke.py` tetap 0 hit. Regex `sampai jumpa` awalnya case-sensitive sehingga kalimat yang
dimulai dengan huruf kapital lolos; ditambahkan `(?i)`. Pemerluasan `BPK-005` diverifikasi
dengan lima kalimat tambahan (`sesuai jadwal`, `berkaitan dengan hal itu`,
`tergantung pada hasil uji`, `berkumpul`, `sampai berjumpa`) yang seluruhnya bersih.
