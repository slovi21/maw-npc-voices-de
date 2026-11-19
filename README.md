# MAW NPC Voices DE

Die deutsche Fassung für **Might and Magic 8 mit MMMerge und der MAW-Mod**, für alle drei Spielwelten
**MM6, MM7 und MM8** und die Ergänzungen von MAW:
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
* Zwei Dateien aus der **deutschen Ausgabe** von Might and Magic 8 im Ordner `Data` deines Spiels:
  * `GermanT.lod` (die deutschen Texte des Originalspiels): **nötig**. Ohne sie bricht der Installer ab und ändert nichts.
  * `GermanD.lod` (die deutschen Sprachaufnahmen des Originalspiels): empfohlen. Ohne sie sprechen deine
    Gruppenmitglieder weiter englisch, alles andere wird deutsch.

## 1. Was im Paket ist

Diese Teile haben wir selbst erstellt. Sie liegen fertig im Download:

* **Rund 4.500 deutsche Sprachaufnahmen für die Leute im Spiel** in MM6, MM7, MM8 und MAW (Begrüßungen,
  Antworten, Gerüchte, Wachen), aufgenommen mit ElevenLabs. Fast alle Dialogtexte sind vertont.
  Männer und Frauen sprechen mit verschiedenen Stimmen.
* **2.903 deutsche Übersetzungen von Dialogen**, die es im deutschen Originalspiel nicht gibt: die Texte aus
  MM6 und MM7 sowie die Texte, die MAW neu geschrieben oder geändert hat. Per KI übersetzt und von Hand geprüft.
* **Deutsche Texte für die Menüs und Meldungen von MAW** (zum Beispiel die MAW-Einstellungsseiten).
* **Vier Skripte**, die das Spiel beim Start lädt: Sprachschalter, Einstellungsseite, Menütexte und Sprachausgabe.
* **Install_German.exe**, der Installer für den zweiten Teil (siehe unten).

## 2. Was der Installer erzeugt

Einige deutsche Texte und Aufnahmen gibt es schon im deutschen Originalspiel von Might and Magic 8
(nur von MM8 liegen die deutschen Originaldateien vor; für MM6 und MM7 sorgen die Übersetzungen und Aufnahmen im Paket). Sie gehören den Rechteinhabern von
Might and Magic, deshalb dürfen wir sie nicht mitliefern. `Install_German.exe` holt sie aus deinem eigenen Spiel.
Er arbeitet nur auf deinem PC, ohne Internet, und braucht 2 bis 5 Minuten. Im Fenster siehst du drei Schritte:

1. **Dialogtexte** („1/3 Dialog texts“): Der Installer liest aus `GermanT.lod` die 965 deutschen Originaldialoge
   von Might and Magic 8. Er fügt sie mit den 2.903 Übersetzungen aus dem Paket zu den deutschen Dialogdateien zusammen.
   Ergebnis: Jeder NPC spricht im Text deutsch, bei MM8-Figuren mit dem Wortlaut des Originals.
2. **Oberflächentexte** („2/3 Interface texts“): Aus `GermanT.lod` übernimmt er die deutschen Namen und
   Beschreibungen von Zaubern, Fähigkeiten, Quests, Orten, Gegenständen und Läden. Er nimmt einen Text nur, wenn er
   zur Fassung von MMMerge passt. Was MMMerge oder MAW geändert haben, bleibt englisch.
3. **Stimmen deiner Gruppenmitglieder** („3/3 Party voices“): Das sind die Sprüche deiner eigenen Helden, zum
   Beispiel Begrüßungen, Bemerkungen beim Fund eines Gegenstands, bei Hunger oder beim Anblick von Monstern.
   `GermanD.lod` enthält deutsche Aufnahmen für 29 der 79 Heldenstimmen (die aus Might and Magic 8). Die übrigen
   50 Stimmen (aus MM6, MM7 und MAW) gab es nie auf Deutsch. Sie bekommen eine deutsche Stimme vom gleichen
   Geschlecht und Volk. So spricht jeder Held deutsch, und verschiedene Helden klingen verschieden.

Zum Schluss trägt der Installer in `MAWSettings.lua` die Zeile `language = "de"` ein und meldet „Done.“
Seine Hilfsdateien löscht er wieder. Die Ergebnisse liegen in `Data\Localization\de` und `Data\Voices\Char_de`.
Nach einem MAW-Update kannst du `Install_German.exe` einfach noch einmal starten.

## Welche Dateien geändert werden

| Bereich | Geändert? |
|---|---|
| **Originalspiel** (Might and Magic 8, auch `GermanT.lod` und `GermanD.lod`) | Nein. Der Installer liest die Dateien nur. |
| **MMMerge** (Patch, Multiplayer, `mmmerge.T.lod`, Tabellen, Skripte) | Nein. |
| **MAW** (Skripte, Daten) | Nein, mit einer Ausnahme: In der Einstellungsdatei `MAWSettings.lua` trägt der Installer die Zeile `language = "de"` ein. Die Seite „Sprache / Language“ ändert dort die Zeilen `language`, `languageItems` und `languageShops`. Alle anderen Einträge bleiben, wie sie sind. |

Alles andere sind **neue Dateien**, die es vorher nicht gab:

* `Scripts\General\zzzMaw_Language.lua`, `zzzMaw_LanguageMenu.lua`, `zzzMaw_LanguageUI.lua`, `zzzMaw_NPCVoices.lua`
* `Data\Localization\de\` (die deutschen Texte)
* `Data\Voices\NPC_de\`, `Data\Voices\Char_de\` und die Listen `names.tsv`, `pics.tsv`, `templates_de.tsv`, `chars_de.tsv` in `Data\Voices`
* `Tools\Voice\`, `Install_German.exe`, `MAW-NPC-Voices-DE-INSTALL.txt`, `MAW-NPC-Voices-DE-LICENSE.txt`
* beim Spielen: `NPCVoicesLog.txt`, `MawLanguageLog.txt` und `MawLanguageUntranslated.txt` im Spielordner

Die Einstellung „Sprachausgabe An/Aus“ speichert das Spiel dort, wo MMMerge seine Einstellungen ablegt (Windows-Registry).
Ist auch MAW NPC Voices EN installiert, haben beide Mods `zzzMaw_NPCVoices.lua`, `names.tsv` und `pics.tsv` gemeinsam.
Die Dateien sind in beiden Paketen gleich, deshalb macht das Überschreiben nichts aus.
Wir haben das nachgeprüft: Nach der Installation beider Mods und dem Lauf von `Install_German.exe` hatte sich im ganzen Spielordner nur `MAWSettings.lua` geändert.

## Installation

1. Spiel schließen.
2. Zip in den Spielordner entpacken (Ordner mit `MM8.exe`), Zusammenführen erlauben.
3. `Install_German.exe` im Spielordner doppelklicken, auf „Done.“ warten, Eingabetaste drücken.
4. Spiel starten.

Die Mod ändert keine MAW-Datei. Einzelheiten und Deinstallation: [INSTALL.txt](INSTALL.txt).

## Einstellungen im Spiel

**Seite „Sprache / Language“:** Im Optionsmenü des Spiels blätterst du mit den Pfeilen durch die
Zusatzseiten von MAW. Eine davon heißt „Sprache / Language“. Ein Klick auf eine Zeile schaltet sie um.

| Zeile | Möglichkeiten | Wirkung |
|---|---|---|
| Sprache | Deutsch / English | Sprache aller Texte und der Sprachausgabe. Gilt nach einem Neustart des Spiels. |
| Gegenstände, Tooltips | English (Standard) / Deutsch | Namen und Beschreibungen der Gegenstände. Gilt nach einem Neustart. |
| Läden, Häuser | English (Standard) / Deutsch | Namen der Läden und Häuser. Gilt nach einem Neustart. |
| Sprachausgabe | An / Aus | Schaltet die NPC-Stimmen ein oder aus. Gilt sofort. |

Gegenstände und Läden sind absichtlich zuerst englisch: Viele Spieler kennen die englischen Namen aus Anleitungen
und Foren. Mit „Sprache: English“ spielen die englischen Stimmen, wenn auch MAW NPC Voices EN installiert ist; sonst bleibt es still.

**Lautstärke:** Die NPC-Stimmen folgen dem Regler für Stimmen in den Spieloptionen.

**Tasten:**

| Taste | Wirkung |
|---|---|
| F9 | wiederholt die letzte Sprachausgabe (innerhalb von 2 Sekunden erneut drücken für die davor, bis zu dreimal) |
| F10 | beendet die Sprachausgabe |

**Für Fortgeschrittene:** In der Datei `MAWSettings.lua` im Spielordner lassen sich weitere Werte eintragen:
`npcVoiceVolume = 0.8` (Lautstärke der NPC-Stimmen von 0.0 bis 1.0 im Verhältnis zum Regler),
`repeatVoiceKey = 120` und `stopVoiceKey = 121` (andere Tasten statt F9 und F10; die Tastencodes stehen in der Datei)
sowie `npcVoices = false` (Sprachausgabe ganz abschalten).

## Grenzen

Einige Texte mit wechselnden Namen oder Zahlen (zum Beispiel die monatlichen Kopfgeld-Aufträge) haben keine
Aufnahme; sie erscheinen deutsch, aber ohne Stimme. Texte, die eine neuere MAW-Version geändert hat, bleiben englisch und stumm, bis wir sie
nachgezogen haben.
Englisch gebliebene Stellen schreibt die Mod in `MawLanguageUntranslated.txt` im Spielordner. Diese Datei hilft uns
bei Fehlermeldungen auf der Seite [Issues](../../issues).

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
