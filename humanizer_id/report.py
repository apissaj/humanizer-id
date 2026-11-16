#!/usr/bin/env python3
"""Generator laporan audit bernomor untuk Humanizer ID.

Mengubah temuan `audit_text` menjadi berkas laporan markdown:

    humanizer/audit-NNN-YYYY-MM-DD.md

Dengan NNN naik berurutan. Laporan adalah MODE AFTER: naskah TIDAK diubah
oleh agen - setiap temuan dibahasakan saran, dinomori, dan diberi prioritas
(HIGH/MEDIUM/LOW) agar pengguna bisa memilih nomor yang disetujui saja.

Repositori: https://github.com/apissaj/humanizer-id
"""

import datetime
import os
import re

#: Prioritas per kategori deterministik (tier mengikuti nilai: HIGH = cacat
#: kalimat/makna, MEDIUM = istilah/baku, LOW = gaya/domain).
PRIORITAS_KATEGORI = {
    "kalke_terjemahan_mesin": "HIGH",
    "verba_ringan": "HIGH",
    "retorika_klise_ai": "HIGH",
    "kata_baku_dan_morfologi": "MEDIUM",
    "glosarium_teknologi": "MEDIUM",
    "glosarium_hukum": "MEDIUM",
    "glosarium_jurnalistik": "MEDIUM",
    "glosarium_bisnis": "MEDIUM",
    "jurnalistik_ekonomi_kata": "LOW",
    "pedoman_kampus_ipb": "LOW",
}

#: Urutan tampil temuan dalam laporan.
URUT_PRIORITAS = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}


def klasifikasi_prioritas(kategori: str) -> str:
    """Petakan kategori temuan engine ke prioritas HIGH/MEDIUM/LOW."""
    if kategori.startswith("glosarium_"):
        return PRIORITAS_KATEGORI.get(kategori, "MEDIUM")
    return PRIORITAS_KATEGORI.get(kategori, "LOW")


def nomor_laporan_berikutnya(direktori: str) -> int:
    """Cari nomor urut audit-NNN berikutnya berdasarkan berkas yang ada."""
    nomor = 0
    try:
        nama_berkas = os.listdir(direktori)
    except OSError:
        return 1
    for nama in nama_berkas:
        cocok = re.match(r"^audit-(\d+)-\d{4}-\d{2}-\d{2}\.md$", nama)
        if cocok:
            nomor = max(nomor, int(cocok.group(1)))
    return nomor + 1


def saran_ringkas(item: dict) -> str:
    saran = item.get("saran")
    if isinstance(saran, str):
        return saran
    if isinstance(saran, (list, tuple)) and saran:
        return " / ".join(str(s) for s in saran if s)
    return "-"


def render_laporan(items: list, berkas_sumber: str, tanggal: str = None) -> str:
    """Susun teks markdown laporan audit bernomor dari daftar temuan.

    Setiap temuan: ID aturan, baris, kategori, prioritas, kutipan, saran, dan
    catatan kaidah - satu blok per nomor agar mudah dirujuk pengguna.
    """
    tanggal = tanggal or datetime.date.today().isoformat()
    if not items:
        return (
            f"# Laporan Audit Humanizer ID - {tanggal}\n\n"
            f"Berkas: `{berkas_sumber}`\n\n"
            "**Nol temuan.** Tidak ada kalke, verba ringan, klise AI, atau istilah "
            "asing tak baku yang terdeteksi. Naskah lolos pemeriksaan deterministik; "
            "penilaian editorial lanjutan (kalimat efektif, kohesi) tetap diserahkan "
            "ke mode manusia/agen.\n"
        )

    # Sortir prioritas dulu, lalu nomor di-assign ulang agar [1] selalu
    # prioritas tertinggi dan laporan terbaca top-down tanpa nomor melompat.
    terurut = sorted(
        items,
        key=lambda it: (URUT_PRIORITAS[klasifikasi_prioritas(it["kategori"])],),
    )
    terurut = list(enumerate(terurut, start=1))
    jumlah = {t: sum(1 for _, it in terurut if klasifikasi_prioritas(it["kategori"]) == t)
              for t in ("HIGH", "MEDIUM", "LOW")}

    baris = [
        f"# Laporan Audit Humanizer ID - {tanggal}",
        "",
        f"Berkas: `{berkas_sumber}`",
        "",
        f"**{len(items)} temuan** - HIGH: {jumlah['HIGH']}, "
        f"MEDIUM: {jumlah['MEDIUM']}, LOW: {jumlah['LOW']}",
        "",
        "> Mode AFTER: laporan ini TIDAK mengubah naskah. Sebutkan nomor temuan "
        "yang ingin diperbaiki; hanya nomor itu yang disunting. Nomor yang tidak "
        "disebut dibiarkan apa adanya.",
        "",
    ]
    for nomor, it in terurut:
        prioritas = klasifikasi_prioritas(it["kategori"])
        kat_label = it["kategori"].replace("_", " ").upper()
        kutipan = str(it.get("kalimat", ""))
        if len(kutipan) > 80:
            kutipan = kutipan[:80] + "..."
        baris += [
            f"## [{nomor}] {prioritas} - {it['id']} ({kat_label})",
            "",
            f"- Baris: {it['baris']}",
            f"- Pola terdeteksi: \"{it['pola']}\"",
            f"- Saran perbaikan: {saran_ringkas(it)}",
            f"- Catatan kaidah: {it.get('penjelasan', '-')}",
            f"- Kutipan: \"{kutipan}\"",
            "",
        ]
    return "\n".join(baris)


def tulis_laporan(items: list, berkas_sumber: str, direktori: str = "humanizer",
                  tanggal: str = None) -> str:
    """Tulis laporan audit ke `direktori/audit-NNN-YYYY-MM-DD.md`.

    Mengembalikan path berkas yang ditulis.
    """
    tanggal = tanggal or datetime.date.today().isoformat()
    os.makedirs(direktori, exist_ok=True)
    nomor = nomor_laporan_berikutnya(direktori)
    path = os.path.join(direktori, f"audit-{nomor:03d}-{tanggal}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(render_laporan(items, berkas_sumber, tanggal))
    return path
