#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry: one sentence, one product.

Writes the pitch to /output/entry.txt. Deterministic, stdlib only.
"""
import os

LINE = (
    "It is like a smoke detector, but for awkward silences: it beeps "
    "whenever a conversation dies, then judges you for letting it happen."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
