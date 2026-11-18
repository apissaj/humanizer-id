# Buku Praktis Bahasa Indonesia 2 — Lanjutan (Bahasa, Istilah, dan Kalimat)

**Sumber primer:** Pusat Bahasa (Badan Pengembangan dan Pembinaan Bahasa), *Buku Praktis Bahasa Indonesia 2*, subhalaman `Bahasa`, `Istilah`, dan `Kalimat` via Wikisource Indonesia (`https://id.wikisource.org/wiki/Buku_Praktis_Bahasa_Indonesia_2`).  
**Status domain:** domain publik Indonesia (UU No. 28 Tahun 2014 tentang Hak Cipta, Pasal 42).  
**Teks ekstraksi:** `work/bpbi2-bahasa-wikitext.txt`, `work/bpbi2-istilah-wikitext.txt`, `work/bpbi2-kalimat-wikitext.txt`.  
**Catatan:** Melengkapi [bpbi-2-1-90-badan-bahasa.md](bpbi-2-1-90-badan-bahasa.md) (bagian 1–90).

---

## 1. Subhalaman *Bahasa* — Ketepatan Ungkapan Resmi & Wilayah Waktu

### A. `BPBI-008` — Ungkapan Dirgahayu & Wilayah Waktu Indonesia
> **SALAH:** *DIRGAHAYU HUT RI KE 52 / DIRGAHAYU RI KE 52 / HARI ULANG TAHUN REPUBLIK INDONESIA KE 52 / SELAMAT DIRGAHAYU RI KE-52 / H.U.T.R.I. KE-52*  
> **BENAR:** *DIRGAHAYU REPUBLIK INDONESIA / DIRGAHAYU RI / HARI ULANG TAHUN KE-52 REPUBLIK INDONESIA / HUT KE-52 RI*

- **Sebab:** *Dirgahayu* bermakna 'berumur panjang' sehingga tidak boleh diikuti kata *HUT* atau bilangan tingkat *ke-N*. Pada frasa *HUT ke-N RI*, pewatas bilangan tingkat *ke-N* menerangkan *HUT*, bukan *RI* (bukan *RI ke-52*, karena Republik Indonesia hanya satu).
- **WIB vs BBWI:** Keppres RI No. 41 Tahun 1987 membakukan singkatan wilayah waktu Indonesia menjadi **WIB** (Waktu Indonesia Barat), **Wita**, dan **WIT** — bukan **BBWI** (*Bagian Barat Wilayah Indonesia* / *Bagian Barat Waktu Indonesia* yang membalik hukum DM).

### B. Penulisan Nama Geografi
- Nama geografi terdiri atas dua unsur ditulis serangkai (*Bandaaceh, Kulonprogo, Sukabumi, Palangkaraya, Bukittinggi*), kecuali unsur tiga kata atau lebih (*Ogan Komering Ulu*) dan unsur arah mata angin (*Jakarta Barat, Kalimantan Timur*). *(Catatan: dalam praktik dokumen pemerintahan modern, ejaan resmi UU pembentukan daerah seperti `Palangka Raya`, `Banda Aceh`, `Kulon Progo` mengikuti nama diri peraturan; dicatat sebagai `[telaah]` bukan regex.)*

---

## 2. Subhalaman *Kalimat* — Kerancuan & Kelengkapan Unsur

### A. `BPBI-009` — Pemilihan Konjungsi `Bahwa` vs `Agar/Supaya`
> *Tepatkah pemakaian kata bahwa pada kalimat "Saya menganjurkan bahwa masyarakat tidak mudah terpancing isu"?*  
> Pemakaian kata *bahwa* pada kalimat itu tidak tepat sebab induk kalimat dan anak kalimat menyatakan hubungan tujuan atau harapan yang diisyaratkan oleh predikat seperti *menganjurkan, mengharapkan, mengimbau, memohon*. Hubungan tersebut wajib ditandai kata penghubung **agar** atau **supaya**. Kata *bahwa* dipakai untuk verba penegasan (*mengatakan, menegaskan, melaporkan*).

### B. `SPK-014` — Kerancuan `Menurut pada X ... mengatakan bahwa`
> *(1) Menurut pada pakar sejarah mengatakan bahwa Candi Borobudur dibangun pada masa Kerajaan Syailendra.*  
> Perbaikan: *(1a) Menurut pakar sejarah, Candi Borobudur dibangun...* atau *(1b) Pakar sejarah mengatakan bahwa Candi Borobudur dibangun...*

### C. Kaidah Surat-Menyurat & Kelengkapan Unsur (`[telaah]`)
- **Pembuka surat `Bersama ini` vs `Dengan ini`:** *Bersama ini* hanya sah apabila surat menyertakan lampiran atau pengiriman barang; surat pemberitahuan tanpa lampiran memakai *Dengan ini* atau langsung verba (*Kami beri tahukan bahwa...*).
- **Penutup surat `Demikian agar Saudara maklum adanya`:** Bukan kalimat lengkap (hanya anak kalimat tanpa induk kalimat); hapus atau ganti kalimat lengkap (*Atas perhatian Saudara, kami ucapkan terima kasih.*).
- **Subjek & predikat wajib hadir:** *Pembangunan itu untuk menyejahterakan masyarakat* (tidak berpredikat) → *Pembangunan itu bertujuan menyejahterakan masyarakat*; *Bagi para siswa... harus melunasi* (subjek berpreposisi) → *Para siswa... harus melunasi*.

---

## 3. Subhalaman *Istilah* — Padanan Istilah Asing Terkurasi untuk Glosarium

Padanan resmi Pusat Bahasa yang relevan untuk naskah bisnis, manajemen, teknologi, dan publik (ditambahkan ke `data/glosarium-lintas-bidang.json` setelah verifikasi nol benturan terhadap korpus negatif):

| Istilah Asing | Padanan Baku Indonesia | Ranah |
|---|---|---|
| `after-sales service` | `layanan pascajual` | Bisnis & Manajemen |
| `customer service` | `layanan pelanggan / layanan nasabah` | Bisnis & Manajemen |
| `cash flow` | `arus kas` | Bisnis & Manajemen |
| `overbooking` | `tempah lajak` | Bisnis & Manajemen |
| `due diligence` | `uji tuntas / kecermatpatutan` | Bisnis & Manajemen |
| `site plan` | `rencana tapak` | Bisnis & Manajemen |
| `master plan` | `rencana induk` | Bisnis & Manajemen |
| `standby loan` | `pinjaman siaga` | Bisnis & Manajemen |
| `showroom` | `ruang pamer / ruang peraga` | Bisnis & Manajemen |
| `boarding pass` | `pas naik` | Bisnis & Manajemen |
| `airworthy` | `laik terbang` | Teknologi & Rekayasa |
| `vacuum cleaner` | `pengisap debu` | Teknologi & Rekayasa |
| `basement` | `basemen / ruang bawah tanah` | Teknologi & Rekayasa |
