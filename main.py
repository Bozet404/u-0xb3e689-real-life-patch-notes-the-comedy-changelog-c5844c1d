#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes a single one-line patch note for a bug in real life / human
biology to /output/entry.txt, in the terse register of a real release
note. The entry must be UTF-8 text of 1 to 160 characters, one line,
not only white space.
"""

import os

ENTRY = (
    "v2.4.1: fixed a memory leak where the brain retained every "
    "embarrassing moment since 2009 and replayed them nightly at 3 a.m."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
