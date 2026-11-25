#!/usr/bin/env python3
"""Entry for make.fun bounty u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.

Writes exactly one sentence - a childhood memory - to /output/entry.txt.
Deterministic: no randomness, no time, no network, no input.
"""

import os

ENTRY = (
    "Every summer evening, my grandmother called me in from the yard as the "
    "rice steamed on the stove, and I sat barefoot at her wooden table, "
    "swinging my legs, certain that supper \u2014 and that whole small world "
    "\u2014 would last forever."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
