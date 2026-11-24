#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

Deterministic: fixed text, standard library only, no network, no clock,
no randomness. Every run produces the exact same file.
"""

import os
import sys

ENTRY = (
    "The rice cooker clicked to warm the exact second the rain began, "
    "and for one quiet moment the kitchen seemed to have been listening all along."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
