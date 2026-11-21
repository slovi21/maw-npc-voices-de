# Änderungen

## 1.1 (2026-11-21)

Männer hören keine Frauenstimmen mehr und umgekehrt.

- Neu: 2.302 Sprachaufnahmen in der zweiten Stimme für Texte, die Leute beider Geschlechter sagen: alle
  Straßen-Nachrichten, die Berufstexte, die Anheuer-Sätze und der Tagesgruß. Der NPC im Gespräch bestimmt,
  ob die Männer- oder die Frauenstimme spielt. Vorher gab es dafür nur eine Aufnahme, sodass etwa jeder zweite
  Straßen-NPC die falsche Stimme hatte.
- Behoben: Andover Potbello galt als Frau. Die Zuordnung Portrait → Geschlecht (`pics.tsv`) stützte sich bei
  zehn Portraits auf Namen, die in der Männer- und der Frauenliste stehen (Pat, Robin, Heather, …). Diese Namen
  stimmen nicht mehr ab.
- Das Paket wächst auf rund 600 MB.

## 1.0 (2026-11-19)

Erste Veröffentlichung als eigene Ergänzung.

- Deutsche Dialoge, Begrüßungen, Gerüchte und Oberflächentexte für MM6, MM7, MM8 und MAW.
- Rund 4.500 deutsche Sprachaufnahmen (ElevenLabs), Stimme nach dem Geschlecht des NPC.
- `Install_German.exe` erzeugt aus dem eigenen deutschen MM8 die Originaltexte (aus `GermanT.lod`, nötig) und die
  Stimmen der Gruppenmitglieder (aus `GermanD.lod`, empfohlen).
- Einstellungsseite „Sprache / Language“: Sprache, Gegenstände, Läden, Sprachausgabe.
- F9 wiederholt, F10 beendet die Sprachausgabe.
- Ändert nur die Sprach-Zeilen in `MAWSettings.lua`; Originalspiel, MMMerge, MAW und Spielstände bleiben unberührt.
- Läuft ohne die englischen Stimmen und zusammen mit MAW NPC Voices EN.
