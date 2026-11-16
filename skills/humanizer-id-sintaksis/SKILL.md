---
name: humanizer-id-sintaksis
description: Use when fixing sintaksis & kalimat efektif Indonesia.
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

# Humanizer ID — Sintaksis

Sub-kaidah Humanizer ID. Muat berkas ini setelah `humanizer-id` (induk) menentukan mode kerja. Aturan integritas ilmiah pada induk tetap mengikat penuh.

---

### H. Lima Ciri Kalimat Efektif (Rujukan Sasangka, 2019 dalam Buku Siswa Kelas XII Kemendikbudristek, 2024, hlm. 30)

1. **Pola:** *Dengan ini bermaksud memberitahukan bahwa...* (basa-basi pembuka klise) → **Perbaikan:** langsung ke informasi penting — **Sebab:** kalimat efektif lugas: hanya informasi penting yang disajikan.
2. **Pola:** kalimat multitafsir (*ambigu*) → **Perbaikan:** makna tunggal sesuai konteks penulisan — **Sebab:** kalimat efektif tepat.
3. **Pola:** *Dalam penelitian ini membahas...* (subjek tak terbaca) → **Perbaikan:** struktur gramatikal baku dengan subjek-predikat jelas — **Sebab:** kalimat efektif jelas; tidak diawali preposisi perusak subjek.
4. **Pola:** *adalah merupakan / melakukan pemeriksaan* → **Perbaikan:** *adalah* atau *merupakan* / *memeriksa* — **Sebab:** kalimat efektif hemat: tanpa kopula ganda dan verba ringan.
5. **Pola:** *pengumpulan, menganalisis, uji* dalam satu deret → **Perbaikan:** *mengumpulkan, menganalisis, menguji* — **Sebab:** kalimat efektif sejajar: bentuk imbuhan seragam dalam satu perincian.

Aturan khusus surat resmi (Buku Siswa XII, hlm. 33): Konjungsi **guna** wajib diikuti verba aktif (*guna meningkatkan*), bukan nomina (*guna peningkatan*). Konjungsi **agar** tidak diikuti verba berimbuhan me- (*agar menjadikan* salah; gunakan *agar menjadi*).

---

### J. Kaidah Konjungsi Korelatif & Tata Bilangan (Rujukan TBBBI Edisi IV, Hasan Alwi dkk.)

1. **Pola:** *antara A dengan B / baik A ataupun B / baik A dan B* → **Perbaikan:** *antara A dan B / baik A maupun B* — **Sebab:** perangkai korelatif baku tak boleh dicampur; *bukan A, melainkan B* untuk kontras nomina, *tidak A, tetapi B* untuk kontras verba.
2. **Pola:** *terdiri dari / berdasarkan pada hasil* → **Perbaikan:** *terdiri atas / berdasarkan hasil* — **Sebab:** anjuran resmi Badan Bahasa; preposisi rangkap mubazir.
3. **Pola:** *25 responden mengisi angket...* (angka di awal kalimat) → **Perbaikan:** *Sebanyak 25 responden mengisi angket...* atau *Dua puluh lima responden...* — **Sebab:** angka arab tak boleh berdiri di awal kalimat; bilangan satu-dua kata ditulis huruf (*tiga kali pengulangan*), kecuali perincian teknis/tabel/statistik.
4. **Pola:** *Adapun tujuan dari penelitian ini...* → **Perbaikan:** *Penelitian ini bertujuan...* — **Sebab:** pembuka basa-basi kuno *adapun* dihapus.

---

### L. Enam Syarat Kalimat Efektif Akademik (Rujukan Suyatno dkk., *Bahasa Indonesia untuk Pergururuan Tinggi*, UIN Syarif Hidayatullah Jakarta, Bab 11 hlm. 100–107)

1. **Pola:** dua gagasan tak berhubungan hierarkis dalam satu kalimat → **Perbaikan:** pecah menjadi dua kalimat — **Sebab:** kesatuan: satu kalimat satu ide pokok.
2. **Pola:** klausa terpatahkan preposisi sembarangan → **Perbaikan:** jaga hubungan antarkata/frasa/klausa/tanda baca pada pola S-P-O-Pel-Ket — **Sebab:** kepaduan (koherensi).
3. **Pola:** *pembelian buku, membuat katalog, dan buku-buku diberi label* → **Perbaikan:** *pembelian buku, pembuatan katalog, dan pelabelan buku* — **Sebab:** keparalelan: unsur rincian wajib sejenis; jika unsur pertama nomina pe-an semua wajib pe-an; jika verba me-kan semua wajib me-kan.
4. **Pola:** *namun demikian / bukan ... namun ...* → **Perbaikan:** *walaupun demikian* atau *namun,* / *bukan ... melainkan ...* (nomina) — **Sebab:** ketepatan diksi & konjungsi: pasangan ganda dilarang; kontras verba/adjektiva memakai *tidak ... tetapi ...*.
5. **Pola:** pleonasme, verba ringan, copula ganda → **Perbaikan:** pangkas kata tak menambah informasi — **Sebab:** kehematan.
6. **Pola:** *Kambing sangat senang bermain hujan* (struktur benar, makna lemah) → **Perbaikan:** kalimat yang logis secara berpikir sistematis — **Sebab:** kelogisan: kalimat benar struktur tetap cacat bila maknanya tidak logis.

Detail contoh salah → benar resmi dari buku tersedia di `references/buku-ajar-bahasa-indonesia-pergururuan-tinggi.md`.

---

### M. Kaidah Kehematan, Superordinat, & Konjungsi Intrakalimat (Rujukan Modul Bahasa Indonesia Universitas Jambi, 2021)

1. **Pola:** *Model A sangat cepat. Sehingga kami memilihnya. / Server A melayani transaksi. Sedangkan Server B mencatat log.* → **Perbaikan:** *Model A sangat cepat sehingga dipilih sebagai arsitektur utama.* / *Server A melayani transaksi, sedangkan Server B mencatat log.* — **Sebab:** konjungsi subordinatif intrakalimat (*sehingga, sedangkan, karena, agar, supaya*) dilarang berdiri di awal kalimat tunggal; ganti konjungsi antarkalimat (*Oleh karena itu,*) bila perlu.
2. **Pola:** *Bahasa Indonesia yang berasal dari bahasa Melayu.* → **Perbaikan:** *Bahasa Indonesia berasal dari bahasa Melayu.* — **Sebab:** predikat didahului *yang* berubah menjadi perluasan frasa subjek; kalimat buntung tanpa predikat.
3. **Pola:** *baju warna merah / pada hari Selasa* → **Perbaikan:** *baju merah / pada Selasa* — **Sebab:** superordinat pada hiponim mubazir: *merah* sudah mencakup warna, *Selasa* sudah mencakup hari.
4. **Pola:** *teknologi terkini / versi terkini* → **Perbaikan:** *teknologi mutakhir / versi terbaru* — **Sebab:** kata populer media penyiaran salah kaprah; secara semantis tak ada yang "lebih kini dari kini".
5. **Pola:** *para dosen-dosen / beberapa data-data* → **Perbaikan:** *para dosen / beberapa data* (atau *dosen-dosen / data-data*) — **Sebab:** penjamakan ganda dilarang: penanda jamak tak boleh menemani reduplikasi.

---

### N. Padanan Tidak Serasi & Larangan Kontaminasi Kaidah (Rujukan Buku Bahasa Indonesia UIN Alauddin Makassar, 2021)

1. **Pola:** *Karena modal terbatas sehingga tidak semua pengusaha memperoleh kredit.* → **Perbaikan:** *Karena modal terbatas, tidak semua pengusaha memperoleh kredit.* — **Sebab:** kontaminasi kausal *karena ... sehingga*: cukup satu konjungsi.
2. **Pola:** *disebabkan karena* → **Perbaikan:** *disebabkan oleh* — **Sebab:** verba pasif *disebabkan* wajib preposisi *oleh*, bukan konjungsi.
3. **Pola:** *Karena latensi tinggi, maka sistem lambat. / untuk ... maka / kalau ... maka* → **Perbaikan:** *Karena latensi tinggi, sistem lambat.* — **Sebab:** pasangan konjungsi ganda: cukup satu.
4. **Pola:** *Meskipun akurasi naik, tetapi biaya membengkak. / walaupun ... namun* → **Perbaikan:** *Meskipun akurasi naik, biaya membengkak.* — **Sebab:** kontaminasi konsesif + pertentangan.
5. **Pola:** *dan lain sebagainya* → **Perbaikan:** *dan lain-lain* (dll.) atau *dan sebagainya* (dsb.) — **Sebab:** pencampuradukan dua bentuk baku; pilih sesuai konteks rincian.
6. **Pola:** *menyuci, menyintai* (meN- + dasar /c/) → **Perbaikan:** *mencuci, mencintai* — **Sebab:** fonem /c/ tidak luluh bila mendapat awalan *meN-*.
7. **Pola:** *nulis, nabrak, nyari, ngantuk, nanam, nyubit* → **Perbaikan:** *menulis, menabrak, mencari, mengantuk, menanam, mencubit* — **Sebab:** penyengauan ragam lisan tidak sah dalam tulisan.
8. **Pola:** *Amerika Serikat luncurkan pesawat.* → **Perbaikan:** *Amerika Serikat meluncurkan pesawat.* — **Sebab:** penanggalan awalan *meng-* hanya boleh pada judul berita koran, bukan teks beritanya.

Kutipan: footnote nama pengarang tidak dibalik (berbeda dari daftar pustaka); halaman ditandai *h. 55–67* (bukan *hh. 55–67*); `et al.` boleh diganti *dkk.*

---


### S. Kata Ganti Impersonal & Verba Mental Ilmiah (Rujukan Modul Direktorat SMA Kemendikbud 2020, KD 3.14/3.15)

1. **Pola:** *saya, kami, kamu, engkau* dalam teks ilmiah → **Perbaikan:** *penulis, peneliti,* atau kalimat pasif ilmiah (*Data dianalisis menggunakan...*) — **Sebab:** kata ganti persona pertama/kedua dilarang keras; wajib impersonal.
2. **Pola:** *Kami berasumsi faktor X berpengaruh.* → **Perbaikan:** *Diduga faktor X berpengaruh.* — **Sebab:** verba mental pasif ilmiah: *diduga, dianalisis, dipahami, teridentifikasi, disimpulkan, diinterpretasikan*.
3. **Pola:** berganti-ganti padanan untuk istilah teknis sama → **Perbaikan:** satu istilah satu makna sepanjang naskah — **Sebab:** konsistensi denotatif (keajegan istilah).

---

### T. Lima Ciri Kalimat Efektif & Lima Rambu-rambu Paragraf (Rujukan Sasangka & Suladi, Seri Penyuluhan Badan Bahasa 2019)

1. **Pola:** *beberapa temuan-temuan penting* → **Perbaikan:** *beberapa temuan penting* — **Sebab:** ganda jamak: penanda jamak (*beberapa, berbagai, para, semua*) tak boleh menemani reduplikasi.
2. **Pola:** *sebagaimana tersebut di atas* → **Perbaikan:** *tersebut* — **Sebab:** redundansi sinonim: *tersebut* dan *di atas* bermakna sama; pilih satu.
3. **Pola:** *gaji karyawan... digaji* → **Perbaikan:** *dibayarkan* (ganti predikat) atau ubah subjek — **Sebab:** duplikasi subjek-predikat.
4. **Pola:** *mau tidak mau / itu sendiri / dapat dikatakan bahwa* → **Perbaikan:** tanggalkan — **Sebab:** frasa mubazir, kelugasan.
5. **Pola:** *..., tetapi karena..., ...* → **Perbaikan:** sejajarkan klausa (S-P dengan S-P; pasif dengan pasif) — **Sebab:** koordinatif (*dan, tetapi, atau*) wajib menghubungkan klausa sejajar; dilarang menghubungkan klausa utama dengan subordinatif.
6. **Pola:** paragraf berisi banyak gagasan / tanpa peranti kohesi / kalimat topik tersirat → **Perbaikan:** satu paragraf satu gagasan; antarkalimat pakai konjungsi/referensi/substitusi/elipsis/leksikal; kalimat topik eksplisit — **Sebab:** kesatuan & kepaduan paragraf (Suladi); gagasan menyimpang (digresi) dikeluarkan atau dipecah.

---

### Y. Pemberantasan Residu Kata Penghubung Melayu 'dimana' & Ragam Objektif-Reproduktif (Rujukan Buku Siswa Kelas XI Kurikulum Merdeka Kemendikbudristek 2021)

1. **Pola:** *Perjumpaan itu menarik dimana orang utan terlihat...* → **Perbaikan:** *Perjumpaan itu menarik karena orang utan terlihat...* / *...menarik; orang utan terlihat...* — **Sebab:** *dimana* hanya kata tanya tempat, bukan penghubung antarklausa; berlaku juga *diketika, disewaktu, dibagaimana*.
2. **Pola:** pernyataan tanpa data empiris → **Perbaikan:** dukung data terukur — **Sebab:** sifat objektif karya ilmiah, bukan opini/perasaan penulis.
3. **Pola:** informasi dengan ruang interpretasi ganda → **Perbaikan:** buat identik dipahami semua pembaca — **Sebab:** sifat reproduktif karya ilmiah.
4. **Pola:** *duduk dengan manis / kuda hitam pertandingan* (konotatif) → **Perbaikan:** diksi denotatif sesuai makna kamus — **Sebab:** ragam ilmiah murni denotatif; kata berasa/emosi dilarang.

---

### AA. Larangan Preposisi Mubazir pada Verba Transitif & Kalimat Buntung Preposisional (Rujukan Bahasa Indonesia untuk Aparatur Pemerintah, Pusat Bahasa Depdiknas)

1. **Pola:** *membahas tentang / membicarakan mengenai / mengkaji akan* → **Perbaikan:** *membahas / membicarakan / mengkaji* (langsung + objek) — **Sebab:** verba transitif (*membahas, membicarakan, mempelajari, meneliti, menguraikan*) langsung memerlukan objek penderita; preposisi disisip dilarang.
2. **Pola:** *Dalam penelitian ini akan membahas efisiensi arsitektur Transformer.* → **Perbaikan:** *Dalam penelitian ini akan dibahas efisiensi arsitektur Transformer.* atau *Penelitian ini membahas efisiensi arsitektur Transformer.* — **Sebab:** kalimat dibuka frasa preposisional wajib predikat pasif, bukan aktif; versi aktif kehilangan subjek.
3. **Pola:** *Pembangunan itu untuk menyejahterakan masyarakat.* → **Perbaikan:** *Pembangunan itu bertujuan menyejahterakan masyarakat.* atau *Pembangunan itu dilakukan untuk menyejahterakan masyarakat.* — **Sebab:** subjek + keterangan bukan kalimat; wajib ada predikat.

---

### AE. Korelatif, Keparalelan & Nalar Frasa (Rujukan Suyatno dkk., *Bahasa Indonesia untuk Perguruan Tinggi*, IN MEDIA, 2017)

1. **Pola:** korelatif disilang (*tidak ... melainkan, bukan ... tetapi*, dsb.) → **Perbaikan:** pasangan baku: *tidak ... tetapi ...; bukan ... melainkan ...; antara ... dan ...; baik ... maupun ...* — **Sebab:** korelatif tak serasi (hlm. 76).
2. **Pola:** *meliputi pembelian buku, membuat katalog, dan buku-buku diberi label* → **Perbaikan:** *meliputi pembelian buku, pembuatan katalog, dan pelabelan buku* — **Sebab:** keparalelan perincian: unsur se-derajat wajib berpola sama (hlm. 103).
3. **Pola:** *bebas parkir* (maksud: gratis) → **Perbaikan:** *parkir gratis / bebas biaya parkir* — **Sebab:** salah nalar: pola *bebas X* bermakna 'tanpa X' (*bebas narkoba*), jadi *bebas parkir* berarti larangan parkir (hlm. 108).

---

### AG. Preposisi & Frase Berpreposisi (Rujukan S. Effendi & Buha Aritonang, *Preposisi dan Frase Berpreposisi*, Pusat Bahasa, 1992)

1. **Pola:** *di tahun 2020, di hari Kamis, di era digital* → **Perbaikan:** *pada tahun 2020, pada hari Kamis, pada era digital* — **Sebab:** titik waktu baku memakai *pada*; *di* interferensi ragam lisan (hlm. 49-50).
2. **Pola:** *selain daripada X* → **Perbaikan:** *selain X / di samping X* — **Sebab:** pleonasme preposisi majemuk; *selain* sudah bermakna pengecualian (hlm. 21-22).
3. **Pola:** *didalam, kedalam, diatas, kedepan, disamping* → **Perbaikan:** *di dalam, ke dalam, di atas, ke atas, di bawah, di depan, di samping* — **Sebab:** preposisi ruang ditulis dua kata; serangkai hanya *kepada* dan *daripada* (hlm. 21-22).

---

### AH. Struktur Kalimat & Konjungsi (Rujukan Sasangka, *Kalimat: Seri Penyuluhan Bahasa Indonesia*, Badan Bahasa, 2019)

1. **Pola:** *Jika A, maka B.* → **Perbaikan:** *Jika/kalau/apabila A, B.* — **Sebab:** konjungsi syarat mandiri; *maka* membuat kalimat kehilangan induk (hlm. 80-81).
2. **Pola:** *memerintahkan kepada X untuk Y* → **Perbaikan:** *memerintahkan penyesuaian kepada X* atau *memerintah X untuk Y* — **Sebab:** objek verba transitif tak boleh disisipi preposisi yang merusak struktur S-P-O (hlm. 78).
3. **Pola:** *walaupun/meskipun + namun/tetapi + maka* dalam satu kalimat → **Perbaikan:** satu konjungsi saja — **Sebab:** larangan konjungsi rangkap tiga (hlm. 82-84).
4. **Pola:** *Menurut pakar X menyatakan bahwa... / Dengan perubahan zaman menuntut...* → **Perbaikan:** *Pakar X menyatakan bahwa... / Perubahan zaman menuntut...* — **Sebab:** pengutip preposisional merusak subjek: preposisi di depan mengubah subjek jadi keterangan (hlm. 28-29).
5. **Pola:** subjek panjang ditutup *dengan berdasarkan pada...* lalu berhenti → **Perbaikan:** munculkan verba predikat utama — **Sebab:** kalimat tanpa predikat berakhir preposisional belum utuh (hlm. 33-35).
6. **Pola:** *Pemberian penghargaan dapat diberikan... / Gaji... digaji* → **Perbaikan:** *Pemberian penghargaan dapat berbentuk... / Penghargaan dapat diberikan... / Gaji... dibayarkan* — **Sebab:** predikat tak boleh seakar subjek peN-an (SPK-006) (hlm. 74-75).
7. **Pola:** *beberapa temuan-temuan / para tamu-tamu* → **Perbaikan:** *beberapa temuan / para tamu* — **Sebab:** penanda jamak tak boleh digandakan dengan reduplikasi (SPK-007) (hlm. 75).
8. **Pola:** *sebagaimana tersebut di atas* → **Perbaikan:** *tersebut* atau *di atas* — **Sebab:** sinonim rangkap penunjuk mubazir (SPK-008) (hlm. 74).
9. **Pola:** *Berbicara kepada media, dia mengatakan...* → **Perbaikan:** beri konjungsi/penanda klausa atau susun ulang — **Sebab:** pembuka partisipial tanpa konjungsi menghilangkan penanda klausa subordinatif [telaah] (SPK-009) (hlm. 82-83).

---

### AS. Sintaksis Hubungan Antarklausa & Pelesapan Konstituen (Rujukan Tata Bahasa Baku Bahasa Indonesia, Edisi Keempat, Bab X, hlm. 354-356)

1. **Pola:** *Setelah dibahas seharian, ...* (subjek anak kalimat tak sama dengan induk) → **Perbaikan:** *Setelah rancangan itu dibahas seharian, ...* atau ubah induk jadi pasif — **Sebab:** pelesapan subjek asimetris (TBB-009): pelesapan hanya sah bila subjek identik dengan induk.
2. **Pola:** *menguji sampel itu atau menganalisis* → **Perbaikan:** *menguji atau menganalisis sampel itu* — **Sebab:** objek bersama dua verba transitif koordinatif wajib setelah verba terakhir (TBB-010).
3. **Pola:** *para guru yang gaji mereka* → **Perbaikan:** *para guru yang gajinya* — **Sebab:** enklitik posesif pada klausa sematan *yang* adalah *-nya* sekalipun pemilik jamak (TBB-011) [telaah].

---

### AT. Pronomina Persona & Perbandingan Adjektiva Baku (Rujukan TBBBI Edisi Keempat, Bab V hlm. 199-201 & Bab VI hlm. 236-241)

1. **Pola:** *mereka* untuk benda/konsep jamak (*model-model, data-data, dokumen-dokumen*) → **Perbaikan:** ulangi nomina atau *semuanya* — **Sebab:** *mereka* hanya mengacu insan (TBB-012); menerjemahkan *they* menjadi *mereka* adalah kalke.
2. **Pola:** *kepada ia* → **Perbaikan:** *kepada dia* / *kepadanya* — **Sebab:** *ia* tidak berterima setelah preposisi (TBB-013).
3. **Pola:** *sama ... seperti* → **Perbaikan:** *se- + adjektiva* (*secantik*) atau *sama [adj]-nya dengan* (*sama cantiknya dengan*) — **Sebab:** formula ekuatif baku; *sama ... seperti* kontaminasi rancu (TBB-014).
4. **Pola:** *paling terbaik* → **Perbaikan:** *terbaik* / *paling baik* — **Sebab:** superlatif tunggal: *ter-* atau *paling*, tidak boleh rangkap (TBB-015).

---

### AU. Preposisi, Verba Semitransitif, dan Notasi Istilah (Rujukan TBBBI Edisi Keempat: Bab IV hlm. 140, Bab VIII hlm. 230-232, dan Lampiran II PUPI Bagian 5.8 hlm. 438-439)

1. **Pola:** *guna untuk / bagi untuk / di dalam rangka untuk* → **Perbaikan:** pilih satu: *guna/untuk/bagi/dalam rangka* — **Sebab:** penumpukan preposisi berfungsi sama adalah pleonasme (TBB-016).
2. **Pola:** *sebagian daripada / 3 daripada 5* → **Perbaikan:** *sebagian dari / 3 dari 5* — **Sebab:** hubungan partitif (porsi/kuantitas) memakai *dari* (TBB-017).
3. **Pola:** *kejatuhan oleh / kehabisan akan / kebanjiran dengan* → **Perbaikan:** *kejatuhan, kehabisan, kemasukan, kebanjiran* (langsung + pelengkap) — **Sebab:** verba semitransitif adversatif langsung mengikat pelengkap nomina (TBB-018).
4. **Pola:** *,05 / .05* → **Perbaikan:** *0,05* atau *0.05* — **Sebab:** bilangan desimal wajib diawali angka nol (PUPI-001).

---

### AV. Kalimat Emfatik, Kesalingan, dan Lambang Bilangan (Rujukan TBBBI Edisi Keempat: Bab IX hlm. 316 & 328, dan Lampiran 1 EYD hlm. 416-418)

1. **Pola:** *Dialah yang yang memulai...* → **Perbaikan:** *Dialah yang memulai...* — **Sebab:** emfatik cukup *-lah* + satu *yang*; penggandaan *yang yang* buntung (TBB-019).
2. **Pola:** *saling [verba] satu sama lain* → **Perbaikan:** *[verba] satu sama lain* — **Sebab:** *satu sama lain* sudah resiprokal; *saling* pleonasme ganda (TBB-020).
3. **Pola:** *15 orang tewas* (angka di awal kalimat) → **Perbaikan:** *Lima belas orang tewas* — **Sebab:** lambang bilangan awal kalimat wajib dieja huruf (EYD-020).
4. **Pola:** *tahun 50an* → **Perbaikan:** *tahun '50-an* / *tahun lima puluhan* — **Sebab:** bilangan *-an* bertanda hubung; *50an* tidak baku (EYD-021).
5. **Pola:** format pecahan hibrida tak lazim → **Perbaikan:** *1/2* atau *setengah* — **Sebab:** pecahan konsisten (EYD-022) [telaah].

---

### AX. Delimitasi Preposisi dan Frasa Berpreposisi (Rujukan Effendi & Aritonang, "Preposisi dan Frase Berpreposisi", Pusat Bahasa Depdikbud 1992)

1. **Pola:** *sejak pada tahun 2015* → **Perbaikan:** *sejak tahun 2015* — **Sebab:** *sejak* sudah menandai titik awal waktu; penumpukan preposisi ganda (PFP-005).
2. **Pola:** *antara 100 sampai 120 derajat / antara ... hingga/atau* → **Perbaikan:** *antara 100 dan 120 derajat* — **Sebab:** pasangan baku *antara* adalah *dan* (PFP-006).
3. **Pola:** *di dalam mana* (untuk *in which, wherein*) → **Perbaikan:** *tempat / dengan / yang memuat* atau strukturisasi ulang — **Sebab:** kalk penghubung klausa relatif asing tak diterjemahkan harfiah (PFP-007).
4. **Pola:** *tanpa tidak mengurangi* → **Perbaikan:** *tanpa mengurangi* — **Sebab:** ingkar ganda; *tanpa* sudah bermakna peniadaan (PFP-008).

---

### BO. Redundansi Sintaksis & Pleonasme Skripsi Mahasiswa (JSI UNNES & DE Journal)

1. **Pola:** *Selain itu juga* → **Perbaikan:** *Selain itu,* — **Sebab:** redundansi konjungsi antarkalimat + partikel aditif mubazir (JRN-001) (DE Journal 2023, hlm. 546).
2. **Pola:** *banyak mengandung unsur-unsur* → **Perbaikan:** *mengandung banyak unsur* / *mengandung unsur-unsur* — **Sebab:** pleonasme penanda jamak ganda berverba (JRN-002) (JSI UNNES 2021, hlm. 7).

---

### BP. Korelatif Taktepat & Pleonasme Klise Skripsi Mahasiswa (Jurnal Genre UAD 2021)

1. **Pola:** *baik dosen ataupun mahasiswa / baik ... dan* → **Perbaikan:** *baik dosen maupun mahasiswa* — **Sebab:** korelatif *baik* wajib berpasangan *maupun* (JRN-003) (hlm. 100).
2. **Pola:** *faktor pertama dan utama* → **Perbaikan:** *faktor utama* — **Sebab:** pleonasme kualitatif klise: *pertama* dan *utama* setara prioritas tertinggi (JRN-004) (hlm. 99).

---

### BS. Konjungsi Koordinatif Awal Kalimat & Kontaminasi Kuantor (Jurnal JPLED Unimal 2024)

1. **Pola:** *Dan penelitian ini menguji...* (mengawali kalimat baru) → **Perbaikan:** gabung dengan koma ke kalimat sebelumnya, atau ganti konjungsi antarkalimat *Selain itu,* — **Sebab:** *dan* penghubung intrakalimat, tak boleh mengawali kalimat mandiri (JRN-009) (hlm. 807).
2. **Pola:** *sebagian banyak* → **Perbaikan:** *sebagian besar* / *banyak* — **Sebab:** kontaminasi kuantor: campuran partitif dan kuantor (JRN-010) (hlm. 809).

---

### BT. Diksi, Pasangan Korelatif & Redundansi Sintaksis Skripsi (Jurnal Ar-Rumman, Lazuardi, ILEAL, Kande)

1. **Pola:** *jumlah rata-rata* → **Perbaikan:** *rata-rata / rerata / jumlah* (sesuai konteks) — **Sebab:** pleonasme kuantitatif leksikal: *rata-rata* sudah menyatakan nilai tengah agregat (JRN-011) (Ar-Rumman 2024, hlm. 548).
2. **Pola:** *hingga ... maupun* → **Perbaikan:** *baik ... maupun ...* — **Sebab:** kontaminasi korelatif: preposisi rentang tak boleh dipadukan konjungsi aditif (JRN-012) (Jurnal Lazuardi 2024, hlm. 58).
3. **Pola:** *bertujuan untuk menganalisis* → **Perbaikan:** *bertujuan menganalisis* — **Sebab:** pleonasme frasa verba bertujuan: *bertujuan* sudah mengandung 'mempunyai tujuan' (JRN-013) (ILEAL 2018, hlm. 6).
4. **Pola:** *Sehingga biaya membengkak.* (awal kalimat) → **Perbaikan:** *..., sehingga biaya membengkak.* atau *Oleh karena itu, / Akibatnya,* — **Sebab:** pemenggalan klausa subordinatif: *sehingga* penanda klausa akibat intrakalimat (JRN-014) (Jurnal Kande 2021, hlm. 155).
