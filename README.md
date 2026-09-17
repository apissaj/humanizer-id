# Humanizer ID

Panduan penyuntingan bahasa Indonesia akademik untuk agen kecerdasan buatan: mengurangi ungkapan klise, memperjelas struktur, dan mempertahankan makna serta suara penulis. Ini panduan editorial, bukan detektor AI atau jaminan skor deteksi.

## Isi

- `SKILL.md` — panduan editorial 25 pola, batasan, prosedur tiga tahap, dan contoh simulasi.
- `LICENSE` — lisensi MIT.

## Penggunaan

Salin `SKILL.md` ke folder skill agen Anda. Pada Hermes Agent:

Simpan sebagai `humanizer-id/SKILL.md` di direktori skill Hermes yang aktif. Lokasi standar dokumentasi adalah `~/.hermes/skills/`; jika memakai `HERMES_HOME` atau profil lain, gunakan direktori skill profil tersebut. Lihat [dokumentasi resmi Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/). Baca isi skill sebelum memasangnya.

Gunakan instruksi seperti “sunting teks ini dengan gaya akademik lugas” atau “periksa kejelasan kalimat tanpa menambah informasi baru”.

## Batasan penting

- **Bukan penjamin bebas deteksi:** turnitin atau detektor lain memiliki kriteria sendiri yang tidak dijamin oleh panduan ini.
- **Integritas isi:** jangan menambahkan data, metode, sitasi, atau kesimpulan yang tidak ada dalam draf penulis.
- **Kepengarangan:** kelancaran bahasa tidak membuktikan teks ditulis sendiri. Ikuti kebijakan institusi mengenai penggunaan alat bantu.

## Contoh simulasi

**Sebelum:**
> Dalam penelitian ini menunjukkan bahwa sistem dapat menyimpan berkas. Selain itu, sistem dapat menampilkan daftar berkas.

**Sesudah:**
> Penelitian ini menunjukkan bahwa sistem dapat menyimpan berkas dan menampilkan daftar berkas.

## Lisensi dan atribusi

Perangkat lunak ini dilisensikan di bawah [Lisensi MIT](LICENSE) © 2026 Hafizh Muzani.

Panduan ini memadukan materi penyuntingan bahasa Indonesia dengan adaptasi pola dari [blader/humanizer](https://github.com/blader/humanizer) karya Siqi Chen (Lisensi MIT, © 2025 Siqi Chen). Pemberitahuan lisensi asli disertakan dalam file `LICENSE`.
