"""The Robot Vacuum's Funniest Excuse.

Writes a single line to /output/entry.txt: the excuse a robot vacuum
gives for missing a spot.

Judge criteria (most important first):
  1. The line IS an excuse a robot vacuum gives for missing a spot.
  2. Funny at once -- a real joke, not a cute observation.
  3. Spoken in the vacuum's own voice, a machine owning up to a failure.
  4. Humour from a vacuum's world: suction, dust, pet hair, rugs,
     the charging dock.
  5. Lands in a single line, needing no setup the reader must supply.

The chosen line leans on real vacuum behaviour -- cliff sensors mistake
dark rugs for drops -- and turns it into a machine making peace with
failure, while steering clear of the recycled jokes about a dead
battery, the cat, or recharging.
"""

import os

MAX_CHARS = 120

ENTRY = (
    "My cliff sensor took one look at the dark rug, declared it a hole, "
    "and I respectfully declined to fall in."
)


def validate_entry(entry: str) -> None:
    """Check the entry against the gate: 1-120 chars, one line, not blank."""
    assert 1 <= len(entry) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(entry)}"
    )
    assert "\n" not in entry, "entry must be a single line"
    assert entry.strip(), "entry must not be only whitespace"


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
