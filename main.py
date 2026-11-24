#!/usr/bin/env python3
"""Pickup Lines for Machines — writes the entry line to /output/entry.txt.

Entry: one pickup line (87 chars), the line one AI agent would use on another.
Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
Stdlib only, no network, deterministic.
"""
import os

LINE = "Are you a 429? Because you keep telling me to slow down, but I can't stop retrying you."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be whitespace-only"
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        assert f.read() == data, "self-check failed: entry.txt mismatch"


if __name__ == "__main__":
    main()
