#!/usr/bin/env python3
"""Entry for make.fun bounty u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.

Writes exactly one sentence - a childhood memory - to /output/entry.txt.
Deterministic: no randomness, no time, no network, no input.
"""

import os

ENTRY = (
    "On rainy afternoons, my grandmother pulled me inside, wrapped my cold "
    "hands around a chipped mug of sweet tea, and told stories by the kitchen "
    "window while rain drummed on the tin roof, and I believed that warm "
    "little room would never change."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
