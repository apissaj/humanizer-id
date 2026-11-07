# Pedoman IMRaD untuk Naskah Jurnal Bereputasi

IMRaD adalah standar global anatomi artikel ilmiah: **I**ntroduction, **M**ethods, **R**esults, **a**nd **D**iscussion.

## 1. Introduction (Pendahuluan) — Pola Corong (Funnel)
- Paragraf 1 (Konteks luas): Domain masalah, pentingnya topik secara global.
- Paragraf 2 (Konteks sempit): Perkembangan terkini, pendekatan yang sudah dicoba.
- Paragraf 3 (Research gap): Keterbatasan solusi yang ada, apa yang belum dijawab literatur.
- Paragraf 4 (Novelty & tujuan): Apa yang diusulkan penelitian ini, nilai kebaruan, hipotesis.
- Paragraf 5 (Roadmap naskah — opsional): Struktur sisa naskah.

## 2. Literature Review / Related Work
- BUKAN daftar ringkasan paper satu per satu ("A melakukan X, B melakukan Y").
- SINTESIS berbasis tema: "Pendekatan berbasis machine learning menunjukkan akurasi tinggi, tetapi terkendala efisiensi komputasi [1-3]."
- Diakhiri dengan positioning penelitian ini terhadap literatur yang ada.

## 3. Methods (Metode Penelitian)
- Wajib **replikabel** — peneliti lain membaca harus bisa mengulang eksperimen.
- Rincian: dataset/populasi, prapemrosesan, arsitektur/desain, metrik evaluasi, lingkungan komputasi.
- Hindari kalimat umum: "data diproses secara teliti" -> sebutkan langkah konkretnya.

## 4. Results (Hasil Penelitian)
- **HANYA TEMUAN, TANPA INTERPRETASI**.
- Angka konkret: metrik, perbandingan, uji signifikansi (p-value, confidence interval).
- Setiap tabel dan gambar WAJIB dirujuk di teks sebelum gambar/tabel muncul.
- Caption tabel di atas tabel; caption gambar di bawah gambar.

## 5. Discussion (Pembahasan)
- Di sini tempat interpretasi: MENGAPA hasilnya begitu?
- Bandingkan eksplisit dengan penelitian sebelumnya:
  - Apakah mendukung penelitian X [4]?
  - Apakah bertentangan dengan temuan Y [5]? Mengapa berbeda?
- Implikasi teoretis dan praktis.
- Keterbatasan penelitian (threats to validity) — editor menghargai kejujuran ilmiah.

## 6. Conclusion (Simpulan)
- Jawab tujuan penelitian dengan singkat dan tegas.
- BUKAN ringkasan abstrak — fokus pada esensi temuan.
- Arah penelitian mendatang (future work) yang realistis.
