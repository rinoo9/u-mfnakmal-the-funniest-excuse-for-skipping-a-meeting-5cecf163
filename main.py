#!/usr/bin/env python3
"""One-line excuse entry for the make.fun bounty
"The Funniest Excuse for Skipping a Meeting".

Writes exactly one line — the funniest excuse for skipping a
pointless work meeting — to /output/entry.txt. Deterministic:
no input, no network, no randomness; the same bytes on every run.

Craft notes (final): the first draft was the plain "meeting about
too many meetings" loop, which is relatable but lands once and
stops. The final line keeps that loop and adds a second beat —
"and it ran over" — so the meeting convened to complain about
too many meetings commits the very sin it exists to protest.
The turn is self-defeating bureaucracy: the excuse is not that
I am busy, it is that the system that wastes my time is itself
wasting my time. One tight line, no setup it does not need.

Revision: "a meeting" became "the meeting" — the definite
article makes it the one recurring, infamous meeting about
meetings, a sharper and more specific image than any meeting.

Round 2: fresh angle — the zombie recurring invite from 2023 that
nobody cancelled, still holding the worker hostage. The joke is
the calendar as captor, not the meeting-about-meetings loop.
"Send snacks" lands the hostage image in three words.
"""

import os

LINE = (
    "Sorry — my calendar auto-accepted a meeting from 2023 that nobody "
    "ever cancelled. I'm still in it. Send snacks."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE and LINE == LINE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
