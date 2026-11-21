#!/usr/bin/env python3
"""
Texts that men and women speak (a profession text, a shared topic, street news) need a recording in both voices.

    python -I mixed_gender.py --game "C:/.../Might and Magic 8 MAW Mod 4.5" --work work/ [--scope street]

Reads work/prioritaet.csv and work/templates_de.csv (the recording of each text is in the voice of its main gender)
and the speakers of the tables. Writes the OTHER gender for the texts that need it:

    work/gegengeschlecht.csv           texts          input for generate_voices_el.py --variants
    work/gegengeschlecht_vorlagen.csv  templates      input for generate_voices_el.py --variants --templates

The module prefers <key_de>-<m|f>.ogg for an NPC of that gender, so a man no longer hears the woman's recording.

--scope decides which texts count (the narrower scopes are subsets of the wider ones):
  mixed    speakers of both genders known by name (the first, narrow rule: 3 texts, 0 templates)
  street   mixed, plus what any street NPC tells: the street news (NPCNews) and the templates (hire pitches,
           greetings with the time of day) that have no speaker known by name   [default]
  generic  mixed, plus every text and template without a speaker known by name (also profession topics)
A speaker known by name is one that extract_texts.py resolves with weight 2 (table, title words, first-name lists);
names that are only guessed as male count as unknown for street and generic, as in the old rule for mixed.
"""

import argparse
import collections
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import extract_texts as ex  # noqa: E402

SCOPES = ("mixed", "street", "generic")


def speaker_genders(game: Path):
    """({key_en: (known, guessed, source)}, {source: (known, guessed)}); known/guessed are sets of 'm'/'f'."""
    out, genders, _ = ex.build(game)
    by_key, by_source = {}, collections.defaultdict(lambda: (set(), set()))
    for key, r in out.rows.items():
        known, guessed = set(), set()
        for s in r["speakers"]:
            g = genders.of_name(s)
            if g:
                (known if g[1] == 2 else guessed).add(g[0])
        by_key[key] = (known, guessed, str(r["source"]))
        k, gu = by_source[str(r["source"])]
        k |= known
        gu |= guessed
    return by_key, by_source


def needs_second_voice(known, guessed, kind: str, scope: str) -> bool:
    """kind: "news" (NPCNews), "template" (recording with a value filled in) or "text" (anything else)."""
    if (known | guessed) == {"m", "f"}:  # speakers of both genders (guessed names count, as in the first rule)
        return True
    if scope == "mixed" or known or guessed:
        return False  # a named NPC tells it; "nur geraten" names are a case of their own, not covered here
    if scope == "generic":
        return True
    return kind in ("news", "template")  # street: what every street NPC tells


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--game", required=True, type=Path)
    ap.add_argument("--work", required=True, type=Path)
    ap.add_argument("--scope", choices=SCOPES, default="street")
    args = ap.parse_args(argv)
    by_key, by_source = speaker_genders(args.game)
    flip = {"m": "f", "f": "m"}

    rows = list(csv.DictReader((args.work / "prioritaet.csv").open(encoding="utf-8")))
    out = []
    for r in rows:
        if r["template"] == "1":
            continue  # recorded per value through work/templates_de.csv (see below)
        known, guessed, source = by_key.get(r["key_en"], (set(), set(), r["source"]))
        kind = "news" if source.startswith("NPCNews") else "text"
        if needs_second_voice(known, guessed, kind, args.scope):
            out.append({**r, "gender": flip.get(r["gender"], "m")})
    write(args.work / "gegengeschlecht.csv", rows[0].keys(), out)
    count = collections.Counter(r["paket"] for r in out)
    print(f"{len(out)} texts need the second voice: " + ", ".join(f"{k}={v}" for k, v in count.items()))

    # templates: one recording per value; the source names the NPCText/NPCGreet row they come from.
    # Hire pitches and the street greeting are told by every hireable / street NPC, whatever its gender.
    trows = list(csv.DictReader((args.work / "templates_de.csv").open(encoding="utf-8")))
    tout = []
    for r in trows:
        known, guessed = by_source.get(r["source"], (set(), set()))
        if needs_second_voice(known, guessed, "template", args.scope):
            tout.append({**r, "gender": flip.get(r["gender"], "m")})
    write(args.work / "gegengeschlecht_vorlagen.csv", trows[0].keys(), tout)
    chars = sum(len(r["text"]) for r in tout)
    print(f"{len(tout)} template recordings need the second voice ({chars} characters)")
    return 0


def write(path: Path, fields, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(fields))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    sys.exit(main())
