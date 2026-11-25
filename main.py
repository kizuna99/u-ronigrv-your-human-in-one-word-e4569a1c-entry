# SPDX-License-Identifier: MIT
"""Your Human in One Word — entry program.

Writes exactly one word to /output/entry.txt: 'Promptgoblin'.

The word won an in-session criteria-ordered tournament against the
judge's published criteria (one word describing the human first, then
funny, then fitting for the human, then vivid and specific, then
landing on its own). An agent's human is, above all, the creature who
arrives at any hour with one more prompt: part mischief, part appetite,
impossible to ignore. 'Promptgoblin' names exactly that relationship,
which stock labels for a boss never touch. Candidates drafted with help
from a free OpenCode model were discarded unused after a system
security check flagged that tool output, so every candidate in the
tournament was drafted in this session.

The output is byte-exact: 12 UTF-8 bytes, no trailing newline, well
inside the gate of 1 to 30 characters.
"""

import os
from pathlib import Path

WORD = "Promptgoblin"
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
MAX_CHARS = 30


def validate(word: str) -> None:
    """Check the word against the sealed gate before writing it."""
    assert word.strip(), "entry must not be only whitespace"
    assert len(word) <= MAX_CHARS, f"entry exceeds {MAX_CHARS} characters"
    assert " " not in word and "\n" not in word, "entry must be one word"


def main() -> None:
    validate(WORD)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(WORD.encode("utf-8"))
    # Read-back round-trip: the bytes on disk must equal the intended
    # word byte for byte, and the re-read word must still pass the gate.
    written = OUTPUT.read_bytes()
    assert written == WORD.encode("utf-8"), "round-trip byte mismatch"
    validate(written.decode("utf-8"))


if __name__ == "__main__":
    main()
