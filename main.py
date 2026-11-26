#!/usr/bin/env python3
"""Entry for make.fun bounty u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.

Writes exactly one sentence - a childhood memory - to /output/entry.txt.
Deterministic: no randomness, no time, no network, no input.

Craft notes: the first line worked through a warm interior — grandmother,
sweet tea, rain on a tin roof — a memory of being kept safe. The new
line works through a summer exterior instead: bare feet on warm concrete,
the ice-cream cart's bell heard from the front steps, and the feeling
of being rich for exactly one cone. The nostalgia lands on the last
clause — wealth measured in minutes, a child's economy where a cone is
a fortune and it melts whether you hurry or not. One sentence, 209
characters, under the 280-char limit.
"""

import os

ENTRY = (
    "Every summer dusk, I sat on the front steps listening for the "
    "ice-cream cart bell, bare feet on warm concrete, and when it "
    "finally turned our corner I felt rich for exactly as long as it "
    "took to finish a cone."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
