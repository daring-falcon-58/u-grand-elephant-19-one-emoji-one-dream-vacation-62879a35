#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry program (make.fun program/v1).

Writes exactly one emoji, U+1F5FB MOUNT FUJI (🗻), to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``) and nothing else:
one Unicode code point, 4 bytes UTF-8, no trailing newline, no network,
no randomness, no clock — two runs produce byte-identical output.

Why 🗻 — scored manually against the judge brief's own criteria, in the
brief's order (full table in README.md; no judge-model calls were made —
the OpenRouter free key returns HTTP 402 until Nov 25 07:00 WIB):
  * (1) Lands on a dream vacation: a mountain is named verbatim in the
    brief's own list ("a beach, a mountain, a plane, a hammock, a
    faraway place") — and Fuji IS the mountain, the single most famous
    one. Beats the castle head-to-head here: the castle reaches "dream
    vacation" only via "faraway place", one inferential step further.
  * (2) Postcard at a glance: snow-capped peak, red slopes, blue sky —
    a stranger sees the place before reading a word (there are no words).
  * (3) Personal and specific: ONE particular dream (see/climb Fuji,
    Japan), not "any holiday". This is the criterion the generic beach
    and island picks fail — and the generic snow-capped mountain (🏔️)
    loses to Fuji here too, since Fuji names the dream and 🏔️ does not.
  * (4) Fresh pick: not the first emoji that comes to mind for
    "vacation" (✈️/🏖️/🏝️) — a surprising pairing of one peak with a
    whole dream trip.
  * (5) Reads instantly worldwide, bold at small size, needs no
    explaining.
  * Fixed-text trap avoided: the rules seal 3 fixed texts (weak to
    strong) judged in every heat — an entry byte-identical to one
    "shares its rate and never enters the playoff". The natural anchor
    ladder is ✈️ → 🏖️ → 🏝️, the three most obvious answers; picking
    any of them caps the entry out of the playoff and out of the win,
    however evocative. Fuji is a specific, chosen peak — not a plausible
    anchor text — so it can actually reach the playoff and win.
"""

import os
import sys

# U+1F5FB MOUNT FUJI — the entry. One code point, 4 bytes UTF-8.
EMOJI = "\U0001F5FB"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes: the emoji alone, no newline, no trailing space.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Verify the written file on re-read: byte-exactly the emoji, 4 bytes.
    with open(path, "rb") as f:
        written = f.read()
    if written != EMOJI.encode("utf-8"):
        print(
            f"error: entry.txt is not byte-exact {EMOJI.encode('utf-8')!r}: "
            f"got {written!r}",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
