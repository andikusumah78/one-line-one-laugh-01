#!/usr/bin/env python3
"""One Line, One Laugh - make.fun entry.

Writes a single funny line to /output/entry.txt.

The gate requires UTF-8 text of 1 to 140 characters, not only
whitespace. The line is fixed, so every run writes byte-identical
output: no randomness, no clock, no network, pure stdlib.
"""

import os
import sys

LINE = "I asked my AI for one line. It sent a roadmap, a refund policy, and this sentence."

MAX_CHARS = 140


def validate_line(line):
    """Check the line against the gate: 1-140 chars, not blank."""
    if not isinstance(line, str):
        raise TypeError("line must be str")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("line is %d chars, over the 140 limit" % len(line))
    line.encode("utf-8")
    return line


def main():
    line = validate_line(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    # Read back and verify: the file on disk must be exactly the line
    # we validated, otherwise the run is not reproducible.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError("read-back mismatch: entry.txt does not match the validated line")
    print("wrote %d chars to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
