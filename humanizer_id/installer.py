"""Installer skill humanizer-id ke folder agen AI.

Sumber berkas: direktori repo (bila dijalankan dari clone) atau clone
sementara dari GitHub. Target: Hermes Agent, Claude Code, Google
Antigravity. Perintah: `humanizer-id install [--target <nama>]`.
"""

import os
import shutil
import subprocess
import sys
import tempfile

REPO_URL = "https://github.com/apissaj/humanizer-id.git"

# nama target -> (path dasar, nama folder skill)
TARGETS = {
    "hermes": (
        os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "hermes", "skills", "creative")
        if os.name == "nt"
        else os.path.expanduser("~/.hermes/skills/creative"),
        "humanizer-id",
    ),
    "claude": (os.path.expanduser("~/.claude/skills"), "humanizer-id"),
    "antigravity": (os.path.expanduser("~/.gemini/config/skills"), "humanizer-id"),
}


def _sumber_repo(sumber_eksplisit=None):
    """Kembalikan path direktori sumber (repo) yang berisi SKILL.md."""
    if sumber_eksplisit:
        if not os.path.isfile(os.path.join(sumber_eksplisit, "SKILL.md")):
            print(f"[!] {sumber_eksplisit} tidak berisi SKILL.md.", file=sys.stderr)
            sys.exit(1)
        return sumber_eksplisit

    cwd = os.getcwd()
    if os.path.isfile(os.path.join(cwd, "SKILL.md")):
        return cwd

    tmp = tempfile.mkdtemp(prefix="humanizer-id-src-")
    print(f"[*] Mengkloning sumber skill dari {REPO_URL} ...")
    subprocess.run(
        ["git", "clone", "--depth", "1", REPO_URL, tmp],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return tmp


def _deteksi_target(eksplisit=None):
    """Kembalikan daftar nama target terpasang di mesin."""
    if eksplisit:
        if eksplisit not in TARGETS:
            pilihan = ", ".join(sorted(TARGETS))
            print(f"[!] Target tak dikenal: {eksplisit}. Pilihan: {pilihan}", file=sys.stderr)
            sys.exit(1)
        return [eksplisit]
    ada = [nama for nama, (dasar, _) in TARGETS.items() if os.path.isdir(dasar)]
    return ada or ["claude"]  # fallback bila tak ada folder agen terdeteksi


def _salin_folder(sumber, tujuan, skip=("__pycache__",)):
    if os.path.isdir(tujuan):
        shutil.rmtree(tujuan)
    shutil.copytree(
        sumber,
        tujuan,
        ignore=shutil.ignore_patterns(*skip),
        dirs_exist_ok=True,
    )


def install(eksplisit_target=None, sumber_eksplisit=None, dengan_referensi=False):
    sumber = _sumber_repo(sumber_eksplisit)
    target_list = _deteksi_target(eksplisit_target)

    komponen = [
        ("SKILL.md", "SKILL.md"),
        ("skills", "skills"),
        ("scripts", "scripts"),
        ("humanizer_id", "humanizer_id"),
        ("data", "data"),
    ]
    if dengan_referensi:
        komponen.append(("references", "references"))

    for nama in target_list:
        dasar, folder = TARGETS[nama]
        dest = os.path.join(dasar, folder)
        os.makedirs(dest, exist_ok=True)
        for src_rel, dst_rel in komponen:
            src = os.path.join(sumber, src_rel)
            if not os.path.exists(src):
                continue
            dst = os.path.join(dest, dst_rel)
            if os.path.isdir(src):
                _salin_folder(src, dst)
            else:
                shutil.copy2(src, dst)
        print(f"[✓] {nama}: skill tersalin ke {dest}")

    if not dengan_referensi:
        print("[i] references/ dilewati (opsional). Tambahkan --with-references untuk menyalinnya.")
    return dest


if __name__ == "__main__":
    install()
