# MAW NPC Voices DE

Might and Magic 8 mit der Fan-Mod MAW **auf Deutsch**: deutsche Texte und rund 4.500 deutsche Sprachaufnahmen
für die Leute im Spiel, in allen drei Welten (MM6, MM7, MM8) und in den Ergänzungen von MAW.

*English: a German edition (German texts and German NPC voices) for MMMerge with MAW. For English NPC voices
see [MAW NPC Voices EN](https://github.com/slovi21/maw-npc-voices-en).*

## Kurz: so geht's

1. Prüfe, ob im Spielordner im Ordner `Data` die Datei `GermanT.lod` liegt (siehe [Voraussetzungen](#voraussetzungen)).
2. [Zum Download](https://github.com/slovi21/maw-npc-voices-de/releases/latest): Klicke dort unter „Assets“ auf
   `MAW-NPC-Voices-DE-…zip` (rund 430 MB).
3. Schließe das Spiel und entpacke die Zip-Datei in den Spielordner.
4. Doppelklicke im Spielordner auf `Install_German.exe` und warte auf „Done.“
5. Starte das Spiel. Es ist jetzt deutsch.

Deine Spielstände bleiben unberührt. Die Mod ändert keine Datei des Spiels, von MMMerge oder von MAW,
nur ein paar Zeilen in der Einstellungsdatei `MAWSettings.lua` (siehe [Was die Mod ändert](#was-die-mod-an-deinem-spiel-ändert)).

## Welche Mod brauche ich?

| Du willst … | Dann nimm … |
|---|---|
| das Spiel auf Deutsch, mit deutschen Stimmen | **diese Mod (DE)** |
| das Spiel auf Englisch, mit englischen Stimmen | [MAW NPC Voices EN](https://github.com/slovi21/maw-npc-voices-en) |
| im Spiel zwischen Deutsch und Englisch umschalten, beide mit Stimmen | beide Mods; sie vertragen sich |

## Voraussetzungen

* **Might and Magic 8 mit MMMerge und MAW**, so installiert, wie es die
  [MAW-Anleitung](https://github.com/Malekitsu/Maw-Mod-MMMerge) beschreibt. Das Spiel muss starten und laufen.
* **Der Spielordner:** Das ist der Ordner mit der Datei `MM8.exe`. Du findest ihn so: Rechtsklick auf die
  Verknüpfung des Spiels, dann „Dateipfad öffnen“.
* **Zwei Dateien aus der deutschen Ausgabe von Might and Magic 8** im Ordner `Data` des Spielordners:
  * `GermanT.lod` (die deutschen Texte): **nötig**. Ohne sie bricht der Installer ab und ändert nichts.
  * `GermanD.lod` (die deutschen Sprachaufnahmen): empfohlen. Ohne sie bleiben die Stimmen deiner Helden,
    die Begrüßungen in den Läden und einige Ereignis-Sätze englisch.

  **Woher?** GOG verkauft Might and Magic 8 auch auf Deutsch. Hast du die deutsche Sprache installiert, liegen
  beide Dateien schon in `Data`. Sonst lade bei GOG die deutsche Sprachversion herunter (in GOG Galaxy über die
  Spracheinstellung des Spiels, beim Offline-Installer über „Optionen“) und kopiere nur diese zwei Dateien aus
  deren Ordner `Data` in den `Data`-Ordner deines Spielordners.

## Installation Schritt für Schritt

1. Schließe das Spiel.
2. Entpacke `MAW-NPC-Voices-DE-<Version>.zip` in den Spielordner. Fragt Windows, ob Ordner zusammengeführt oder
   Dateien ersetzt werden sollen, antworte mit „Ja“.
3. Doppelklicke im Spielordner auf `Install_German.exe`.
   Windows warnt eventuell („Der Computer wurde durch Windows geschützt“), weil die Datei neu und nicht signiert ist.
   Klicke auf „Weitere Informationen“, dann auf „Trotzdem ausführen“.
4. Ein schwarzes Fenster zeigt drei Schritte (siehe unten). Nach einigen Minuten erscheint „Done.“.
   Drücke die Eingabetaste, um das Fenster zu schließen.
5. Starte das Spiel.

Nach einem MAW-Update kannst du `Install_German.exe` einfach noch einmal starten.

## Was im Paket ist und was der Installer macht

**Im Download steckt alles, was wir selbst gemacht haben:**

* rund 4.500 deutsche Sprachaufnahmen für die Leute im Spiel, aufgenommen mit ElevenLabs. Männer und Frauen
  sprechen mit verschiedenen Stimmen.
* deutsche Begrüßungen der Ladenbesitzer (eigene Aufnahmen)
* unsere deutschen Übersetzungen: 2.903 Dialoge, für die es kein passendes deutsches Original gibt (vor allem aus
  MM6, MM7 und MAW), und die Texte, die MMMerge und MAW hinzugefügt haben. Die Übersetzungen stammen von einer KI
  und wurden automatisch und in Stichproben geprüft.
* vier Skripte, die das Spiel beim Start lädt, und `Install_German.exe`

**Nicht im Download sind die deutschen Texte und Aufnahmen des Originalspiels.** Sie gehören den Rechteinhabern
von Might and Magic, deshalb dürfen wir sie nicht weitergeben. `Install_German.exe` holt sie aus deinen Dateien
`GermanT.lod` und `GermanD.lod`. Er arbeitet nur auf deinem PC und braucht kein Internet. Im Fenster siehst du:

1. **„1/3 Dialog texts“:** Der Installer nimmt die 965 deutschen Originaldialoge von MM8 aus `GermanT.lod` und
   fügt sie mit den Übersetzungen aus dem Paket zu den deutschen Dialogdateien des Spiels zusammen.
2. **„2/3 Interface texts“:** Er übernimmt aus `GermanT.lod` die deutschen Namen und Beschreibungen von Zaubern,
   Fähigkeiten, Quests, Orten, Gegenständen und Läden, soweit sie zum Spiel mit MMMerge passen. Dazu kommen unsere
   Übersetzungen der Texte von MMMerge und MAW.
3. **„3/3 Party voices“:** Er macht die Stimmen deiner Helden deutsch. Das sind ihre Sprüche, zum Beispiel
   Begrüßungen, Bemerkungen beim Fund eines Gegenstands, bei Hunger oder beim Anblick von Monstern. Für 29 der 79
   Heldenstimmen gibt es deutsche Originalaufnahmen in `GermanD.lod`. Die übrigen 50 bekommen eine dieser deutschen
   Stimmen, vom gleichen Geschlecht und, wo es geht, vom gleichen Volk. In diesem Schritt werden auch die
   Laden-Begrüßungen aus dem Paket angemeldet.

Zum Schluss trägt er in `MAWSettings.lua` die Zeile `language = "de"` ein. Seine Hilfsdateien löscht er wieder.

## Einstellungen im Spiel

**Seite „Sprache / Language“:** Im Optionsmenü des Spiels blätterst du mit den Pfeilen durch die Zusatzseiten
von MAW. Eine davon heißt „Sprache / Language“. Ein Klick auf eine Zeile schaltet sie um.

| Zeile | Möglichkeiten | Was sie umschaltet | Wann es gilt |
|---|---|---|---|
| Sprache | Deutsch / English | alle Texte und die Sprachausgabe | nach Neustart des Spiels |
| Gegenstände, Tooltips | English (Standard) / Deutsch | Namen und Beschreibungen der Gegenstände | nach Neustart |
| Läden, Häuser | English (Standard) / Deutsch | Namen, Besitzer und Schilder von Läden und Häusern, die Gespräche mit den Bewohnern von Häusern und die Begrüßung im Laden | nach Neustart |
| Sprachausgabe | An / Aus | die Stimmen der Leute im Spiel | sofort |

Gegenstände, Läden und Häuser sind absichtlich zuerst englisch, weil viele Spieler die englischen Namen aus
Anleitungen und Foren kennen. Stelle beide Zeilen auf „Deutsch“, wenn du alles auf Deutsch willst.
Mit „Sprache: English“ hörst du englische Stimmen, wenn auch MAW NPC Voices EN installiert ist. Sonst bleibt es still.

**Lautstärke:** Die Stimmen folgen dem Regler für Stimmen in den Optionen des Spiels.

**Tasten:**

| Taste | Wirkung |
|---|---|
| F9 | spielt den letzten Satz noch einmal. Drückst du innerhalb von 2 Sekunden wieder F9, kommt der Satz davor, beim dritten Mal der davor. |
| F10 | beendet die Sprachausgabe. Ein langer Text spricht sonst weiter, auch wenn du das Gespräch schon geschlossen hast. |

**Für Fortgeschrittene** (Datei `MAWSettings.lua` im Spielordner, mit dem Editor öffnen, die Zeile innerhalb von
`return { … }` einfügen, danach das Spiel neu starten):

| Zeile | Wirkung |
|---|---|
| `npcVoiceVolume = 0.8,` | Lautstärke der Stimmen von 0.0 bis 1.0 im Verhältnis zum Regler (Standard 1.0) |
| `repeatVoiceKey = 120,` | andere Taste statt F9 (die Tastencodes stehen in der Datei) |
| `stopVoiceKey = 121,` | andere Taste statt F10 |
| `npcVoices = false,` | Sprachausgabe ganz abschalten. Der Schalter „Sprachausgabe“ auf der Seite oben wirkt dann nicht mehr. |

Hat die MAW-Seite für Tastenbelegung noch zwei freie Plätze, erscheinen die beiden Tasten dort als
„VOICE AGAIN“ und „VOICE STOP“ und werden dort eingestellt. Mit MAW 4.5 ist dort kein Platz frei.

## Was die Mod an deinem Spiel ändert

| Bereich | Geändert? |
|---|---|
| Originalspiel (auch `GermanT.lod`, `GermanD.lod`) | nein, der Installer liest sie nur |
| MMMerge | nein |
| MAW | nur `MAWSettings.lua`: Der Installer trägt `language = "de"` ein; die Seite „Sprache / Language“ ändert die Zeilen `language`, `languageItems` und `languageShops`. Alles andere in der Datei bleibt, wie es ist. |
| Spielstände | nein |

Der Schalter „Sprachausgabe An/Aus“ wird dort gespeichert, wo MMMerge seine Einstellungen ablegt (in der Windows-Registry).
Alles andere sind neue Dateien (Liste unter [Deinstallieren](#deinstallieren)). Ist auch MAW NPC Voices EN installiert,
teilen sich beide Mods drei Dateien; sie sind in beiden Paketen gleich, das Überschreiben schadet also nicht.

## Deinstallieren

1. Lösche im Spielordner unter `Scripts\General` die Dateien `zzzMaw_Language.lua`, `zzzMaw_LanguageMenu.lua` und
   `zzzMaw_LanguageUI.lua`.
2. Lösche die Ordner `Data\Localization\de`, `Data\Voices\NPC_de`, `Data\Voices\Char_de` und `Tools\Voice`.
3. Lösche in `Data\Voices` die Dateien `templates_de.tsv` und `chars_de.tsv`.
4. Lösche im Spielordner `Install_German.exe`, `MAW-NPC-Voices-DE-INSTALL.txt`, `MAW-NPC-Voices-DE-LICENSE.txt`,
   `MawLanguageLog.txt` und `MawLanguageUntranslated.txt` (bei Version 1.0.0 heißen die zwei Textdateien
   `MAW-NPC-Voices-Deutsch-…`).
5. **Nur wenn MAW NPC Voices EN nicht installiert ist:** Lösche auch `Scripts\General\zzzMaw_NPCVoices.lua`,
   `Data\Voices\names.tsv`, `Data\Voices\pics.tsv` und `NPCVoicesLog.txt`.

Die Zeilen `language`, `languageItems` und `languageShops` in `MAWSettings.lua` können bleiben; ohne die Mod beachtet
MAW sie nicht.

## Wenn etwas nicht geht

* **Der Installer meldet fehlende Dateien:** `GermanT.lod` fehlt im Ordner `Data`, oder der Installer liegt nicht im
  Spielordner (dem Ordner mit `MM8.exe`).
* **Keine Stimmen:** Steht „Sprachausgabe“ auf „An“? Steht der Regler für Stimmen in den Spieloptionen über null?
* **Ein Text ist englisch:** Entweder hat eine neuere MAW-Version ihn geändert, oder er gehört zu Gegenständen,
  Läden oder Häusern (Einstellung oben). Geänderte MAW-Texte bleiben englisch und stumm, bis wir sie nachziehen.
* **Ein deutscher Text ist stumm:** Einige Texte mit wechselnden Namen oder Zahlen (zum Beispiel die monatlichen
  Kopfgeld-Aufträge) haben keine Aufnahme.
* **MAWs Dateiprüfung („Check game files“) meldet unsere vier Skripte als „Unknown“:** Das ist richtig so, die Mod ist
  eine Ergänzung und kein Teil von MAW. Lösche die Skripte nicht.
* **Fehler melden:** auf der Seite [Issues](../../issues). Hänge bitte `MawLanguageLog.txt`,
  `MawLanguageUntranslated.txt` und `NPCVoicesLog.txt` aus dem Spielordner an.

## Technisches

| Pfad | Inhalt |
|---|---|
| `Scripts/General/zzzMaw_Language.lua` | Sprachschalter: ersetzt die Texte durch die deutschen |
| `Scripts/General/zzzMaw_LanguageMenu.lua` | Einstellungsseite „Sprache / Language“ |
| `Scripts/General/zzzMaw_LanguageUI.lua` | deutsche Texte der MAW-Einstellungsseiten |
| `Scripts/General/zzzMaw_NPCVoices.lua` | Sprachausgabe (dieselbe Datei wie in MAW NPC Voices EN) |
| `Tools/Voice/de/` | Übersetzung, Aufnahmen, Paketbau und Installer (`install_german.py`, `build_release.py`) |

Mit `SHA256SUMS.txt` auf der Download-Seite lässt sich prüfen, ob die Zip-Datei unbeschädigt angekommen ist.

## Lizenz

Siehe [LICENSE.txt](LICENSE.txt). Nicht-kommerzielles Fan-Projekt, nicht von den Rechteinhabern von
Might and Magic erstellt oder genehmigt. MAW stammt von Malekitsu; diese Ergänzung ist kein Teil von MAW.
