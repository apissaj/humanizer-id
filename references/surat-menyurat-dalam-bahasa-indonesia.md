# Ekstrak Kaidah: Seri Penyuluhan Surat-Menyurat dalam Bahasa Indonesia (Pusat Bahasa)

## 1. Identitas Dokumen Sumber

- **Judul Buku:** *Surat-Menyurat dalam Bahasa Indonesia: Seri Penyuluhan 2*
- **Penulis/Penyusun:** Tim Pusat Pembinaan dan Pengembangan Bahasa, Departemen Pendidikan dan Kebudayaan RI, Jakarta (1991)
- **Tebal:** viii + 48 hlm. Berkas dump: `work/text_dumps/surat_menyurat_dalam_bahasa_indonesia.txt` (`HAL 1` s.d. `HAL 55`).
- **Paginasi:** Offset penanda dump `HAL N − 6 = hlm. cetak` (dump `HAL 18` = cetak `hlm. 12`; `HAL 34` = cetak `hlm. 28`; `HAL 42` = cetak `hlm. 36`).
- **Fokus Ekstraksi:** Standar bahasa surat dinas/resmi: kejelasan struktur gramatikal (S-P-O-K), eliminasi kalke dan ragam lisan, penulisan alamat dan salam, perbaikan kalimat penutup mubazir, serta penghapusan enklitika *-nya* tak tentu.

---

## 2. Peta Kaidah Preskriptif (SMD-001..016)

### A. Struktur Kepala, Tanggal, & Alamat Surat

- **ID: SMD-001** (hlm. 12; HAL 18)
  - **Kaidah Tanggal Surat:** Tanggal surat dinas yang berkop/berkepala surat **tidak didahului nama kota** karena nama kota sudah tercantum pada kepala surat. Nama bulan ditulis dengan huruf utuh (bukan angka/singkatan). Tidak diakhiri tanda titik atau titik koma.
  - **Baku:** `22 Maret 1990`
  - **Salah:** *Jakarta, 22-3-1990*; *Jakarta 22 Maret 1990;*; *22 Mrt 90*; *22.03.90*.

- **ID: SMD-002** (hlm. 12–13; HAL 18–19)
  - **Kaidah Penulisan Nomor & Lampiran:** Singkatan *No.* dan *Lamp.* wajib taat-asas (konsisten). Jumlah lampiran ditulis dengan huruf bilangan kata, bukan angka semata (`Satu berkas`, `Dua eksemplar`).

- **ID: SMD-003** (hlm. 14–16; HAL 20–22, 42)
  - **Kaidah Alamat Tujuan & Sapaan:**
    - Kata *Kepada* di depan *Yth.* dianjurkan ditiadakan karena mubazir (surat langsung mengarah ke penerima).
    - Kata sapaan *Bapak/Ibu/Saudara* hanya dipakai jika diikuti nama orang, bukan nama jabatan/instansi.
    - **Baku:** `Yth. Manajer PT Rekabusana Anggun`, `Yth. Bapak Sukoco`.
    - **Salah:** *Kepada Yth. Bapak Manajer...*; *Kepada Yth. PT...*.
    - Kata `di-` di depan nama kota tujuan tidak perlu diberi tanda hubung (`di Jakarta`, bukan *di- Jakarta .-*) dan pada surat resmi alamat tujuan cukup di lembar surat / amplop.

### B. Salam Pembuka & Salam Penutup

- **ID: SMD-004** (hlm. 17–18; HAL 23–24)
  - Salam pembuka dan salam penutup diakhiri tanda koma `,`. Huruf pertama kata pertama kapital, kata kedua huruf kecil.
  - **Baku:** `Dengan hormat,`, `Hormat kami,`, `Hormat saya,`, `Salam takzim,`.
  - **Salah:** *Dengan Hormat*; *Hormat Saya.*; *Wasalam -*.

### C. Paragraf Isi & Bahasa Surat

- **ID: SMD-005** (hlm. 23–24; HAL 29–30)
  - **Tiga Ciri Bahasa Surat:** Jelas (memiliki subjek, predikat, objek, dan keterangan yang terang), lugas (tidak bermakna ganda/ambigu, hemat kata), dan komunikatif (pokok pikiran runtut dan logis).

- **ID: SMD-006** (hlm. 28; HAL 34)
  - **Kaidah Penulisan Tingkat/HUT:** Penulisan bilangan bertingkat menggunakan angka Arab berawalan *ke-* ATAU angka Romawi tanpa *ke-*.
  - **Baku:** `ke-45` atau `XLV`.
  - **Salah:** *ke-XLV* (kontaminasi angka Romawi dengan awalan ke-).

- **ID: SMD-007** (hlm. 18–19, 28; HAL 24–25, 34)
  - **Kaidah Penutup Surat & Larangan Enklitika *-nya*:**
    - Enklitika *-nya* mengacu pada orang ketiga tunggal (*buku-dia*); menggunakan *atas perhatiannya* pada surat yang ditujukan kepada lawan tutur (*Bapak/Ibu/Saudara*) adalah kesalahan acuan pronomina.
    - **Baku:** `Atas perhatian Bapak/Ibu/Saudara, kami mengucapkan terima kasih.`
    - **Salah:** *Atas perhatiannya, diucapkan terima kasih.*
    - **Salah Eufemisme Berlebih:** *...dihaturkan beribu-ribu terima kasih* (kata *dihaturkan* adalah kalke ragam daerah krama Jawa; gunakan *kami mengucapkan*).

### D. Bentuk Frasa & Kata Majemuk Surat

- **ID: SMD-008** (hlm. 30; HAL 36, 42)
  - **Gabungan Kata Berawalan:** Imbuhan yang hanya melekat di awal kata majemuk ditulis terpisah: `berlipat ganda`, `bertanggung jawab`, `tersebar luas`, `bergaris bawah`, `berolah raga`. Jika mendapat konfiks pengapit, ditulis serangkai: `pertanggungjawaban`, `melipatgandakan`.

- **ID: SMD-009** (hlm. 36; HAL 42)
  - **Eliminasi Frasa Kuno/Mubazir:**
    - Hindari rumus klise: *Demikianlah harap maklum*, *Demikian agar menjadikan periksa*, *Bersama ini saya kabarkan*.
    - Gunakan penegasan langsung: "Demikian surat permohonan ini kami sampaikan."

---

## 3. Calon Aturan untuk Engine & Dataset

1. `ke-45` / `XLV` $\leftarrow$ `ke-XLV` / `ke-IV` / `ke-X` (kontaminasi bilangan bertingkat Romawi)
2. `kami mengucapkan terima kasih` $\leftarrow$ `dihaturkan terima kasih` / `dihaturkan beribu-ribu terima kasih`
3. `atas perhatian Saudara / Bapak / Ibu` $\leftarrow$ `atas perhatiannya` (pada posisi penutup surat)
