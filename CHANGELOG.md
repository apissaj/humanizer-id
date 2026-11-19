# Changelog

Semua perubahan penting pada proyek ini dicatat di berkas ini. Format mengikuti [Keep a Changelog](https://keepachangelog.com/id/1.1.0/) dan versi mengikuti [SemVer](https://semver.org/lang/id/).

## [Belum dirilis]

### Bedah *Pedoman Penyuntingan Naskah* Badan Bahasa 2023/2024 (`750 -> 755` kaidah, Siklus 39)

- **Setyo Untoro dkk. (*Pedoman Penyuntingan Naskah Cerita Anak*, Pusat Pembinaan Bahasa dan Sastra, Badan Bahasa 2023/2024, ISBN 978-623-118-861-8):**
  - `PPN-001` — larangan tanda tanya/seru ganda atau berulang (`?!`, `!?`, `???`, `!!!`, hlm. 64–65).
  - `PPN-002` — kapitalisasi nonkapital kata kekerabatan berpewatas posesif/demonstrativa (`pamanku`, `paman itu`, `ibuku`, `bapaknya`, hlm. 60–61; EYD V).
  - `PPN-003` — kata sandang `si`/`sang` nonkapital di tengah kalimat/judul kecuali unsur nama Tuhan (`Sang Pencipta`, hlm. 62–63).
  - `PPN-004` — ungkapan terbata-bata memakai elipsis berspasi (`Si ... si ... siapa`), bukan tanda hubung berulang (`Si-si-siapa`, hlm. 65).
  - `PPN-005` (`[telaah]`) — bentuk ulang berimbuhan pada judul (`Berjalan-jalan`), konsistensi sudut pandang pronomina paragraf, dan pembedaan resmi *Kata Pengantar*, *Sambutan*, *Prakata*, dan *Sekapur Sirih* (hlm. 62, 70, 73–76, 84–88).
- Referensi baru: `references/pedoman-penyuntingan-naskah-badan-bahasa-2024.md`; Blok `CX` ditambahkan ke `skills/humanizer-id-ejaan-morfologi/SKILL.md` dan Blok `BO` ke `skills/humanizer-id-naskah-resmi/SKILL.md`.

### Integrasi *Wikipedia:Signs of AI writing* (*WP:AISIGNS*) & Tipografi EYD V (`740 -> 750` kaidah)

- **10 kaidah baru (`AIS-001`..`AIS-010`) di `data/kalke-indonesia.json` + 8 regex aktif di `humanizer_id/matchers.py`:**
  - `AIS-001` — analisis berekor partisipial kosong (*..., menyoroti pentingnya...*, *..., memastikan integrasi yang mulus...*).
  - `AIS-002` — atribusi kabur tanpa rujukan (*para ahli berpendapat*, *banyak pengamat menilai*, *laporan industri menunjukkan*).
  - `AIS-003` — pengantar menggurui khas chatbot (*penting untuk dicatat bahwa*, *perlu diingat bahwa*, *tak dapat dipungkiri bahwa*).
  - `AIS-004` — sisa percakapan & pujian chatbot (*Tentu, berikut...*, *Pertanyaan yang bagus*, *Semoga membantu!*).
  - `AIS-005` — inflasi signifikansi & kopula promosi (*menjadi bukti nyata atas*, *berdiri sebagai simbol*, *menandai tonggak bersejarah*).
  - `AIS-006` — paralelisme negatif formulaik (*bukan sekadar X, melainkan sebuah Y*).
  - `AIS-007` — templat tantangan & prospek masa depan (*Meskipun memiliki banyak kelebihan, X menghadapi sejumlah tantangan*).
  - `AIS-008` — tanda pisah em-dash berspasi khas keluaran LLM (` — `) yang melanggar EYD V (tanda pisah tanpa spasi mengapit).
  - `AIS-009`..`AIS-010` (`[telaah]`) — *synonym cycling*, rentang semu (*false ranges*), *rule of three* mekanis, daftar ber-**boldface**, *Title Case* Inggris, dan emoji di naskah formal.
- Referensi baru: `references/wp-aisigns-indonesia.md`; Blok `BW` ditambahkan ke `skills/humanizer-id-wacana-retorika/SKILL.md`.

### Penguatan & Perluasan Sub-Skill Domain (`11 -> 14` sub-skill: 5 strata + 9 domain)

- **3 sub-skill domain baru (`version: 2.4.6`):**
  - `skills/humanizer-id-terjemahan-lokalisasi/SKILL.md` — eliminasi kalke terjemahan mesin (`KLK-001..006`, `SPK-019`), urutan padanan PUPI (`TMS-048`), adaptasi serapan (`TMS-001`, `TMS-047`), lokalisasi UI/UX & safeguard.
  - `skills/humanizer-id-pendidikan-ajar/SKILL.md` — bahasa instruksional modul/LKPD, ejaan soal & satuan (`BSXI-001..003`, `UIN-011`), KTI/PTK guru (`KTI-001`), dan penjenjangan BIPA (`RGM-001..002`).
  - `skills/humanizer-id-esai-konten-digital/SKILL.md` — pembersihan klise blog/LinkedIn AI (`RET-001..006`), suara penulis & ritme semi-formal, salindia presentasi, copy web, dan media luar ruang.
- **Penguatan 3 sub-skill domain eksisting:**
  - `skills/humanizer-id-bisnis-korporat/SKILL.md`, `skills/humanizer-id-teknis-it/SKILL.md`, dan `skills/humanizer-id-hukum-regulasi/SKILL.md` diperkuat dengan pemetaan ID aturan terverifikasi (`VRB-*`, `KLK-*`, `RET-*`, `TMP-001`, `BSXI-001`, `HKT-015..016`, `SPK-007..010`, `UIN-003..004`, `DIN-003..004`, `SMD-003`), tabel *mini diff*, serta checklist Audit Mode AFTER.
- Tabel rute di `SKILL.md`, `README.md`, dan `tests/test_installer.py` (`11 -> 14`) diselaraskan.

### Ekspansi Autofix, 200 Istilah Glosarium, 11 Sub-Skill Domain & 3 Studi Kasus Baru

- **Perluasan autofix deterministik (`humanizer_id/engine.py`, `tests/test_fix.py`):**
  - `fix_text()` kini membongkar pasangan leksikal 1-ke-1 berpemisah garis miring (`/`) pada kategori `kata_baku_dan_morfologi` serta mengompilasi pola sekali di luar loop baris — cakupan autofix meningkat dari **336 -> 733 aturan deterministik** (`+397`) dengan **0 perubahan palsu** pada korpus bersih (`corpus_negative.json` + seluruh 740 `contoh_benar`).
  - Ditambahkan 2 pengujian unit baru di `tests/test_fix.py` (`test_fix_slash_paired_lexical_rules` dan `test_fix_zero_false_changes_on_clean_corpus`).
- **200 padanan glosarium lintas bidang (`data/glosarium-lintas-bidang.json`):**
  - `hukum_dan_regulasi` diperluas **10 -> 20** (+10: `addendum`, `affidavit`, `amicus curiae`, `bailout`, `class action`, `disclaimer`, `injunction`, `jurisprudence`, `power of attorney`, `whistleblower`).
  - `jurnalistik_dan_media` diperluas **15 -> 25** (+10: `anchorman`, `byline`, `deadline`, `embargo`, `feature`, `headline`, `infographic`, `live streaming`, `press release`, `prime time`).
  - Total glosarium kini **200 istilah** (Teknologi 68, Bisnis 60, Linguistik 27, Jurnalistik 25, Hukum 20), tersinkronisasi identik dengan `humanizer_id/data/glosarium-lintas-bidang.json`.
- **2 sub-skill domain baru (`9 -> 11` sub-skill: 5 strata + 6 domain):**
  - `skills/humanizer-id-surat-dinas/SKILL.md` (TND 2025, alamat `Yth.`, salam/penutup resmi, pasif diri, `NIP`/`a.n.`, frasa pewara bernalar).
  - `skills/humanizer-id-teknis-it/SKILL.md` (zona terlarang kode & satuan EYD V, 68 istilah PASTI TI, safeguard serapan baku, prosedur & paper teknik).
  - Tabel rute di `SKILL.md`, `README.md`, serta `tests/test_installer.py` (`9 -> 11`) diperbarui.
- **3 studi kasus domain baru di `examples/` (`6 -> 9` contoh, reduksi 100%):**
  - `examples/surat-dinas-korporat.md` (`16 -> 0` temuan)
  - `examples/artikel-jurnalistik-opini.md` (`13 -> 0` temuan)
  - `examples/ringkasan-hukum-regulasi.md` (`9 -> 0` temuan)
- **Sinkronisasi dokumentasi & `PROMPT.md`:**
  - `SKILL.md` dan `README.md` diselaraskan ke angka terkini (740 kaidah, 200 istilah glosarium, 18 preset, 11 sub-skill); `PROMPT.md` diperbarui dengan ringkasan EYD V, TBBBI Ed. 4, TND 2025, urutan padanan Baharman, dan panduan 4 domain.

### 740 kaidah + 180 istilah glosarium

Bedah lanjutan *Bahan Penyuluhan Tata Naskah Dinas* (Karenisa dkk., Badan Bahasa 2025) dan buku ajar perguruan tinggi (Halimah dkk. 2020; Ifnaldi 2021; UNJA) (Siklus 37–38):

- **Kity Karenisa dkk. (*Tata Naskah Dinas*, Badan Bahasa 2025, hlm. 27, 30, 46–47):**
  - `DIN-010` — penghubung surat dinas kontaminatif `Maka dengan ini` / `, maka dengan ini`.
  - `TMS-052` — `keikut sertaan` -> `keikutsertaan`, `legitimate` -> `legitimasi`, `cendikia/cendikiawan` -> `cendekia/cendekiawan`, dan `memperngaruhi` -> `memengaruhi`.
- **Andi Halimah dkk. (*Bahasa Indonesia untuk Perguruan Tinggi*, UIN Alauddin 2020, hlm. 61, 110–111):**
  - `RGM-002` — penyengauan lisan tanpa awalan *meN-* (`ngail`, `ngantuk`, `nabrak`, `nulis`, `nyubit`, `nyabut`, `nyari`, `nyuap`, `nolak`, `nanam`) dan dialek `ketawa` (`tertawa`).
  - `UIN-011` — penulisan lambang bilangan angka di awal kalimat (`50 siswa ...`, `3 pemenang ...` -> `Lima puluh siswa ...`).

Referensi baru: `references/tnd-2025-dan-buku-ajar-pt-lanjutan.md`; blok `CV`–`CW` pada sub-skill terkait dan `SKILL.md` diperbarui.

### 736 kaidah + 180 istilah glosarium

Mekanisasi lanjutan *Surat-Menyurat dalam Bahasa Indonesia* (Pusat Bahasa 1991), *Cerdas Cergas Kelas XI*, *Diklat KTI/PTK*, dan *Buletin MABBIM* Vol. 15 (2024) (Siklus 35–36):

- **Pusat Bahasa (*Surat-Menyurat*, 1991, hlm. 17–18, 36):**
  - `SMD-003`..`SMD-004` — kapitalisasi salam surat resmi (`Dengan hormat,`, `Hormat saya,`, `Hormat kami,`) dan penghapusan rumus klise surat lama (`Bersama ini kami kabarkan`, `Demikianlah harap maklum`).
- **Kemendikbud (*Cerdas Cergas Kelas XI*, hlm. 12, 255–261; *Diklat KTI/PTK*) & *Buletin MABBIM* (2024):**
  - `BSXI-001`..`BSXI-003`, `KTI-001` — spasi angka-satuan (`50 cm`, `15 m`), bentuk baku (`kategori`, `spesies`, `keramba`), kontaminasi `Dengan alasan inilah maka`, serta `[telaah]` kaidah penyusunan KTI & pembalikan nama daftar pustaka.
- **2 padanan glosarium baru (178 -> 180):** `content creator` (`pencipta konten / kreator konten`, MABBIM 2024) dan `tautology` (`tautologi`, Kridalaksana 1979).

Referensi baru: `references/mekanisasi-surat-kti-kelasxi-mabbim.md`; blok `CS`–`CU` pada sub-skill terkait dan `SKILL.md` diperbarui.

### 730 kaidah + 178 istilah glosarium

Mekanisasi lanjutan *Latihan Kemahiran Berbahasa Indonesia* (Badan Bahasa 2016) & *Daftar Istilah Linguistik* (Kridalaksana 1979) (Siklus 33–34):

- **Kaniah dkk. (*Latihan Kemahiran Berbahasa Indonesia*, Badan Bahasa 2016, hlm. 12–23 / 70–84) & Modul Karya Ilmiah SMA:**
  - `LKB-048`..`LKB-052` — bentukan `se-` + wilayah geografis huruf kecil (`sekabupaten`, `seprovinsi`, `seindonesia`), gelar depan tanpa spasi setelah titik (`Dr.Maman`, `Prof.Ahmad`), konstruksi takbaku `untuk jangan` & `berapa pukul`, verba lokasi `mendatangkan lokasi` -> `mendatangi lokasi`, serta `[telaah]` pewatas pasif tanpa `yang` dan larangan `ibid./op.cit./loc.cit.`.
- **Harimurti Kridalaksana (*Daftar Istilah Linguistik Asing – Indonesia*, 1979):**
  - 8 padanan istilah linguistik baku (170 -> 178): `discourse` (`wacana`), `deep structure` (`struktur batin`), `surface structure` (`struktur lahir`), `paraphrase` (`parafrase`), `ambiguity` (`ketaksaan / ambiguitas`), `redundancy` (`kelimpahan / kelewahan`), `colloquialism` (`ragam tak resmi`), `metalanguage` (`metabahasa`).

Referensi baru: `references/latihan-kemahiran-dan-istilah-linguistik-lanjutan.md`; blok `CP`–`CR` pada sub-skill terkait dan `SKILL.md` diperbarui.

### 725 kaidah + 170 istilah glosarium

Bedah lanjutan Pedoman Penerbitan Buku LIPI Press (2016), Modul Opini KD 3.11, dan Buku Saku Media Luar Ruang / Semiloka 2019 (Siklus 31–32):

- **LIPI Press (`books/pedoman_penerbitan_buku_lipi_press.pdf`, hlm. 60, 67), Modul Opini (`hlm. 31`), & Semiloka 2019 (`hlm. 241`):**
  - `BRN-005`..`BRN-007` — pemisahan `ke luar negeri/kota/daerah`, preposisi waktu `pada pagi/siang/sore/malam hari` (bukan `di ... hari`), serta ejaan baku `bertaraf`, `skala`, `suvenir`, `musala`, dan `gaji`.
- **Buku Saku Media Luar Ruang 2015 (`hlm. 22–89, 110–124`) & Semiloka 2019 (`hlm. 271–272, 522–549`):**
  - `PSB-035`..`PSB-036` — serapan baku `kontemporer`, `butik`, `fotokopi`, `taksi`, `mal`, serta `[telaah]` hukum DM–MD pada penamaan dan tanda seru (`!`) pada imbauan/larangan.
  - 2 padanan sektor usaha (168 -> 170): `cottage` -> `pondok`, `food and beverage` -> `makanan dan minuman`.

Referensi baru: `references/pedoman-lipi-press-dan-media-luar-ruang-lanjutan.md`; blok `CN`–`CO` pada sub-skill terkait dan `SKILL.md` diperbarui.

### 720 kaidah + 168 istilah glosarium

Bedah lanjutan edisi revisi Badan Bahasa & Seri Penyuluhan 9 EYD (Siklus 29–30):

- **Seri Penyuluhan 9 EYD (`books/seri_penyuluhan_9_eyd.pdf`, hlm. 38–44) & Prosiding Semiloka 2019:**
  - `E9L-026`..`E9L-027` — ejaan serapan/digraf/apostrof surat kabar & latihan EYD (`azasi`, `muqaddimah`, `akhlaq`, `centraal`, `romadhon`, `teknologie`, `kwota`, `extradiksi`, `effektiv`, `psikhologi`, `alkuran`, `ma'siat`, `sa'at`) dan larangan tanda titik pada singkatan lembaga/istilah umum (`D.P.R.`, `U.U.D.`, `K.B.`, `S.M.A.`, `S.M.P.`).
  - `EYD-076` — preposisi serangkai tambahan (`diseluruh`, `ditempat`, `diantara`, `ketengah`).
- **Seri Penyuluhan Bahasa Indonesia: Kalimat Edisi v2 (`books/seri_penyuluhan_kalimat_badanbahasa_v2.pdf`, hlm. 25–32, 75–80):**
  - `SPK-017`..`SPK-021` — larangan preposisi sebelum objek langsung (`mengharap atas`, `membangun daripada`), pemasifan takgramatikal kopula/intransitif (`dijadi`, `dirupakan`), kalke siaran (`Ini [Nama] melaporkan dari [Kota]`), serta `[telaah]` larangan pemasifan pelengkap, kesejajaran klausa majemuk koordinatif (`S-P dan P-S`), dan kelengkapan objek/pelengkap wajib.
- **M. Zaim (UNP 2018, hlm. 2 — `books/serapan_istilah_ti_2018.pdf`):**
  - 4 padanan istilah TI resmi (164 -> 168): `download` -> `unduh`, `upload` -> `unggah`, `offline` -> `luring / luar jaringan`, `mouse` -> `tetikus`.

Referensi baru: `references/seri-penyuluhan-9-eyd-dan-kalimat-v2.md`; blok `CK`–`CM` pada sub-skill terkait dan `SKILL.md` diperbarui.

### 712 kaidah + 164 istilah glosarium

Penyapuan tuntas sumber Pusat Bahasa & mekanisasi lanjutan temuan jurnal skripsi (Siklus 26–28):

- **Pusat Bahasa — *Beberapa Permasalahan Pemakaian Bahasa Indonesia* (`books/beberapa_permasalahan_pemakaian_bahasa_indonesia.pdf`, hlm. 38–39, 81–85, 121–123) & BRIN (2022, hlm. 17):**
  - `TMS-049`..`TMS-051` — peluluhan *mempedomani* -> *memedomani*, ejaan *Februari*, *transportasi*, *imbauan/mengimbau*, *meminimalkan* (JURRIBAH 2026 hlm. 478), preposisi serangkai (*ke arah*, *di daerah*, *di luar*, *di samping*), gabungan kata bebas *wali kota* terpisah vs konfiks penuh *menindaklanjuti* serangkai.
  - `EYD-074`..`EYD-075` — larangan spasi sekitar tanda hubung kata ulang (*hal-hal*, *rata-rata*) dan kapital awal unsur singkatan gelar/lembaga (*S.Sos.*, *M.Si.*, *S.Pd.*, *A.Md.*, *MTs*).
- **Mekanisasi lanjutan jurnal empiris skripsi (`KIBASP` 2026, `JURRIBAH` 2026, `DEIKTIS` 2026, `DiSastra` 2021, `BB Unmuh Jember` 2020):**
  - `JSK-012`..`JSK-018` — klitika *-nya* terpisah (*banyak nya* -> *banyaknya*), titik ganda pernyataan (`..`), titik koma keliru sesudah *yaitu;*/*yakni;*, tipografi & kapitalisasi aplikasi (*manajemen*, *sehingga*, *lingkungan*, *Google Form*, *WhatsApp*), ragam cakap *pastinya*, format sitasi subjek `Menurut (Nama Tahun) menyatakan...`, serta `[telaah]` nomenklatur binomial ICN/ICZN & judul karya.
- **4 padanan glosarium baru (160 -> 164):** `public figure`, `storyteller`, `library research`, dan `hard copy`.

Referensi baru: `references/beberapa-permasalahan-pemakaian-lanjutan.md` dan `references/kompilasi-jurnal-skripsi-undhari-unimal-lanjutan.md`; blok `CH`–`CJ` pada `skills/humanizer-id-{ejaan-morfologi,sintaksis,diksi-istilah}/SKILL.md` serta `humanizer-id-skripsi-kampus` dan `SKILL.md` diperbarui.

### 700 kaidah + 160 istilah glosarium

Bedah lanjutan lima sumber rujukan resmi & empiris (Siklus 23–25):

- **Baharman (UNM)** — *Penguatan Penyerapan dan Pemadanan Istilah Asing sebagai Pembinaan dan Pengembangan Bahasa Indonesia* (`books/penguatan_penyerapan_pemadanan_istilah.pdf`, 22 hlm.):
  - `TMS-047` — salah adaptasi serapan (`misskoordinasi` -> `miskoordinasi`, `volantilitas` -> `volatilitas`, `investation` -> `investasi`, `illegal` -> `ilegal`).
  - `TMS-048` (`[telaah]`) — urutan wajib mendahulukan padanan Indonesia sebelum istilah asing dalam tanda kurung (hlm. 9).
  - 9 padanan istilah pers/ekonomi/TI baru di `data/glosarium-lintas-bidang.json` (`commuter line`, `busway`, `reshuffle`, `selfie`, `rising star`, `community relation`, `year to date`, `month to month`, `online`).
- **Kompilasi 3 Jurnal Empiris Skripsi & BIPA** (`books/jurnal_iain_curup_kesalahan_eyd_skripsi.pdf` Khair 2018; `books/jurnal_unnes_kesalahan_sintaksis_skripsi.pdf` Saputra & Alber 2021; `books/jurnal_umk_kesalahan_diksi_kalimat.pdf` Yahya dkk. 2018):
  - `JSK-007`..`JSK-011` — ejaan leksikal proposal skripsi (`pengetahuan`, `cenderung`, `definisi`, `kesanggupan`, `alternatif`), preposisi `di`/`ke` serangkai (`di kelas`, `ke jenjang`, `di sana`, `di sini`, `di situ`), leksikon BIPA/skripsi (`kaus`, `silakan`, `membawa`, `tetapi`, `sudah`, `hanya`), serta `[telaah]` fragmen tanpa subjek (`Yang disebabkan...`) dan pembalikan hukum DM-MD (`pengetahuan kemampuan`); ditambah padanan `email` -> `pos-el / surat elektronik (surel)`.
- ***Tata Bahasa Baku Bahasa Indonesia* (TBBBI) Edisi IV (2017)** (`books/tata_bahasa_baku_bahasa_indonesia_edisi_4_2017.pdf`):
  - `TBB-032`..`TBB-036` — larangan `-kah` pada kalimat tanya S-P berawal `Yang ...` (`Yang ... apakah?`), larangan konjungsi `Tetapi` mengawali kalimat baru, artikula `para` dengan nomina takspesifik (`*para anak`, `*para orang`, `*para manusia`), penanda sebab lisan tidak baku (`gara-gara`, `mentang-mentang`), serta `[telaah]` larangan kepemilikan pronomina `ia` (`*istri ia`) dan diatesis pasif `-i` vs `-kan` (`ditugasi` vs `ditugaskan`).

Referensi baru: `references/baharman-penyerapan-pemadanan-istilah.md`, `references/jurnal-curup-unnes-umk-kesalahan-skripsi.md`, dan `references/tbbbi-edisi-4-2017-lanjutan.md`; blok `CE`–`CG` ditambahkan pada `skills/humanizer-id-{ejaan-morfologi,sintaksis,diksi-istilah}/SKILL.md` serta pembaruan `humanizer-id-skripsi-kampus`, `humanizer-id-jurnalistik-media`, dan `SKILL.md`.

### 4 sub-skill domain baru (`skills/`)

- `skills/humanizer-id-skripsi-kampus/SKILL.md` — peta 18 preset kampus (`pedoman-kampus.json`), daftar penyakit khas draf skripsi mahasiswa (5 jurnal empiris + Winarti 2009), dan pemisahan Simpulan vs Saran.
- `skills/humanizer-id-bisnis-korporat/SKILL.md` — prinsip KISS dan surat instruksi 5W1H / siaran pers piramida terbalik (Rahman, BRIN 2022) serta padanan bisnis baku.
- `skills/humanizer-id-jurnalistik-media/SKILL.md` — 7 sifat bahasa pers (Badudu), ekonomi kata Tempo, batas 17–20 kata/kalimat (Pusdiklat Kemendikbud 2018), padanan media, dan struktur artikel opini.
- `skills/humanizer-id-hukum-regulasi/SKILL.md` — batas zona terlarang kontrak/pasal, anti-multimakna, pasif normatif pelengkap, dan diksi klaim produk realistis (*Hukum dalam Teroka Linguistik*, BRIN 2023).
- Tabel rute `SKILL.md` induk dan `README.md` diperbarui mencakup 5 strata + 4 domain (`9 sub-skill` + modul `jurnal/`).

### 688 kaidah + 150 istilah glosarium

Bedah menyeluruh lima rujukan resmi (Siklus 20–22):

- **EYD Edisi V (SK Kepala Badan Bahasa No. 0424/I/BS.00.01/2022) & Seri Penyuluhan Ejaan v2** (`books/eyd_edisi_5_2022.pdf`, `books/seri_penyuluhan_ejaan_badanbahasa_v2.pdf`):
  - `EYD-065`..`EYD-068` — gabungan kata padu (`darmabakti`, `sukarela`, `saputangan`, `belasungkawa`, `manasuka`, `adakalanya`), gabungan kata bebas/berimbuhan sepihak (`tanda mata`, `kaki tangan`, `kaki lima`, `orang tua`, `berpesta pora`, `kerja baktikan`), gabungan kata berkonfiks penuh (`menyamaratakan`, `menganaktirikan`, `mengambinghitamkan`, `ketidaktahuan`, `keputusasaan`), serta bentuk terikat (`Yang Maha Kuasa`, `ekabahasa`, `nirgagasan`, `antar jemput`).
  - `BAK-012` disempurnakan agar kata dasar `antar` bermakna 'bawa/kirim' (*antar jemput*, *antar barang*) tidak tertandai keliru.
  - `EYD-069`..`EYD-070` — singkatan surat-menyurat bergaris miring (`a/n`, `u/p`, `u/b`, `d/a`), format `Rp` bertitik/berspasi, tanda titik setelah perincian berkurung `(a).`, tanda baca akhir ganda `?.`/`!.`, serta skor pertandingan bertitik dua (`skor 3:1` -> `skor 3-1`).
  - `EYD-071`..`EYD-072` — unsur serapan EYD V Bab IV (asing: `akomodasi`, `aksesori`, `konsekuen`, `ekuivalen`, `suvenir`, `deskripsi`, `stereo`, `espreso`, `tenteram`; Arab: `tafakur`, `umat`, `kafah`, `tamat`, `nasihat`, `hakikat`, `makhluk`, `sahih`, `uzur`, `zalim`, `pikir`, `napas`, `faedah`).
  - `EYD-073` (`[telaah]`) — huruf miring istilah asing/daerah, huruf tebal penegas, dan tanda pisah (`—`) untuk rentang.
- **Winarti dkk. (2009), Subbab 2.3.3–2.11** (Jurnal Ekonomi Pertanian, Mahakam, Didaktika, Dedikasi, Prediksi, Sosial Politik, Forum Ekonomi, Dinamika Ilmu, Poltanesa, hlm. 38–137):
  - `TMS-043`..`TMS-046` — peluluhan KTSP (`mengursuskan`, `menyukseskan`, `menyejahterakan`, `memercayai`, `ditelurkannya`), serapan ilmiah (`mendiskreditkan`, `sekretaris`, `seyogianya`, `praktik`, `ditoleransi`, `konferensi`), gabungan kata (`tenaga kerja`, `semipermeabel`, `menitikberatkan`), kerancuan diksi (`mengacu pada`, `hidup-hidup`, `membahas`, `di samping itu`, `pada/antara tahun`), serta perluasan `TMS-038` untuk `sejak ... sampai`.
- **Buku Praktis Bahasa Indonesia 2 (Bahasa, Istilah, Kalimat), Sasangka (2015) Kalimat, & Suladi (2015) Paragraf**:
  - `BPBI-008`..`BPBI-009` — ungkapan `Dirgahayu RI` / `HUT ke-N RI` / `WIB` (bukan `BBWI`) serta konjungsi `agar/supaya` (bukan `bahwa`) sesudah verba harapan/anjuran (`menganjurkan`, `mengharapkan`, `mengimbau`, `memohon`).
  - `SPK-014`..`SPK-016` — kerancuan `Menurut pada X` & preposisi objek verba transitif (`mengamanatkan kepada`, `menyimpulkan tentang`), koma sesudah penghubung antarkalimat (`Oleh sebab itu,`, `Meskipun demikian,`, `Walaupun demikian,`, `Sehubungan dengan itu,`, `Berkaitan dengan hal itu,`), dan `[telaah]` kalimat partisipial awal verba (Sasangka 2015, hlm. 88–96).
  - Glosarium lintas bidang bertambah 13 padanan resmi Pusat Bahasa (137 -> 150 istilah).

Referensi baru: `references/eyd-v-2022-lengkap.md`, `references/seri-penyuluhan-ejaan-v2-badan-bahasa.md`, `references/kaltim-2009-jurnal-mahakam-sospol-ekonomi.md`, `references/bpbi-2-bahasa-istilah-kalimat.md`, dan `references/kalimat-efektif-sasangka-2015.md`; sub-skill `skills/humanizer-id-ejaan-morfologi/SKILL.md`, `skills/humanizer-id-sintaksis/SKILL.md`, `skills/humanizer-id-diksi-istilah/SKILL.md`, dan tabel rute `SKILL.md` diperbarui.

### 670 kaidah

Bedah lanjut Winarti dkk. (2009): subbab 2.1.3-2.1.4 Jurnal Budidaya Pertanian (hlm. 14-23)
dan 2.3.1-2.3.2 Jurnal Ekonomi Pertanian dan Pembangunan (hlm. 32-37).

- `TMS-042` - `teoritis` -> `teoretis` (penyerapan langsung dari *theoretical*, bukan
  teori + -tis) dan `sekedar` -> `sekadar` (kadar + se-).
- `SPK-012` - subjek didahului penghubung `bahwa` setelah keterangan `Menurut X,`:
  `Menurut Kim H. Tan (1991), bahwa Al ...` -> penghubung dihilangkan.
- `SPK-013` - frasa keterangan mengambil posisi subjek: `Berdasarkan hasil penelitian
  menunjukkan bahwa ...` -> `Hasil penelitian menunjukkan bahwa ...`. Varian berkoma tetap
  lolos karena frasa keterangan diikuti subjek sah.
- `SPK-001` diperluas: daftar konjungsi syarat `jika|kalau|apabila` ditambah `bila`, mengikuti
  contoh `bila melapuk maka tidak bisa diserap` pada hlm. 14. Kalimat `Pengujian dilakukan bila
  cuaca mendukung.` tetap bersih.

Sembilan bentuk lain pada bab yang sama sudah tertangkap mesin lama (`KK-001`, `TMS-001`,
`BPK-032`, `BAK-011`, `BAK-001`, `KK-003`, `BAK-005`, `TBB-004`, `TMS-029`). Kasus yang
menuntut analisis fungsi sintaksis - subjek berkata depan `Pada ...`, redundans
`pemanfaatan ... dimanfaatkan`, dan `memiliki/mempunyai` - dicatat `[telaah]` tanpa pola.

Referensi baru: `references/kaltim-2009-penyusunan-kalimat-dan-ekonomi.md`.

Verifikasi: `work/test_tms42_spk012_013.py` 18/18, `uv run pytest -q` 45 passed, uji nol
positif palsu tetap 0.

### 667 kaidah

Bedah lanjut Winarti dkk. (2009) subbab 2.2.1-2.2.3, Jurnal Agrifor (hlm. 24-32):

- `TMS-039` - serapan dan turunannya: `memposisikan` -> `memosisikan`, `marjinal` ->
  `marginal`, `hektar` -> `hektare`.
- `TMS-040` - nomina `hasil` hanya dapat menerima konfiks: `menghasil` -> `menghasilkan`.
  Pasangan `diprioritas` pada halaman yang sama sudah dijaga `KK-004`, sehingga tidak
  diduplikasi.
- `TMS-041` - `respon` -> `respons`; regex `respon` tanpa `\w*` di awal agar
  `responden` tidak tertandai.

Kaidah buku yang sudah tertangkap mesin lama: `dirubah` (`BAK-002`/`BPK-019`), `tehnik`
(`BPK-030`), `dianalisa` (`BAK-005`), `mempengaruhi` (`BAK-001`), `terdiri dari`
(`TBB-004`), dan pembanding `lebih ... dari` (`TMS-029`).

Empat kasus penyusunan kalimat sengaja tidak dipola dan dicatat `[telaah]`: kesejajaran
deret perincian, subjek preposisional `Oleh X + predikat aktif`, subjek berkata depan, dan
verba kedua tanpa penghubung.

Referensi baru: `references/kaltim-2009-terbitan-ilmiah-kalimat-jurnal-agrifor.md`.

Verifikasi: `work/test_tms39_41.py` 15/15, `uv run pytest -q` 45 passed, uji nol positif
palsu tetap 0.

### 664 kaidah

Bedah pindah ke Winarti dkk. (2009), *Kesalahan Berbahasa Indonesia dalam Terbitan Ilmiah
Perguruan Tinggi di Kalimantan Timur*, subbab 2.1.1-2.1.2 (hlm. 7-14):

- `TMS-037` - perangkapan verba, penyerapan keliru, dan preposisi serangkai:
  `menstimulir` -> `menstimulasi`, `panili` -> `vanili`, `disekitar`/`diareal`/`diladang`
  ditulis terpisah. `mensuplai`, `dianalisa`, dan `produktifitas` tidak dibuat kaidah baru
  karena sudah tertangkap `BDD-006`, `BAK-005`, dan `BPK-027`.
- `TMS-038` - preposisi gabungan tidak lengkap: `mulai Maret sampai Mei` dan
  `dari Senin sampai Kamis` -> `sampai dengan`. Regex memakai huruf kapital nama bulan atau
  angka sebagai penanda rentang waktu agar kalimat seperti "mulai naik setelah remedial
  sampai tuntas" tidak tertandai; versi pertama dengan `(?i)` gagal kasus negatif itu dan
  dipersempit.

Referensi baru: `references/kaltim-2009-terbitan-ilmiah-pembentukan-kata.md` (kutipan
verbatim hlm. 7-14 + penanda `[OCR]` + penjelasan penyerempitan regex).

Verifikasi: `work/test_tms37_38.py` 19/19, `uv run pytest -q` 45 passed, uji nol positif
palsu tetap 0.

### 662 kaidah

Bedah dilanjutkan ke Mustakim (2019), subbab 3.1.3 keserasian kata (hlm. 60-68):

- `TMS-035` - verba tanpa awalan ber- sebagai predikat ragam resmi: `sudah kumpul`,
  `telah kumpul`, `sampai jumpa` -> `berkumpul`, `berjumpa` (hlm. 62).
- `TMS-036` - bentuk tidak baku dari tabel baku-tidak baku hlm. 67-68 yang belum tercakup
  kaidah lain: `akte`, `beaya`, `efektip`, `effektif`, `effisien`. Bentuk baku tertangkap
  kaidah lama: `analisa` -> `BAK-005`, `aktifitas` -> `TIQ-003`, `resiko` -> `BAK-008`,
  `kwalitas`/`kwitansi`/`jadual` -> `BPK-015`, dan seterusnya.
- `BPK-005` - daftar nomina ungkapan idiomatis tanpa preposisi diperluas dari daftar tertutup
  menjadi terbuka: `tergantung cuaca`, `bergantung anggaran`, `tergantung penilaian` kini
  tertandai. Frasa pendek yang lazim pada naskah hukum (`sesuai undang-undang`,
  `sesuai jadwal`) sengaja tetap dibiarkan dan dicatat `[telaah]`.

Referensi baru: `references/mustakim-2019-keserasian-kata-dan-tabel-baku.md` (kutipan
verbatim hlm. 60-68 + tabel status mesin untuk seluruh lajur baku-tidak baku + anotasi
`[telaah]` untuk `BPK-013`/`BPK-014` dan pasangan `antara lain`/`misalnya`).

Verifikasi: `work/test_tms35_36.py` 16/16, `uv run pytest -q` 45 passed, uji nol positif
palsu tetap 0. Regex `sampai jumpa` awalnya case-sensitive dan telah diberi `(?i)`.

### 660 kaidah

Melanjutkan bedah Rusbiyantoro dkk. (2009), kali ini subbab 3.6 (tanda baca, hlm. 27-37) dan
3.7 (unsur serapan, hlm. 38-41):

- `TMS-032` - akhiran serapan `-ir` tidak baku: `dilegalisir`, `menginventarisir`,
  `terakomodir`, `terorganisir`, `mengkoordinir`, `diregionalisir` -> bentuk `-asi`/`-isasi`.
- `TMS-033` - ejaan serapan yang belum disesuaikan: `tehknik`, `enerjik`, `rejional`,
  `aktip`, `perogram`.
- `TMS-034` - penghubung antarkalimat berunsur dua kata di awal kalimat tanpa koma:
  `Sementara itu`, `Oleh karena itu`, `Dengan demikian`, `Selain itu`; melengkapi `SPE-003`
  yang hanya menangani bentuk satu kata (`Namun`, `Bahkan`, `Kemudian`, `Lagi pula`).

Tiga kaidah lama yang ada di data tanpa mesin kini punya matcher: `BAK-005` (`analisa`),
`BAK-007` (`praktek`, tanpa menandai `praktis`), dan `BPK-038` (`mengaktipkan`).
Contoh buku (91)-(93) tentang koma sebelum anak kalimat kausal terverifikasi sudah
tertangkap `KJK-005` dan `SPE-001`; contoh (107) `Hut ke 58` sudah tertangkap `EYD-027`.

Lima kaidah buku sengaja tidak diaktifkan dan dicatat `[telaah]` di referensi: singkatan
gelar tanpa titik (EYD V memperbolehkan), angka ribuan tanpa titik, koma serial sebelum
`dan` (EYD V menjadikannya pilihan penulis), koma sebelum `tetapi`/`sedangkan` antarklausa,
dan kutipan langsung tanpa tanda petik.

Referensi baru: `references/pusat-bahasa-2009-tanda-baca-dan-serapan.md` (kutipan verbatim
hlm. 27-41 + penanda `[OCR]` + anotasi `[telaah]`).

Verifikasi: `work/test_tms32_33.py` 28/28, `work/test_tms34.py` 11/11, `uv run pytest -q`
45 passed, uji nol positif palsu tetap 0.


### 657 kaidah

Wenni Rusbiyantoro, Nur Bety, dan Mardi Nugroho, *Beberapa Permasalahan Pemakaian Bahasa
Indonesia* (Pusat Bahasa, Departemen Pendidikan Nasional, 2009), subbab 3.8.1-3.8.3
(hlm. 42-53):

- `TMS-030` - gabungan kata dan partikel yang salah rangkai: `salahsatunya`, `tindaklanjuti`,
  `unjukrasa`, `lagipula`, `non aktif`. Bentuk berimbuhan yang benar (`ditindaklanjuti`,
  `menindaklanjuti`) sengaja dibiarkan lolos.
- `TMS-031` - `kordinator`/`kordinasi` (KBBI memakai dua vokal `/oo/`) dan `mengkomentari`
  (fonem awal `/k/` luluh menjadi `mengomentari`).

Empat kaidah lama yang ada di data tanpa mesin kini punya matcher: `BAK-002` (`merubah`,
`dirubah`), `BAK-004` (`mentargetkan`), `BPK-044` (`penanggungjawab`), `BPK-045`
(`bekerjabakti`). `SPE-014` (`tandatangani`) ikut dipasang dengan regex yang tidak menangkap
`ditandatangani`. `BDD-009` (klise `, di mana hal ini`) dipasang dengan syarat koma di depan
agar klausa relatif yang sah tidak tertandai. `KPT-009` (`kerjasama`) sengaja tetap tanpa
matcher `CUSTOM_RULES` karena `kerjasama` sudah dilaporkan mesin kata tidak baku di
`engine.py`; menambah blok baru hanya menggandakan laporan.

Referensi baru: `references/pusat-bahasa-2009-permasalahan-pemakaian-bahasa.md` (kutipan
verbatim hlm. 42-53, penanda `[OCR]` untuk salah baca `l`->`I` dan `rn`->`m`, plus anotasi
`[telaah]` untuk `ranking`, `beking`, `open race`, dan `dimana` di awal kalimat yang sengaja
belum dipola).

Verifikasi: `work/test_tms30_31.py` 29/29, `uv run pytest -q` 45 passed, uji nol positif
palsu tetap 0.


## [2.4.6] - 2026-11-17

### 655 kaidah

Mustakim, *Bentuk dan Pilihan Kata: Seri Penyuluhan Bahasa Indonesia* (Badan Pengembangan
Bahasa dan Perbukuan, 2019), subbab 3.3 c-h (hlm. 76-82):

- `TMS-029` - adjektiva pembanding (`lebih`/`kurang` + adjektiva) diikuti `dari`, seharusnya
  `daripada`. Kalimat (50) dan (51) buku dipakai sebagai pasangan salah-benar.
- Pemerluasan regex kaidah lama, tanpa entri baru:
  - `BPK-006` - tambah `berasal`, `terbentuk`, `tersusun` (asal/sumber bahan).
  - `BPK-007` - tambah bentuk label `Jam: 09.00`.
  - `BPK-008` - tambah nomina predikat `benda`, `alat`, sehingga kalimat (54)
    "Logam yaitu suatu benda ..." tertangkap.
  - `BPK-009` - tambah jabatan `camat`, `lurah`, `hakim`, `jaksa`, `sekretaris`, `duta`.

Referensi baru: `references/mustakim-2019-bentuk-pilihan-kata-mantan-bekas-dari-daripada.md`
(kutipan verbatim hlm. 76-82 + catatan `[telaah]` untuk kalimat (52), (53), (57), (58) yang
sengaja belum dipola).

Perbaikan proses: tiga blok matcher duplikat untuk `BPK-007/008/009` ditemukan dan dihapus -
kaidah itu sudah punya matcher di indeks 68-70 yang tidak menyebut ID pada komentarnya,
sehingga `grep` atas ID memberi kesan "tanpa matcher". Jumlah aturan `CUSTOM_RULES` kembali
313 -> 310, dan seluruh perilaku baru dicapai lewat pemerluasan regex lama.

### Ditambahkan
- **Lima entri kaidah Buku Praktis Bahasa Indonesia (Badan Bahasa)** — `BPBI-001` (17 pasang: erobik→aerobik, akountan→akuntan, arkhais→arkais, gladi→geladi, hirarki→hierarki, karir→karier, kuatir→khawatir, konggres→kongres, kurve→kurva, nahkoda→nakhoda, perangko→prangko, setasiun→stasiun, sahdu→syahdu, trampil→terampil, trotoir→trotoar, wakap→wakaf, wassalam→wasalam) dan `BPBI-002` (12 pasang: antri→antre, atlit→atlet, ajimat→azimat, faksimil→faksimile, filem→film, ijin→izin, joang→juang, khabar→kabar, kangker→kanker, kongkrit→konkret, tentram→tenteram, jiarah→ziarah) dari BPBI1/Kata; `BPBI-003` (`karenanya`/`makanya` → *oleh karena itu*/*oleh sebab itu*/*jadi*) dari BPBI1/Kalimat; `BPBI-004` (8 pasang: dekret→dekrit, azas→asas, hutang→utang, maghrib→magrib, atmosfir→atmosfer, eksim→eksem, apotik→apotek, kridit→kredit) dari BPBI2/1-30 & 31-60; `BPBI-005` (`contohnya seperti`/`umpamanya seperti` sebagai pleonasme) dari BPBI2/61-90; `BPBI-006` (`dilola`→`dikelola`, `sanjak`→`sajak`) dari BPBI1/Lain-lain & Sastra. `BPBI-007` (`pirsawan`->`pemirsa`, `debet`->`debit`, `voucher`->`voucer`) dari BPBI2 bagian 1-90. Total entri **618 -> 625**. Ditambah dua entri dari *Taktis Menyunting: Panduan Menyunting Naskah* (BRIN, 2019): `TMS-001` (16 pasang ejaan serapan: frustasi, negoisasi, interprestasi, konkrit, komoditi, horisontal, infantri, marjin, dirijen, otobiografi, pondasi, birahi, minimun, orisinil, quantum, malpraktik) dan `TMS-002` (14 bentuk tidak baku: telanjur, perduli, autodidak, trend, goncang, inagurasi, rubuh, contek, nampak, juridis, qori', propemerintah, cindera mata, cenderamata) dari Tabel 5.1 dan 5.16 buku tersebut, sehingga total entri **625 -> 627**. Ditambah `TBI-001` dari Winarti dkk., *Kesalahan Berbahasa Indonesia dalam Terbitan Ilmiah Perguruan Tinggi di Kalimantan Timur* (Pusat Bahasa, 2009): 10 bentuk keliru pada artikel jurnal ilmiah (propesional, kerampilan, ketrampilan, mengkomunikasikan, mendiskritkan, tehnologi, mengasilkan, prosentasi, nampaknya, tergantung dari) beserta halaman penilaian penulisnya, sehingga total menjadi **628**. Ditambah `TMS-003` dan `TMS-004` dari *Taktis Menyunting* (BRIN, 2019), Tabel 5.18 (hlm. 115) dan Tabel 5.20 (hlm. 117): 6 bentuk terikat yang dipisah spasi (antar golongan, multi lateral, purna wirawan, nara hubung, pra jabatan, sapta krida) dan 13 gabungan kata padu yang dipisah (acap kali, sedia kala, kaca mata, karya wisata, kasat mata, suka cita, kosa kata, syah bandar, mata hari, olah raga, peri bahasa, duka cita, puspa warna), sehingga total menjadi **630**. Ditambah `TMS-005` dan `TMS-006` dari *Taktis Menyunting* (BRIN, 2019), Tabel 5.6 (hlm. 102-103) dan Tabel 5.8 (hlm. 105-106): 14 bentuk lewah yang belum berkaidah (sangat sempurna sekali, sangat jauh sekali, banyak buku-buku, beberapa pendapat-pendapat, melakukan penangkapan, melakukan pembinaan, melakukan perubahan, menyatakan pendapat, menggabungkan menjadi satu, saling salip-menyalip, menanyakan pertanyaan, berencana akan, maka daripada itu, maju ke depan) dan 3 ungkapan idiomatik berpreposisi keliru (berdasarkan atas, bergantung kepada, terjadi atas), sehingga total menjadi **632**. Ditambah `TMS-007` (partikel pun yang wajib serangkai: ada pun, jika pun, andai pun, kalau pun, atau pun, kendati pun, sungguh pun, bagaimana pun, walau pun, biar pun, meski pun, sementang pun, dari Tabel 5.21 hlm. 119) dan `TMS-008` (angka berakhiran -an wajib bertanda hubung: tahun 1980an, Rp2.000an, dari Tabel 5.23 hlm. 122), sehingga total menjadi **634**. Ditambah empat kaidah tanda baca dari *Taktis Menyunting* (BRIN, 2019, hlm. 123-126): `TMS-009` spasi keliru pada tanda baca, `TMS-010` koma dan tanda tanya kalimat langsung yang jatuh di luar tanda petik, `TMS-011` elipsis tanpa spasi, dan `TMS-012` tanda hubung yang dipakai untuk rentang waktu alih-alih tanda pisah en dash, sehingga total menjadi **638**. Ditambah `TMS-013` (konjungsi korelatif yang memakai `tapi juga` alih-alih `tetapi juga` atau `melainkan juga`, Tabel 5.29 hlm. 128-129) dan `TMS-014` (kalimat tidak sepadan: subjek didahului preposisi pada pola `kepada`/`bagi` + `diharap(k)an`/`diminta`, Tabel 5.32 hlm. 130), sehingga total menjadi **640**. Ditambah `TMS-015` (`media masa` -> `media massa`, `nara blog` -> `narablog`; Zaim, 2018) dan `TMS-016` (`impelementasi`, `pelaksaan`, `instrument penelitian`; Sihombing dkk., 2024), sehingga total menjadi **642**. Ditambah `TMS-017` (kata depan `di` serangkai dengan nomina: `dimasa`, `diinternet`), `TMS-018` (imbuhan terpecah spasi: `memudah kan`, `menumbuh kembangkan`, `men translasi`), dan `TMS-019` (nama bahasa berhuruf kecil: `bahasa inggris`), ketiganya dari Kemas Ferri Rahman, *Komunikasi Perusahaan Melalui Tulisan* (BRIN, 2022, hlm. 34-35), sehingga total menjadi **645**. Ditambah `TMS-020` (gabungan kata bentuk bebas keliru diserangkai: `sumberdaya`, `tatausaha`, `jurutulis`, `serahterima`) dan `TMS-021` (unsur terikat keliru dipisah: `non migas`, `antar daerah`, `purna jual`, `pra sejarah`, `sub sistem`), keduanya dari Mustakim, *Bahasa Indonesia untuk Aparatur Pemerintah* (Badan Bahasa, 2016, hlm. 12-13), sehingga total menjadi **647**. Referensi: `references/bp2-2016-aparatur-pemerintah-gabungan-kata.md`. Ditambah lima kaidah surat dinas dari buku yang sama (hlm. 57-60): `TMS-022` (Kepada Yth. tanpa kata kepada), `TMS-023` (singkatan Jl./Jln./Telp./Tip.), `TMS-024` (format tanggal surat), `TMS-025` (jumlah lampiran), dan `TMS-026` (nomor surat diakhiri titik atau titik-hubung), sehingga total menjadi **652**. Referensi: `references/bp2-2016-aparatur-pemerintah-surat-dinas.md`. Dari bagian penutup surat dan Bab IV buku yang sama ditambah `TMS-027` (NIP berkapitalisasi campur atau berangka berspasi) dan `TMS-028` (pihak pemberi tembusan didahului Yth. atau diikuti *sebagai laporan*) menjadi **654**; `BPK-007` (*jam* alih-alih *pukul*) ternyata sudah bermesin — kesan "tanpa matcher" muncul karena blok lamanya tidak menyebut ID kaidah pada komentarnya — sehingga yang dilakukan adalah menambah bentuk label `Jam: 09.00` pada regex lama; dan `NIP` dikeluarkan dari pola `MBI-004` karena NIP pada blok tanda tangan surat resmi bukan data responden. Referensi: `references/bp2-2016-aparatur-pemerintah-penutup-surat-dan-laporan.md`. Referensi: `references/zaim-2018-serapan-ti-dan-sihombing-2024-diksi.md`. Referensi: `references/taktis-menyunting-brin-konjungsi-kalimat.md`. Referensi: `references/taktis-menyunting-brin-tanda-baca.md`. Referensi: `references/taktis-menyunting-brin-partikel-pun-angka.md`. Referensi: `references/taktis-menyunting-brin-lewah-idiomatik.md`. Referensi: `references/taktis-menyunting-brin-bentuk-terikat-gabungan-kata.md`. Referensi verbatim: `references/kesalahan-berbahasa-terbitan-ilmiah-kaltim-leksikal.md`; metadata referensi lama (2005, 170 hlm) dikoreksi menjadi cetakan 2009, xvi + 156 hlm. Referensi verbatim: `references/taktis-menyunting-brin-ejaan-kata.md`.
- **Matcher `BPBI-001`–`BPBI-005`** di `humanizer_id/matchers.py` — case-insensitive, `` word boundary; uji positif/negatif lolos tanpa false positive.
- **Ekstrak referensi verbatim + sitasi**: `references/bpbi-1-kata-badan-bahasa.md`, `references/bpbi-1-kalimat-badan-bahasa.md`, `references/bpbi-1-tanya-kebahasaan-badan-bahasa.md`, `references/bpbi-2-tanya-jawab-badan-bahasa.md`, `references/bpbi-1-lain-lain-badan-bahasa.md`, `references/bpbi-2-1-90-badan-bahasa.md`, `references/bpbi-1-sastra-badan-bahasa.md` (id.wikisource.org, domain publik UU No. 28/2014).

### Diperbaiki
- **Kontradiksi `CX11-002`**: entri sempat menyarankan `namun demikian` sebagai bentuk benar, padahal Buku Praktis 1 (`namun demikian` = *tetapi demikian* yang janggal) dan `PT-001` menyatakan salah. Saran diganti menjadi `meskipun demikian` / `(cukup 'namun')`.
- **`PT-001`** diperkaya sitasi Buku Praktis Bahasa Indonesia 1 sebagai sumber kedua.

### Dipertahankan
- `baud→baut`, `sutra→sutera`, `lembab→lembap` tercantum di buku namun **tidak diaktifkan** — `baud` sah sebagai satuan laju data, `sutra` sah dalam konteks akademik/keagamaan, `lembab` lazim dipakai (menunggu telaah semantik).
- `hisap→isap` dan `himbau→imbau` **tidak diaktifkan** — kontroversial dalam pemakaian modern.
- `mengetrapkan→menerapkan` dan `mengenyampingkan→mengesampingkan` dari BPBI1/Lain-lain **tidak diduplikasi** — sudah aktif di BPK-012 dan KRF-001.
- Pembahasan "majas vs gaya bahasa" (BPBI1/Sastra) hanya telaah terminologis — tidak dijadikan matcher.
- Pasangan BPBI2 **tidak diaktifkan**: `relawan->sukarelawan` (sumber merujuk KBBI 1996; KBBI V sudah memuat `relawan`), `para hadirin` (BPBI2 menilai tidak mubazir), `kurban/korban` (beda makna), `elit/elite` + `bonafid/bonafide` + `faksimil/faksimile` (pelafalan, false-positive tinggi).

## [2.4.5] — 2026-11-17

### Diperbaiki
- **Demote 6 kaidah sufiks asing ke `[telaah]`** (`TII-010`..`TII-014`, `TII-016`): pola *-ization, -logy, -ity, -ism, hyper-/poly-* rawan salah tangkap pada kata Indonesia (mis. *Laboratorium*), jadi dijadikan rujukan telaah, bukan aturan aktif.
- **Matcher `TII-015` lambang satuan salah kapital** — case-sensitive, menangkap *5 Newton*, *3 Kg*, *10 KM* tanpa salah tangkap lambang SI baku *N, J, W, kg, km, MB, GB*.
- **Konsol Windows UTF-8** — `main()` memaksa `stdout/stderr` ber-encoding UTF-8 agar panah/simbol laporan tidak membuat audit gagal di tengah jalan.
- Hapus `CUSTOM_RULES` mati milik kaidah yang di-demote.

### Diubah
- **`references/pupi-2004-kepmendiknas146.md`** — tulis ulang ekstrak verbatim.
- Blok `BW` sub-skill `ejaan-morfologi` kini 19 entri (menambah `TII-010`..`TII-016` sebagai butir 13–19).
- Angka kaidah terhitung ulang: **611 → 618** (582 aktif + 36 telaah).

## [2.4.4] — 2026-11-17

### Ditambahkan
- **12 kaidah penyerapan istilah dari PUPI** (Kepmendiknas 146/U/2004): `PUPI-002`..`PUPI-009` untuk bentuk serapan leksikal (*frekwensi, subyektif, propinsi, komplek, jaman, kaedah, managemen, ekstrim*) dan `PUPI-010`..`PUPI-013` untuk bentuk terikat (*pra-, ekstra-, anti-, multi-*).
- **`references/pupi-2004-kepmendiknas146.md`** — ekstrak verbatim 1.322 baris (Bab I–IV) termasuk tabel penyesuaian ejaan prefiks dan sufiks.
- **Blok `BW`** pada sub-skill `ejaan-morfologi` berisi 12 entri Pola → Perbaikan → Sebab plus tabel rujukan serapan sufiks/prefiks.

### Diperbaiki
- Blok `BV2` sub-skill `ejaan-morfologi`: butir 4–7 sebelumnya kehilangan **Perbaikan/Sebab** karena penggabungan baris.

### Catatan rilis
- Versi 2.4.1–2.4.3 tidak tercatat terpisah di berkas ini; ketiganya berisi integrasi EYD V, EYD 1987, dan PUEBI 2015 (kaidah `EYD-058`..`EYD-064`).

## [2.4.0] — 2026-11-17

### Ditambahkan
- **Installer `humanizer-id install`** — menyalin `SKILL.md`, `skills/`, `scripts/`, `humanizer_id/`, dan `data/` ke folder agen AI (Hermes Agent, Claude Code, Google Antigravity) secara otomatis. Deteksi target otomatis; `--target` memilih satu, `--with-references` menyertakan `references/`.
- **Test konsistensi versi** — pytest yang memastikan `pyproject.toml`, `__init__.py`, `SKILL.md` induk, 5 sub-skill, dan `uv.lock` selalu seversi.

## [2.3.1] — 2026-11-17

### Diperbaiki
- Deskripsi paket (README) di PyPI dan rujukan eksternal yang tidak relevan dihapus.
- 75 blok sub-skill dinormalisasi ke format entri **Pola → Perbaikan → Sebab** dengan sitasi halaman.

## [2.3.0] — 2026-11-17

### Ditambahkan
- **Mode AFTER — audit bernomor** (`--report`): temuan bernomor `humanizer/audit-NNN-YYYY-MM-DD.md` tanpa menyunting naskah; eksekusi hanya nomor yang disetujui.
- Generator laporan markdown `humanizer_id/report.py` dengan prioritas HIGH/MEDIUM/LOW.

## [2.2.0] — 2026-11-16

### Ditambahkan
- **Delivery Gate** PASS/FAIL dan Checklist Editorial pada `SKILL.md`.
- Konvensi entri kaidah Pola → Perbaikan → Sebab.

## [2.1.0] — 2026-11-16

### Diubah
- `SKILL.md` monolitik (~113 KB) dipecah menjadi induk ~195 baris + 5 sub-skill on-demand (ejaan-morfologi, sintaksis, diksi-istilah, wacana-retorika, naskah-resmi).

## [2.0.0] — 2026-11-15

### Ditambahkan
- 592 kaidah preskriptif total (integrasi pedoman jurnal Dikbud, surat-menyurat Pusat Bahasa, modul jurnalistik).

## Sebelum 2.0.0

Riwayat v1.x (mesin audit deterministik, autofix, glosarium lintas bidang) tersedia di [Releases](https://github.com/apissaj/humanizer-id/releases).
