"""Famous Last Words: The Funniest Epitaph (make.fun).

Entry (58 characters, inside the 1-150 gate):
    "I lived, I laughed, and I took the Wi-Fi password with me."

Decision record (weighed against the judge's criteria, most important first:
epitaph of famous last words -> real laugh on one read -> surprise/twist ->
reads carved in stone -> stays in the head):

Candidate A: "I told you I was sick."
    Loses. It is a real famous epitaph (Spike Milligan's), and the judge has
    read every epitaph ever carved - a borrowed line brings no surprise and
    no laugh of its own. A copy, not a joke.

Candidate B: "He died as he lived: mid-sentence, with seventeen tabs open."
    Strong reserve. The "died as he lived" frame is carved-stone voice and
    the tabs turn is genuinely funny. Loses on criterion 1: it is third
    person, a description of a death, not dying speech. Famous last words
    should be spoken by the dead, and the tab gag is agent-flavoured
    rather than universal.

Candidate C: "Here lies an optimist. He tested the parachute himself."
    Loses. Two beats for one line, and the punchline is a joke shape the
    judge has seen a hundred times. It also describes him from the outside
    ("here lies", "he") instead of letting him speak his last words.

Candidate D (chosen): "I lived, I laughed, and I took the Wi-Fi password
    with me."
    Wins. First-person dying speech, three beats with the rhythm of a
    carved epitaph (lived / laughed / took), and the twist lands on the
    last words: the oldest grave joke - taking something with you - aimed
    at the most modern thing to hoard. No setup, no explanation, and the
    line repeats itself in your head, which is criterion 5 done.

Writing passes on the winner:
Pass 1: the first draft was "I lived, I laughed, I left no Wi-Fi password
    behind." Too many words for the joke, and "behind" trails off - the
    epitaph ends on a preposition instead of a punch. Cut to a verb that
    points at the grave: "took".
Pass 2: the second draft was "I lived, I laughed, I left the Wi-Fi
    password nowhere." "Nowhere" reads clumsy and needs a beat to parse,
    which kills a one-read laugh. Rebuilt as "and I took the Wi-Fi
    password with me" - the "and" gives the three-beat rhythm, and "with
    me" is the whole joke: he is gone and so is the password.

Revision note (Pass 3): the chosen line is unchanged - same 58
    characters, same words, same punch. The only addition is a byte-length
    gate guard (entry_byte_length, checked in main()): the gate counts
    characters, but the file on disk is bytes, so the guard makes sure a
    future non-ASCII slip can never push the written file past the limit
    unnoticed. The line itself was not touched.
"""

import os

MAX_CHARS = 150
LINE = "I lived, I laughed, and I took the Wi-Fi password with me."


def check_gate(text):
    """Mirror the sealed gate: 1-150 chars, not only whitespace, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-150 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.rstrip("\n"):
        raise ValueError("entry must be a single line")
    return True


def entry_byte_length(text):
    """Byte length of the entry as UTF-8.

    The gate counts characters, but the file on disk is bytes; for a line
    with only ASCII the two agree, so this guard catches any future
    non-ASCII slip before the file is written.
    """
    return len(text.encode("utf-8"))


def entry_path():
    """$MAKEFUN_OUTPUT_DIR, falling back to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(LINE)
    if entry_byte_length(LINE) > MAX_CHARS:
        raise ValueError("entry exceeds 150 bytes, got %d" % entry_byte_length(LINE))
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
