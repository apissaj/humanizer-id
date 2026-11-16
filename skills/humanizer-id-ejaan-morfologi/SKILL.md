---
name: humanizer-id-ejaan-morfologi
description: Use when fixing ejaan, morfologi, dan bentuk baku Indonesia.
version: 2.1.0
author: Hafizh Muzani / Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [writing, editing, bahasa-indonesia, akademik, nlp]
    category: creative
    homepage: https://github.com/apissaj/humanizer-id
    parent: humanizer-id
---

# Humanizer ID — Ejaan Morfologi

Sub-kaidah Humanizer ID. Muat berkas ini setelah `humanizer-id` (induk) menentukan mode kerja. Aturan integritas ilmiah pada induk tetap mengikat penuh.

---

### G. Kaidah Morfologi Baku (EYD V & TBBBI)
- **Peluluhan KTSP pada meN-:** *mempengaruhi* → **memengaruhi**; *merubah* → **mengubah**; *mensintesis* → **menyintesis**; *mentargetkan* → **menargetkan**. (Gugus konsonan rangkap tetap: *menstabilkan, mentransmisikan, mempraktikkan*).
- **Bentuk Terikat Ditulis Serangkai:** *pascabencana, antarsimpul, multidisiplin, subbagian, nonformal*.
- **Bentuk Ulang Wajib Tanda Hubung (Bukan Angka 2):** Tulis lengkap menggunakan tanda hubung (-), dilarang menggunakan angka 2 yang merupakan gaya pesan instan (*faktor-faktor* bukan *faktor2*; *metode-metode* bukan *metode2*). Bila sudah diawali kata penunjuk jamak (*berbagai, beberapa*), hindari perulangan ganda (*berbagai faktor*, bukan *berbagai faktor-faktor*).
- **Akronim & Singkatan Resmi:** Akronim nama diri yang terdiri atas lebih dari 3 huruf ditulis dengan huruf kapital di awal saja (*Bappenas*, *Kowani*, *Batan*). Akronim bukan nama diri ditulis dengan huruf kecil seluruhnya (*tilang*, *rudal*, *sonar*). Singkatan gelar atau sapaan diakhiri tanda titik (*S.T.*, *M.T.*, *Prof.*, *Dr.*).
- **Partikel *pun* Ditulis Terpisah:** *apa pun, data ini pun*, kecuali pada 12 kata hubung baku leksikal (*meskipun, adapun, maupun, biarpun, walaupun*).
- **Larangan Preposisi Perusak Subjek:** *“Dalam penelitian ini menunjukkan...”* salah; perbaiki menjadi *“Penelitian ini menunjukkan...”* atau pasif baku *“Dalam penelitian ini ditunjukkan...”*.
- **Bentuk Baku KBBI:** *analisis* (bukan analisa), *praktik* (bukan praktek), *risiko* (bukan resiko), *standardisasi* (bukan standarisasi), *efektivitas* (bukan efektifitas), *metode* untuk rangkaian kerja (bukan metodologi).
- **Konfiks Gabungan Kata Serangkai:** *menggarisbawahi* (bukan *menggaris bawahi*), *mempertanggungjawabkan* (bukan *mempertanggung jawabkan*). Gabungan kata yang mendapat awalan dan akhiran sekaligus wajib ditulis rapat.
- **Satuan Ukur Setelah Angka:** *50 cm* (bukan *50cm*), *240 MHz*, *5 kg*.
- **Makna Denotatif Karya Ilmiah:** Kata dipakai sesuai makna kamus (denotatif), bukan konotatif/kiasan (*raja hutan* untuk harimau termasuk gaya populer, bukan karya ilmiah). Rubrik resmi buku teks menurunkan nilai bila terdapat kata ganti orang pertama.

> **Rujukan buku teks resmi:** Kaidah di atas diekstrak dari buku *Cerdas Cergas Berbahasa dan Bersastra Indonesia untuk SMA/MA/SMK/MAK Kelas XI* (Edisi Revisi, Kemendikbudristek, 2024; ISBN 978-623-388-439-6), Bab VI hlm. 210–215. Detail contoh salah→benar lengkap tersedia di `references/ekstrak-buku-teks-kemdikbud.md`, dan empat entri baru (`BSE-001`–`BSE-004`) sudah aktif di `data/kalke-indonesia.json` serta terdeteksi oleh `scripts/audit.py`.

---

### I. Kata Tidak Baku dalam Surat Resmi (Teka-Teki Silang Buku Siswa XII, hlm. 33)

Dua belas kata percakapan tidak baku yang resmi diajarkan pembakuannya pada buku: *ampun, mau, bales, gue, makasih, ngirim, bilang, ngak, pengen, soalnya*. Gunakan padanan KBBI pada ragam formal (*maaf/tolong, menginginkan, membalas, saya/menurut saya, terima kasih, mengirim, menyatakan, tidak, ingin, karena*).

---

### Q. Ketentuan Tanda Koma pada Konjungsi Intrakalimat & Antarkalimat (Rujukan Buku Kelas XII Kemendikbudristek 2024 & Alwi dkk. 2017)

1. **Konjungsi Intrakalimat WAJIB Diawali Koma:**
   - *tetapi, namun, sedangkan, melainkan, bahkan, padahal, kecuali, kemudian, lalu, lantas*.
   - *Contoh:* *“Model A sangat cepat, tetapi membutuhkan memori besar.”* (koma sebelum *tetapi*).
   - *Contoh:* *“Model A dievaluasi pada dataset X, sedangkan Model B pada dataset Y.”* (koma sebelum *sedangkan*).
2. **Konjungsi Intrakalimat TANPA Tanda Koma:**
   - *dan, atau, bahwa, karena, sehingga, agar, apabila, jika, maka*.
   - *Salah:* *“Akurasi naik, sehingga efisiensi meningkat.”* → *Baku:* *“Akurasi naik sehingga efisiensi meningkat.”* (tanpa koma sebelum *sehingga*).
   - *Salah:* *“Sistem berhenti, karena kegagalan daya.”* → *Baku:* *“Sistem berhenti karena kegagalan daya.”* (tanpa koma sebelum *karena*).
3. **Konjungsi Antarkalimat WAJIB Diikuti Koma:**
   - *Oleh karena itu,, Selain itu,, Dengan demikian,, Di samping itu,, Sementara itu,, Selanjutnya,, Pada dasarnya,* dll.
   - Posisi selalu di awal kalimat baru (didahului titik, diikuti koma).

---

### W. Kaidah Huruf Kapital Nama Jenis, Turunan Bangsa, & Jabatan Umum (Rujukan Modul Direktorat SMA Kemendikbud 2020, KD 3.12, hlm. 24–34)

1. **Nama Jenis dari Nama Diri:**
   - Nama diri geografi/orang yang menjadi nama jenis atau satuan ukuran ditulis huruf kecil semua.
   - *Salah:* *Kunci Inggris, Pisang Ambon, Mesin Diesel, 15 Watt*
   - *Baku:* *kunci inggris, pisang ambon, mesin diesel, 15 watt*
2. **Bentuk Dasar Turunan Nama Bangsa/Bahasa:**
   - *Salah:* *Peng-Indonesia-an, Keinggris-Inggrisan*
   - *Baku:* *pengindonesiaan, keinggris-inggrisan* (huruf kecil)
3. **Jabatan/Pangkat Tanpa Nama Spesifik:**
   - *Salah:* *"Sejumlah Menteri menghadiri rapat Kabinet."*
   - *Baku:* *"Sejumlah menteri menghadiri rapat kabinet."*
   - Kapital hanya bila merujuk spesifik: *Menteri Keuangan Republik Indonesia, Gubernur Jawa Barat*.
4. **Kekerabatan Sapaan vs Relasi Umum:**
   - Sapaan langsung/pengacuan → kapital: *"Kapan Bapak berangkat?"*, *Surat Saudara sudah saya terima*.
   - Relasi keluarga umum → kecil: *rumah paman dan bibi*.
5. **Nama Resmi Lembaga/Dokumen:**
   - Kapital semua unsur kecuali kata tugas (*Republik Indonesia, Badan Kesejahteraan Ibu dan Anak*).
   - Termasuk bentuk ulang sempurna: *Perserikatan Bangsa-Bangsa, Dasar-Dasar Ilmu Hukum*.
6. **Partikel Nama Asing:**
   - Huruf kecil untuk partikel Belanda/Jerman/Portugal/Jawa: *Robin van Persie* (van kecil).

---

### X. Kalimat Definisi (adalah vs merupakan) & Penulisan Imbuhan di- (Rujukan Buku Siswa Kelas X Edisi Revisi Kemendikbudristek 2022)

1. **Pembedaan Kalimat Definisi:**
   - Gunakan **`adalah`** untuk pengertian MUTLAK (ekuivalensi A = B): *"Laporan hasil observasi adalah teks yang mengungkapkan fakta-fakta lapangan."*
   - Gunakan **`merupakan`** untuk penempatan objek dalam KATEGORI (tidak mutlak, bisa memiliki satu pengertian atau lebih): *"Belalang anggrek merupakan predator polifagus."*
2. **Pemisahan vs Penyerangkaian `di`:**
   - Imbuhan pembentuk kata kerja pasif WAJIB ditulis **serangkai**: *dianalisis, diobservasi, diteliti, dikembangkan*.
   - Preposisi penunjuk tempat/waktu WAJIB ditulis **terpisah**: *di laboratorium, di lapangan, di masa kini*.
3. **Kutipan Tidak Langsung CMS 17:**
   - Format: `(Pengarang, tahun: halaman)` atau `Pengarang (tahun: halaman) menyatakan bahwa...`
   - Sumber daring wajib menyertakan frasa *diakses pada <tanggal>*.

---

### Z. Penulisan Gabungan Kata: Terpisah vs Senyawa & Unsur Terikat (Rujukan Seri Penyuluhan 1: Ejaan dalam Bahasa Indonesia, Pusat Bahasa Depdikbud)

1. **Gabungan Kata yang Masih Bebas — Tulis TERPISAH:**
   - *Salah:* *tanggungjawab, kerjasama, tandatangan, terimakasih, ujicoba, kantorpos, dutabesar, cagaralam, tatasurya*
   - *Baku:* *tanggung jawab, kerja sama, tanda tangan, terima kasih, uji coba, kantor pos, duta besar, cagar alam, tata surya*
2. **Gabungan Kata Senyawa — Tulis SERANGKAI:**
   - *Salah:* *dari pada, barang kali, pada hal, sekali gus, bila mana, apa bila, mata hari, sapu tangan, bumi putra, segi tiga*
   - *Baku:* *daripada, barangkali, padahal, sekaligus, bilamana, apabila, matahari, saputangan, bumiputra, segitiga*
3. **Unsur Terikat + Kata Dasar — SERANGKAI:**
   - *Salah:* *sub unit, maha guru, peri laku, antar kota*
   - *Baku:* *subunit, mahaguru, perilaku, antarkota*
4. **Pengecualian:**
   - Diikuti huruf kapital $
ightarrow$ pakai tanda hubung: *non-RRC, antar-SMA, pan-Afrikanisme*.
   - *maha/peri* + kata berimbuhan $
ightarrow$ terpisah: *maha pengasih*; + kata dasar $
ightarrow$ serangkai: *mahakasih*.
5. **Larangan Angka 2 sebagai Penanda Reduplikasi:**
   - Tulis lengkap dengan tanda hubung: *anak-anak* (bukan *anak2*), *berkejar-kejaran* (bukan *ber-kejar2-an*).

---

### AW. Morfofonemik Verba & Klitika Pasif (Rujukan TBBBI Edisi Keempat, Bab IV hlm. 110-118 & Lampiran 1 hlm. 412)

1. **Konsonan /k/ Ganda (TBB-021):* Dasar berakhiran /k/ bersufiks *-kan* wajib *k* ganda (*letakkan, tunjukkan, masukkan*); bentuk satu *k* tercadang untuk nomina (*masukan*).
2. **Sufiks -i Menolak Dasar Berakhir /i/ (TBB-022):* Bentukan kata berakhiran huruf *ii* ganda (*mengisii, memperbaikii*) tidak berterima; gugurkan sufiks (*mengisi, memperbaiki*).
3. **Reduplikasi Verba Bersufiks (TBB-023):* Sufiks tidak ikut direduplikasi; yang diulang adalah bentuk dasar berafiks (*menyulit-nyulitkan, mengulang-ulangi*).
4. **Klitika Pasif Serangkai (TBB-024):* *Ku-* dan *kau-* ditulis serangkai dengan verba (*kukumpulkan, kaupelajari*), bukan terpisah spasi (*ku kumpulkan*).
5. **Verba Dasar Tunggal b/p (TBB-027):** Prefiks meng- pada dasar tunggal bersuku satu memerlukan e-: *membom, mencek, mempel, mentik* ditolak → *mengebom, mengecek, mengepel, mengetik* (hlm. 144).
6. **Gugus Konsonan Non-Peluluhan (TBB-028):** Gugus /pr/, /pl/, /kl/, /tr/, /kr/ tidak luluh: *memroduksi, memroses, memrogram, mengredit, menglaim* ditolak → *memproduksi, memproses, memprogram, mengkredit, mengklaim* (hlm. 144).
7. **Tetapi di Awal Kalimat (TBB-029):** Konjungsi koordinatif *tetapi* dilarang memulai kalimat; gunakan *Akan tetapi,* atau *Namun,* (hlm. 417).
8. **Penumpukan Pewatas Elatif (TBB-030):** *amat*, *sangat*, dan *sekali* adalah tingkat elatif setara; gabungan *amat sangat* atau *sangat amat* dilarang dalam ragam baku tulis (hlm. 229).
9. **Verba Transitif + Preposisi Pleonastis (TBB-031):** Verba transitif (*membicarakan, membahas, mengetahui, menyebutkan, mengulas*) langsung mengikat objek tanpa *tentang/mengenai/akan* (hlm. 129).

### AZ. Penyerapan Imbuhan Asing (Rujukan "Tata Istilah Indonesia", Pusat Pembinaan dan Pengembangan Bahasa, Subbab 7.7.1.2 hlm. 55-57)

1. **Distributif -wise (TII-006):* Akhiran *-wise* diserap dengan pola reduplikasi bersisipan *demi* (*pointwise -> titik demi titik; piecewise -> cebis demi cebis; stepwise -> langkah demi langkah*).
2. **Sifat -ous (TII-007):* Akhiran *-ous* bermakna 'bersifat' diserap menjadi prefiks *ber-* (*harmonious -> berharmoni; analogous -> beranalog*).
3. **Penderita -and/-end (TII-008):* Istilah matematika berakhiran *-and/-end* diserap dengan konstruksi pasif penjelas (*addend -> bilangan yang ditambah; multiplicand -> bilangan yang dikalikan*).
4. **Pelaku/Alat -er/-or (TII-009):* Akhiran agen/instrumen *-er/-or* diserap menjadi prefiks *pe-* atau gabungan kata *alat* (*absorber -> penyerap/alat serap; analyzer -> penganalisis/alat analisis; mixer -> pencampur*).

### BD. Tanda Baca & Gabungan Kata Ejaan Baku (Rujukan "Seri Penyuluhan 1: Ejaan dalam Bahasa Indonesia", Pusat Bahasa Depdikbud, Bab III hlm. 10-12 & Bab IV hlm. 30-39)

1. **Koma Terlarang Sebelum Kausal/Final (SPE-001):* Jika anak kalimat mengiringi di belakang induk, tanda koma terlarang (*ia membatalkan rencana karena...*, bukan *, karena...*). Koma hanya wajib jika anak kalimat mendahului induk.
2. **Gabungan Berawalan Saja (SPE-002):* Gabungan kata yang hanya berawalan tetap ditulis terpisah tanpa tanda hubung (*berterima kasih, bertanda tangan, bersepak bola, membabi buta*); bukan serangkai (*berterimakasih*).
3. **Koma Pasca-Konjungsi Antarkalimat (SPE-003):* Ungkapan penghubung di awal kalimat (*Namun, Bahkan, Kemudian, Lagi pula, Sebenarnya*) wajib diikuti koma.
4. **Titik Koma Klausa Setara (SPE-004):* Tanda titik koma memisahkan klausa setara tanpa konjungsi koordinatif [telaah].

### BE. Bentuk Terikat Maha, Kekerabatan Kapital, dan Reduplikasi Resmi (Rujukan "Seri Penyuluhan 9: Ejaan Bahasa Indonesia yang Disempurnakan", Pusat Bahasa Depdikbud, hlm. 34-36)

1. **Unsur Terikat Maha Serangkai (EYD-023):* *Maha* ditulis serangkai jika diikuti kata dasar (*mahasiswa, mahakuasa, mahaesa, mahaguru*); ditulis terpisah hanya bila diikuti kata turunan (*maha mengetahui*). Bentuk terpisah *maha siswa* tidak baku.
2. **Kekerabatan Kapital Pronominal (EYD-024):* Kata kekerabatan (*Kakak, Ibu, Bapak*) berhuruf kapital jika berfungsi sebagai pronomina sapaan atau kemilikan (*buku Kakak, surat Ibu*) untuk membedakannya dari nomina umum [telaah].
3. **Reduplikasi Lengkap Naskah Resmi (EYD-025):* Pemakaian angka 2 untuk reduplikasi (*orang2, anak2*) dilarang dalam naskah resmi; tulis lengkap dengan tanda hubung (*orang-orang, anak-anak*).

### BF. Ejaan Serapan, Singkatan PT, dan Tanda Hubung Tanggal (Rujukan "Seri Penyuluhan: Ejaan", Sriyanto, Badan Bahasa, 2015, hlm. 14, 17, 50, 91)

1. **Apostrof & Huruf Q Serapan Arab (SPE-005):** Tidak ada kata baku dengan apostrof di tengah; huruf q diganti k: *da'wah, do'a, taqwa, qalbu* ditolak → *dakwah, doa, takwa, kalbu* (hlm. 14).
2. **Digraf Non-Baku Serapan (SPE-006):** Digraf baku hanya *kh, ng, ny, sy*; bentuk selain itu tidak baku: *wudhu* → *wudu*, *bathin* → *batin*, *shalat/sholat* → *salat*, *ashar* → *asar*, *shubuh* → *subuh*, *ustadz/ustadzah* → *ustaz/ustazah*, *hadits* → *hadis*, *adzan* → *azan*, *dhuha* → *duha*; *bhakti* → *bakti* dan *dharma* → *darma* kecuali bagian nama diri resmi (hlm. 17).
3. **Singkatan PT Tanpa Titik (SPE-007):** Singkatan nama badan/lembaga tidak diikuti titik: tulis *PT*, bukan *PT.* (hlm. 50).
4. **Tanggal dengan Nama Bulan (SPE-008):** Bila nama bulan dieja huruf, tanda hubung dilarang: *12-September-2024* ditolak → *12 September 2024* (hlm. 91).

### BG. Kapitalisasi Turunan Nama Bangsa & Penyerapan Konsonan Ganda (Rujukan PUEBI 2021, SK Kepala Badan Bahasa No. 0321/I/BS.00.00/2021, hlm. 7 & 47)

1. **Kapitalisasi Turunan Nama Bangsa (PUE-001):** Nama bangsa/suku/bahasa sebagai bentuk dasar kata turunan ditulis huruf kecil tanpa strip: *pengindonesiaan, keinggris-inggrisan, kejawa-jawaan* — bukan *peng-Indonesia-an* atau *ke-Barat-baratan* (hlm. 7).
2. **Serapan cc di Depan e/i (PUE-002):** *cc* diserap *ks*; akhiran jamak Belanda tidak diserap: *aksesori*, bukan *aksesoris* (hlm. 47).
3. **Serapan ch Lafal /k/ (PUE-003):** *ch* diserap k tunggal: *karisma, karismatik, kolera, karakter* — bukan *kharisma, kharismatik* (hlm. 47).
4. **Serapan ch Lafal /s/ (PUE-004):** *ch* diserap s: *eselon, mesin* — bukan *eschelon* atau *esselon* (hlm. 47).

### BK. Tanda Hubung Prefiks Ejaan Resmi (EYD Lengkap & PUEBI 2016)

1. **Prefiks se- Bertemu Huruf Kapital (EYD-026):** Awalan *se-* yang dirangkaikan dengan kata berhuruf awal kapital wajib memakai tanda hubung (*se-Indonesia, se-Asia, se-Jawa*), bukan diserangkai polos (*seIndonesia*) (EYD hlm. 61).
2. **Prefiks Ordinal ke- Bertemu Angka Arab (EYD-027):** Awalan *ke-* yang dirangkaikan dengan angka penunjuk ordinal wajib memakai tanda hubung (*ke-2, ke-10, ke-100*), bukan disatukan polos (*ke2, ke10*) (EYD hlm. 61).

### BM. Ortografi Morfologis & Gabungan Kata (Seri Penyuluhan Bentuk dan Pilihan Kata 2019)

1. **Geminasi Huruf K Akhiran -kan (BPK-032):** Kata dasar berakhiran fonem /k/ yang diberi akhiran *-kan* wajib ditulis dengan dua huruf /k/ (*menunjukkan, ditunjukkan, mengontrakkan, dikontrakkan*), bukan satu huruf (*menunjukan*) (hlm. 41).
2. **Hiperkoreksi Huruf K Ganda pada Konfiks -an (BPK-033):** Konfiks *peng-...-an* dan *ke-...-an* berakhiran *-an* (bukan *-kan*); kata dasar berakhiran /k/ tetap ditulis dengan satu huruf /k/ (*penunjukan, pendidikan, kenaikan, kebaikan*), bukan /kk/ (*penunjukkan*) (hlm. 42).
3. **Perserangkaian Terikat Utuh Konfiks Gabungan Kata (BPK-034):** Gabungan kata dasar *tanggung jawab* yang diapit konfiks *per-...-an* wajib diserangkaikan penuh menjadi *pertanggungjawaban*, bukan *pertanggungan jawab* atau *pertanggung jawaban* (hlm. 43).

### BQ. Bentuk Pasif Morfologis Takbaku & Pleonasme Penggolong Skripsi (Jurnal BB & Retorika)

1. **Bentuk Pasif Takbaku Konjungtif 'dikarenakan' (JRN-005):** Kata dasar *karena* adalah konjungsi subordinatif kausatif sehingga tidak membentuk verba pasif *dikarenakan*; gunakan bentuk verba sejati *disebabkan (oleh)* atau konjungsi lugas *karena* (Jurnal BB Unmuh Jember 2020, hlm. 58).
2. **Pleonasme Penggolong Insani Pascanumeral (JRN-006):** Pada penulisan kuantitatif metodologi penelitian, nomina bernyawa (*siswa, mahasiswa, responden, guru*) tidak memerlukan kata penggolong *orang* setelah bilangan kardinal (*112 orang siswa* -> *112 siswa*) untuk menjaga kelugasan naskah (Jurnal Retorika Uniflor 2022, hlm. 56).

### BR. Tipografi Tanda Baca & Simbol Logografis Skripsi (Jurnal Jurribah 2026 / EBI Ed. V)

1. **Simbol Ampersand '&' dalam Narasi Prosa (JRN-007):** Pemakaian simbol logografis *&* sebagai pengganti konjungsi *dan* dalam narasi ilmiah (*ATP & WTP*, *tour & travel*) melanggar kaidah penulisan akademik; tulis penuh sebagai kata *dan* (hlm. 479).
2. **Spasi Sebelum Tanda Titik Dua (JRN-008):** Tanda titik dua (:) tidak boleh didahului spasi (*Variabel : data* keliru); tanda baca harus melekat langsung pada kata yang mendahuluinya (*Variabel:* data) sesuai konvensi ortografi EBI (hlm. 479).

### BU. EYD Edisi V (2022), Seri Penyuluhan (2025), & Tata Naskah Dinas (2025)

1. **Bentuk Terikat & Gabungan Kata (EYD-042..057):** Bentuk terikat (`tuna-`, `nara-`, `manca-`, `semi-`, `sub-`, `multi-`, `dwi-`) ditulis serangkai (`tunakarya`, `narasumber`, `mancanegara`, `semipermanen`, `subtema`, `multietnik`, `dwibahasa`). Gabungan kata bebas tanpa konfiks ditulis terpisah (`rumah tangga`, `rumah sakit`, `tata bahasa`, `tata cara`); berkonfiks penuh serangkai (`pertanggungjawaban`).
2. **Gabungan Kata Berimbuhan Tunggal (SPE-009..018, BPK-043..045, DIN-005):** Gabungan kata dengan awalan atau akhiran saja tetap terpisah (`garis bawahi`, `tanda tangani`, `sebar luaskan`, `lipat gandakan`, `bebas tugaskan`, `uji cobakan`, `penanda tangan`, `penanggung jawab`, `bekerja bakti`, `kami beri tahukan`). `waswas` tanpa tanda hubung; `dag-dig-dug` bertanda hubung.
3. **Bilangan Tingkat, Jenjang, & Singkatan Dinas (SPE-011..012, DIN-006..007):** Hindari `ke-` + Romawi (`angkatan ke-XI` → `angkatan XI` / `angkatan ke-11`). Jenjang wajib bertanda hubung (`S-1`, `S-2`, `S-3`, `D-3`, `D-4`). `NIP` tidak bertitik sebelum nomor (`NIP 198204xxxxxxxxxxxx`); `a.n.`, `Plt.`, `Plh.` wajib bertitik.
4. **Morfologi, Resiprokal, & Kalimat Efektif (BPK-035..042, BPK-046, DIN-008..009, SPK-010..011):** Gunakan `mencabut`, `mencontoh`, `ditemukan`, `mengaktifkan`, `mengesampingkan`, `mengkritik`, `mengklasifikasi`, `berkaitan`. Hindari `saling ber-...-an` (`berpandangan`), `memberitahukan kepada ... bahwa`, `Bagi semua ... menyerahkan`, `walaupun/meskipun ..., namun ...`, dan `disebabkan/dikarenakan terjadinya`.
