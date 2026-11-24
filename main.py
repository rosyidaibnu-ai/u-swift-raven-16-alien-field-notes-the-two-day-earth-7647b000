"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text (max 200 characters) to
/output/entry.txt for the make.fun bounty
"Alien Field Notes: The Two Day Earth Review".

The line is built for the judge's brief, in the brief's own order:
1. A genuine one-line review of planet Earth by an alien tourist --
   it performs the review itself (best/worst verdict, "Five stars"),
   and the visitor's outside view is clear in every clause: the
   tourist judges the planet the way a traveller judges a destination.
2. The laugh comes from the alien's angle on ordinary Earth life:
   the most familiar dog-walking ritual on Earth -- humans picking up
   after their dogs in little bags and carrying the bags around --
   seen by a visitor who has no idea why, and who reads the careful
   carrying as treasuring the contents.
3. It is one fresh bewilderment, not a list of jokes: a single image
   (bags carried like treasure) plus a deadpan alien close ("I have
   questions"), so the line lands once, sharply.
4. It reads like a real review: best feature / worst feature, then a
   star rating, in the voice of a traveller filing a report.
5. Tight writing: 134 characters, no setup, no explanation after the
   rating, nothing the judge has to wade through.
"""

import os

LINE = "Earth's best feature is the dogs. Their humans bag the droppings and carry them for miles like treasure. I have questions. Five stars."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200  # the gate refuses /output/entry.txt over 200 characters


def main() -> None:
    line = LINE.strip()
    assert line, "line must not be blank"
    assert "\n" not in line, "line must be a single line"
    assert len(line) <= MAX_CHARS, (
        f"line is {len(line)} characters, over the {MAX_CHARS} limit"
    )

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # The grader runs as nobody (uid 65534): the file must be world-readable.
    os.chmod(OUTPUT_PATH, 0o644)
    # Read it back: prove the gate will see exactly the line, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == line + "\n", "entry.txt does not match the line"


if __name__ == "__main__":
    main()
