---
name: humanizer-id-ejaan-morfologi
description: Use when fixing ejaan, morfologi, dan bentuk baku Indonesia.
version: 2.4.3
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

1. **Pola:** *mempengaruhi / merubah / mensintesis / mentargetkan* → **Perbaikan:** *memengaruhi / mengubah / menyintesis / menargetkan* — **Sebab:** peluluhan KTSP pada prefiks *meN-*; gugus konsonan rangkap tetap (*menstabilkan, mentransmisikan, mempraktikkan*) (EYD V).
2. **Pola:** *pasca bencana / antar simpul / multi disiplin / sub bagian / non formal* → **Perbaikan:** *pascabencana, antarsimpul, multidisiplin, subbagian, nonformal* — **Sebab:** bentuk terikat ditulis serangkai.
3. **Pola:** *faktor2 / metode2* → **Perbaikan:** *faktor-faktor / metode-metode* — **Sebab:** reduplikasi wajib tanda hubung, angka 2 adalah gaya pesan instan; bila sudah diawali penanda jamak (*berbagai, beberapa*) hindari perulangan ganda (*berbagai faktor*, bukan *berbagai faktor-faktor*).
4. **Pola:** *BAPPENAS / TILANG* (akronim) → **Perbaikan:** *Bappenas / tilang* — **Sebab:** akronim nama diri > 3 huruf kapital di awal saja; akronim bukan nama diri ditulis kecil seluruhnya.
5. **Pola:** *S.T, M.T, Prof, Dr* → **Perbaikan:** *S.T., M.T., Prof., Dr.* — **Sebab:** singkatan gelar/sapaan diakhiri tanda titik.
6. **Pola:** *apapun / datainipun* → **Perbaikan:** *apa pun / data ini pun* — **Sebab:** partikel *pun* ditulis terpisah, kecuali 12 kata hubung baku leksikal (*meskipun, adapun, maupun, biarpun, walaupun*).
7. **Pola:** *Dalam penelitian ini menunjukkan...* → **Perbaikan:** *Penelitian ini menunjukkan...* / *Dalam penelitian ini ditunjukkan...* — **Sebab:** preposisi pembuka tidak boleh merusak subjek.
8. **Pola:** *analisa, praktek, resiko, standarisasi, efektifitas, metodologi* → **Perbaikan:** *analisis, praktik, risiko, standardisasi, efektivitas, metode* — **Sebab:** bentuk baku KBBI; *metode* untuk rangkaian kerja.
9. **Pola:** *menggaris bawahi / mempertanggung jawabkan* → **Perbaikan:** *menggarisbawahi / mempertanggungjawabkan* — **Sebab:** gabungan kata berkonfiks (awalan+akhiran) wajib serangkai.
10. **Pola:** *50cm / 240MHz* → **Perbaikan:** *50 cm / 240 MHz* — **Sebab:** satuan ukur dipisah spasi setelah angka.
11. **Pola:** *raja hutan* (untuk harimau) → **Perbaikan:** *harimau* — **Sebab:** karya ilmiah wajib makna denotatif, bukan konotatif/kiasan; kata ganti orang pertama menurunkan nilai rubrik resmi buku teks.

> **Rujukan buku teks resmi:** Kaidah di atas diekstrak dari buku *Cerdas Cergas Berbahasa dan Bersastra Indonesia untuk SMA/MA/SMK/MAK Kelas XI* (Edisi Revisi, Kemendikbudristek, 2024; ISBN 978-623-388-439-6), Bab VI hlm. 210–215. Detail contoh salah→benar lengkap tersedia di `references/ekstrak-buku-teks-kemdikbud.md`, dan empat entri baru (`BSE-001`–`BSE-004`) sudah aktif di `data/kalke-indonesia.json` serta terdeteksi oleh `scripts/audit.py`.

---
### I. Kata Tidak Baku dalam Surat Resmi (Teka-Teki Silang Buku Siswa XII, hlm. 33)

1. **Pola:** *ampun, mau, bales, gue, makasih, ngirim, bilang, ngak, pengen, soalnya* → **Perbaikan:** *maaf/tolong, menginginkan, membalas, saya/menurut saya, terima kasih, mengirim, menyatakan, tidak, ingin, karena* — **Sebab:** kata percakapan tidak baku wajib diganti padanan KBBI pada ragam formal.

---
### Q. Ketentuan Tanda Koma pada Konjungsi Intrakalimat & Antarkalimat (Rujukan Buku Kelas XII Kemendikbudristek 2024 & Alwi dkk. 2017)

1. **Pola:** *Model A sangat cepat tetapi membutuhkan memori besar* → **Perbaikan:** *Model A sangat cepat, tetapi membutuhkan memori besar.* — **Sebab:** konjungsi intrakalimat (*tetapi, namun, sedangkan, melainkan, bahkan, padahal, kecuali, kemudian, lalu, lantas*) wajib diawali koma.
2. **Pola:** *Akurasi naik, sehingga efisiensi meningkat / Sistem berhenti, karena kegagalan daya* → **Perbaikan:** *Akurasi naik sehingga efisiensi meningkat / Sistem berhenti karena kegagalan daya* — **Sebab:** konjungsi intrakalimat (*dan, atau, bahwa, karena, sehingga, agar, apabila, jika, maka*) ditulis tanpa koma pendahulu.
3. **Pola:** *Oleh karena itu / Selain itu / Dengan demikian* tanpa koma lanjutan → **Perbaikan:** *Oleh karena itu, / Selain itu, / Dengan demikian,* — **Sebab:** konjungsi antarkalimat selalu di awal kalimat baru, didahului titik dan diikuti koma.

---
### W. Kaidah Huruf Kapital Nama Jenis, Turunan Bangsa, & Jabatan Umum (Rujukan Modul Direktorat SMA Kemendikbud 2020, KD 3.12, hlm. 24–34)

1. **Pola:** *Kunci Inggris, Pisang Ambon, Mesin Diesel, 15 Watt* → **Perbaikan:** *kunci inggris, pisang ambon, mesin diesel, 15 watt* — **Sebab:** nama diri geografi/orang yang menjadi nama jenis atau satuan ukuran ditulis huruf kecil semua.
2. **Pola:** *Peng-Indonesia-an, Keinggris-Inggrisan* → **Perbaikan:** *pengindonesiaan, keinggris-inggrisan* — **Sebab:** bentuk dasar turunan nama bangsa/bahasa ditulis huruf kecil.
3. **Pola:** *Sejumlah Menteri menghadiri rapat Kabinet* → **Perbaikan:** *Sejumlah menteri menghadiri rapat kabinet* — **Sebab:** jabatan/pangkat tanpa nama spesifik ditulis kecil; kapital hanya bila merujuk spesifik (*Menteri Keuangan Republik Indonesia, Gubernur Jawa Barat*).
4. **Pola:** *Kapan bapak berangkat? / rumah Paman dan Bibi* → **Perbaikan:** *Kapan Bapak berangkat? / rumah paman dan bibi* — **Sebab:** sapaan langsung/pengacuan kapital; relasi keluarga umum ditulis kecil.
5. **Pola:** *republik indonesia / Perserikatan Bangsa Bangsa* → **Perbaikan:** *Republik Indonesia / Perserikatan Bangsa-Bangsa* — **Sebab:** nama resmi lembaga/dokumen kapital semua unsur kecuali kata tugas; bentuk ulang sempurna tetap bertanda hubung.
6. **Pola:** *Robin Van Persie* → **Perbaikan:** *Robin van Persie* — **Sebab:** partikel nama asing (Belanda/Jerman/Portugal/Jawa) ditulis huruf kecil.

---
### X. Kalimat Definisi (adalah vs merupakan) & Penulisan Imbuhan di- (Rujukan Buku Siswa Kelas X Edisi Revisi Kemendikbudristek 2022)

1. **Pola:** *Belalang anggrek adalah predator polifagus* → **Perbaikan:** *Belalang anggrek merupakan predator polifagus* — **Sebab:** *adalah* untuk pengertian mutlak (ekuivalensi A = B); *merupakan* untuk penempatan objek dalam kategori.
2. **Pola:** *di analisis, di observasi* → **Perbaikan:** *dianalisis, diobservasi, diteliti, dikembangkan* — **Sebab:** imbuhan pembentuk kata kerja pasif wajib serangkai.
3. **Pola:** *dilaboratorium, dimasa kini* → **Perbaikan:** *di laboratorium, di lapangan, di masa kini* — **Sebab:** preposisi penunjuk tempat/waktu wajib ditulis terpisah.
4. **Pola:** kutipan tidak langsung tanpa halaman → **Perbaikan:** *(Pengarang, tahun: halaman)* atau *Pengarang (tahun: halaman) menyatakan bahwa...* — **Sebab:** format CMS 17; sumber daring wajib frasa *diakses pada <tanggal>*.

---
### Z. Penulisan Gabungan Kata: Terpisah vs Senyawa & Unsur Terikat (Rujukan Seri Penyuluhan 1: Ejaan dalam Bahasa Indonesia, Pusat Bahasa Depdikbud)

1. **Pola:** *tanggungjawab, kerjasama, tandatangan, terimakasih, ujicoba, kantorpos, dutabesar, cagaralam, tatasurya* → **Perbaikan:** *tanggung jawab, kerja sama, tanda tangan, terima kasih, uji coba, kantor pos, duta besar, cagar alam, tata surya* — **Sebab:** gabungan kata yang masih bebas ditulis terpisah.
2. **Pola:** *dari pada, barang kali, pada hal, sekali gus, bila mana, apa bila, mata hari, sapu tangan, bumi putra, segi tiga* → **Perbaikan:** *daripada, barangkali, padahal, sekaligus, bilamana, apabila, matahari, saputangan, bumiputra, segitiga* — **Sebab:** gabungan kata senyawa ditulis serangkai.
3. **Pola:** *sub unit, maha guru, peri laku, antar kota* → **Perbaikan:** *subunit, mahaguru, perilaku, antarkota* — **Sebab:** unsur terikat + kata dasar ditulis serangkai.
4. **Pola:** *non RRC, antar SMA* → **Perbaikan:** *non-RRC, antar-SMA, pan-Afrikanisme* — **Sebab:** pengecualian: diikuti huruf kapital memakai tanda hubung; *maha/peri* + kata berimbuhan terpisah (*maha mengetahui*), + kata dasar serangkai (*mahakasih*).
5. **Pola:** *anak2 / ber-kejar2-an* → **Perbaikan:** *anak-anak / berkejar-kejaran* — **Sebab:** angka 2 dilarang sebagai penanda reduplikasi; tulis lengkap dengan tanda hubung.

---
### AW. Morfofonemik Verba & Klitika Pasif (Rujukan TBBBI Edisi Keempat, Bab IV hlm. 110-118 & Lampiran 1 hlm. 412)

1. **Pola:** *letakan, tunjukan, masukan* (verba) → **Perbaikan:** *letakkan, tunjukkan, masukkan* — **Sebab:** dasar berakhiran /k/ bersufiks *-kan* wajib /k/ ganda (TBB-021); bentuk satu *k* tercadang untuk nomina (*masukan*).
2. **Pola:** *mengisii, memperbaikii* → **Perbaikan:** *mengisi, memperbaiki* — **Sebab:** sufiks *-i* menolak dasar berakhir /i/; bentukan *ii* ganda tidak berterima (TBB-022).
3. **Pola:** *mengulang-i-ulangi* (sufiks ikut direduplikasi) → **Perbaikan:** *mengulang-ulangi / menyulit-nyulitkan* — **Sebab:** reduplikasi verba bersufiks: sufiks tidak ikut diulang; yang diulang bentuk dasar berafiks (TBB-023).
4. **Pola:** *ku kumpulkan / kau pelajari* → **Perbaikan:** *kukumpulkan, kaupelajari* — **Sebab:** klitika pasif *ku-*, *kau-* ditulis serangkai dengan verba (TBB-024).
5. **Pola:** *membom, mencek, mempel, mentik* → **Perbaikan:** *mengebom, mengecek, mengepel, mengetik* — **Sebab:** prefiks *meng-* pada dasar tunggal bersuku satu memerlukan e- (TBB-027) (hlm. 144).
6. **Pola:** *memroduksi, memroses, memrogram, mengredit, menglaim* → **Perbaikan:** *memproduksi, memproses, memprogram, mengkredit, mengklaim* — **Sebab:** gugus /pr/, /pl/, /kl/, /tr/, /kr/ tidak luluh (TBB-028) (hlm. 144).
7. **Pola:** *Tetapi, ...* (memulai kalimat) → **Perbaikan:** *Akan tetapi, ... / Namun, ...* — **Sebab:** konjungsi koordinatif *tetapi* dilarang memulai kalimat (TBB-029) (hlm. 417).
8. **Pola:** *amat sangat / sangat amat* → **Perbaikan:** pilih satu (*amat sangat* → *sangat* atau *amat*) — **Sebab:** penumpukan pewatas elatif: *amat, sangat, sekali* setara; gabungan dilarang ragam baku tulis (TBB-030) (hlm. 229).
9. **Pola:** *membicarakan tentang, membahas mengenai, mengetahui akan* → **Perbaikan:** *membicarakan, membahas, mengetahui* (langsung) — **Sebab:** verba transitif langsung mengikat objek tanpa preposisi pleonastis (TBB-031) (hlm. 129).

---

### AZ. Penyerapan Imbuhan Asing (Rujukan "Tata Istilah Indonesia", Pusat Pembinaan dan Pengembangan Bahasa, Subbab 7.7.1.2 hlm. 55-57)

1. **Pola:** *pointwise, piecewise, stepwise* → **Perbaikan:** *titik demi titik, cebis demi cebis, langkah demi langkah* — **Sebab:** akhiran distributif *-wise* diserap pola reduplikasi bersisipan *demi* (TII-006).
2. **Pola:** *harmonious, analogous* → **Perbaikan:** *berharmoni, beranalog* — **Sebab:** akhiran sifat *-ous* bermakna 'bersifat' diserap prefiks *ber-* (TII-007).
3. **Pola:** *addend, multiplicand* → **Perbaikan:** *bilangan yang ditambah, bilangan yang dikalikan* — **Sebab:** istilah matematika berakhiran *-and/-end* diserap konstruksi pasif penjelas (TII-008).
4. **Pola:** *absorber, analyzer, mixer* → **Perbaikan:** *penyerap/alat serap, penganalisis/alat analisis, pencampur* — **Sebab:** akhiran agen/instrumen *-er/-or* diserap prefiks *pe-* atau gabungan *alat* (TII-009).

---

### BD. Tanda Baca & Gabungan Kata Ejaan Baku (Rujukan "Seri Penyuluhan 1: Ejaan dalam Bahasa Indonesia", Pusat Bahasa Depdikbud, Bab III hlm. 10-12 & Bab IV hlm. 30-39)

1. **Pola:** *ia membatalkan rencana, karena...* → **Perbaikan:** *ia membatalkan rencana karena...* — **Sebab:** koma terlarang sebelum kausal/final bila anak kalimat mengiringi di belakang induk; koma hanya wajib bila anak kalimat mendahului induk (SPE-001).
2. **Pola:** *berterimakasih* → **Perbaikan:** *berterima kasih, bertanda tangan, bersepak bola, membabi buta* — **Sebab:** gabungan berawalan saja tetap terpisah tanpa tanda hubung (SPE-002).
3. **Pola:** *Namun / Bahkan / Kemudian / Lagi pula / Sebenarnya* tanpa koma → **Perbaikan:** *Namun, Bahkan, Kemudian, Lagi pula, Sebenarnya,* — **Sebab:** ungkapan penghubung di awal kalimat wajib diikuti koma (SPE-003).
4. **Pola:** dua klausa setara digabung koma tanpa konjungsi → **Perbaikan:** pisah dengan titik koma — **Sebab:** titik koma memisahkan klausa setara tanpa konjungsi koordinatif [telaah] (SPE-004).

---

### BE. Bentuk Terikat Maha, Kekerabatan Kapital, dan Reduplikasi Resmi (Rujukan "Seri Penyuluhan 9: Ejaan Bahasa Indonesia yang Disempurnakan", Pusat Bahasa Depdikbud, hlm. 34-36)

1. **Pola:** *maha siswa, maha kuasa* → **Perbaikan:** *mahasiswa, mahakuasa, mahaesa, mahaguru* — **Sebab:** unsur terikat *maha* serangkai bila diikuti kata dasar; terpisah hanya bila diikuti kata turunan (*maha mengetahui*); *maha siswa* tidak baku (EYD-023).
2. **Pola:** *buku kakak, surat ibu* (sebagai sapaan/milik) → **Perbaikan:** *buku Kakak, surat Ibu* — **Sebab:** kata kekerabatan kapital bila pronomina sapaan/kemilikan, membedakannya dari nomina umum [telaah] (EYD-024).
3. **Pola:** *orang2, anak2* → **Perbaikan:** *orang-orang, anak-anak* — **Sebab:** angka 2 dilarang untuk reduplikasi dalam naskah resmi (EYD-025).

---

### BF. Ejaan Serapan, Singkatan PT, dan Tanda Hubung Tanggal (Rujukan "Seri Penyuluhan: Ejaan", Sriyanto, Badan Bahasa, 2015, hlm. 14, 17, 50, 91)

1. **Pola:** *da'wah, do'a, taqwa, qalbu* → **Perbaikan:** *dakwah, doa, takwa, kalbu* — **Sebab:** tidak ada kata baku dengan apostrof di tengah; huruf q diganti k (SPE-005) (hlm. 14).
2. **Pola:** *wudhu, bathin, shalat, ashar, shubuh, ustadz, hadits, adzan, dhuha, bhakti, dharma* → **Perbaikan:** *wudu, batin, salat, asar, subuh, ustaz, hadis, azan, duha, bakti, darma* — **Sebab:** digraf baku hanya *kh, ng, ny, sy*; bentuk lain tidak baku; *bhakti/dharma* kecuali nama diri resmi (SPE-006) (hlm. 17).
3. **Pola:** *PT. X* → **Perbaikan:** *PT X* — **Sebab:** singkatan nama badan/lembaga tidak diikuti titik (SPE-007) (hlm. 50).
4. **Pola:** *12-September-2024* → **Perbaikan:** *12 September 2024* — **Sebab:** bila nama bulan dieja huruf, tanda hubung dilarang (SPE-008) (hlm. 91).

---

### BG. Kapitalisasi Turunan Nama Bangsa & Penyerapan Konsonan Ganda (Rujukan PUEBI 2021, SK Kepala Badan Bahasa No. 0321/I/BS.00.00/2021, hlm. 7 & 47)

1. **Pola:** *peng-Indonesia-an, ke-Barat-baratan* → **Perbaikan:** *pengindonesiaan, keinggris-inggrisan, kejawa-jawaan* — **Sebab:** nama bangsa/suku/bahasa sebagai bentuk dasar turunan ditulis kecil tanpa strip (PUE-001) (hlm. 7).
2. **Pola:** *aksesoris* → **Perbaikan:** *aksesori* — **Sebab:** *cc* diserap *ks*; akhiran jamak Belanda tidak diserap (PUE-002) (hlm. 47).
3. **Pola:** *kharisma, kharismatik* → **Perbaikan:** *karisma, karismatik, kolera, karakter* — **Sebab:** *ch* lafal /k/ diserap k tunggal (PUE-003) (hlm. 47).
4. **Pola:** *eschelon, esselon* → **Perbaikan:** *eselon, mesin* — **Sebab:** *ch* lafal /s/ diserap s (PUE-004) (hlm. 47).

---

### BK. Tanda Hubung Prefiks Ejaan Resmi (EYD Lengkap & PUEBI 2016)

1. **Pola:** *seIndonesia, seAsia* → **Perbaikan:** *se-Indonesia, se-Asia, se-Jawa* — **Sebab:** awalan *se-* + kata berawal kapital wajib tanda hubung, bukan serangkai polos (EYD-026) (EYD hlm. 61).
2. **Pola:** *ke2, ke10* → **Perbaikan:** *ke-2, ke-10, ke-100* — **Sebab:** awalan *ke-* + angka ordinal wajib tanda hubung, bukan disatukan polos (EYD-027) (EYD hlm. 61).

---

### BM. Ortografi Morfologis & Gabungan Kata (Seri Penyuluhan Bentuk dan Pilihan Kata 2019)

1. **Pola:** *menunjukan, ditunjukan, mengontrakan* → **Perbaikan:** *menunjukkan, ditunjukkan, mengontrakkan, dikontrakkan* — **Sebab:** dasar berakhiran /k/ + akhiran *-kan* wajib dua huruf /k/ (BPK-032) (hlm. 41).
2. **Pola:** *penunjukkan, pendidikkan* → **Perbaikan:** *penunjukan, pendidikan, kenaikan, kebaikan* — **Sebab:** hiperkoreksi: konfiks *peng-...-an* dan *ke-...-an* berakhiran *-an* (bukan *-kan*); dasar berakhiran /k/ tetap satu huruf /k/ (BPK-033) (hlm. 42).
3. **Pola:** *pertanggungan jawab / pertanggung jawaban* → **Perbaikan:** *pertanggungjawaban* — **Sebab:** gabungan kata dasar *tanggung jawab* diapit konfiks *per-...-an* wajib diserangkaikan penuh (BPK-034) (hlm. 43).

---

### BQ. Bentuk Pasif Morfologis Takbaku & Pleonasme Penggolong Skripsi (Jurnal BB & Retorika)

1. **Pola:** *dikarenakan* → **Perbaikan:** *disebabkan (oleh)* atau *karena* — **Sebab:** *karena* konjungsi subordinatif kausatif, tidak membentuk verba pasif (JRN-005) (Jurnal BB Unmuh Jember 2020, hlm. 58).
2. **Pola:** *112 orang siswa / 40 orang responden* → **Perbaikan:** *112 siswa / 40 responden* — **Sebab:** pleonasme penggolong insani: nomina bernyawa tidak perlu *orang* setelah kardinal dalam penulisan kuantitatif metodologi (JRN-006) (Jurnal Retorika Uniflor 2022, hlm. 56).

---

### BR. Tipografi Tanda Baca & Simbol Logografis Skripsi (Jurnal Jurribah 2026 / EBI Ed. V)

1. **Pola:** *ATP & WTP / tour & travel* → **Perbaikan:** tulis penuh *dan* — **Sebab:** simbol logografis *&* sebagai pengganti konjungsi dalam narasi ilmiah melanggar kaidah akademik (JRN-007) (hlm. 479).
2. **Pola:** *Variabel : data* → **Perbaikan:** *Variabel: data* — **Sebab:** titik dua tidak boleh didahului spasi; tanda baca melekat kata pendahulu (JRN-008) (hlm. 479).

---

### BU. EYD Edisi V (2022), Seri Penyuluhan (2025), & Tata Naskah Dinas (2025)

1. **Pola:** *tuna karya, nara sumber, manca negara, semi permanen, sub tema, multi etnik, dwi bahasa* → **Perbaikan:** *tunakarya, narasumber, mancanegara, semipermanen, subtema, multietnik, dwibahasa* — **Sebab:** bentuk terikat (*tuna-, nara-, manca-, semi-, sub-, multi-, dwi-*) ditulis serangkai (EYD-042..057).
2. **Pola:** *rumahtangga, pertanggung jawaban* → **Perbaikan:** *rumah tangga, rumah sakit, tata bahasa, tata cara* (terpisah); *pertanggungjawaban* (serangkai) — **Sebab:** gabungan kata bebas tanpa konfiks terpisah; berkonfiks penuh serangkai.
3. **Pola:** *garisbawahi, tandatangani, sebarluaskan, lipatgandakan, bebastugaskan, ujicobakan* → **Perbaikan:** *garis bawahi, tanda tangani, sebar luaskan, lipat gandakan, bebas tugaskan, uji cobakan* — **Sebab:** gabungan kata berimbuhan tunggal (awalan/akhiran saja) tetap terpisah (SPE-009..018, BPK-043..045, DIN-005).
4. **Pola:** *penandatangan, penanggungjawab, bekerjabakti* → **Perbaikan:** *penanda tangan, penanggung jawab, bekerja bakti, kami beri tahukan* — **Sebab:** sama — berimbuhan tunggal tetap terpisah; *waswas* tanpa tanda hubung, *dag-dig-dug* bertanda hubung.
5. **Pola:** *angkatan ke-XI* → **Perbaikan:** *angkatan XI* / *angkatan ke-11* — **Sebab:** hindari *ke-* + angka Romawi (SPE-011..012, DIN-006..007).
6. **Pola:** *S1, S2, D3* → **Perbaikan:** *S-1, S-2, S-3, D-3, D-4* — **Sebab:** jenjang wajib bertanda hubung.
7. **Pola:** *NIP. 198204...* → **Perbaikan:** *NIP 198204...* — **Sebab:** *NIP* tidak bertitik sebelum nomor; sedangkan *a.n.*, *Plt.*, *Plh.* wajib bertitik.
8. **Pola:** *mencabut, mencontoh* (bentuk lama) → **Perbaikan:** *mencabut, mencontoh, ditemukan, mengaktifkan, mengesampingkan, mengkritik, mengklasifikasi, berkaitan* — **Sebab:** bentuk baku yang disarankan (BPK-035..042, BPK-046, DIN-008..009, SPK-010..011).
9. **Pola:** *saling berpandangan* → **Perbaikan:** *berpandangan* — **Sebab:** hindari resiprokal *saling ber-...-an*.
10. **Pola:** *memberitahukan kepada ... bahwa / Bagi semua ... menyerahkan* → **Perbaikan:** buang kata hubung berlebih; *... menyerahkan* — **Sebab:** kalimat efektif: hindari *kepada ... bahwa* dan *Bagi ... menyerahkan*.
11. **Pola:** *walaupun/meskipun ..., namun ...* → **Perbaikan:** *walaupun/meskipun X, Y* — **Sebab:** hindari ganda konjungsi konsesif.
12. **Pola:** *disebabkan/dikarenakan terjadinya* → **Perbaikan:** *disebabkan oleh / karena* — **Sebab:** hindari *disebabkan/dikarenakan terjadinya* (tidak baku).

### BV2. Huruf Kapital Khusus EYD V (Rujukan EYD Edisi V, SK Kepala Badan Bahasa No. 0424/I/BS.00.01/2022, Bab I F — transkrip Wikisource)

1. **Pola:** *teori darwin / hukum archimedes / rumus pythagoras* → **Perbaikan:** *teori Darwin / hukum Archimedes / rumus Phytagoras* — **Sebab:** kapital pada nama orang dalam nama teori, hukum, dan rumus (Butir 4 Bab I F, hlm. 8; `EYD-058`).
2. **Pola:** *Fatimah Binti Salim / Charles Adriaan Van Ophuijsen* → **Perbaikan:** *Fatimah binti Salim / Charles Adriaan van Ophuijsen* — **Sebab:** kata bermakna "anak dari" (*bin, binti, boru, van*) nonkapital di tengah nama, kecuali di awal nama atau kata tugas *dari* (Butir 5 Bab I F, hlm. 8; `EYD-059`).
3. **Pola:** *Proklamasi kemerdekaan / Perang Dunia* (peristiwa sejarah generik) → **Perbaikan:** *proklamasi kemerdekaan / perang dunia* — **Sebab:** peristiwa sejarah yang tidak digunakan sebagai nama ditulis nonkapital (Butir 15 Bab I F, hlm. 11; `EYD-060`).
4. **Pola:** *batik cirebon / soto banjar / kopi gayo / bubur manado*
5. **Pola:** *buku bahasa dan sastra / majalah bahasa dan sastra*
6. **Pola:** kutipan langsung bahasa asing/daerah tanpa pencetakan miring → **Perbaikan:** cetak miring seluruh kutipan asing — **Sebab:** kalimat/teks asing yang dikutip langsung wajib miring (PUEBI 2015 Bab I hlm. 12; `EYD-063`).
7. **Pola:** *Michael Porter / World Bank* (nama diri asing) ditulis miring → **Perbaikan:** tulis tegak — **Sebab:** nama diri asing/daerah (orang, lembaga, organisasi) tidak ditulis miring (PUEBI 2015 Bab I hlm. 12; `EYD-064`). → **Perbaikan:** *buku Bahasa dan Sastra / majalah Bahasa dan Sastra* — **Sebab:** kapital semua kata (termasuk kata ulang sempurna) pada nama buku/majalah/surat kabar/judul karangan, kecuali kata tugas non-awal (EYD 1987 butir 12 Bab II; `EYD-062`). → **Perbaikan:** *batik Cirebon / soto Banjar / kopi Gayo / bubur Manado* — **Sebab:** nama geografi yang menyatakan asal daerah ditulis kapital (Butir 19 Bab I F, hlm. 12; `EYD-061`).

> **Sumber verbatim:** teks resmi EYD V tersedia via transkripsi Wikisource Indonesia (`Halaman:SK_EYD_Edisi_V_16082022.pdf`) — detail pemetaan di `references/eyd-v-wikisource-2022.md`. PUEBI (SK 0321/I/BS.00.00/2021) telah dicabut oleh EYD V (Diktum KEEMPAT).
