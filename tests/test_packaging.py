"""Regresi tata letak paket (packaging).

Konteks: sebelumnya `load_data()` menghitung direktori dataset sebagai
`dirname(dirname(__file__))/data`, sehingga pada paket yang terpasang lewat
pip (site-packages/humanizer_id/...) dataset dicari di site-packages/data
yang tidak ada. Akibatnya seluruh temuan kosong dan CLI mencetak laporan
"naskah terbaca lugas" padahal naskah penuh kalke AI.

Dua hal yang dikunci di sini:
1. Dataset ditemukan saat paket berada di direktori tanpa `data/` di root.
2. Dataset yang hilang harus berhenti dengan galat jelas, bukan laporan bersih.
"""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG_SRC = os.path.join(ROOT, "humanizer_id")


def _copy_pkg_without_root_data():
    """Salin paket ke direktori kosong: meniru bentuk site-packages."""
    tmp = tempfile.mkdtemp(prefix="humanizer-id-pkg-")
    shutil.copytree(PKG_SRC, os.path.join(tmp, "humanizer_id"))
    return tmp


class TestPackagedLayout(unittest.TestCase):
    def test_data_resolves_from_package_dir(self):
        tmp = _copy_pkg_without_root_data()
        code = (
            "import sys; sys.path.insert(0, %r);"
            "from humanizer_id.engine import load_data;"
            "kalke, glos, _ = load_data();"
            "print(sorted(kalke.get('kategori', {}).keys()))" % tmp
        )
        proc = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("kalke_terjemahan_mesin", proc.stdout)

    def test_missing_dataset_fails_loudly(self):
        tmp = _copy_pkg_without_root_data()
        shutil.rmtree(os.path.join(tmp, "humanizer_id", "data"))
        env = dict(os.environ)
        env["PYTHONPATH"] = tmp
        proc = subprocess.run(
            [sys.executable, "-m", "humanizer_id.cli", "--demo"],
            cwd=tmp,
            capture_output=True,
            text=True,
            env=env,
        )
        self.assertEqual(proc.returncode, 2, proc.stdout + proc.stderr)
        self.assertNotIn("Tidak ditemukan penanda", proc.stdout)
        self.assertIn("dataset kaidah tidak ditemukan", proc.stderr.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
