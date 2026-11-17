# Mustakim (2019), *Bentuk dan Pilihan Kata* - mantan/bekas, dari/daripada, yaitu/yakni

**Sumber primer:** Mustakim. *Bentuk dan Pilihan Kata: Seri Penyuluhan Bahasa Indonesia*.
Jakarta: Badan Pengembangan Bahasa dan Perbukuan, Kementerian Pendidikan dan Kebudayaan, 2019.
Berkas: `books/buku_seri_penyuluhan_bentuk_dan_pilihan_kata_2019.pdf`.
Kutipan diambil dari hasil ekstraksi `pdftotext -enc UTF-8` (`work/bpik-text.txt`); nomor
halaman mengikuti angka yang tercetak di kaki halaman buku dan ditandai `[hlm. N]`.

Cakupan catatan ini: Subbab 3.3 poin c-h (hlm. 76-82). Semua kutipan verbatim; anotasi
bertanda `[telaah]` adalah penilaian penyusun kaidah, bukan pernyataan buku.

---

## c. Pemakaian Kata Mantan dan Bekas `[hlm. 76-77]`

> Kata mantan dan bekas sebenarnya memiliki pengertian yang sama, yaitu 'tidak berfungsi
> lagi'. Kedua kata itu merupakan padanan kata asing *ex* (Inggris). Namun, kata bekas
> cenderung mengandung konotasi yang negatif, terutama jika digunakan untuk mengacu pada
> 'orang'. Oleh karena itu, kata mantan kemudian dipilih sebagai penggantinya.

> mantan menteri mantan gubernur mantan camat mantan kepala desa mantan kepala biro

> Adapun kata bekas penggunaannya hanya dilazimkan untuk menyebut barang-barang yang sudah
> tidak terpakai lagi atau orang yang tidak harus dihormati. Misalnya:

> bekas mobil bekas tempat rokok bekas pencuri bekas perampok

**Kaidah aktif:** `BPK-009` (substring predikat `'kata bekas untuk mengacu pada manusia'`).
Buku membedakan dua ranah pemakaian: `bekas` untuk barang (`bekas mobil`, `bekas tempat
rokok`) dan untuk orang yang tidak dihormati (`bekas pencuri`), sedangkan jabatan dan
profesi yang dihormati memakai `mantan`.

`[telaah]` Matcher hanya mengenali jabatan/profesi, bukan ranah "orang yang tidak
dihormati": buku menulis `bekas pencuri` dan `bekas perampok` sebagai pemakaian yang
dilazimkan, jadi keduanya **tidak** boleh ditandai. Karena itu, pemerluasan daftar pada
siklus ini terbatas pada kata jabatan yang jelas dihormati (`camat`, `lurah`, `hakim`,
`jaksa`, `sekretaris`, `duta`) dan tidak menyentuh `pencuri`/`perampok`.

---

## d. Pemakaian Kata Jam dan Pukul `[hlm. 77-78]`

> Kata jam selain menyatakan makna 'durasi atau jangka waktu', juga menyatakan makna
> 'arloji' atau 'alat penunjuk waktu', sedangkan kata pukul menyatakan 'waktu atau saat'.
> Dengan demikian, jika yang ingin diungkapkan adalah 'waktu', kata yang harus digunakan
> adalah pukul.

> (43) Mereka akan berangkat pada pukul 09.30. (44) Rapat itu akan diselenggarakan pada
> pukul 10.00.

> (45) Para pekerja di Indonesia rata-rata bekerja selama delapan jam sehari.

**Kaidah aktif:** `BPK-007`. Subbab ini mengulang aturan yang sama dengan Mustakim (2016,
hlm. 67) dan entri `BPK-007` (Mustakim 2019, hlm. 78); siklus ini hanya menambah pola label
`Jam: 09.00` pada regex yang sudah ada.

`[telaah]` `jam tangan` dan `selama delapan jam` sengaja tetap lolos: keduanya makna sah
menurut buku ini (arloji dan durasi).

---

## e. Pemakaian Kata Dari dan Daripada `[hlm. 78-80]`

> Kata dari lazimnya digunakan untuk menyatakan makna 'asal', baik 'asal tempat' maupun
> 'asal bahan'.

> (46) Mereka baru pulang dari Yogyakarta. (47) Meja ini terbuat dari marmer.

> Berbeda dengan kata dari, kata daripada hanya digunakan untuk menyatakan perbandingan,
> seperti yang dapat diperhatikan pada contoh berikut.

> (48) Ali lebih pandai daripada Temon. (49) Gunung Himalaya lebih tinggi daripada Gunung
> Kelud.

> (50) Kota Jakarta lebih besar dari kota Bandung. (?) (51) New York lebih jauh dari
> London. (?)

> Penggunaan kata dari sebagai pengganti daripada seperti pada contoh tersebut tentu tidak
> tepat karena, baik fungsi maupun maknanya, kedua kata itu berbeda.

> (52) Disiplin kerja merupakan pangkal daripada produktivitas.
> (53) Seluruh biaya daripada pembangunan masjid itu ditanggung oleh masyarakat.

> (52a) Disiplin kerja merupakan pangkal produktivitas. (53a) Seluruh biaya pembangunan
> masjid itu ditanggung (oleh) masyarakat.

**Kaidah baru:** `TMS-029` - adjektiva pembanding (`lebih`/`kurang` + adjektiva) diikuti
`dari`. Kalimat (50) dan (51) adalah pasangan salah-benar yang dipakai sebagai
`contoh_salah` dan `contoh_benar` entri ini; tanda `(?)` pada buku dibaca sebagai penanda
ketidaktepatan.

**Kaidah lama yang diperluas:** `BPK-006` (makna `daripada` untuk asal/sumber/penjelasan,
bukan perbandingan). Regex lama hanya mencakup `terbuat daripada`, `tujuan daripada`, dan
`maksud daripada`; siklus ini menambahkan `berasal`, `terbentuk`, dan `tersusun` karena
buku menegaskan `daripada` tidak pernah menyatakan asal.

`[telaah]` Kalimat (52) dan (53) - `daripada` yang mubazir pada `pangkal daripada ...` dan
`biaya daripada ...` - **belum dipola**. Keduanya hanya dapat dikenali dari konteks
leksikal (kata benda + `daripada` tanpa perbandingan), dan daftar kata bendanya terbuka;
memola `daripada` tanpa syarat akan menandai perbandingan yang benar.

---

## f. Pemakaian Kata Yaitu dan Yakni `[hlm. 80-81]`

> Dalam penggunaan bahasa Indonesia tidak jarang kata yaitu dan yakni penggunaannya
> dipertukarkan. Dalam posisi kata yaitu orang sering menggunakan kata yakni, begitu pula
> sebaliknya.

> (54) Logam yaitu suatu benda yang dapat memuai jika dipanaskan.

> Penggunaan kata yaitu pada kalimat (54) tidak tepat karena pada posisi kata itu yang
> diperlukan adalah kata yang berfungsi predikatif.

> Kata yaitu berfungsi untuk menerangkan. Oleh karena itu, penggunaannya yang tepat adalah
> pada akhir kalimat yang sudah lengkap dan perlu diberi keterangan. Misalnya:

> (55) Ada dua hal yang menyebabkan kenaikan harga kebutuhan pokok, yaitu persediaan yang
> semakin tipis dan kenaikan harga BBM.

> (56) Ada dua hal yang menyebabkan kenaikan harga kebutuhan pokok, yakni persediaan yang
> semakin tipis dan kenaikan harga BBM.

**Kaidah aktif:** `BPK-008` (predikat `'verba kopula predikat definisi'`). Pemerluasan
siklus ini menambah `benda` dan `alat` pada daftar nomina predikat, sehingga kalimat (54)
- contoh utama buku ini - ikut tertangkap.

`[telaah]` Kalimat (55) dan (56) benar dan harus tetap lolos: `yaitu`/`yakni` yang didahului
koma tidak ditandai oleh regex mana pun. Ini diuji eksplisit di `work/test_tms29.py`.

---

## g. Pemakaian Kata Adalah dan Ialah `[hlm. 81]`

> Kata yang memiliki fungsi predikatif adalah ialah atau adalah, bukan yaitu.

> (54a) Logam adalah suatu benda yang dapat memuai jika dipanaskan.
> (54b) Logam ialah suatu benda yang dapat memuai jika dipanaskan.

> Jika penggunaannya dicermatkan, kata adalah dan ialah juga berbeda dalam penggunaannya.
> Kata adalah digunakan untuk mendefinisikan, sedangkan ialah digunakan untuk menjelaskan.

**Kaidah aktif:** `BPK-010` sudah membedakan `adalah` (mendefinisikan) dan `ialah`
(menjelaskan); subbab ini tidak menambah kaidah baru, hanya menegaskan bahwa pasangan
perbaikan untuk `BPK-008` adalah `adalah`/`ialah`, bukan `merupakan`.

---

## h. Pemakaian Kata Antara Lain dan Misalnya `[hlm. 81-82]`

> Dalam posisi kata yakni dan yaitu, kata misalnya dan antara lain juga sering digunakan.
> Namun, kedua kata itu penggunaannya berbeda dengan kata yakni dan yaitu. Tempatnya memang
> sama, yaitu sesudah sebuah kalimat itu lengkap dan berfungsi untuk memberi keterangan.

> Kata yaitu dan yakni digunakan untuk menyebutkan seluruhnya, sedangkan kata misalnya dan
> antara lain digunakan untuk menyebutkan sebagian dari jumlah yang lebih banyak.

> (57) Banyak hal yang menyebabkan kenaikan harga kebutuhan pokok, antara lain persediaan
> barang yang semakin tipis dan kenaikan harga BBM.

> (58) Ada beberapa hal yang menyebabkan kenaikan harga kebutuhan pokok, misalnya
> persediaan barang yang semakin tipis dan kenaikan harga BBM.

`[telaah]` Belum dipola. Pembedaan "seluruhnya" (yaitu/yakni) versus "sebagian"
(misalnya/antara lain) menuntut pengetahuan tentang jumlah acuan pada kalimat sebelumnya,
sesuatu yang tidak dapat diputuskan dari satu kalimat. Menandainya akan menghasilkan
tuduhan yang tidak dapat dipertanggungjawabkan.

---

## Catatan proses: matcher ganda

Pada siklus ini sempat ditambahkan tiga blok matcher baru untuk `BPK-007`, `BPK-008`, dan
`BPK-009`. Ternyata ketiga kaidah itu **sudah punya matcher** (indeks 68-70 di
`CUSTOM_RULES`); blok lamanya tidak menyebut ID kaidah pada komentar, sehingga `grep` atas
ID tidak menemukannya. Karena `_find_custom_rule` memakai kecocokan pertama, blok baru
menjadi kode mati dan tidak pernah dieksekusi - terlihat dari `berasal daripada` yang tetap
tidak tertangkap walaupun regex baru memuat `berasal`.

Perbaikan: tiga blok duplikat dihapus, lalu regex **lama** yang diperluas. Jumlah aturan
kembali 310 (dari 313) setelah pembersihan. Pelajaran: verifikasi keberadaan matcher lewat
`[i for i,(pred,_) in enumerate(CUSTOM_RULES) if pred(pola)]`, bukan `grep` atas ID.
