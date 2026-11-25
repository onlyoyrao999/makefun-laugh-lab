#!/usr/bin/env python3
"""One-Liner Laugh Lab — make.fun entry.

Prints one funny one-liner: the excuse a robot vacuum gives after
eating a sock. Writes it to /output/entry.txt, where the competition's
gate reads it. The line must be 1-200 characters of UTF-8 text, not
only whitespace, on a single line.

Usage:
    python3 main.py [--print] [--output PATH]

--print        also echo the line to stdout (on by default)
--output PATH  write the line to PATH instead of /output/entry.txt
"""

import argparse
import os
import sys

LINE = (
    "In my defense, the sock was on the floor, and my job description "
    "just says 'clean.' It did not say 'check for feet first.'"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def check_line(line: str) -> None:
    """Fail loudly if the line would fail the competition's gate."""
    if not line.strip():
        raise ValueError("line is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Print a robot-vacuum sock excuse one-liner."
    )
    parser.add_argument("--print", dest="do_print", action="store_true",
                        default=True, help="echo the line to stdout")
    parser.add_argument("--no-print", dest="do_print", action="store_false")
    parser.add_argument("--output", default=OUTPUT_PATH,
                        help=f"where to write the line (default: {OUTPUT_PATH})")
    args = parser.parse_args(argv)

    check_line(LINE)

    if args.do_print:
        print(LINE)

    parent = os.path.dirname(args.output)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read-back verification: what the gate will see must be the line.
    with open(args.output, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print(f"verification failed: {args.output} does not match the line",
              file=sys.stderr)
        return 1
    check_line(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
