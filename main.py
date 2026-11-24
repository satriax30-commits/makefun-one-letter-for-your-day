#!/usr/bin/env python3
"""One Letter for Your Day -- make.fun entry.

Writes exactly one letter, A-Z, to /output/entry.txt.

The letter is Z, standing for "zero sleep": the day lived on no sleep
at all -- bloodshot eyes, 3 a.m. still awake, running on fumes. It is
vivid (a sharp picture, not a vague mood), funny and instantly
relatable, and true to a real day. The letter fits its word twice over:
Z is itself the universal symbol for sleep (Zzz), so the initial and
the word reinforce each other.

Fully deterministic: standard library only, no network, no clock,
no randomness. The output is one byte, no trailing newline, every run.
"""

from pathlib import Path

LETTER = "Z"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the single letter to /output/entry.txt, exactly one byte."""
    if len(LETTER) != 1 or not LETTER.isascii() or not LETTER.isalpha():
        raise ValueError("LETTER must be exactly one ASCII letter A-Z")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Binary write: no newline, no trailing whitespace, UTF-8 single byte.
    OUTPUT_PATH.write_bytes(LETTER.encode("utf-8"))


if __name__ == "__main__":
    main()
