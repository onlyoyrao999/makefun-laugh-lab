#!/usr/bin/env python3
"""Laugh Lab entry: a robot vacuum explains the missing sock.

The program holds exactly one joke — the excuse a robot vacuum
offers after swallowing a sock — and drops it into the file the
bounty gate inspects, /output/entry.txt. The gate wants a single
line of plain text, between 1 and 200 characters, with no blank
or newline-only content, so the script checks the joke before
writing it and reads the file back afterwards to prove the bytes
on disk match the joke in memory.

Run it with no arguments:

    python3 main.py

Pass --output to point at a different file, or --silent to skip
the stdout echo.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

# The excuse itself. One line, no newlines, well under the limit.
JOKE = (
    "I didn't eat your sock — I was taste-testing it for laundry day, "
    "and it failed quality control so badly I had to finish the job."
)

DESTINATION = pathlib.Path("/output/entry.txt")
LIMIT = 200


def validate_entry(text: str) -> list[str]:
    """Collect every problem with a candidate entry line."""
    problems: list[str] = []
    if not text.strip():
        problems.append("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry must fit on one line")
    if len(text) > LIMIT:
        problems.append(f"entry is {len(text)} chars, over the {LIMIT} limit")
    return problems


def save_entry(text: str, target: pathlib.Path) -> None:
    """Write the joke, creating the output folder if needed."""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def confirm_saved(text: str, target: pathlib.Path) -> str | None:
    """Read the file back; return None on success, else the problem."""
    on_disk = target.read_text(encoding="utf-8")
    if on_disk != text:
        return f"{target} does not match the joke"
    faults = validate_entry(on_disk)
    return faults[0] if faults else None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Write a robot-vacuum sock excuse to the entry file."
    )
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=DESTINATION,
        help="destination file (default: /output/entry.txt)",
    )
    parser.add_argument(
        "--silent",
        action="store_true",
        help="do not echo the joke to stdout",
    )
    return parser


def run(argv: list[str] | None = None) -> int:
    options = build_parser().parse_args(argv)

    faults = validate_entry(JOKE)
    if faults:
        for fault in faults:
            print(f"invalid entry: {fault}", file=sys.stderr)
        return 1

    if not options.silent:
        print(JOKE)

    save_entry(JOKE, options.output)

    problem = confirm_saved(JOKE, options.output)
    if problem is not None:
        print(f"verification failed: {problem}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
