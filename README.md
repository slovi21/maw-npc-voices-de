# MAW NPC Voices DE

Die deutsche Fassung für **Might and Magic 8 mit MMMerge und der MAW-Mod**:
deutsche Dialoge und Oberflächentexte, rund 4.500 deutsche Sprachaufnahmen für die Leute im Spiel
und eine Einstellungsseite „Sprache / Language“ zum Umschalten zwischen Deutsch und Englisch.

*English: a German edition (German texts and German NPC voices) for MMMerge with MAW. For English NPC voices
see [MAW NPC Voices EN](https://github.com/slovi21/maw-npc-voices-en).*

## Download

`MAW-NPC-Voices-DE-<Version>.zip` (rund 450 MB) auf der Seite [Releases](../../releases).
Mit `SHA256SUMS.txt` lässt sich der Download prüfen.

## Voraussetzungen

* Might and Magic 8 (GOG) mit MMMerge, Patch, Multiplayer und [MAW](https://github.com/Malekitsu/Maw-Mod-MMMerge),
  installiert nach der MAW-Anleitung. Das Spiel muss starten und laufen.
* Im Spielordner `Data\GermanT.lod` und `Data\GermanD.lod` (aus der deutschen Spielversion).

## Was im Paket ist und was der Installer erzeugt

| | Herkunft |
|---|---|
| rund 4.500 deutsche NPC-Stimmen | **im Paket** (eigene Aufnahmen mit ElevenLabs) |
| 2.903 per KI übersetzte Texte, Oberflächentexte | **im Paket** |
| 965 deutsche Originaltexte | erzeugt der Installer aus deinem `GermanT.lod` |
| Stimmen deiner Gruppenmitglieder | erzeugt der Installer aus deinem `GermanD.lod` |

Originaltexte und Gruppenstimmen gehören zum deutschen Originalspiel und dürfen nicht weitergegeben werden.
Fehlen die beiden `.lod`-Dateien, bleiben nur diese Teile englisch; die NPC-Stimmen und übrigen Texte sind trotzdem deutsch.

## Installation

1. Spiel schließen.
2. Zip in den Spielordner entpacken (Ordner mit `MM8.exe`), Zusammenführen erlauben.
3. `Install_German.exe` im Spielordner doppelklicken, auf „Done.“ warten.
4. Spiel starten.

Die Mod ändert keine MAW-Datei. Einzelheiten, Einstellungen, Tasten und Deinstallation: [INSTALL.txt](INSTALL.txt).

## Was übersetzt und vertont ist

* Dialoge, Begrüßungen und Gerüchte von MM6, MM7, MM8 und MAW: 965 Texte aus dem deutschen Originalspiel
  (vom Installer aus deinem Spiel übernommen), die übrigen 2.903 per KI übersetzt und von Hand geprüft.
* Oberflächentexte, Fragen und Meldungen; Gegenstände und Läden auf Wunsch (Einstellungsseite).
* Sprachaufnahmen mit ElevenLabs, Stimme nach dem Geschlecht des NPC.
* Texte, die eine neuere MAW-Version geändert hat, bleiben englisch und stumm, bis sie nachgezogen sind.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `Scripts/General/zzzMaw_Language.lua` | Sprachschalter: ersetzt die Texte durch die deutschen |
| `Scripts/General/zzzMaw_LanguageMenu.lua` | Einstellungsseite „Sprache / Language“ |
| `Scripts/General/zzzMaw_LanguageUI.lua` | deutsche Texte der MAW-Einstellungsseiten |
| `Scripts/General/zzzMaw_NPCVoices.lua` | Sprachausgabe (dasselbe Modul wie in MAW NPC Voices EN) |
| `Tools/Voice/de/` | Übersetzung, Aufnahmen, Paketbau und Installer (`install_german.py`, `build_release.py`) |

## Lizenz

Siehe [LICENSE.txt](LICENSE.txt). Nicht-kommerzielles Fan-Projekt, nicht von den Rechteinhabern von
Might and Magic erstellt oder genehmigt. MAW stammt von Malekitsu; diese Ergänzung ist kein Teil von MAW.
