"""Validate research YAML against shared/schemas/."""

from __future__ import annotations

import sys

from src.utils.validate import RESEARCH_FILES, validate_research


def main() -> int:
    failures = validate_research(RESEARCH_FILES)
    if failures:
        for message in failures:
            print(message, file=sys.stderr)
        return 1
    print(f"OK: validated {len(RESEARCH_FILES)} research files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
