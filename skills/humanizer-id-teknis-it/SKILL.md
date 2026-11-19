---
name: humanizer-id-teknis-it
description: Use when auditing or editing Indonesian technical documentation, software engineering docs, IT proposals, READMEs, RFCs, or computer science/engineering papers.
version: 2.4.6
author: Hafizh Muzani / Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [writing, editing, bahasa-indonesia, teknis, it, rekayasa, dokumentasi]
    category: creative
    homepage: https://github.com/apissaj/humanizer-id
    parent: humanizer-id
---

# Humanizer ID — Dokumentasi Teknis, TI & Rekayasa

Sub-kaidah domain Humanizer ID untuk dokumentasi perangkat lunak, RFC, spesifikasi arsitektur, README, proposal TI, serta makalah teknik/informatika (*Penyerapan Istilah TI*, Zaim 2018; Glosarium PASTI/BPBI TI; EYD V tipografi kode & satuan; pedoman teknik UI/ITB/ITS/Telkom/UDINUS). Muat berkas ini setelah `humanizer-id` (induk) dengan `--preset teknis`.

---

### A. Zona Terlarang Teknis & Tipografi Kode (EYD V; `SKILL.md` Seksi 1.A)

1. **Pola:** menerjemahkan paksa blok kode, nama *flag* CLI, variabel, *endpoint* REST, *identifier* pustaka, atau singkatan standar (`API`, `SDK`, `URL`, `JSON`, `HTTP`, `SQL`, `CI/CD`) → **Perbaikan:** **PERTAHANKAN** kode, *inline code* (`` `...` ``), *identifier*, nama produk/aplikasi sesuai kapitalisasi resmi (*WhatsApp*, *GitHub*, *PostgreSQL*, *Google Form*), serta singkatan standar dalam kapital yang tepat — **Sebab:** mengubah *identifier* atau *casing* teknis merusak akurasi dokumentasi dan dapat mematahkan perintah yang disalin pembaca.
2. **Pola:** penulisan satuan/besaran tanpa spasi atau salah kapitalisasi (*50cm*, *10GB* vs *10 GB*, *500ms* di prosa) → **Perbaikan:** beri satu spasi antara angka dan simbol satuan baku SI/komputasi (*50 cm*, *10 GB*, *500 ms*, *2,4 GHz*), kecuali simbol persen (`95%`) dan derajat (`30°C`) — **Sebab:** kaidah EYD V dan ISO/SI memisahkan nilai numerik dari lambang satuan.

---

### B. Pemadanan Istilah TI & Penyerapan Baku (Zaim 2018; PASTI/BPBI)

1. **Pola:** campur kode Inggris-Indonesia mentah di prosa teknis (*melakukan deploy ke server*, *user bisa meng-upload file ke cloud*, *sistem mengalami bug dan crash*, *melakukan backup database*) → **Perbaikan:** gunakan padanan baku PASTI/KBBI yang wajar dan mudah dipahami tim (*menerapkan/meluncurkan ke peladen*, *pengguna dapat mengunggah berkas ke komputasi awan*, *sistem mengalami kutu/galat dan mogok*, *mencadangkan basis data*) — **Sebab:** 68 istilah baku bidang `teknologi_dan_rekayasa` di `data/glosarium-lintas-bidang.json` menjaga konsistensi terminologi tanpa mengorbankan presisi teknis.
2. **Pola:** urutan penyebutan istilah asing mendahului padanan (*latency (latensi)*, *scalability (skalabilitas)*) atau penulisan imbuhan asing-Indonesia yang tidak baku (*di-deploy*, *meng-compile*, *meng-update*) → **Perbaikan:** dahulukan padanan Indonesia baru istilah asing bercetak miring dalam kurung pada kemunculan pertama (*latensi (latency)*, *skalabilitas (scalability)*), dan jika terpaksa menyisipkan kata asing berimbuhan Indonesia, gunakan tanda hubung + cetak miring (*di-*deploy*, *meng-*update*) — **Sebab:** kaidah EYD V dan urutan penyebutan istilah baku (`TMS-048`, `TMS-050`).
3. **Safeguard istilah serapan baku:** **JANGAN** mengubah istilah serapan baku teknik/sains (*konduktivitas*, *rekursif*, *skalabilitas*, *entalpi*, *algoritma*, *kompilator*, *enkripsi*, *autentikasi*, *latensi*, *throughput* bila belum berpadanan mantap di ranah jaringan) menjadi padanan paksaan yang justru membingungkan praktisi.

---

### C. Kejelasan Prosedur, Daftar & Kaidah Paper Teknik/Informatika

1. **Pola:** dokumentasi penuh hiperbola pemasaran AI (*arsitektur revolusioner yang secara mulus mengintegrasikan skalabilitas tanpa batas*) atau kalimat prosedur pasif berlapis → **Perbaikan:** tulis spesifikasi terukur (angka latensi, *throughput*, batas memori, versi dependensi), gunakan kalimat imperatif aktif untuk langkah instalasi/konfigurasi, dan jelaskan *mengapa* suatu keputusan arsitektur diambil (bukan hanya *apa*).
2. **Pola:** makalah teknik/informatika mencampur gaya kutipan, menulis tabel/gambar tanpa rujukan teks, atau memakai subjek *saya/kita* di metode/hasil → **Perbaikan:** rujuk setiap gambar/tabel secara eksplisit sebelum tampil (*seperti ditunjukkan pada Gambar 1*), gunakan kalimat pasif objektif atau subjek artefak (*Model diuji pada 1.200 sampel...*), dan cocokkan preset kampus bila menulis tugas akhir (`--preset ui`, `--preset itb`, `--preset its`, `--preset telkom`, `--preset udinus`).

```bash
# Audit dokumentasi teknis atau README berbahasa Indonesia
python scripts/audit.py docs/arsitektur.md --preset teknis --report
```
