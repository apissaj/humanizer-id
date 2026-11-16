"""Versi harus konsisten di seluruh artefak: pyproject, __init__, SKILL.md, sub-skill, uv.lock."""

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _baca(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def test_semua_versi_sama():
    pyproject = re.search(r'^version = "([^"]+)"', _baca("pyproject.toml"), re.M).group(1)
    init = re.search(r'__version__ = "([^"]+)"', _baca("humanizer_id/__init__.py")).group(1)
    induk = re.search(r"^version: (\S+)", _baca("SKILL.md"), re.M).group(1)
    lock = None
    lock_txt = _baca("uv.lock")
    m = re.search(r'name = "humanizer-id"\nversion = "([^"]+)"', lock_txt)
    if m:
        lock = m.group(1)

    bersalah = []
    if pyproject != init:
        bersalah.append(f"pyproject {pyproject} != __init__ {init}")
    if induk != init:
        bersalah.append(f"SKILL.md {induk} != __init__ {init}")
    if lock is not None and lock != init:
        bersalah.append(f"uv.lock {lock} != __init__ {init}")

    for f in sorted((ROOT / "skills").glob("*/SKILL.md")):
        sub = re.search(r"^version: (\S+)", f.read_text(encoding="utf-8"), re.M).group(1)
        if sub != init:
            bersalah.append(f"{f.as_posix()} {sub} != __init__ {init}")

    assert not bersalah, "Versi tidak konsisten:\n" + "\n".join(bersalah)
