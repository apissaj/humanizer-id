"""CLI entrypoint untuk perintah `humanizer-id`."""

import sys
import os

from .engine import load_data, main as engine_main


def main():
    # Delegasikan seluruh argumen ke CLI engine asli (sudut perilaku identik)
    # engine.main membaca sys.argv[1:] sendiri
    if len(sys.argv) >= 2 and sys.argv[1] in ("-v", "--version"):
        from . import __version__
        print(f"humanizer-id v{__version__}")
        sys.exit(0)
    engine_main()


if __name__ == "__main__":
    main()
