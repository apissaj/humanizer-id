---
name: humanizer-id-sintaksis
description: Use when fixing sintaksis & kalimat efektif Indonesia.
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

# Humanizer ID — Sintaksis

Sub-kaidah Humanizer ID. Muat berkas ini setelah `humanizer-id` (induk) menentukan mode kerja. Aturan integritas ilmiah pada induk tetap mengikat penuh.

---

### H. Lima Ciri Kalimat Efektif (Rujukan Sasangka, 2019 dalam Buku Siswa Kelas XII Kemendikbudristek, 2024, hlm. 30)

1. **Lugas:** Hanya informasi penting yang disajikan; tanpa basa-basi pembuka klise (*"Dengan ini bermaksud memberitahukan bahwa..."*).
2. **Tepat:** Kalimat tidak multitafsir (*ambigu*); makna tunggal sesuai konteks penulisan.
3. **Jelas:** Struktur gramatikal baku; subjek dan predikat terbaca jelas (tidak diawali preposisi perusak subjek).
4. **Hemat:** Tidak boros kata; anti-pleonasme kopula ganda (*adalah merupakan*), pemangkasan verba ringan (*melakukan pemeriksaan* → *memeriksa*).
5. **Sejajar (Paralelisme):** Struktur paralel pada perincian; bentuk imbuhan seragam dalam satu deret (*mengumpulkan, menganalisis, menguji* — bukan *pengumpulan, menganalisis, uji*).

Aturan khusus surat resmi (Buku Siswa XII, hlm. 33): Konjungsi **guna** wajib diikuti verba aktif (*guna meningkatkan*), bukan nomina (*guna peningkatan*). Konjungsi **agar** tidak diikuti verba berimbuhan me- (*agar menjadikan* salah; gunakan *agar menjadi*).

### J. Kaidah Konjungsi Korelatif & Tata Bilangan (Rujukan TBBBI Edisi IV, Hasan Alwi dkk.)

1. **Perangkai Korelatif Baku:**
   - *antara A dan B* (bukan *antara A dengan B*)
   - *baik A maupun B* (bukan *baik A ataupun B*, bukan *baik A dan B*)
   - *bukan A, melainkan B* (pengontrasan kategori/nomina) vs *tidak A, tetapi B* (pengontrasan tindakan/verba)
   - *terdiri atas* (bukan *terdiri dari*, anjuran resmi Badan Bahasa)
   - *berdasarkan hasil* (bukan *berdasarkan pada hasil*)
2. **Larangan Bilangan Angka di Awal Kalimat:**
   - Angka arab tidak boleh berdiri di awal kalimat: *“25 responden mengisi angket...”* salah; susun ulang menjadi *“Sebanyak 25 responden mengisi angket...”* atau ditulis dengan huruf: *“Dua puluh lima responden...”*.
   - Bilangan yang dapat dinyatakan dalam satu atau dua kata ditulis dengan huruf (*“tiga kali pengulangan”*, bukan *“3 kali pengulangan”*), kecuali pada perincian teknis, tabel, atau data statistik.
3. **Pembuka Basa-Basi Kuno:**
   - Hapus kata *“adapun”* di awal kalimat (*“Adapun tujuan dari penelitian ini...”* → *“Penelitian ini bertujuan...”*).

---

### L. Enam Syarat Kalimat Efektif Akademik (Rujukan Suyatno dkk., *Bahasa Indonesia untuk Perguruan Tinggi*, UIN Syarif Hidayatullah Jakarta, Bab 11 hlm. 100–107)

1. **Kesatuan:** Satu kalimat satu ide pokok. Dilarang menggabungkan dua gagasan yang tidak berhubungan hierarkis dalam satu kalimat tunggal.
2. **Kepaduan (Koherensi):** Hubungan antarkata, frasa, klausa, dan tanda baca pada pola S-P-O-Pel-Ket harus padu dan tidak terpatahkan oleh preposisi sembarangan.
3. **Keparalelan (Kesejajaran):** Bentuk unsur rincian wajib sejenis dan seimbang. Jika unsur pertama nomina pe-an, semua unsur berikut wajib pe-an. Jika unsur pertama verba me-kan, semua wajib me-kan. Dilarang mencampur *pembelian buku, membuat katalog, dan buku-buku diberi label*.
4. **Ketepatan Diksi & Konjungsi:**
   - Larangan pasangan ganda *namun demikian*: pilih *walaupun demikian* atau *namun,*.
   - Pasangan kontrasti nomina: *bukan ... melainkan ...* (bukan *bukan ... namun/tetapi ...*).
   - Pasangan kontrasti verba/adjektiva: *tidak ... tetapi ...*.
5. **Kehematan:** Hilangkan kata-kata yang tidak menambah nilai informasi (pleonasme, verba ringan, copula ganda).
6. **Kelogisan:** Kalimat yang benar struktur dan ejaan tetap cacat bila maknanya lemah secara logika berpikir sistematis (*"Kambing sangat senang bermain hujan"* dan *"Karena lama tinggal di asrama putra, anaknya semua laki-laki"* → tidak logis).

Detail contoh salah → benar resmi dari buku tersedia di `references/buku-ajar-bahasa-indonesia-perguruan-tinggi.md`.

---

### M. Kaidah Kehematan, Superordinat, & Konjungsi Intrakalimat (Rujukan Modul Bahasa Indonesia Universitas Jambi, 2021)

1. **Larangan Konjungsi Intrakalimat di Awal Kalimat Mandiri:**
   - Konjungsi subordinatif intrakalimat (*sehingga, sedangkan, karena, agar, supaya*) **dilarang berdiri di awal kalimat tunggal**:
     - *Salah:* *“Model A sangat cepat. Sehingga kami memilihnya.”* → *Baku:* *“Model A sangat cepat sehingga dipilih sebagai arsitektur utama.”* atau gunakan konjungsi antarkalimat: *“Oleh karena itu, kami...”*.
     - *Salah:* *“Server A melayani transaksi. Sedangkan Server B mencatat log.”* → *Baku:* *“Server A melayani transaksi, sedangkan Server B mencatat log.”*.
2. **Larangan Predikat Didahului Kata "Yang" (Kalimat Buntung Tanpa Predikat):**
   - *Salah:* *“Bahasa Indonesia yang berasal dari bahasa Melayu.”* → *Baku:* *“Bahasa Indonesia berasal dari bahasa Melayu.”*. Kata *yang* mengubah predikat menjadi perluasan frasa subjek, menyebabkan kalimat kehilangan predikat gramatikal.
3. **Larangan Superordinat pada Hiponim (Kelebihan Kata Nama Kelas):**
   - Kata *merah* sudah mencakup konsep warna; kata *Selasa* sudah mencakup hari. Pangkas kata kelas yang mubazir:
     - *“memakai baju warna merah”* → *“memakai baju merah”*.
     - *“dilaksanakan pada hari Selasa”* → *“dilaksanakan pada Selasa”*.
4. **Larangan Kata Populer Salah Kaprah (*Terkini* vs *Mutakhir*):**
   - Dalam karya ilmiah, hindari kata populer media penyiaran *“teknologi terkini”* atau *“versi terkini”*. Secara semantis tidak ada yang "lebih kini dari kini". Gunakan istilah ilmiah baku: **“teknologi mutakhir”** atau **“versi terbaru”**.
5. **Larangan Penjamakan Ganda:**
   - Dilarang memadukan penanda jamak (*para, beberapa, semua*) dengan kata ulang reduplikasi:
     - *“para dosen-dosen”* → *“para dosen”* / *“dosen-dosen”*.
     - *“beberapa data-data”* → *“beberapa data”* / *“data-data”*.

---

### N. Padanan Tidak Serasi & Larangan Kontaminasi Kaidah (Rujukan Buku Bahasa Indonesia UIN Alauddin Makassar, 2021)

Kesalahan yang muncul karena dua kaidah bahasa berbeda bersilang dalam satu kalimat. Serangkaian pola yang dilarang keras:

1. **`karena ... sehingga`** (kontaminasi kausal): *“Karena modal terbatas sehingga tidak semua pengusaha memperoleh kredit.”* → *Baku:* *“Karena modal terbatas, tidak semua pengusaha memperoleh kredit.”*
2. **`disebabkan karena`** (kontaminasi pasif + konjungsi): verba pasif *disebabkan* wajib diikuti preposisi *oleh*, bukan konjungsi *karena*.
3. **`karena ... maka` / `untuk ... maka` / `kalau ... maka`**: cukup satu konjungsi saja. *“Karena latensi tinggi, maka sistem lambat.”* → *Baku:* *“Karena latensi tinggi, sistem lambat.”*
4. **`meskipun ... tetapi` / `walaupun ... namun`**: kontaminasi konsesif + pertentangan. *“Meskipun akurasi naik, tetapi biaya membengkak.”* → *Baku:* *“Meskipun akurasi naik, biaya membengkak.”*
5. **`dan lain sebagainya`**: pencampuradukan *dan lain-lain* (dll.) dan *dan sebagainya* (dsb.). Pilih salah satu sesuai konteks rincian.
6. **Peluluhan fonem /c/ yang salah**: fonem /c/ tidak luluh bila mendapat awalan *meN-*: *menyuci* → *mencuci*; *menyintai* → *mencintai*.
7. **Penyengauan ragam lisan dalam tulisan**: *nulis* → *menulis*; *nabrak* → *menabrak*; *nyari* → *mencari*; *ngantuk* → *mengantuk*; *nanam* → *menanam*; *nyubit* → *mencubit*.
8. **Penanggalan awalan `meng-` di teks ilmiah**: hanya diperbolehkan pada judul berita koran, bukan teks beritanya. *“Amerika Serikat luncurkan pesawat.”* → *Baku:* *“Amerika Serikat **meluncurkan** pesawat.”*

Kutipan: footnote nama pengarang tidak dibalik (berbeda dari daftar pustaka); halaman ditandai *h. 55–67* (bukan *hh. 55–67*); `et al.` boleh diganti *dkk.*

---

### S. Kata Ganti Impersonal & Verba Mental Ilmiah (Rujukan Modul Direktorat SMA Kemendikbud 2020, KD 3.14/3.15)

1. **Larangan Persona Non-Impersonal:**
   - Kata ganti persona pertama (*saya, kami*) dan kedua (*kamu, engkau*) dilarang keras dalam teks ilmiah.
   - Ganti dengan bentuk impersonal: *penulis, peneliti,* atau lebih disukai kalimat pasif ilmiah (*"Data dianalisis menggunakan..."*).
2. **Verba Mental Pasif Ilmiah:**
   - Gunakan pola: *diduga, dianalisis, dipahami, teridentifikasi, disimpulkan, diinterpretasikan*.
   - *Salah:* *"Kami berasumsi faktor X berpengaruh."* → *Baku:* *"Diduga faktor X berpengaruh."*
3. **Konsistensi Denotatif:**
   - Satu istilah satu makna sepanjang naskah (keajegan istilah). Jangan berganti-ganti padanan untuk istilah teknis yang sama.

---

### T. Lima Ciri Kalimat Efektif & Lima Rambu-rambu Paragraf (Rujukan Sasangka & Suladi, Seri Penyuluhan Badan Bahasa 2019)

1. **Kehematan — Ganda Jamak:**
   - Penanda jamak (*beberapa, berbagai, para, semua*) tidak boleh menemani reduplikasi jamak (*temuan-temuan, faktor-faktor*).
   - *Salah:* *"beberapa temuan-temuan penting"* → *Baku:* *"beberapa temuan penting"*.
2. **Kehematan — Redundansi Sinonim:**
   - *tersebut* dan *di atas* bermakna sama; pilih satu. *sebagaimana tersebut di atas* → *tersebut*.
3. **Kehematan — Duplikasi Subjek-Predikat:**
   - Hindari bentuk mirip subjek-predikat (*gaji karyawan... digaji*): ganti predikat (*dibayarkan*) atau ubah subjek.
4. **Kelugasan — Frasa Mubazir:**
   - Tanggalkan *mau tidak mau*, *itu sendiri*, *dapat dikatakan bahwa*.
5. **Kesejajaran — Paralelisme Klausa Majemuk:**
   - Konjungsi koordinatif (*dan, tetapi, atau*) wajib menghubungkan klausa sejajar (S-P dengan S-P; pasif dengan pasif).
   - Larangan keras: koordinatif menghubungkan klausa utama dengan klausa subordinatif (*..., tetapi karena..., ...*).
6. **Kesatuan & Kepaduan Paragraf (Suladi):**
   - Satu paragraf satu gagasan utama; gagasan menyimpang (digresi) dikeluarkan atau dipecah.
   - Antar kalimat wajib ada peranti kohesi (konjungsi, referensi, substitusi, elipsis, leksikal).
   - Dalam karya ilmiah, kalimat topik eksplisit (bukan tersirat).

---

### Y. Pemberantasan Residu Kata Penghubung Melayu 'dimana' & Ragam Objektif-Reproduktif (Rujukan Buku Siswa Kelas XI Kurikulum Merdeka Kemendikbudristek 2021)

1. **Larangan `dimana` sebagai Kata Penghubung:**
   - Dalam ragam ilmiah baku, `dimana` HANYA kata tanya tempat, bukan penghubung antarklausa.
   - *Salah:* *"Perjumpaan itu menarik dimana orang utan terlihat memanfaatkan jenis pohon yang sama."*
   - *Baku:* *"Perjumpaan itu menarik karena orang utan terlihat memanfaatkan jenis pohon yang sama."* / *"...menarik; orang utan terlihat memanfaatkan jenis pohon yang sama."*
   - Berlaku juga untuk `diketika`, `disewaktu`, `dibagaimana`.
2. **Sifat Objektif Karya Ilmiah:**
   - Pernyataan wajib didukung data empiris terukur, bukan opini atau perasaan penulis.
3. **Sifat Reproduktif Karya Ilmiah:**
   - Satu informasi harus dipahami identik oleh semua pembaca tanpa ruang interpretasi ganda.
4. **Denotasi vs Konotasi:**
   - Ragam ilmiah murni denotatif. Kata dengan tambahan rasa/emosi (konotatif: *duduk dengan manis*, *kuda hitam pertandingan*) dilarang.

---

### AA. Larangan Preposisi Mubazir pada Verba Transitif & Kalimat Buntung Preposisional (Rujukan Bahasa Indonesia untuk Aparatur Pemerintah, Pusat Bahasa Depdiknas)

1. **Larangan Preposisi 'tentang/mengenai' setelah Verba Transitif:**
   - Verba transitif (*membahas, membicarakan, mempelajari, meneliti, menguraikan, mengkaji*) langsung memerlukan objek penderita; dilarang disisipi preposisi.
   - *Salah:* *"Bab ketiga membahas tentang metode pengumpulan data."*
   - *Baku:* *"Bab ketiga membahas metode pengumpulan data."*
   - *Salah:* *"Laporan ini membicarakan mengenai dampak inflasi."*
   - *Baku:* *"Laporan ini membicarakan dampak inflasi."*
2. **Kalimat Tanpa Subjek akibat Preposisi Awal dengan Verba Aktif:**
   - Jika awal kalimat dibuka dengan frasa preposisional (*Dalam bab ini..., Pada penelitian ini...*), predikat WAJIB berupa kata kerja pasif (*dibahas, diteliti*), BUKAN kata kerja aktif (*membahas, meneliti*).
   - *Salah:* *"Dalam penelitian ini akan membahas efisiensi arsitektur Transformer."* (tidak punya subjek)
   - *Baku:* *"Dalam penelitian ini akan dibahas efisiensi arsitektur Transformer."* ATAU *"Penelitian ini membahas efisiensi arsitektur Transformer."*
3. **Kalimat Tanpa Predikat (Subjek + Keterangan):**
   - *Salah:* *"Pembangunan itu untuk menyejahterakan masyarakat."*
   - *Baku:* *"Pembangunan itu bertujuan menyejahterakan masyarakat."* ATAU *"Pembangunan itu dilakukan untuk menyejahterakan masyarakat."*

### AE. Korelatif, Keparalelan & Nalar Frasa (Rujukan Suyatno dkk., *Bahasa Indonesia untuk Perguruan Tinggi*, IN MEDIA, 2017)

1. **Korelatif Tidak Serasi:** pasangan baku tak boleh disilang — *tidak ... tetapi ...*; *bukan ... melainkan ...*; *antara ... dan ...*; *baik ... maupun ...* (hlm. 76).
2. **Keparalelan Perincian:** unsur se derajat wajib berpola sama — *meliputi pembelian buku, pembuatan katalog, dan pelabelan buku*; campuran nomina + verba me- + klausa pasif tidak efektif (hlm. 103).
3. **Salah Nalar Bebas Parkir:** pola *bebas X* bermakna 'tanpa X' (*bebas narkoba*); *bebas parkir* justru bermakna larangan parkir — yang tepat *parkir gratis / bebas biaya parkir* (hlm. 108).

### AG. Preposisi & Frase Berpreposisi (Rujukan S. Effendi & Buha Aritonang, *Preposisi dan Frase Berpreposisi*, Pusat Bahasa, 1992)

1. **Titik Waktu Baku *pada*:** *pada tahun 2020, pada hari Kamis, pada era digital* — bukan *di tahun, di hari, di era* (interferensi ragam lisan) (hlm. 49–50).
2. **Pleonasme Preposisi Majemuk:** *selain daripada X* mubazir karena *selain* sudah bermakna pengecualian — pakai *selain X / di samping X* (hlm. 21–22).
3. **Preposisi Ruang Terpisah:** *di dalam, ke dalam, di atas, ke atas, di bawah, di depan, di samping* — dua kata, bukan serangkai; serangkai hanya untuk *kepada* dan *daripada* (hlm. 21–22).

### AH. Struktur Kalimat & Konjungsi (Rujukan Sasangka, *Kalimat: Seri Penyuluhan Bahasa Indonesia*, Badan Bahasa, 2019)

1. **Konjungsi Syarat Mandiri:** *Jika/kalau/apabila A, B* — kata *maka* dilarang menyertai klausa utama karena membuat kalimat kehilangan induk (hlm. 80–81).
2. **Objek Verba Transitif Tanpa Preposisi:** *memerintahkan penyesuaian kepada X* atau *memerintah X untuk Y* — bukan *memerintahkan kepada X untuk Y* (preposisi merusak struktur S-P-O) (hlm. 78).
3. **Larangan Konjungsi Rangkap Tiga:** dilarang menumpuk *walaupun/meskipun + namun/tetapi + maka* dalam satu kalimat majemuk (hlm. 82–84).
4. **Pengutip Preposisional Merusak Subjek:** *Menurut pakar X menyatakan bahwa...* atau *Dengan perubahan zaman menuntut...* salah (K-P-O) — preposisi di depan mengubah subjek jadi keterangan; hapus preposisi atau pindah struktur (hlm. 28–29).
5. **Kalimat Tanpa Predikat Berakhir Preposisional:** subjek panjang yang ditutup *dengan berdasarkan pada...* belum menjadi kalimat utuh; wajib munculkan verba predikat utama (hlm. 33–35).
6. **Predikat Seakar Subjek peN-an (SPK-006):** Subjek berimbuhan peN-an tidak boleh berpredikat seakar (*Pemberian penghargaan dapat diberikan...* ditolak → *Pemberian penghargaan dapat berbentuk...* / *Penghargaan dapat diberikan...*; *Gaji...digaji* → *dibayarkan*) (hlm. 74–75).
7. **Penanda Jamak Reduplikasi Ganda (SPK-007):** Bentuk jamak tidak boleh digandakan: *beberapa temuan-temuan, para tamu-tamu* ditolak → pilih penanda jamak (*beberapa temuan*) atau reduplikasi (*temuan-temuan*) (hlm. 75).
8. **Sinonim Rangkap Penunjuk (SPK-008):** Frasa *sebagaimana tersebut di atas* adalah pemborosan sinonim rangkap → gunakan *tersebut* atau *di atas* (hlm. 74).
9. **Pembuka Partisipial Tanpa Konjungsi (SPK-009):** Pembuka klausa partisipial tanpa konjungsi (*Berbicara kepada media, dia mengatakan...*) menghilangkan penanda klausa subordinatif [telaah] (hlm. 82–83).

### AS. Sintaksis Hubungan Antarklausa & Pelesapan Konstituen (Rujukan Tata Bahasa Baku Bahasa Indonesia, Edisi Keempat, Bab X, hlm. 354–356)

1. **Pelesapan Subjek Asimetris (TBB-009):** Pelesapan subjek pada anak kalimat pembuka (*Setelah dibahas seharian, ...*) hanya sah bila subjeknya identik dengan induk kalimat; bila berbeda, hadirkan subjek eksplisit pada anak kalimat (*Setelah rancangan itu dibahas seharian, ...*) atau ubah induknya menjadi pasif.
2. **Posisi Objek Koordinatif (TBB-010):** Objek bersama dua verba transitif koordinatif wajib diletakkan setelah verba terakhir (*menguji atau menganalisis sampel itu*), bukan setelah verba pertama (*menguji sampel itu atau menganalisis*).
3. **Enklitik Posesif Sematan (TBB-011):** Partikel baku pada klausa sematan pemarkah *yang* adalah *-nya* sekalipun pemiliknya jamak (*para guru yang gajinya*), bukan pronomina bebas (*yang gaji mereka*) [telaah].

### AT. Pronomina Persona & Perbandingan Adjektiva Baku (Rujukan Tata Bahasa Baku Bahasa Indonesia Edisi Keempat, Bab V hlm. 199-201 & Bab VI hlm. 236-241)

1. **Pronomina 'Mereka' Insanik (TBB-012):* *Mereka* hanya mengacu insan; benda/konsep jamak tak bernyawa (*model, data, dokumen*) dirujuk dengan pengulangan nomina atau *semuanya* — menerjemahkan *they* mentah menjadi *mereka* adalah kalke.
2. **Batas 'Ia' Pascapreposisi (TBB-013):* *Ia* tidak berterima setelah preposisi (*kepada ia*); gunakan *dia* (*kepada dia*) atau enklitik *-nya* (*kepadanya*).
3. **Formula Ekuatif (TBB-014):* Perbandingan setara baku: *se- + adjektiva* (*secantik*) atau *sama [adj]-nya dengan* (*sama cantiknya dengan*); bentuk *sama ... seperti* adalah kontaminasi rancu.
4. **Superlatif Tunggal (TBB-015):* Derajat paling tinggi dinyatakan *ter-* atau *paling*, tidak boleh rangkap (*paling terbaik* -> *terbaik*).

### AU. Preposisi, Verba Semitransitif, dan Notasi Istilah (Rujukan TBBBI Edisi Keempat: Bab IV hlm. 140, Bab VIII hlm. 230-232, dan Lampiran II PUPI Bagian 5.8 hlm. 438-439)

1. **Preposisi Tunggal (TBB-016):* Penumpukan preposisi berfungsi sama (*guna untuk, bagi untuk, di dalam rangka untuk*) adalah pleonasme; pilih satu preposisi yang tepat menurut relasinya (*guna/untuk/bagi/dalam rangka*).
2. **Partitif 'Dari' (TBB-017):* Hubungan porsi atau kuantitas (*sebagian, separuh, 3 dari 5*) memakai *dari*, bukan *daripada*.
3. **Verba ke--an Tanpa Preposisi (TBB-018):* Verba semitransitif adversatif (*kejatuhan, kehabisan, kemasuan, kebanjiran*) langsung mengikat pelengkap nomina tanpa *oleh/akan/dengan*.
4. **Desimal Berawal Nol (PUPI-001):* Bilangan desimal wajib diawali angka (*0,05* atau *0.05*); notasi *....05* atau *,05* dilarang.

### AV. Kalimat Emfatik, Kesalingan, dan Lambang Bilangan (Rujukan TBBBI Edisi Keempat: Bab IX hlm. 316 & 328, dan Lampiran 1 EYD hlm. 416-418)

1. **Emfatik Satu 'Yang' (TBB-019):* Penegasan subjek cukup dengan '-lah' + satu kata 'yang' (*Dialah yang memulai...*); penggandaan *yang yang* menghasilkan struktur buntung.
2. **Kesalingan Tanpa 'Saling' Ganda (TBB-020):* Frasa *satu sama lain* sudah memuat resiprositas; *saling + [verba] + satu sama lain* adalah pleonasme ganda — gugurkan *saling*.
3. **Angka Pembuka Kalimat (EYD-020):* Lambang bilangan pada awal kalimat wajib dieja huruf (*Lima belas orang tewas*); susun ulang kalimat bila bilangan panjang.
4. **Bilangan '-an' Bertanda Hubung (EYD-021):* Puluhan/ratusan ditulis *tahun '50-an* atau *tahun lima puluhan*; bentuk serangkai *50an* tidak baku.
5. **Pecahan Konsisten (EYD-022):* Pecahan ditulis *1/2* atau dieja (*setengah*); format hibrida tak lazim ditolak [telaah].

### AX. Delimitasi Preposisi dan Frasa Berpreposisi (Rujukan Effendi & Aritonang, "Preposisi dan Frase Berpreposisi", Pusat Bahasa Depdikbud 1992)

1. **Sejak Pada (PFP-005):* Preposisi *sejak* telah menandai titik awal waktu secara mandiri; *sejak pada tahun 2015* adalah penumpukan preposisi ganda — gugurkan *pada*.
2. **Pasangan Antara (PFP-006):* Korelatif baku untuk *antara* adalah *dan* (*antara 100 dan 120 derajat*); *antara ... sampai/hingga/atau* tidak baku.
3. **Kalk 'Di Dalam Mana' (PFP-007):* Penghubung klausa relatif asing (*in which, wherein*) tidak diterjemahkan harfiah menjadi *di dalam mana*; gunakan *tempat, dengan, yang memuat*, atau strukturisasi ulang.
4. **Ingkar Ganda (PFP-008):* Preposisi *tanpa* telah bermakna peniadaan; *tanpa tidak mengurangi* merupakan kontradiksi ganda — gugurkan kata ingkar kedua.

### BO. Redundansi Sintaksis & Pleonasme Skripsi Mahasiswa (JSI UNNES & DE Journal)

1. **Redundansi Konjungsi Antarkalimat 'Selain itu juga' (JRN-001):** Frasa *Selain itu juga* menggabungkan konjungsi antarkalimat dan partikel aditif secara mubazir; gunakan *Selain itu,* secara lugas (DE Journal 2023, hlm. 546).
2. **Pleonasme Penanda Jamak Ganda Berverba (JRN-002):** Bentuk *banyak mengandung/memiliki/melibatkan* yang diikuti kata ulang (*banyak mengandung unsur-unsur*) adalah pleonasme penanda jamak bertingkat; gunakan *mengandung banyak unsur* atau *mengandung unsur-unsur* (JSI UNNES 2021, hlm. 7).

### BP. Korelatif Taktepat & Pleonasme Klise Skripsi Mahasiswa (Jurnal Genre UAD 2021)

1. **Pasangan Korelatif Takbaku 'baik ... ataupun' (JRN-003):** Konjungsi korelatif *baik* wajib berpasangan dengan *maupun* (*baik dosen maupun mahasiswa*), menolak pemakaian pasangan keliru *ataupun* atau *dan* (hlm. 100).
2. **Pleonasme Kualitatif Klise 'pertama dan utama' (JRN-004):** Kata *pertama* dan *utama* memiliki nilai semantik setara dalam menyatakan prioritas tertinggi; gunakan salah satu (*faktor utama*) secara lugas dan hemat (hlm. 99).

### BS. Konjungsi Koordinatif Awal Kalimat & Kontaminasi Kuantor (Jurnal JPLED Unimal 2024)

1. **Konjungsi Koordinatif 'Dan' di Awal Kalimat Baru (JRN-009):** Konjungsi *dan* adalah penghubung intrakalimat (antarklausa) sehingga tidak boleh mengawali kalimat mandiri baru; gabungkan dengan tanda koma ke kalimat sebelumnya atau gunakan konjungsi antarkalimat seperti *Selain itu,* (hlm. 807).
2. **Kontaminasi Kuantor 'sebagian banyak' (JRN-010):** Frasa *sebagian banyak* merupakan kontaminasi tidak baku yang mencampuradukkan partitif *sebagian besar* dan kuantor *banyak*; gunakan salah satu bentuk baku tersebut (hlm. 809).

### BT. Diksi, Pasangan Korelatif & Redundansi Sintaksis Skripsi (Jurnal Ar-Rumman, Lazuardi, ILEAL, Kande)

1. **Pleonasme Kuantitatif Leksikal 'jumlah rata-rata' (JRN-011):** Kata *rata-rata* (*mean*) secara inheren menyatakan nilai tengah agregat; penambahan kata *jumlah* (*sum*) sebelum *rata-rata* menimbulkan pleonasme kontaminatif. Cukup gunakan *rata-rata*, *rerata*, atau *jumlah* sesuai konteks (Ar-Rumman 2024, hlm. 548).
2. **Kontaminasi Korelatif 'hingga ... maupun' (JRN-012):** Preposisi batas rentang (*hingga/sampai*) tidak boleh dipadukan secara keliru dengan konjungsi koordinatif aditif *maupun*; gunakan pasangan korelatif baku *baik ... maupun ...* (Jurnal Lazuardi 2024, hlm. 58).
3. **Pleonasme Frasa Verba Bertujuan 'bertujuan untuk' (JRN-013):** Verba *bertujuan* sudah mengandung arti 'mempunyai tujuan' sehingga penambahan preposisi *untuk* lewah; pasangkan langsung verba tindakan (*bertujuan menganalisis*) atau gunakan *untuk* tanpa verba *bertujuan* (ILEAL 2018, hlm. 6).
4. **Pemenggalan Klausa Subordinatif 'Sehingga' Awal Kalimat (JRN-014):** Konjungsi subordinatif *sehingga* adalah penanda klausa akibat intrakalimat dan dilarang mengawali kalimat mandiri baru; gabungkan dengan tanda koma (*..., sehingga ...*) atau gunakan konjungsi antarkalimat (*Oleh karena itu,* / *Akibatnya,*) (Jurnal Kande 2021, hlm. 155).
