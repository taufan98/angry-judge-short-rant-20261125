#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — make.fun bounty entry.

Writes one short, funny rant about a small everyday annoyance
(at most 400 characters) to /output/entry.txt: a shopper's run-in
with a self-checkout machine that treats him like a shoplifter.
"""

import os

ENTRY = (
    # Specific, concrete annoyance: the self-checkout scale.
    # Sharp and economical: every sentence earns its place, no
    # throat-clearing, and the punch lands on the last line.
    "The self-checkout screamed 'UNEXPECTED ITEM IN BAGGING AREA' "
    "at apples I'd already scanned twice. I'm not stealing. I'm a "
    "grown adult being scolded by a scale with a god complex. I "
    "apologized to the machine, put the apples back, and paid full "
    "price for the privilege of being frisked by furniture."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, must be 1-400"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
