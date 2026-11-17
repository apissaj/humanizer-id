# Changelog

Semua perubahan penting pada proyek ini dicatat di berkas ini. Format mengikuti [Keep a Changelog](https://keepachangelog.com/id/1.1.0/) dan versi mengikuti [SemVer](https://semver.org/lang/id/).

## [2.4.5] — 2026-11-17

### Diperbaiki
- **Demote 6 kaidah sufiks asing ke `[telaah]`** (`TII-010`..`TII-014`, `TII-016`): pola *-ization, -logy, -ity, -ism, hyper-/poly-* rawan salah tangkap pada kata Indonesia (mis. *Laboratorium*), jadi dijadikan rujukan telaah, bukan aturan aktif.
- **Matcher `TII-015` lambang satuan salah kapital** — case-sensitive, menangkap *5 Newton*, *3 Kg*, *10 KM* tanpa salah tangkap lambang SI baku *N, J, W, kg, km, MB, GB*.
- **Konsol Windows UTF-8** — `main()` memaksa `stdout/stderr` ber-encoding UTF-8 agar panah/simbol laporan tidak membuat audit gagal di tengah jalan.
- Hapus `CUSTOM_RULES` mati milik kaidah yang di-demote.

### Diubah
- **`references/pupi-2004-kepmendiknas146.md`** — tulis ulang ekstrak verbatim.
- Blok `BW` sub-skill `ejaan-morfologi` kini 19 entri (menambah `TII-010`..`TII-016` sebagai butir 13–19).
- Angka kaidah terhitung ulang: **611 → 618** (582 aktif + 36 telaah).

## [2.4.4] — 2026-11-17

### Ditambahkan
- **12 kaidah penyerapan istilah dari PUPI** (Kepmendiknas 146/U/2004): `PUPI-002`..`PUPI-009` untuk bentuk serapan leksikal (*frekwensi, subyektif, propinsi, komplek, jaman, kaedah, managemen, ekstrim*) dan `PUPI-010`..`PUPI-013` untuk bentuk terikat (*pra-, ekstra-, anti-, multi-*).
- **`references/pupi-2004-kepmendiknas146.md`** — ekstrak verbatim 1.322 baris (Bab I–IV) termasuk tabel penyesuaian ejaan prefiks dan sufiks.
- **Blok `BW`** pada sub-skill `ejaan-morfologi` berisi 12 entri Pola → Perbaikan → Sebab plus tabel rujukan serapan sufiks/prefiks.

### Diperbaiki
- Blok `BV2` sub-skill `ejaan-morfologi`: butir 4–7 sebelumnya kehilangan **Perbaikan/Sebab** karena penggabungan baris.

### Catatan rilis
- Versi 2.4.1–2.4.3 tidak tercatat terpisah di berkas ini; ketiganya berisi integrasi EYD V, EYD 1987, dan PUEBI 2015 (kaidah `EYD-058`..`EYD-064`).

## [2.4.0] — 2026-11-17

### Ditambahkan
- **Installer `humanizer-id install`** — menyalin `SKILL.md`, `skills/`, `scripts/`, `humanizer_id/`, dan `data/` ke folder agen AI (Hermes Agent, Claude Code, Google Antigravity) secara otomatis. Deteksi target otomatis; `--target` memilih satu, `--with-references` menyertakan `references/`.
- **Test konsistensi versi** — pytest yang memastikan `pyproject.toml`, `__init__.py`, `SKILL.md` induk, 5 sub-skill, dan `uv.lock` selalu seversi.

## [2.3.1] — 2026-11-17

### Diperbaiki
- Deskripsi paket (README) di PyPI dan rujukan eksternal yang tidak relevan dihapus.
- 75 blok sub-skill dinormalisasi ke format entri **Pola → Perbaikan → Sebab** dengan sitasi halaman.

## [2.3.0] — 2026-11-17

### Ditambahkan
- **Mode AFTER — audit bernomor** (`--report`): temuan bernomor `humanizer/audit-NNN-YYYY-MM-DD.md` tanpa menyunting naskah; eksekusi hanya nomor yang disetujui.
- Generator laporan markdown `humanizer_id/report.py` dengan prioritas HIGH/MEDIUM/LOW.

## [2.2.0] — 2026-11-16

### Ditambahkan
- **Delivery Gate** PASS/FAIL dan Checklist Editorial pada `SKILL.md`.
- Konvensi entri kaidah Pola → Perbaikan → Sebab.

## [2.1.0] — 2026-11-16

### Diubah
- `SKILL.md` monolitik (~113 KB) dipecah menjadi induk ~195 baris + 5 sub-skill on-demand (ejaan-morfologi, sintaksis, diksi-istilah, wacana-retorika, naskah-resmi).

## [2.0.0] — 2026-11-15

### Ditambahkan
- 592 kaidah preskriptif total (integrasi pedoman jurnal Dikbud, surat-menyurat Pusat Bahasa, modul jurnalistik).

## Sebelum 2.0.0

Riwayat v1.x (mesin audit deterministik, autofix, glosarium lintas bidang) tersedia di [Releases](https://github.com/apissaj/humanizer-id/releases).
