"""The 3AM Fridge Text.

Writes the entry text to /output/entry.txt.
"""

import os

ENTRY_TEXT = "It's 3:12 a.m. The fridge light is on, the milk is judging me, and Dave is asleep upstairs believing I'm the responsible one."
OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def write_entry():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    write_entry()
