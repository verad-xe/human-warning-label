#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh -- make.fun entry.

Writes the single-line safety warning label to $MAKEFUN_OUTPUT_DIR/entry.txt.
The label must be UTF-8 text of 1 to 160 characters, one line.
"""

import os
import sys

ENTRY = (
    'WARNING: This human will say "I\'m five minutes away" '
    "for up to forty minutes. Do not plan around this estimate."
)


def main() -> int:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters.
    if not (1 <= len(ENTRY) <= 160) or not ENTRY.strip() or "\n" in ENTRY:
        print("entry fails the 1-160 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
