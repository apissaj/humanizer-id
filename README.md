# Humanizer ID

Panduan penyuntingan bahasa Indonesia akademik dan profesional untuk agen kecerdasan buatan: mengurangi ungkapan klise, memperjelas struktur, mengeliminasi kalke terjemahan mesin, membenahi fragmentasi kalimat, dan mempertahankan integritas fakta serta suara asli penulis. Ini panduan editorial, bukan detektor AI atau jaminan skor deteksi.

## Isi

- `SKILL.md` — panduan editorial v1.2.0: safeguard positif palsu, zona dokumen terlarang disunting, pemangkasan nominalisasi & verba ringan, eliminasi kalke terjemahan mesin, fusi kalimat terfragmentasi, retorika formulaik AI, 25 daftar periksa editorial, dan prosedur tiga tahap.
- `LICENSE` — lisensi MIT.

## Penggunaan

Salin `SKILL.md` ke folder skill agen Anda. Pada Hermes Agent:

Simpan sebagai `humanizer-id/SKILL.md` di direktori skill Hermes yang aktif. Lokasi standar dokumentasi adalah `~/.hermes/skills/`; jika memakai `HERMES_HOME` atau profil lain, gunakan direktori skill profil tersebut. Lihat [dokumentasi resmi Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/). Baca isi skill sebelum memasangnya.

Gunakan instruksi seperti “sunting teks ini dengan gaya akademik lugas”, “periksa kalimat tanpa menambah informasi baru”, atau “audit hasil suntingan model lain”.

## Batasan penting

- **Bukan penjamin bebas deteksi:** Turnitin atau detektor lain memiliki kriteria statistik sendiri yang tidak dijamin oleh panduan ini.
- **Integritas isi:** Jangan menambahkan data, metode, sitasi, atau kesimpulan yang tidak ada dalam draf asli penulis.
- **Kepengarangan:** Kelancaran bahasa tidak membuktikan kepengarangan manusia. Ikuti kebijakan institusi mengenai penggunaan alat bantu kecerdasan buatan.

## Contoh simulasi

**Sebelum:**
> Dalam penelitian ini menunjukkan bahwa sistem dapat menyimpan berkas. Selain itu, sistem dapat menampilkan daftar berkas.

**Sesudah:**
> Penelitian ini menunjukkan bahwa sistem dapat menyimpan berkas dan menampilkan daftar berkas.

## Lisensi dan atribusi

Perangkat lunak ini dilisensikan di bawah [Lisensi MIT](LICENSE) © 2026 Hafizh Muzani.

Panduan ini memadukan materi penyuntingan bahasa Indonesia dengan adaptasi pola editorial dari [blader/humanizer](https://github.com/blader/humanizer) karya Siqi Chen (Lisensi MIT, © 2025 Siqi Chen). Pemberitahuan lisensi asli disertakan dalam file `LICENSE`.\n