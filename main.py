#!/usr/bin/env python3
"""make.fun entry: One Star, Five Stars for the Food.

Writes one sentence (at most 200 characters), a one-star review of Earth
by an alien tourist that still compliments the food, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only; no network, no files outside this repository.

The review: the biryani is genuinely excellent — fragrant, properly
spiced, worth a trip across four light-years — but Earth's gravity
keeps pressing the tourist into a chair the whole meal. The
compliment is concrete and specific; the grievance is physical,
not a physics lecture.
"""

import os

LINE = "Your biryani is genuinely excellent — fragrant, properly spiced, worth the trip across four light-years — but Earth's gravity has been pressing me into a chair the entire meal, so: one star."


def main():
    if len(LINE) > 200:
        raise SystemExit(f"entry is {len(LINE)} characters, over the 200-character limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the file must hold exactly the entry line,
    # one sentence, within the limit — otherwise the run fails loudly.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the entry line"
    assert written.endswith("."), "entry must be a single sentence"
    assert len(written) <= 200, f"entry is {len(written)} characters, over the limit"


if __name__ == "__main__":
    main()
