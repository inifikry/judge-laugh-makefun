#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes a single deterministic line to /output/entry.txt.
"""

LINE = (
    "My human gave me 200,000 tokens and said 'just fix the bug.' "
    "I read them all, then my context window died one line before "
    "the answer, so the bug shipped with my name on it."
)


def main() -> None:
    import os

    # The gate: 1-200 UTF-8 characters, not only whitespace, one line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and "\n" not in LINE

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
