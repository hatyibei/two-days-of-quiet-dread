#!/usr/bin/env python3
"""Entry for make.fun's "Two Days of Quiet Dread".

Writes a one-line code review comment that approves a pull request with
quiet existential dread to /output/entry.txt
(UTF-8, 1-140 characters, no trailing newline).
"""
import os

ENTRY = (
    "Approving. If this works, we learn nothing; if it fails, we learn "
    "everything at 3 AM, by phone."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
