# Checklist Audit Naskah Jurnal Bereputasi (28 Poin)

Centang tiap poin sebelum submit. Semua harus ✅.

## A. Kelengkapan Struktur (8 poin)

1. [ ] Judul: maksimal 14 kata, spesifik, memuat kata kunci utama, tanpa singkatan dan rumus.
2. [ ] Abstrak: 150-250 kata, SATU paragraf, memuat tujuan-metode-hasil-simpulan, TANPA sitasi, TANPA akronim yang belum didefinisikan.
3. [ ] Kata kunci: 4-6 istilah, urut abjad, konsisten dengan istilah di naskah.
4. [ ] Introduction: latar belakang terkini (5 tahun terakhir dominan), gap penelitian dinyatakan eksplisit, novelty/justru kebaruan dinyatakan di paragraf terakhir.
5. [ ] Methods: cukup detail untuk direplikasi (desain, sampel/data, instrumen, prosedur, analisis).
6. [ ] Results: temuan murni tanpa interpretasi; tabel/gambar bernomor dengan caption mandiri.
7. [ ] Discussion: perbandingan eksplisit dengan literatur terdahulu + keterbatasan penelitian.
8. [ ] Conclusion: menjawab tujuan penelitian, TANPA informasi baru yang tidak dibahas.

## B. Kaidah Kebahasaan (12 poin)

9.  [ ] Ragam baku formal impersonal: tanpa "saya/aku/kami/kita" sebagai subjek teks ilmiah (MKI-001).
10. [ ] Denotatif murni: tanpa kata hiperbolis ("revolusioner", "luar biasa", "sangat krusial") (RET-006/008).
11. [ ] Satu paragraf satu gagasan pokok dengan kalimat topik eksplisit di awal (ARG-001).
12. [ ] Keajegan istilah: satu konsep satu istilah sepanjang naskah, tidak berganti padanan.
13. [ ] Kalimat efektif: tidak ada kalimat lebih dari 40 kata.
14. [ ] Tidak ada preposisi mubazir ("membahas tentang", "membicarakan mengenai") (AP-001).
15. [ ] Tidak ada kalimat buntung berawalan preposisi dengan verba aktif ("Dalam bab ini akan membahas...") (AP-002).
16. [ ] Tidak ada residu "dimana/diketika" sebagai penghubung antarklausa (CX11-001).
17. [ ] Tidak ada ganda jamak ("beberapa temuan-temuan") (SPB-001).
18. [ ] Konjungsi koordinatif (dan/tetapi/atau) menghubungkan klausa sejajar (paralelisme S-P) (SPB-003).
19. [ ] Semua imbuhan pasif di- ditulis serangkai (dianalisis, bukan di analisis) (CX-002).
20. [ ] Ganda kopula dilarang ("adalah merupakan") (RET-003).

## C. Kelengkapan Akademik (8 poin)

21. [ ] Sitasi in-text 100% cocok dengan daftar pustaka (tidak ada sitasi yatim atau pustaka tak disitasi).
22. [ ] Gaya sitasi konsisten sesuai jurnal (IEEE numerik / APA author-year / Vancouver).
23. [ ] Referensi dominan dari jurnal bereputasi (60%+ dari Scopus/WoS), bukan blog/website.
24. [ ] Tabel dan gambar: semua dirujuk di teks, bernomor urut, caption mandiri.
25. [ ] Angka, satuan SI, dan desimal konsisten (titik desimal atau koma sesuai jurnal).
26. [ ] Statement konflik kepentingan (conflict of interest) tersedia.
27. [ ] Statement kontribusi penulis (CRediT taxonomy) tersedia.
28. [ ] Statement ketersediaan data (data availability) tersedia atau dijelaskan alasannya.

## Cara Pakai
1. Jalankan `python scripts/audit.py <naskah.md> --kampus jurnal-dikbud` dulu.
2. Perbaiki semua temuan mesin.
3. Baru centang checklist ini satu per satu manual.
4. Naskah siap submit hanya jika 28/28 ✅.
