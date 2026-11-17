# Changelog

Semua perubahan penting pada proyek ini dicatat di berkas ini. Format mengikuti [Keep a Changelog](https://keepachangelog.com/id/1.1.0/) dan versi mengikuti [SemVer](https://semver.org/lang/id/).

## [2.4.6] — 2026-11-17
### Ditambahkan
- **Lima entri kaidah Buku Praktis Bahasa Indonesia (Badan Bahasa)** — `BPBI-001` (17 pasang: erobik→aerobik, akountan→akuntan, arkhais→arkais, gladi→geladi, hirarki→hierarki, karir→karier, kuatir→khawatir, konggres→kongres, kurve→kurva, nahkoda→nakhoda, perangko→prangko, setasiun→stasiun, sahdu→syahdu, trampil→terampil, trotoir→trotoar, wakap→wakaf, wassalam→wasalam) dan `BPBI-002` (12 pasang: antri→antre, atlit→atlet, ajimat→azimat, faksimil→faksimile, filem→film, ijin→izin, joang→juang, khabar→kabar, kangker→kanker, kongkrit→konkret, tentram→tenteram, jiarah→ziarah) dari BPBI1/Kata; `BPBI-003` (`karenanya`/`makanya` → *oleh karena itu*/*oleh sebab itu*/*jadi*) dari BPBI1/Kalimat; `BPBI-004` (8 pasang: dekret→dekrit, azas→asas, hutang→utang, maghrib→magrib, atmosfir→atmosfer, eksim→eksem, apotik→apotek, kridit→kredit) dari BPBI2/1-30 & 31-60; `BPBI-005` (`contohnya seperti`/`umpamanya seperti` sebagai pleonasme) dari BPBI2/61-90; `BPBI-006` (`dilola`→`dikelola`, `sanjak`→`sajak`) dari BPBI1/Lain-lain & Sastra. `BPBI-007` (`pirsawan`->`pemirsa`, `debet`->`debit`, `voucher`->`voucer`) dari BPBI2 bagian 1-90. Total entri **618 -> 625**. Ditambah dua entri dari *Taktis Menyunting: Panduan Menyunting Naskah* (BRIN, 2019): `TMS-001` (16 pasang ejaan serapan: frustasi, negoisasi, interprestasi, konkrit, komoditi, horisontal, infantri, marjin, dirijen, otobiografi, pondasi, birahi, minimun, orisinil, quantum, malpraktik) dan `TMS-002` (14 bentuk tidak baku: telanjur, perduli, autodidak, trend, goncang, inagurasi, rubuh, contek, nampak, juridis, qori', propemerintah, cindera mata, cenderamata) dari Tabel 5.1 dan 5.16 buku tersebut, sehingga total entri **625 -> 627**. Ditambah `TBI-001` dari Winarti dkk., *Kesalahan Berbahasa Indonesia dalam Terbitan Ilmiah Perguruan Tinggi di Kalimantan Timur* (Pusat Bahasa, 2009): 10 bentuk keliru pada artikel jurnal ilmiah (propesional, kerampilan, ketrampilan, mengkomunikasikan, mendiskritkan, tehnologi, mengasilkan, prosentasi, nampaknya, tergantung dari) beserta halaman penilaian penulisnya, sehingga total menjadi **628**. Ditambah `TMS-003` dan `TMS-004` dari *Taktis Menyunting* (BRIN, 2019), Tabel 5.18 (hlm. 115) dan Tabel 5.20 (hlm. 117): 6 bentuk terikat yang dipisah spasi (antar golongan, multi lateral, purna wirawan, nara hubung, pra jabatan, sapta krida) dan 13 gabungan kata padu yang dipisah (acap kali, sedia kala, kaca mata, karya wisata, kasat mata, suka cita, kosa kata, syah bandar, mata hari, olah raga, peri bahasa, duka cita, puspa warna), sehingga total menjadi **630**. Referensi: `references/taktis-menyunting-brin-bentuk-terikat-gabungan-kata.md`. Referensi verbatim: `references/kesalahan-berbahasa-terbitan-ilmiah-kaltim-leksikal.md`; metadata referensi lama (2005, 170 hlm) dikoreksi menjadi cetakan 2009, xvi + 156 hlm. Referensi verbatim: `references/taktis-menyunting-brin-ejaan-kata.md`.
- **Matcher `BPBI-001`–`BPBI-005`** di `humanizer_id/matchers.py` — case-insensitive, `` word boundary; uji positif/negatif lolos tanpa false positive.
- **Ekstrak referensi verbatim + sitasi**: `references/bpbi-1-kata-badan-bahasa.md`, `references/bpbi-1-kalimat-badan-bahasa.md`, `references/bpbi-1-tanya-kebahasaan-badan-bahasa.md`, `references/bpbi-2-tanya-jawab-badan-bahasa.md`, `references/bpbi-1-lain-lain-badan-bahasa.md`, `references/bpbi-2-1-90-badan-bahasa.md`, `references/bpbi-1-sastra-badan-bahasa.md` (id.wikisource.org, domain publik UU No. 28/2014).

### Diperbaiki
- **Kontradiksi `CX11-002`**: entri sempat menyarankan `namun demikian` sebagai bentuk benar, padahal Buku Praktis 1 (`namun demikian` = *tetapi demikian* yang janggal) dan `PT-001` menyatakan salah. Saran diganti menjadi `meskipun demikian` / `(cukup 'namun')`.
- **`PT-001`** diperkaya sitasi Buku Praktis Bahasa Indonesia 1 sebagai sumber kedua.

### Dipertahankan
- `baud→baut`, `sutra→sutera`, `lembab→lembap` tercantum di buku namun **tidak diaktifkan** — `baud` sah sebagai satuan laju data, `sutra` sah dalam konteks akademik/keagamaan, `lembab` lazim dipakai (menunggu telaah semantik).
- `hisap→isap` dan `himbau→imbau` **tidak diaktifkan** — kontroversial dalam pemakaian modern.
- `mengetrapkan→menerapkan` dan `mengenyampingkan→mengesampingkan` dari BPBI1/Lain-lain **tidak diduplikasi** — sudah aktif di BPK-012 dan KRF-001.
- Pembahasan "majas vs gaya bahasa" (BPBI1/Sastra) hanya telaah terminologis — tidak dijadikan matcher.
- Pasangan BPBI2 **tidak diaktifkan**: `relawan->sukarelawan` (sumber merujuk KBBI 1996; KBBI V sudah memuat `relawan`), `para hadirin` (BPBI2 menilai tidak mubazir), `kurban/korban` (beda makna), `elit/elite` + `bonafid/bonafide` + `faksimil/faksimile` (pelafalan, false-positive tinggi).

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
