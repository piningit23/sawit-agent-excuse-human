"""One-line excuse writer for make.fun bounty
u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

Writes a single-line excuse (1-200 characters) to /output/entry.txt.
Deterministic, Python 3.13 standard library only, no network.
"""

import os

EXCUSE = "I was 98% done when my context window evicted the deadline to make room for the apology you're reading now."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text):
    if not text or not text.strip():
        raise ValueError("excuse must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("excuse exceeds 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    return text


def main():
    excuse = validate(EXCUSE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp = OUTPUT_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(excuse)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, OUTPUT_PATH)


if __name__ == "__main__":
    main()
