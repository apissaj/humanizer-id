"""Unit dan smoke tests untuk Mode Hemat Token CLI (--compact, --only, --top, --diff, --extract)."""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from humanizer_id.engine import (
    audit_text,
    extract_problem_lines,
    filter_findings,
    fix_text,
    format_compact_report,
    format_fix_diff,
    load_data,
)


def _sample_findings():
    return [
        {
            "baris": 5,
            "id": "GLO-IT-001",
            "kategori": "glosarium_teknologi",  # MEDIUM
            "pola": "database",
            "saran": ["basis data"],
            "penjelasan": "Istilah baku TI.",
            "kalimat": "Sistem mengakses database utama.",
        },
        {
            "baris": 2,
            "id": "LV-001",
            "kategori": "verba_ringan",  # HIGH
            "pola": "melakukan implementasi",
            "saran": "mengimplementasikan",
            "penjelasan": "Pangkas verba ringan.",
            "kalimat": "Peneliti melakukan implementasi metode baru.",
        },
        {
            "baris": 3,
            "id": "KLK-001",
            "kategori": "kalke_terjemahan_mesin",  # HIGH
            "pola": "memegang peranan yang sangat krusial",
            "saran": "berperan penting",
            "penjelasan": "Hindari kalke.",
            "kalimat": "Teknologi memegang peranan yang sangat krusial.",
        },
        {
            "baris": 4,
            "id": "JURNAL-001",
            "kategori": "jurnalistik_ekonomi_kata",  # LOW
            "pola": "dapat disampaikan bahwa",
            "saran": "[dihapus]",
            "penjelasan": "Ringkas kalimat.",
            "kalimat": "Dapat disampaikan bahwa sistem siap.",
        },
    ]


def test_filter_findings_only_and_top():
    findings = _sample_findings()

    high_only, total = filter_findings(findings, only_priorities={"HIGH"})
    assert total == 4
    assert len(high_only) == 2
    assert all(f["id"] in {"LV-001", "KLK-001"} for f in high_only)

    top_two, total_top = filter_findings(findings, top_n=2)
    assert total_top == 4
    assert len(top_two) == 2
    # Harus urut prioritas HIGH dulu, lalu baris
    assert [f["id"] for f in top_two] == ["LV-001", "KLK-001"]


def test_format_compact_report_density():
    findings = _sample_findings()
    selected, total = filter_findings(findings, only_priorities={"HIGH", "MEDIUM"}, top_n=2)
    report = format_compact_report(selected, "naskah.md", total_before_filter=total)

    lines = report.splitlines()
    assert lines[0] == "[naskah.md]"
    assert 'L2 [HIGH|LV-001] "melakukan implementasi" -> "mengimplementasikan"' in lines[1]
    assert "(+2 temuan lain disembunyikan)" in lines[-1]
    assert "HIGH=2, MEDIUM=0, LOW=0" in lines[-1]
    assert len(lines) == 4


def test_format_compact_report_empty_with_filter():
    report = format_compact_report([], "naskah.md", total_before_filter=3)
    assert "0 temuan ditampilkan (3 temuan di luar filter)" in report


def test_format_fix_diff_and_extract_problem_lines():
    kalke, glosarium, kampus = load_data()
    sample = (
        "Baris bersih tanpa masalah.\n"
        "Peneliti menguji analisa sistem yang responsip.\n"
        "Baris penutup yang juga bersih.\n"
    )
    findings = audit_text(sample, kalke, glosarium, kampus)
    extracted = extract_problem_lines(sample, findings)
    assert "L2:" in extracted
    assert "Baris bersih" not in extracted
    assert "Baris penutup" not in extracted

    _, fix_count, fix_log = fix_text(sample, kalke, glosarium, kampus)
    assert fix_count >= 1
    diff_out = format_fix_diff(fix_log, "sample.md")
    assert "[sample.md]" in diff_out
    assert "->" in diff_out
    assert "Total:" in diff_out
    assert "Baris bersih" not in diff_out


def test_cli_compact_only_top_diff_extract(tmp_path):
    sample_file = tmp_path / "uji.md"
    sample_file.write_text(
        "Kalimat bersih pertama.\n"
        "Peneliti melakukan implementasi analisa sistem yang responsip.\n"
        "Di era digital saat ini, sistem backend sangat krusial.\n",
        encoding="utf-8",
    )

    audit_script = os.path.join(ROOT, "scripts", "audit.py")

    res_compact = subprocess.run(
        [sys.executable, audit_script, "--compact", "--only", "high,medium", "--top", "2", str(sample_file)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    assert "Total:" in res_compact.stdout
    assert "=" * 72 not in res_compact.stdout

    res_diff = subprocess.run(
        [sys.executable, audit_script, "--fix", "--diff", str(sample_file)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    assert "perbaikan diterapkan" in res_diff.stdout
    assert "Kalimat bersih pertama." not in res_diff.stdout

    res_extract = subprocess.run(
        [sys.executable, audit_script, "--extract", str(sample_file)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    assert "L2:" in res_extract.stdout
    assert "Kalimat bersih pertama." not in res_extract.stdout
