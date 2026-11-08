# Ringkasan Ekstraksi Rujukan: Paragraf — Seri Penyuluhan Bahasa Indonesia (Suladi, Badan Bahasa 2019)

## 1. Identitas Dokumen Sumber

- **Judul Buku:** *Paragraf: Seri Penyuluhan Bahasa Indonesia*
- **Penulis:** Drs. Suladi, M.Pd.
- **Penyunting:** Eko Marini, M.Hum.
- **Pengantar:** Hurip Danu Ismadi (Kepala Pusat Pembinaan Bahasa dan Sastra)
- **Penerbit:** Badan Pengembangan Bahasa dan Perbukuan, Kementerian Pendidikan dan Kebudayaan
- **Tahun Terbit:** 2019 (Jakarta, Oktober 2019)
- **Tebal:** x + 129 halaman
- **Sifat:** Bahan penguatan pemasyarakatan bahasa Indonesia; hakikat paragraf (gagasan utama, struktur), jenis paragraf (pernalaran, gaya pengungkapan, urutan), kepaduan (konjungsi, referensi, substitusi, elipsis, sinonimi, antonimi, hiponimi, meronimi, repetisi), kelengkapan/ketuntasan, keruntutan, konsistensi sudut pandang, dan pengembangan paragraf.

## 2. Intisari Kaidah Preskriptif

### A. Referensi Anaforis vs Kataforis (hlm. 33–34)
Referensi endoforis dibedakan menurut arah acuan:
- **anaforis**: mengacu ke belakang (kiri) pada maujud yang sudah disebut — lazim pronomina persona (enklitik *-nya*, kata ganti orang III) atau pronomina demonstrativa.
- **kataforis**: mengacu ke depan (kanan) pada maujud yang akan disebut.
Syarat mutlak: konstituen pengacuan dan yang diacukan harus **berkoreferensi** (memiliki referen yang sama). Kerancuan arah acuan (pronomina muncul sebelum anteseden yang tidak eksplisit) merusak kepaduan antarkalimat.

### B. Keruntutan Penanda Ordinal Perincian (hlm. 55–56, contoh 43)
Paragraf perincian dengan gagasan utama 'beberapa faktor' menuntut penanda penjumlah ordinal yang **runtut dan konsisten**: *Pertama, Kedua, Ketiga, Keempat*. Buku menampilkan contoh keliru (*Pertama, Kedua, Ketiga, Ketiga*) dan menegaskan keruntutan sebagai syarat paragraf yang baik: informasi disajikan urut tanpa melompat (hlm. 56), termasuk urutan penanda perinciannya.

### C. Kelengkapan dan Ketuntasan Perincian (hlm. 55)
Gagasan utama berbilangan pasti ('tiga faktor') wajib dikembangkan dengan jumlah penjelas yang sama persis; pembahasan yang tidak tuntas menghasilkan simpulan yang salah, tidak sahih, dan tidak valid. Ketuntasan klasifikasi menuntut tidak ada bagian yang tak masuk kelompok.

### D. Konsistensi Sudut Pandang (hlm. 58–61)
Sudut pandang (orang pertama *aku/saya/kita*, orang ketiga *dia*, pengamat serba tahu, campuran) wajib dipilih dan dipertahankan ajek dari awal hingga akhir; peralihan sudut pandang tanpa pola menyebabkan paragraf tidak konsisten.

### E. Kaidah Lain yang Terdokumentasi (sudah dicakup entri lama)
- Kesatuan paragraf: dua gagasan utama harus dipisah menjadi dua paragraf (hlm. 14–17, contoh 6a/6b) — bukan kandidat matcher (butuh telaah manusia).
- Konjungsi antarkalimat sesuai hubungan logis (hlm. 18–27): *namun/walaupun demikian* (pertentangan), *selanjutnya/kemudian* (kelanjutan), *selain itu/lagi pula* (penambahan), *sebaliknya* (kebalikan), *bahkan/malahan* (penguatan), *oleh karena itu/jadi* (konsekuensi), *dengan demikian* (akibat).
- Substitusi leksikal untuk menghindari repetisi monoton (hlm. 40–41).

## 3. Pemetaan ke Dataset `data/kalke-indonesia.json`

| ID | Kaidah | Kategori | Kode Regex Utama |
|---|---|---|---|
| `PRL-001` | Referensi kataforis rancu: pronomina demonstratif tanpa anteseden eksplisit di awal paragraf | `retorika_klise_ai` | `^(Dengan begitu\|Dengan demikian\|Karena itu\|Setelah menyelidikinya)\b[^.!?]*\b(itu\|ini\|ia\|dia)\b` |
| `PRL-002` | Penomoran ordinal perincian berulang/lompat (*Pertama, Kedua, Ketiga, Ketiga*) | `retorika_klise_ai` | `\bPertama\b[^P]{0,80}?Kedua\b[^K]{0,80}?Ketiga\b[^P]{0,80}?Ketiga\b` |
