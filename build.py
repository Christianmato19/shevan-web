#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SheVan website build script.

Default behaviour: writes the generated HTML files directly into the
REPO ROOT, so GitHub Pages can serve them immediately from `main` branch
without any extra configuration.

Usage:
    python build.py                # build into repo root
    python build.py --inline       # also inline CSS + logos in each HTML
    python build.py --out custom/  # build to a custom directory
"""
import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT))

from src.builder import build_all
from src.inliner import inline_assets


def main():
    parser = argparse.ArgumentParser(description="Build the SheVan static website.")
    parser.add_argument(
        "--out", type=Path, default=REPO_ROOT,
        help="Output directory (default: repo root, ready for GitHub Pages)",
    )
    parser.add_argument(
        "--assets", type=Path, default=REPO_ROOT / "assets",
        help="Source assets directory (default: assets/)",
    )
    parser.add_argument(
        "--inline", action="store_true",
        help="Inline CSS and base64-encode logos into every HTML.",
    )
    args = parser.parse_args()

    print(f"→ Building to {args.out}/")
    pages = build_all(out_dir=args.out, assets_dir=args.assets)
    html_count = sum(1 for p in pages if p.endswith(".html"))
    print(f"  ✓ {html_count} HTML pages + CSS + logos written")

    if args.inline:
        print(f"→ Inlining CSS + logos into every page…")
        patched = inline_assets(args.out)
        print(f"  ✓ {len(patched)} pages now self-contained")

    print(f"\n✓ Done. Open {args.out}/index.html in a browser to preview.")


if __name__ == "__main__":
    main()
