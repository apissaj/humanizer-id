# Changelog

Semua perubahan penting pada proyek ini dicatat di berkas ini. Format mengikuti [Keep a Changelog](https://keepachangelog.com/id/1.1.0/) dan versi mengikuti [SemVer](https://semver.org/lang/id/).

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
