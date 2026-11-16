"""Tes installer: deteksi target, salin komponen, parse argumen CLI."""

import os
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from humanizer_id.installer import TARGETS, _deteksi_target, install


def test_daftar_target_valid():
    assert set(TARGETS) == {"hermes", "claude", "antigravity"}


def test_deteksi_target_eksplisit():
    assert _deteksi_target("claude") == ["claude"]
    assert _deteksi_target("hermes") == ["hermes"]


def test_deteksi_target_eksplisit_tak_dikenal(capsys):
    try:
        _deteksi_target("vscode")
        assert False, "harusnya exit"
    except SystemExit:
        keluar = capsys.readouterr().err
        assert "Target tak dikenal" in keluar


def test_install_ke_tmp(tmp_path):
    repo = pathlib.Path(__file__).resolve().parent.parent
    # siapkan 1 target palsu dengan cara monkeypatch dict TARGETS
    TARGETS["_uji"] = (str(tmp_path), "humanizer-id")
    try:
        install(eksplisit_target="_uji", sumber_eksplisit=str(repo), dengan_referensi=False)
    finally:
        TARGETS.pop("_uji")
    dest = tmp_path / "humanizer-id"
    for komponen in ["SKILL.md", "skills", "scripts", "humanizer_id", "data"]:
        assert (dest / komponen).exists(), f"komponen {komponen} hilang"
    assert not (dest / "references").exists(), "references harusnya dilewati"
    assert (dest / "SKILL.md").read_text(encoding="utf-8").startswith("---")
    # skills tersalin penuh 5 sub-skill
    subs = [d.name for d in (dest / "skills").iterdir() if d.is_dir()]
    assert len(subs) == 5, f"sub-skill {len(subs)} != 5"


def test_install_dengan_references(tmp_path):
    repo = pathlib.Path(__file__).resolve().parent.parent
    TARGETS["_uji2"] = (str(tmp_path), "humanizer-id")
    try:
        install(eksplisit_target="_uji2", sumber_eksplisit=str(repo), dengan_referensi=True)
    finally:
        TARGETS.pop("_uji2")
    assert (tmp_path / "humanizer-id" / "references").exists()
