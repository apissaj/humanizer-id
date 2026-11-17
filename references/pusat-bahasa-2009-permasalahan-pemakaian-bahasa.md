# Rusbiyantoro dkk. (2009), *Beberapa Permasalahan Pemakaian Bahasa Indonesia* - kata, imbuhan, dan penghubung

**Sumber primer:** Wenni Rusbiyantoro, Nur Bety, dan Mardi Nugroho. *Beberapa Permasalahan
Pemakaian Bahasa Indonesia*. Jakarta: Pusat Bahasa, Departemen Pendidikan Nasional, 2009.
x + 150 hlm. ISBN 978-602-95465-3-8.
Berkas: `books/beberapa_permasalahan_pemakaian_bahasa_indonesia.pdf`.

Kutipan diambil dari hasil ekstraksi `pdftotext -enc UTF-8` (`work/bppbi-text.txt`). Kualitas
OCR berkas ini rendah: huruf /l/ sering terbaca `I`, gugus `rn` terbaca `m`, dan angka
romawi pada nomor contoh kadang berubah (`(ISO)` untuk `(150)`). Bagian yang jelas salah baca
diberi penanda `[OCR]` dan **tidak** dijadikan dasar pola regex.

Cakupan catatan ini: Subbab 3.8.1-3.8.3 (hlm. 42-53), yaitu ketidakcermatan penulisan kata,
pembentukan kata, dan pemilihan kata pada surat kabar *Kaltim Post*. Anotasi bertanda
`[telaah]` adalah penilaian penyusun kaidah, bukan pernyataan penulis.

---

## 3.8.1 Penulisan Kata yang Tidak Cermat `[hlm. 42-46]`

> Jika bentuk dasar berupa gabungan kata yang lazim disebut kata majemuk, termasuk istilah
> khusus, unsur-unsurnya ditulis terpisah.

> (120) Rasa kebersamaan masyarakat Poso dalam mensukseskan Pilkada sangat kental dan
> sama-sama mempunyai rasa tanggungjawab khususnya dalam hal keamanan. (KP, 2/7, hlm. 6)

> Sesuai dengan kaidah ejaan, cara penulisan gabungan kata, yang lazim disebut kata majemuk,
> adalah bagian-bagiannya dituliskan secara terpisah. Secara berurutan, penulisan gabungan
> kata yang benar dari kalimat (121)-(124), yaitu kerja sama, unjuk rasa, tanda tangan, dan
> lagi pula.

> (125) Dia menambahkan. dua hal isi SMS yang paling urgent dia tindaldanjuti adalah soal
> korupsi ... `[OCR]` `tindaldanjuti` = `tindaklanjuti`

> Gabungan kata yang unsur-unsurnya mandiri dituliskan secara terpisah ... Data (126) juga
> terdiri dari dua kata, yaitu salah dan satu. jadi, penulisannya terpisah meskipun kata
> tersebut mendapat akhiran -i untuk kata tindak lanjut dan partikel -nya untuk kata salah
> satu.

> (127a) "Semua kemungkinan dan informasi yang kami terima akan ditindaklanjuti. ..."

> Seperti kata ditindaklanjuti pada kalimat (127), kata menumbuh kembangkan penulisannya hams
> dirangkaikan. `[OCR]` `hams` = `harus`

> Ketidakcermatan penulisan kata dalam kalimat (129) berikut terdapat pada kata non akti£
> `[OCR]` `akti£` = `aktif`

> Menurut kaidah ejaan, jika salah satu unsur gabungan kata hanya dipakai dalam kombinasi,
> gabungan kata itu ditulis serangkai. Jadi, perbaikan penulisan kata tersebut adalah sebagai
> berikut. (129a) ... hams nonakti£ `[OCR]`

> (131) Sementara Kordinator Wilayah (Korwil) yang sebelumnya enam direvisi menjadi empat
> Korwil. (KP, 7/5, him. 3) `[OCR]` `him.` = `hlm.`

> Sesuai dengan Kamus Besar Bahasa Indonesia (2002: 593), penulisannya yang benar adalah
> koordinator.

**Kaidah aktif:**

| Kaidah | Bentuk ditandai | Perbaikan |
|---|---|---|
| `BPK-044` | `penanggungjawab` | `penanggung jawab` |
| `BPK-045` | `bekerjabakti` | `bekerja bakti` |
| `TMS-030` | `salahsatunya`, `tindaklanjuti`, `unjukrasa`, `lagipula`, `non aktif` | `salah satunya`, `tindak lanjut`, `unjuk rasa`, `lagi pula`, `nonaktif` |
| `TMS-031` | `kordinator`, `kordinasi` | `koordinator`, `koordinasi` |

`[telaah]` Kalimat (127) menunjukkan bahwa `ditindaklanjuti` **benar** dan
`ditindak lanjuti` **salah**. Regex `TMS-030` karena itu menandai `tindaklanjuti` (bentuk
dasar yang ditulis serangkai tanpa awalan) dan `tindak lanjuti`/`ditindak lanjuti`/
`menindak lanjuti` (bentuk berimbuhan yang dipisah), tetapi membiarkan `ditindaklanjuti` dan
`menindaklanjuti` lolos.

`[telaah]` `tanggungjawab`, `kerjasama`, dan `tandatangan` dari kalimat (120)-(123) **tidak**
dijadikan kaidah baru karena sudah tertangkap `EJ-001`, dengan turunan `TIQ-004`,
`KPT-009`, `SPE-002`, `BPK-022`, dan `SPE-014`.

---

## 3.8.2 Pembentukan Kata yang Tidak Cermat `[hlm. 46-49]`

> (134) "... saya sendiri tak berbak mengkomentari trak record calon yang diajukan presiden,"
> tambah Jimly. (KP, 3/7, hlm. 9) `[OCR]` `berbak` = `berhak`

> Kata mengkomentari dalam kalimat (134) berkata dasar komentar yang mendapat awalan meng- dan
> akhiran -i-. Dalam Tata Bahasa Baku Bahasa Indonesia disebutkan bahwa fonem awal /k/ ...
> menjadi luluh ...

> (135) ... baik Desa Suliliran Baru pun Desa Muara Payang menta.rgetkan kemenangan bagi
> Yusmar diatas 70 persen. `[OCR]`

> Menurut kaidah bahasa Indonesia, fonem itu seharusnya lebur menjadi sengau, yaitu /t/
> menjadi /n/. Jadi, perbaikan kalimat di atas adalah sebagai berikut. (135a) ... menargetkan

> (143) PM China Wen ]iabao menegaskan pihaknya tidak akan merubah nilai tukar mata uang
> China ...

> Menurut Kamus Besar Bahasa Indonesia, kata rubah mempunyai arti 'binatang jenis, bermoncong
> panjang, dan makanannya daging ikan' (2001: 965). Dengan semikian, kata merubah tidak sesuai
> dengan konteks kalimatnya. Kata dasar yang benar adalah ubah dan mendapat awalan meng-
> sehingga menjadi mengubah. `[OCR]` `semikian` = `demikian`

**Kaidah aktif:** `TMS-031` (`mengkomentari` -> `mengomentari`), `BAK-004`
(`mentargetkan` -> `menargetkan`), `BAK-002` (`merubah`/`dirubah` -> `mengubah`/`diubah`).

`[telaah]` `memroses` (kalimat 142) dan `diatas` (kalimat 135) juga disebut buku ini, tetapi
keduanya sudah punya kaidah bermesin (`TBB-028`, `PFP-003`), sehingga tidak diduplikasi.

---

## 3.8.3 Pemilihan Kata yang Tidak Cermat `[hlm. 50-53]`

> Kata ranking berarti 'pemeringkatan' ... Jika kata ranking yang digunakan dalam pengertian
> peringkat, jelas pemakaian itu tidak cermat.

> (145) ... Karang Taruna Karya Usaha lebih jauh di bawahnya, yakni hanya mampu berada pada
> posisi peringbt ranking XVI. `[OCR]` `peringbt` = `peringkat`

> Pada data kalimat (145) kata ranking dan peringkat ditulis semuanya. Jika dibaca dan
> diartikan, menjadi peringkat peringkat.

> Dalam KBBI tidak terdapat kata beking. ... lebih tepat digunakan kata 'dukungan' atau
> 'sokongan'.

> Ketidakcermatan pemilihan kata yang berfungsi sebagai penghubung antarkalimat banyak
> ditemukan dalam surat kabar Kaltim Post. Penggunaan bentuk di mana dalam bahasa Indonesia
> kemungkinan besar dipengaruhi oleh bahasa asing, khususnya bahasa Inggris where.

> (ISO) Dirnaml tinggal sejumlah ekspatriat ... `[OCR]` nomor contoh = (150), `Dirnaml` =
> `Dinamai`

> Kata dimana pada kalimat (ISO) tidak tepat dalam pemakaiannya karena kata dimana terletak di
> awal kalimat seperti menandakan kalimat tanya. ... kata dimana dapat diganti dengan kata
> tempat.

> (152) Hal itu terkait keterbatasan dana yang dimiliki Bapomi, dimana biaya yang dibutuhkan
> untuk membawa jatah kuota 4 adet di masing-masing cabang olahraga, memerlukan tidak kurang
> dari Rp 70 juta. (KP, 5/6, him. 16)

> Penggunaan kata dimana pada kalimat (152) sebagai kata penghubung tidaklah tepat. ... lebih
> tepat menggunakan kata karena.

**Kaidah aktif:** `BDD-009` (klise `, di mana hal ini`). Matcher sengaja mensyaratkan koma di
depan frasa agar klausa relatif yang sah - `Desa di mana hal ini terjadi` - tidak tertandai.

`[telaah]` `dimana` di awal kalimat (kalimat 150 dan 151) belum dipola secara khusus: varian
ini sudah tertangkap `CX11-001` (kata penghubung `dimana/diketika/disewaktu`), sehingga pola
tambahan hanya akan menandai satu kalimat dua kali.

`[telaah]` `ranking` untuk makna 'peringkat', `beking` untuk 'dukungan', dan `open race` untuk
'arena terbuka' sengaja belum dipola. Ketiganya kosakata jurnalistik bertanggal; `ranking`
kini lazim dipakai sebagai istilah kolokial dan menandainya akan menghasilkan tuduhan palsu
pada konteks olahraga dan pemasaran.

---

## Catatan verifikasi matcher

Empat kaidah lama yang sebelumnya ada di data tanpa mesin - `BAK-002`, `BAK-004`, `BPK-044`,
`BPK-045` - kini punya matcher. Pemeriksaan dilakukan dengan
`[i for i,(pred,_) in enumerate(CUSTOM_RULES) if pred(pola)]` (bukan `grep` atas ID, karena
blok lama sering tidak menyebut ID pada komentarnya), dan setiap pola menghasilkan tepat satu
indeks, artinya tidak ada blok lain yang menelannya lebih dahulu. Matcher `SPE-014`
(`tandatangani`) ikut dipasang pada siklus ini dengan regex `tandatangani` yang
sengaja tidak menangkap `ditandatangani` (bentuk berimbuhan yang benar). `KPT-009`
tidak diberi matcher `CUSTOM_RULES` karena `kerjasama` sudah dilaporkan lewat mesin
kata tidak baku di `engine.py`; menambah blok baru hanya akan menggandakan laporan.
