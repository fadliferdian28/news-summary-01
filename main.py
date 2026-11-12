"""news-summary-01 entry, v4 (Python 3.13, standard library only).

The summary lives in summary.txt beside this file; the program copies it to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
No network, no randomness: every run writes the same bytes.

Local check:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    # Entry point: copy summary.txt to the grader's output file.
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "summary.txt", OUT_DIR / "entry.txt")


if __name__ == "__main__":
    main()
