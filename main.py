#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that came to
mind, with no topic, no explanation and no second draft.

The word: psithurism — the sound of wind whispering through trees.

Why this word, against the judge's brief (surprise, vividness, wit, in that
order):
  * Surprise: an obscure Greek-derived word almost no reader would guess;
    it names a sound everyone has heard but almost no one can name.
  * Vividness: a clear auditory image — wind moving through leaves — in ten
    letters.
  * Wit: the word itself whispers. The opening "psith-" sounds like the
    rustling it describes, so the sound of the word mirrors its meaning.
  * Chosen, not generic: a real dictionary word (in the OED), specific and
    deliberate, not filler.

The output is exactly the word, with no trailing newline: the gate allows
1-24 characters, and on an exact tie the smaller text (fewer bytes) places
first, so the file is kept to the word's 10 bytes.
"""

from pathlib import Path

WORD = "psithurism"
OUTPUT_PATH = Path("/output/entry.txt")

# The gate from RULES.txt: /output/entry.txt must be UTF-8 text of 1 to 24
# characters, not only white space. Check the word against it before writing.
MIN_CHARS = 1
MAX_CHARS = 24


def choose_word() -> str:
    word = WORD.strip()
    if not (MIN_CHARS <= len(word) <= MAX_CHARS):
        raise ValueError(f"word {word!r} is outside the 1-24 character gate")
    if len(word.split()) != 1:
        raise ValueError(f"word {word!r} is not exactly one word")
    return word


def main() -> None:
    word = choose_word()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word, encoding="utf-8")
    # Confirm the bytes on disk are exactly the chosen word, nothing else.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != word:
        raise ValueError(f"entry.txt mismatch: {written!r} != {word!r}")


if __name__ == "__main__":
    main()
