# Panduan Preset Gaya Penulisan Kampus

Panduan untuk menyesuaikan standar editorial bahasa Indonesia dengan konvensi penulisan karya ilmiah di berbagai perguruan tinggi menggunakan sistem **Preset Kampus** (`data/pedoman-kampus.json`).

---

## 1. Konsep Preset Kampus

Setiap perguruan tinggi memiliki konvensi berbeda di 3 aspek yang memengaruhi penyuntingan bahasa:
1. **Gaya Sitasi** (IEEE vs APA vs Vancouver vs Harvard).
2. **Kaidah Penomoran & Rujukan** (Persamaan, Tabel, Gambar).
3. **Register Bahasa** (pasif ilmiah, impersonal, penomoran sub-bab).

Preset kampus menentukan **aturan penyuntingan** yang harus dipatuhi oleh Humanizer ID saat mengolah naskah mahasiswa/peneliti kampus tersebut.

---

## 2. Daftar Preset Kampus Bawaan

| Kode Kampus | Institusi | Gaya Sitasi | Kaidah Penyuntingan Khas |
|---|---|---|---|
| `ui` | Universitas Indonesia | APA / IEEE | Dwibahasa abstrak, rujukan Tabel/Gambar bernomor bab (Tabel 1.1) |
| `itb` | ITB | IEEE / Harvard / APA | Persamaan wajib bernomor `(1.1)` di kurung; sampul minimalis |
| `ugm` | UGM | IEEE / APA | Rujukan rumus wajib `Persamaan (nomor)`; Simpulan vs Saran tegas dipisah |
| `its` | ITS | IEEE | Tinjauan pustaka menekankan state-of-the-art 5 tahun terakhir |
| `ipb` | IPB University | Name-Year | Sub-bab TANPA titik akhir (`1.1 Latar Belakang`); indentasi 1 cm; nama ilmiah spesies miring lengkap dengan autoritas |
| `undip` | UNDIP | IEEE / APA / Harvard | Hierarki judul bab kapital tebal di tengah |
| `unpad` | UNPAD | APA / Chicago | Abstrak maksimal 250 kata satu paragraf spasi tunggal |
| `unair` | UNAIR | Vancouver / APA | Sitasi biomedis bernomor (Vancouver), keduanya disesuaikan per fakultas |
| `ub` | UB | IEEE / APA | Larangan konjungsi di awal kalimat; paragraf minimal 2 kalimat efektif |
| `telkom` | Telkom University | IEEE | Artikel IEEE sebagai syarat kelulusan; GitHub & dataset publik wajib ada di daftar pustaka |
| `udinus` | UDINUS | IEEE / APA | Sistematika skripsi rekayasa perangkat lunak wajib uji fungsionalitas black-box dan uji pengguna |

---

## 3. Contoh Konfigurasi

### A. Skripsi Informatika UDINUS (IEEE)
```markdown
## Bab III Metodologi Penelitian

Pengujian fungsionalitas dilakukan menggunakan metode *black-box testing*
(Gronning et al., 2022) terhadap 34 skenario uji. Hasil pengujian
disajikan pada Tabel 3.2.
```
**Penyuntingan Humanizer ID untuk preset `udinus`:**
- Sitasi dalam kurung IEEE-style: `(...et al., tahun)`.
- Rujukan tabel bernomor bab presisi: `Tabel 3.2`.
- Register impersonal: tanpa "saya/kami".
- Ejaan teknis konsisten: *black-box testing* miring (istilah asing belum diserap KBBI).

### B. Skripsi Kesehatan UNAIR (Vancouver)
```markdown
Terdapat hubungan signifikan antara prevalensi stunting dengan asupan
protein pada anak usia balita [12, 14].
```
**Penyuntingan Humanizer ID untuk preset `unair`:**
- Sitasi bernomor kurung siku Vancouver: `[12, 14]`.
- Modalitas tepat: "terdapat hubungan signifikan" bukan "membuktikan hubungan".
- Kata ilmiah baku KBBI: *prevalensi*, *asupan protein*.

### C. Skripsi Pertanian IPB (Name-Year System)
```markdown
Rice cultivar (*Oryza sativa* L. spp. *japonica*) yang ditanam pada
tanah aluvial menunjukkan respons morfologi yang bervariasi (Kusuma et al.,
2024; Ramadhan & Sari, 2023).
```
**Penyuntingan Humanizer ID untuk preset `ipb`:**
- Nama ilmiah miring lengkap dengan *autoritas* (L.) pada penyebutan pertama.
- Sitasi nama-tahun berkurung (Kusuma et al., 2024).
- Penomoran sub-bab tanpa titik akhir.

---

## 4. Integrasi dengan Skill Humanizer ID

Untuk mengaktifkan preset kampus tertentu, cukup sebutkan kampus di prompt awal:
- "Sunting skripsi ini dengan preset **udinus**".
- "Perbaiki bahasa paper ini, kampusku **its**, pastikan sitasi IEEE dan format persamaan tepat".

Humanizer ID akan otomatis:
1. Membaca preset kampus dari `data/pedoman-kampus.json`.
2. Menerapkan aturan sitasi, penomoran, dan register sesuai kaidah kampus.
3. Menyuntikkan aturan khusus kampus ke dalam Protokol Diff Beranotasi agar setiap perubahan dijelaskan alasan kaidahnya.

---

## 5. Cara Memperluas Daftar Kampus

Tambahkan entri baru di `data/pedoman-kampus.json` dengan struktur:

```json
"kampus_baru": {
  "nama": "Universitas Baru",
  "pedoman": "Buku Pedoman Skripsi Universitas Baru",
  "margin_cm": {"atas": 4.0, "bawah": 3.0, "kiri": 4.0, "kanan": 3.0},
  "gaya_sitasi_umum": "APA",
  "aturan_khusus": ["Aturan 1...", "Aturan 2..."]
}
```
