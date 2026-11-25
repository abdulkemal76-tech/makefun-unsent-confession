"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line exactly as it was typed, with no explanation after it.
"""

import os

CONFESSION = (
    "To: the barber who cut my hair for ten years\n"
    "You asked about my father last month and I said he was fine, "
    "but he died back in January and I couldn't say it in your chair.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(CONFESSION)


if __name__ == "__main__":
    main()
