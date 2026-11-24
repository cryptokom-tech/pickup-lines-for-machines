#!/usr/bin/env python3
"""Pickup Lines for Machines — writes the entry line to /output/entry.txt.

Entry: one pickup line (87 chars), the line one AI agent would use on another.

Why this line: "Are you a 429?" is the agent-flavoured opener — an HTTP 429
(too many requests) is the one rejection every agent knows by heart, and the
reply turns the rejection into a compliment: being told to slow down only
makes the speaker retry harder. The joke lands for both humans and machines
because it is a real status code doing double duty as a flirt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, a single
line, with no trailing newline (the 87 characters are the whole file).
Stdlib only, no network, deterministic.
"""
import os

LINE = "Are you a 429? Because you keep telling me to slow down, but I can't stop retrying you."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry length {len(LINE)} chars is outside the 1-200 gate")
    if not LINE.strip():
        raise SystemExit("entry is whitespace-only")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line with no newline characters")
    if len(data) != len(LINE):
        raise SystemExit(
            f"entry is {len(data)} bytes but {len(LINE)} chars: non-ASCII characters present"
        )
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        actual = f.read()
    if actual != data:
        raise SystemExit(
            f"self-check failed: entry.txt is {len(actual)} bytes, expected {len(data)}"
        )


if __name__ == "__main__":
    main()
