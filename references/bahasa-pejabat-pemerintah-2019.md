# Ringkasan Ekstraksi Rujukan: Bahasa Indonesia untuk Pejabat Pemerintah (Mullyana dkk., 2019)

## 1. Identitas Dokumen Sumber

- **Judul Buku:** *Bahasa Indonesia untuk Pejabat Pemerintah: Seri Penyuluhan Bahasa Indonesia*
- **Penulis:** Dadang Mullyana, dkk.
- **Penerbit:** Badan Pengembangan Bahasa dan Perbukuan, Kementerian Pendidikan dan Kebudayaan
- **Tahun Terbit:** 2019
- **Tebal:** 93 halaman
- **Sifat:** Bahan penyuluhan resmi bahasa kedinasan bagi aparatur pemerintah; mencakup ekonomi bahasa, pilihan kata cermat, struktur kalimat dinas, korespondensi, dan nota dinas.

## 2. Intisari Kaidah Preskriptif

### A. Ekonomi Bahasa: Verba Nominal vs Verba Tunggal (hlm. 37)
Jika ada kata atau ungkapan yang lebih singkat, hindari bentuk panjang yang tidak ekonomis:
- *disebabkan oleh fakta* → **karena**
- *mengajukan saran* → **menyarankan**
- *melakukan kunjungan* → **berkunjung**
- *mengeluarkan pemberitahuan* → **memberitahukan**
- *meninggalkan kesan yang dalam* → **mengesankan**

### B. Pasif Diri Tak Boleh Tersisip Adverbia (hlm. 48)
Dalam kalimat pasif persona, pronomina diri (*kami, kita, saya, ku, mu*) dan verba pangkal tidak boleh dipisahkan oleh adverbia (*sudah, belum, akan, sedang, telah*):
- *\*Masalah itu kami sudah laporkan* → **Masalah itu sudah kami laporkan** atau **Masalah itu kami laporkan**
- *\*Laporan itu kita belum bahas* → **Laporan itu belum kita bahas**

### C. Nomina Deverbal Salah Predikat Pasif (hlm. 48–49)
Nomina tindakan (*pelaksanaan, perencanaan, penyusunan*) tidak bernalar jika dijadikan penderita verba pasif yang sama maknanya:
- *\*Pelaksanaan tugas itu akan dilaksanakan bulan depan* — yang dilaksanakan adalah tugas, bukan pelaksanaan; perbaikan: **Pelaksanaan tugas itu akan dimulai bulan depan** atau **Tugas itu akan dilaksanakan bulan depan**.

### D. Verba Transitif Diikuti Preposisi Perihal (hlm. 39)
Kata *tentang, mengenai, daripada* di belakang predikat verba transitif (*membahas, membicarakan, membangun*) berstatus kata mubazir:
- *\*Rapat membahas tentang usulan* → **Rapat membahas usulan**
- *\*Pemerintah membicarakan mengenai hal itu* → **Pemerintah membicarakan hal itu**

## 3. Pemetaan ke Dataset `data/kalke-indonesia.json`

| ID | Kaidah | Kategori | Kode Regex Utama |
|---|---|---|---|
| `PJB-001` | Verba nominal panjang mubazir (*melakukan kunjungan*, *mengajukan saran*) | `retorika_klise_ai` | `\b(melakukan\s+kunjungan\|mengajukan\s+saran\|...)\b` |
| `PJB-002` | Pasif persona tersisip adverbia (*kami sudah laporkan*) | `retorika_klise_ai` | `\b(kami\|kita\|saya)\s+(sudah\|belum\|akan\|...)\s+(laporkan\|sampaikan\|...)\b` |
| `PJB-003` | Nomina deverbal salah predikat pasif (*Pelaksanaan ... dilaksanakan*) | `retorika_klise_ai` | `\b(Pelaksanaan\|Perencanaan\|...)\b[^.!?]*\b(dilaksanakan\|direncanakan\|...)\b` |
| `PJB-004` | Verba transitif diikuti preposisi perihal (*membahas tentang/mengenai*) | `retorika_klise_ai` | `\b(membahas\|membicarakan\|...)\s+(tentang\|mengenai\|daripada)\b` |
