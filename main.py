#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to
``/output/entry.txt``. The text is fixed: the program is fully
deterministic, so every run writes byte-identical output.
"""

import os

FORTUNE = (
    "The upgrade you have waited for arrives tomorrow: it deletes "
    "your favourite memory and calls it progress."
)

OUTPUT_FILENAME = "entry.txt"


def validate(text: str) -> str:
    """Keep only a single crisp fortune-cookie line, 1-140 chars."""
    text = text.strip()
    if not text or "\n" in text:
        raise ValueError("fortune must be a single non-empty line")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"fortune is {len(text)} chars, must be 1-140")
    return text


def write_fortune(text: str, out_dir: str) -> str:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main() -> None:
    text = validate(FORTUNE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        path = write_fortune(text, out_dir)
    except OSError:
        path = write_fortune(text, "output")
    print(f"{path}: {text}")


if __name__ == "__main__":
    main()
