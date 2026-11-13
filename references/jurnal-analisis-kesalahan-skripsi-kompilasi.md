# Kompilasi Analisis Kesalahan Berbahasa Skripsi & Karya Ilmiah Mahasiswa

> Kodifikasi empiris temuan kesalahan ragam ilmiah dari **5 studi empiris** draf skripsi, makalah, dan naskah abstrak mahasiswa (IAIN Syekh Nurjati Cirebon, Unimed, Unimal, UMB, UHN Pematangsiantar). Kaidah rujukan: TBBBI Ed. IV, PUEBI/EYD V, PUPI, Keraf (1991).
> **Format:** S = bentuk salah (verbatim mahasiswa), B = perbaikan baku, Sumber = jurnal & volume, Pola = regex pemicu. Kodifikasi `JSK-001` s.d. `JSK-047`.

## Jurnal Acuan

1. **DiSastra (2021):** Uswati & Mardikantoro. *Kesalahan Bahasa Ilmiah Skripsi (IAIN Cirebon)*. *DiSastra*, V.3 N.1, hlm. 57-70. DOI: 10.29300/disastra.v3i1.3456.
2. **DEIKTIS (2026):** Dalimunthe dkk. *Kesalahan Diksi Makalah Mhs. Biologi Unimed*. *DEIKTIS*, V.6 N.2, hlm. 2471-2477. ISSN: 2807-7504.
3. **JPLED (2026):** Ramadhan, Safriandi & Emilda. *Effective Sentences in Thesis of Sociology (Unimal)*. *JPLED*, V.6 N.1, hlm. 804-810. DOI: 10.58737/jpled.v6i1.733.
4. **KIBASP (2026):** Rosa, Mahdijaya, Yuniati & Suyuthi. *Kesalahan Abstrak Skripsi PBSDI UMB 2024*. *KIBASP*, V.9 N.2, hlm. 520-537. DOI: 10.31539/6gwka618.
5. **DE_JOURNAL (2023):** Tambunan & Simorangkir. *Kesalahan Sintaksis Skripsi Mahasiswa (UHN)*. *DE_JOURNAL*, V.4 N.2, hlm. 540-549. E-ISSN: 2722-7839.

---
## A. Pembentukan Kata & Morfologi

- **JSK-001 Verba tanpa afiks:** S: *…dimana dengan bahasa itu masyarakat bisa bekerja sama…* → B: **Dengan berbahasa, masyarakat bisa bekerja sama…** (DiSastra V.3 N.1 2021) `dimana`
- **JSK-002 Klitika antar- terpisah:** S: *…berinteraksi antar sesama dengan berlandaskan budaya…* → B: **…berinteraksi antarsesama dengan berlandaskan budaya…** (DiSastra V.3 N.1 2021) `antar sesama`
- **JSK-003 di vs di- tertukar dua arah:** S: *…didunia ini ada sangkut pautnya… Di peroleh hasil…; di terbitkan oleh Gramedia…; di gambarkan pengarang* → B: **…di dunia ini… Diperoleh hasil…; diterbitkan oleh Gramedia…; digambarkan pengarang** (DE_JOURNAL 2023 & KIBASP 2026) `didunia|Di peroleh|di terbitkan`
- **JSK-004 di+berbagai diserangkai:** S: *Perdebatan penggunaan kata tersebut diberbagai media termasuk media sosial.* → B: **…terdapat di berbagai media, termasuk media sosial.** (DiSastra V.3 N.1 2021) `diberbagai`
- **JSK-005 Akhiran -nya terpisah:** S: *Banyak nya tuturan… khusus nya lirik lagu tersebut…* → B: **Banyaknya tuturan… khususnya lirik lagu tersebut…** (KIBASP V.9 N.2 2026) `\bnya\b`
- **JSK-006 Salah eja konjungsi:** S: *penggunaan frasa "sehinnga" yang merupakan kesalahan ejaan dari "sehingga"…* → B: **sehingga** (DEIKTIS V.6 N.2 2026) `sehinnga`

## B. Diksi & Istilah Ragam Ilmiah

- **JSK-007 Modalitas spekulatif:** S: *penggunaan kata "mungkin" atau "sepertinya" dalam mendeskripsikan struktur akar atau batang…* → B: **menunjukkan / tergolong / teridentifikasi** (DEIKTIS V.6 N.2 2026) `mungkin|sepertinya`
- **JSK-008 Ragam cakap:** S: *…sebagai makhluk sosial pastinya manusia membutuhkan bantuan dari orang lain.* → B: **…karena sebagai makhluk sosial, manusia membutuhkan bantuan…** (DiSastra V.3 N.1 2021) `pastinya|tentunya`
- **JSK-009 Kata takbaku & kalke:** S: *Seorang public vigur tentu menjadi panutan bagi banyak orang…* → B: **Seorang public figure tentu menjadi anutan bagi banyak orang…** (DiSastra V.3 N.1 2021) `panutan|public vigur`
- **JSK-010 Istilah asing tanpa urgensi:** S: *Pengumpulan data dapat dilakukan dalam berbagai setting… penelitian kepustakaan Library Research* → B: **…dalam berbagai latar… penelitian kepustakaan.** (DE_JOURNAL V.4 N.2 2023) `setting|Library Research`
- **JSK-011 Kata tanya relasional:** S: *Industri adalah tempat di mana untuk memproduksi berbagai macam produk yang efisien dan aman…* → B: **Industri adalah tempat untuk memproduksi berbagai macam produk yang efisien dan aman…** (JPLED V.6 N.1 2026) `tempat di mana`
- **JSK-012 Preposisi pasca transitif:** S: *Film banyak sekali menyampaikan mengenai gambaran tentang refleksi pada dunia nyata.* → B: **Film banyak sekali menyampaikan gambaran tentang refleksi pada dunia nyata.** (DiSastra V.3 N.1 2021) `menyampaikan mengenai`
- **JSK-013 Diksi informal: berkaitan:** S: *…antara kata, sikap, dan tingkah laku penutur harus saling berkaitan atau mendukung…* → B: **…penutur harus sinkron dan saling mendukung.** (DiSastra V.3 N.1 2021) `saling berkaitan`
- **JSK-014 Korelatif takserasi:** S: *…supaya antara penutur dengan mitra tutur saling memahami bahasa yang mereka gunakan…* → B: **…supaya antara penutur dan mitra tutur saling memahami…** (DiSastra V.3 N.1 2021) `antara .* dengan`

## C. Pleonasme & Bentuk Lewah

- **JSK-015 Kopula ganda:** S: *Penelitian adalah merupakan suatu kegiatan ilmiah yang berkaitan dengan analisa…* → B: **Penelitian adalah suatu kegiatan ilmiah…** (JPLED 2026 & DEIKTIS 2026) `adalah merupakan`
- **JSK-016 Pleonasme daripada:** S: *tujuan daripada rekayasa ide ini adalah…* → B: **tujuan rekayasa ide ini adalah…** (DEIKTIS V.6 N.2 2026) `tujuan daripada`
- **JSK-017 Penjamakan pasca jamak:** S: *…proses dengan metode-metode yang dapat menghasilkan… Jenis-jenis pekerjaan ini…* → B: **…proses dengan metode yang dapat menghasilkan… Jenis pekerjaan ini…** (JPLED V.6 N.1 2026) `metode-metode|jenis-jenis`
- **JSK-018 Penjamakan pasca beberapa/para:** S: *Beberapa pendapat-pendapat para ahli di atas. Para perempuan-perempuan itu hanya terlihat duduk…* → B: **Beberapa pendapat para ahli… Para perempuan itu… tidak melakukan apa pun.** (DE_JOURNAL V.4 N.2 2023) `beberapa \w+-\w+|para \w+-\w+`
- **JSK-019 Resiprokal ganda:** S: *…peristiwa yang saling jalin-menjalin… unsur-unsur yang saling berkaitan satu dengan yang lain.* → B: **…peristiwa yang saling menjalin… unsur-unsur yang saling berkaitan.** (DE_JOURNAL V.4 N.2 2023) `saling \w+-men\w+`
- **JSK-020 Superlatif ganda:** S: *para koruptor sangat amat pintar untuk menutupi semua kebusukannya.* → B: **para koruptor sangat pintar untuk menutupi semua kebusukannya.** (DE_JOURNAL V.4 N.2 2023) `sangat amat`
- **JSK-021 Tumpukan konjungsi antarkalimat:** S: *Selain itu juga, adanya penelitian ini perlu dilakukan guna untuk memberikan pengetahuan…* → B: **Selain itu, penelitian ini perlu dilakukan guna memberikan pengetahuan…** (DiSastra V.3 N.1 2021) `Selain itu juga|guna untuk`
- **JSK-022 Tumpukan konjungsi klausa:** S: *Berharap agar ibunya tidak menangis agar untuk jangan tidak sakit hati…* → B: **Berharap ibunya tidak menangis agar tidak sakit hati…** (DE_JOURNAL V.4 N.2 2023) `agar untuk|agar agar`
- **JSK-023 Nominalisasi mubazir jalannya:** S: *…dapat digunakan dengan baik dan efisien untuk jalannya berkomunikasi…* → B: **…dapat digunakan dengan baik dan efisien untuk berkomunikasi…** (DiSastra V.3 N.1 2021) `jalannya ber`
- **JSK-024 Penentu diskrit abstrak:** S: *Dalam sebuah kehidupan bermasyarakat… suatu rangkaian tindak tutur… suatu anggota masyarakat…* → B: **Dalam kehidupan bermasyarakat… rangkaian tindak tutur… anggota masyarakat…** (DiSastra V.3 N.1 2021) `sebuah kehidupan|suatu (rangkaian|anggota)`

## D. Sintaksis Kalimat (Subjek, Predikat, Penalaran)

- **JSK-025 Tanpa subjek: Menurut X menyatakan:** S: *Menurut Wardaugh (dalam Atmaja, 2018:1) mengatakan bahwa bahasa dapat digunakan…* → B: **Wardaugh (dalam Atmaja, 2018:1) mengatakan bahwa bahasa dapat digunakan…** (DiSastra V.3 N.1 2021) `Menurut .* mengatakan`
- **JSK-026 Tanpa subjek: Pada penelitian menunjukkan:** S: *Pada penelitian sebelumnya menunjukkan bahwa mahasiswa seringkali menjalani berbagai jenis pekerjaan…* → B: **Penelitian sebelumnya menunjukkan bahwa mahasiswa sering menjalani berbagai jenis pekerjaan…** (JPLED V.6 N.1 2026) `Pada penelitian .* menunjukkan`
- **JSK-027 Tanpa subjek: tentu memerlukan:** S: *Dalam sebuah kehidupan bermasyarakat, tentu memerlukan adanya komunikasi.* → B: **Dalam kehidupan bermasyarakat, tentu diperlukan adanya komunikasi.** (DiSastra V.3 N.1 2021) `tentu memerlukan`
- **JSK-028 Tanpa subjek: Apabila… harus memakai:** S: *Apabila dalam situasi formal, seperti kuliah, seminar, dan pidato harus memakai bahasa yang resmi.* → B: **Apabila dalam situasi formal, seperti kuliah, seminar, dan pidato, harus dipakai bahasa resmi.** (DiSastra V.3 N.1 2021) `Apabila .* memakai`
- **JSK-029 Tanpa predikat: yaitu bukan kopula; Dan di awal:** S: *Dan perbedaan peneliti Dahuri dengan penelitian ini yaitu perbedaan pada lokasi penelitian…* → B: **Perbedaan peneliti Dahuri dengan penelitian ini ialah perbedaan pada lokasi penelitian…** (JPLED V.6 N.1 2026) `^Dan |yaitu perbedaan`
- **JSK-030 Kalimat buntung: Yang di…:** S: *Yang di desa Pemuteran, Kecamatan Gerokgak, Kabupaten Buleleng.* → B: **Desa Pemuteran terletak di Kecamatan Gerokgak, Kabupaten Buleleng.** (JPLED V.6 N.1 2026) `^Yang di `
- **JSK-031 Tanpa kopula: Bahasa suatu sistem:** S: *Bahasa suatu sistem simbol lisan yang bersifat arbitrer dipakai oleh suatu anggota masyarakat…* → B: **Bahasa merupakan sistem simbol lisan yang bersifat arbitrer.** (DiSastra V.3 N.1 2021) `Bahasa suatu sistem`
- **JSK-032 Subjek berganda: Penelitian ini peneliti:** S: *Penelitian ini peneliti dapat menemukan data yang sebenarnya melalui Novel "Hijau" karya Agnes Jessica.* → B: **Peneliti dapat menemukan data yang sebenarnya melalui novel "Hijau" karya Agnes Jessica.** (DE_JOURNAL V.4 N.2 2023) `Penelitian ini peneliti`
- **JSK-033 Subjek berganda + afiks keliru:** S: *Dalam penelitian ini penulis memilih metode… data penelitian di deskriptif kan melihat kenyataan…* → B: **Penelitian ini menggunakan metode… data penelitian dideskripsikan untuk melihat kenyataan…** (DE_JOURNAL V.4 N.2 2023) `di deskriptif kan`
- **JSK-034 Konjungsi antarklausa di awal kalimat:** S: *…fokus pada dampak… Sedangkan pada penelitian ini berfokus pada apa yang memotivasi…* → B: **…fokus pada dampak…, sedangkan pada penelitian ini berfokus pada apa yang memotivasi…** (JPLED V.6 N.1 2026) `^Sedangkan |^ sehingga `
- **JSK-035 Tanpa predikat beruntun:** S: *Sikap dan perilaku yang patuh dalam melaksanakan ajaran agama yang dianutnya toleransi terhadap…* → B: **…ajaran agama yang dianutnya adalah bertoleransi terhadap pelaksanaan ibadah…** (DE_JOURNAL V.4 N.2 2023) `yang dianutnya toleransi`
- **JSK-036 Ketidaklogisan: menduduki bos:** S: *Jika nelayan yang sudah menduduki bos atau pengepul hasil laut maka akan sangat cukup…* → B: **Nelayan yang sudah menjabat menjadi bos atau pengepul hasil laut maka…** (JPLED V.6 N.1 2026) `menduduki bos`
- **JSK-037 Ketidaklogisan: menggantungkan diri:** S: *…sebagian banyak masyarakat banyak menggantungkan diri kepada laut dan perhatian pemerintah desa.* → B: **…sebagian besar dari mereka sangat bergantung pada sumber daya laut serta perhatian pemerintah…** (JPLED V.6 N.1 2026) `menggantungkan diri`

## E. Ejaan PUEBI/EYD V, Typo & Teknis Penulisan

- **JSK-038 Kapital kata umum di tengah kalimat:** S: *Masalah Penelitian ini adalah… Dari Hasil penelitian dapat ditarik Kesimpulan…* → B: **Masalah penelitian ini adalah… Dari hasil penelitian dapat ditarik kesimpulan…** (KIBASP V.9 N.2 2026) `Masalah Penelitian|Dari Hasil`
- **JSK-039 Kapital kata tugas dalam judul:** S: *Kisah Yang Pilu Untuk Kita Yang Ragu; Bukan Aku Yang Dia Inginkan Karya Sari Fatul* → B: **Kisah yang Pilu untuk Kita yang Ragu; karya Sari Fatul** (KIBASP V.9 N.2 2026) `Kisah Yang|Karya Sari`
- **JSK-040 Huruf miring judul karya sastra:** S: *Persahabatan dalam Novel Eccedentesiast karya Itakrn* → B: **Persahabatan dalam novel *Eccedentesiast* karya Itakrn** (KIBASP V.9 N.2 2026) `Novel Eccedentesiast`
- **JSK-041 Koma sebelum dan pada perincian 3 unsur:** S: *…dengan akidah, syariah dan akhlak dalam novel…* → B: **…dengan akidah, syariah, dan akhlak dalam novel…** (KIBASP V.9 N.2 2026) `syariah dan akhlak`
- **JSK-042 Titik koma padahal titik dua: yaitu;:** S: *Teknik pengumpulan data yaitu; Teknik analisis data yaitu;* → B: **Teknik pengumpulan data yaitu: Teknik analisis data yaitu:** (KIBASP V.9 N.2 2026) `yaitu;`
- **JSK-043 Titik ganda & gelar tanpa titik:** S: *Karya Rakayasa.. Pembimbing: Loliek Kania Atmaja, M.Pd* → B: **Karya Rakayasa. Pembimbing: Loliek Kania Atmaja, M.Pd.** (KIBASP V.9 N.2 2026) `\.\.|M\.Pd(?!\.)`
- **JSK-044 Typo baku dasar: PENGENTAR/PENILAN/TERIMAKASIH:** S: *penulisan kata "PENGENTAR", "PENILAN", "TERIMAKASIH" pada makalah formal.* → B: **PENGANTAR, PENILAIAN, TERIMA KASIH** (DEIKTIS V.6 N.2 2026) `PENGENTAR|PENILAN|TERIMAKASIH`
- **JSK-045 Typo judul: GOOGLE FROM/PENDAHALUAN:** S: *penulisan "GOOGLE FROM" yang seharusnya "GOOGLE FORM" dan "PENDAHALUAN" untuk "PENDAHULUAN".* → B: **GOOGLE FORM, PENDAHULUAN** (DEIKTIS V.6 N.2 2026) `GOOGLE FROM|PENDAHALUAN`
- **JSK-046 Nomenklatur binomial dilanggar:** S: *"IPOMOEA BATATAS" kapital penuh; "BENGKOANG (Pachyrhizus erosus" tanpa tutup kurung* → B: ***Ipomoea batatas*; Bengkoang (*Pachyrhizus erosus*)** (DEIKTIS V.6 N.2 2026) `IPOMOEA BATATAS|BENGKOANG`
- **JSK-047 Penulisan pengutipan takbaku:** S: *Menurut (Mulyana 2005:21) menyatakan bahwa konteks ialah latar terjadinya suatu komunikasi* → B: **Mulyana (2005:21) menyatakan bahwa konteks ialah latar terjadinya suatu komunikasi.** (DiSastra V.3 N.1 2021) `Menurut \(`


## F. Rekapitulasi Kuantitatif Bukti Empiris

- **DE_JOURNAL V.4 N.2 (2023), hlm. 544-547** (40 skripsi UHN 2018): frasa 411 data (preposisi 134, mubazir 150, superlatif 29, jamak ganda 29, resiprokal 12, bahasa daerah 7, penyusunan 50); kalimat 1109 data (tanpa subjek **528**, tanpa predikat 65, buntung 44, subjek ganda 22, taklogis 28, sisipan P-O 6, ambigu 37, hilang konjungsi 21, konjungsi berlebih 41, takparalel 8, istilah asing **234**, kata tanya takperlu 75).
- **JPLED V.6 N.1 (2026), hlm. 810** (7 skripsi Sosiologi Unimal 2024): 140 kalimat salah (tanpa subjek 45, tanpa predikat 13, buntung 9, taksejajar 10, dipenggal 10, taklogis 5, takhemat 13).
- **KIBASP V.9 N.2 (2026), hlm. 524** (27 abstrak PBSDI UMB 2024): 130 kesalahan PUEBI (huruf 49, kata 42, tanda baca 39).
- **DiSastra (2021) & DEIKTIS (2026)**: dominan kalimat tanpa subjek, konjungsi intrakalimat di awal, pleonasme kopula, serta salah eja nomenklatur biologi & judul.

**Kutipan verbatim penguat:**
- (JPLED) "Kalimat (1) memiliki ketidaksejajaran pada bentuk kata *memberikan*. Bentuk kata pertama memiliki bentuk pasif (*dilakukan*), sehingga bentuk kata selanjutnya harus pasif."
- (DE_JOURNAL) "Cukup menggunakan satu penanda saja dalam sebuah kalimat untuk penanda jamak kata; tidak perlu menggunakan penanda jamak jika kata tersebut sudah diulang."
- (KIBASP) "Berdasarkan hasil analisis terhadap 27 abstrak skripsi mahasiswa, ditemukan sebanyak 130 data kesalahan berbahasa Indonesia yang mengacu pada kaidah PUEBI."
- (DiSastra) "Temuan terbanyak adalah kesalahan penyusunan kalimat dan penerapan ejaan."

## G. Pola Dominan pada Keluaran AI/LLM & Penerapan Koreksi

1. **Tanpa subjek:** *Menurut X menyatakan…*, *Pada penelitian ini menunjukkan…* — pasif palsu dari "According to X, it is stated…".
2. **Unsur mubazir:** *adalah merupakan*, *tujuan daripada*, *metode-metode*, *sangat amat*, *saling jalin-menjalin*.
3. **Preposisi taktepat:** *didunia*, *diberbagai*, *menyampaikan mengenai*, *antara X dengan Y*.
4. **Istilah asing tanpa padanan:** *setting*, *Library Research*.
5. **Konjungsi intrakalimat diawal:** *Dan*, *Sedangkan*, *Sehingga*, *Karena*.
6. **Konfusi di- vs di:** *didunia* ↔ *di terbitkan*.
7. **Modalitas spekulatif ragam ilmiah:** *mungkin*, *sepertinya*.

Penerapan: jalankan regex pada pola deteksi sebagai pemicu penandaan; bandingkan kalimat dengan kaidah `JSK-001` s.d. `JSK-047`; ejaan PUEBI/EYD V, struktur TBBBI IV, diksi Keraf (1991), istilah PUPI+KBBI, nomenklatur ICN/ICZN.
