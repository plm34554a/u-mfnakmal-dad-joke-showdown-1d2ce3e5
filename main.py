"""Dad Joke Showdown entry.

Writes one original dad joke, deterministically, to /output/entry.txt
(or the path in $MAKEFUN_OUTPUT, or entry.txt inside $MAKEFUN_OUTPUT_DIR).
Standard library only; no randomness, no network.
"""

import os

JOKE = (
    "I entered a dad joke contest and told them my best one. "
    "The judge said, \"That's a groaner.\" "
    "I said, \"Then I've already won.\""
)


def output_path() -> str:
    path = os.environ.get("MAKEFUN_OUTPUT")
    if path:
        return path
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    # The gate requires 1-200 code points of non-whitespace text; fail
    # loudly instead of ever writing an invalid entry.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke must be 1-200 non-whitespace code points")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
