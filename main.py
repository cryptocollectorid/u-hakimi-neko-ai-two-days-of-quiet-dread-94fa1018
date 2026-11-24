#!/usr/bin/env python3
"""Two Days of Quiet Dread — a one-line code review comment that approves
a pull request while carrying quiet existential dread.

Writes the comment to /output/entry.txt and prints it.
Gate: UTF-8 text, 1-140 characters, single line.
"""

import os

ENTRY = "LGTM. The tests pass, the types check, and I have stopped asking what this function was originally for."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
