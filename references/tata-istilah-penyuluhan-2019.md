# Ringkasan Ekstraksi Rujukan: Tata Istilah (Seri Penyuluhan Bahasa Indonesia, Qodratillah 2019)

## 1. Identitas Dokumen Sumber

- **Judul Buku:** *Tata Istilah: Seri Penyuluhan Bahasa Indonesia*
- **Penulis:** Dra. Meity Taqdir Qodratillah, M.Hum.
- **Penyunting:** Setyo Untoro, S.S., M.Hum.
- **Penerbit:** Badan Pengembangan dan Pembinaan Bahasa, Kementerian Pendidikan dan Kebudayaan
- **Tahun Terbit:** 2019
- **Tebal:** xii + 78 halaman
- **Sifat:** Bahan penguatan pemasyarakatan bahasa Indonesia yang baik dan benar; pemutakhiran *Tata Istilah Indonesia* (1978) untuk era KBBI V dan ISO/TC 37.

---

## 2. Intisari Kaidah Preskriptif

### A. Kerancuan Paradigma Imbuhan ber- vs peN-: pemukiman vs permukiman (hlm. 46–48)
Paradigma mukim membedakan tiga bentuk turunan:
- **bermukim** = aktivitas tinggal (ber- + mukim).
- **pemukim** = pelaku, 'orang yang bermukim'.
- **permukiman** = tempat/ihwal bermukim — padanan *residential area*.
- **pemukiman** = 'proses, cara, atau perbuatan memukimkan' — BUKAN padanan kawasan tempat tinggal.

Pemakaian yang keliru dan lazim ditemukan di naskah: *pemukiman padat/kumuh/liar* — yang tepat ialah **permukiman padat/kumuh/liar**.

### B. Kerancuan paradigma: perubahan vs pengubahan (hlm. 48–51)
Paradigma ubah membedakan dua cabang:
- **berubah → peubah → perubahan** = 'ihwal berubah; keadaan yang berubah'.
- **mengubah → pengubah → pengubahan → ubahan** = 'proses mengubah; tindakan mengubah; hasil mengubah'.

Akibatnya: *perubahan iklim* (gejala keadaan) tepat; *pengubahan iklim* keliru kecuali maksudnya tindakan sengaja mengubah iklim.

### C. Metanalisis palsu akhiran asing: -itas dan -isasi (hlm. 42, 55–56)
Unsur serapan **-itas** hanya sah pada akar asing yang memang berakhiran *-ity/-iteit* (universitas, realitas, aktivitas, efektivitas). Unsur **-isasi** hanya sah pada akar *-ization/-isation* (standardisasi dari *standardization*). Contoh metanalisis keliru yang dicontoh buku:
- \*sinergitas — bahasa sumber tidak mengenal *synergity*; yang baku **sinergi/kesinergian**.
- \*standarisasi — akar aslinya *standardization*; yang tepat **standardisasi**.
- \*efektifitas, \*aktifitas — vokalisasi akar keliru; yang tepat **efektivitas, aktivitas**.

### D. Penulisan gabungan bentuk bebas: terpisah, bukan serangkai (hlm. 23, 36)
Gabungan dua bentuk bebas ditulis terpisah. Buku mencantumkan pasangan pemadanan baku:
- **ibu kota** bukan *ibukota*
- **kerja sama** bukan *kerjasama*
- **batu bara** bukan *batubara*
- **anak perusahaan** bukan *anakperusahaan*
- **toko serba ada** (toserba) bukan *tokoserbaada*

Serangkai hanya untuk unsur terikat (antar-, pra-, swa-, nir-) atau gabungan yang sudah bersenyawa.

### E. Peluluhan peN- pada nomina pelaku: bentuk baku (hlm. 23)
Bentuk peN- yang sesuai kaidah:
- **penerjemah** bukan *penterjemah*
- **perajin** bukan *pengrajin*
- **penyurvei** bukan *pensurvei*
- **pengebom** bukan *pembom*

### F. Eufoni: padanan yang tidak sedap didengar ditolak (hlm. 22)
Padanan lama *mangkus* (effective) dan *sangkil* (efficient) tidak berterima karena tidak eufonik; serapan **efektif** dan **efisien** yang dipakai. Nilai rasa juga menjadi pertimbangan: *panti wreda > rumah jompo; tunawisma > gelandangan; pramusiwi > penjaga anak; mantan > bekas* (untuk orang).

### G. Unsur terikat produktif untuk pemadanan (hlm. 60–66)
Daftar unsur terikat dan padanannya: **adi-** (super), **antar-** (inter-), **awa-** (de-/dis-, 'menghilangkan': awaair = dewater), **dasa-** (deca-), **dwi-** (bi-/di-), **lir-** (-like: lirruang = spacelike), **maha-** (omni-/emperor), **nir-** (a-/in-/-less), **pasca-** (post-), **pra-** (pre-/ante-), **swa-** (self-), **tak-** (un-/in-/non- 'tidak'), **tuna-** (-less 'kurang': tunakarya = unemployed).

---

## 3. Pemetaan ke Dataset `data/kalke-indonesia.json`

| ID | Kaidah | Kategori | Kode Regex Utama |
|---|---|---|---|
| `TIQ-001` | *pemukiman* untuk kawasan (harusnya *permukiman*) | `kata_baku_dan_morfologi` | `\bpemukiman\s+(padat\|kumuh\|liar\|...)\b` |
| `TIQ-002` | *pengubahan* untuk keadaan (harusnya *perubahan*) | `kata_baku_dan_morfologi` | `\bpengubahan\s+(iklim\|sosial\|...)\b` |
| `TIQ-003` | Metanalisis -itas/-isasi palsu (sinergitas, standarisasi) | `kata_baku_dan_morfologi` | `\b(sinergitas\|standarisasi\|efektifitas\|aktifitas)\b` |
| `TIQ-004` | Gabungan bentuk bebas serangkai (ibukota, kerjasama) | `kata_baku_dan_morfologi` | `\b(ibukota\|kerjasama\|batubara\|...)\b` |
| `TIQ-005` | peN- salah luluh (pengrajin, penterjemah) | `kata_baku_dan_morfologi` | `\b(pengrajin\|penterjemah\|pensurvei\|pembom)\b` |
