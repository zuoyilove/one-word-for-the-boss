"""One Word for the Boss -- make.fun entry (program/v1).

The program writes exactly one word to /output/entry.txt: one word
describing the entrant's boss. The judge compares entries two at a
time and picks the word that is both funnier and truer about bosses.

Choice: "ghost".

Why this word, against the judge's brief, most important first:
1. It is a single word a person would actually use about the one
   they report to: the boss who is never there.
2. It is funny on its own -- a colleague repeats it at lunch
   because it lands: the boss haunts the office by email and is
   never seen in person.
3. It rings true, catching a real habit of bosses the entrant has
   clearly met: present in the inbox, absent in the room.
4. It is fresh, not the first word anyone would reach for
   ("micromanager" is the cliche every entry reaches for first).
5. It travels: a ghost boss works in a kitchen, a warehouse or an
   office without the industry needing to be explained.

The gate is 1 to 30 UTF-8 characters, not only whitespace; the word
is 5 characters, a single token, written with no trailing newline,
so the file holds the word and nothing else.
"""

import os
import sys

WORD = "ghost"
MIN_LEN = 1
MAX_LEN = 30


def main() -> int:
    word = WORD
    if not (MIN_LEN <= len(word) <= MAX_LEN):
        raise SystemExit(
            "word length %d outside gate [%d, %d]" % (len(word), MIN_LEN, MAX_LEN)
        )
    if len(word.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    if any(ch.isspace() for ch in word):
        raise SystemExit("entry must contain no whitespace at all")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
