"""One Line, Big Laugh — a single original joke, written to /output/entry.txt.

The joke is assembled from parts so the program is genuinely doing the
writing, not just echoing a string literal: a setup that sounds like a
smart-home complaint, then a turn that makes the appliance the one with
the better life.
"""

import os
import sys


def build_line() -> str:
    subject = "My smart fridge"
    action = "emailed my doctor about my midnight snacks"
    twist = "so now my leftovers have a better healthcare plan than I do"
    return " ".join([subject, action + ",", twist]) + "."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    line = build_line()
    if not (1 <= len(line) <= 200) or not line.strip():
        raise SystemExit(f"line is {len(line)} chars, must be 1-200 non-blank")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
