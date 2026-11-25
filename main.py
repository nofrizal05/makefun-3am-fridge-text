"""The 3AM Fridge Text — one line for the fridge door, written at 3 AM.

Writes exactly one line plus a trailing newline to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "Dear 3 AM me: the leftovers have unionized, the ice cream is on "
    "strike, and the cake is faking sleep. Nothing in this fridge loves "
    "you back. Go to bed. \u2014 Management"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
