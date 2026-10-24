# memory.md – Leonard der Superheld

Gedächtnis des Projekts. Hier steht alles, was du (oder ein Agent) brauchst, um nach längerer Pause weiterzumachen.
Zuerst diese Datei lesen, dann loslegen. Nach jeder Arbeitssitzung unten im **Verlauf** eine Zeile ergänzen.

Zuletzt aktualisiert: 2026-10-24 (Claude, Session Windows-PC Sascha-Lenovo)

---

## 1. Worum geht es?

Kurze Animationsfilme im Pixar-Stil über **Leonard**, einen kleinen Jungen mit blonden, verwuschelten Haaren, der zum Superhelden wird.
Die Bilder und Clips entstehen mit KI (Bild- und Video-Generator). Danach werden die Clips am Rechner zu einer Folge zusammengeschnitten, mit Übergängen und Soundeffekten.

Leonards Aussehen (wichtig, damit neue Clips zusammenpassen):
- Schlafanzug: grau, einteilig, barfuß
- Superheldenanzug: grün mit dunkelblauen Seiten, gelber Gürtel, Stern auf der Brust, grünes Cape mit gelbem Rand, grüne Stiefel
- dazu eine grüne Kappe, verkehrt herum getragen
- Zimmer: Holzbett mit bunter Decke, Wecker und grüne Kappe auf dem Nachttisch, Holzschrank mit bunten Shirts, Superhelden-Poster an der Wand, Spiegel neben der Tür

---

## 2. Stand der Folgen

| Folge | Stand | Datei im Repo | Länge |
|---|---|---|---|
| 1. Leonard erwacht | **fertig** (24.10.2026) | `Leonard-erwacht/Leonard_erwacht_FINAL.mp4` | 39 s, 640x360, 24 fps |
| Teaser „Leonard der Superheld“ (Hollywood-Stil) | **fertig, Version 1** (24.10.2026), Hafen-Szene fehlt noch | `Teaser/Leonard_Teaser_16x9.mp4` | 22,9 s, 1920x1080, 24 fps |
| 2. ? | Idee offen | – | – |

**Neu seit dem Teaser:** Leonard hat jetzt eine Familie im Team: **Papa** (graue Haare, Bart, grün-goldener Anzug mit „S“-Stern, goldene Schulterpanzer) und die **Schwester** (blond, pinke Katzenaugen-Sonnenbrille, grün-pinker Anzug mit „J“-Stern, Laser aus den Händen). Leonards Anzug trägt ein „L“ im Stern. Referenzbild: `C:\Users\Neu\Videos\Leonard der Superheld\Neuer Ordner\Gemini_Generated_Image_sj810msj810msj81.jpg`.

Bilder für mögliche nächste Szenen gibt es schon (siehe Abschnitt 4): „Boy vowing to hunt villain“ (Leonard schwört, den Bösewicht zu jagen), „Cartoon boy jumping with joy“, „Cartoon boy thinking“. Daraus ließe sich Folge 2 bauen: Leonard entdeckt seine Kräfte und schwört, einen Bösewicht zu jagen.

---

## 3. Folge 1 „Leonard erwacht“ im Detail

### Die vier Clips (je 10 Sekunden, 640x360, 24 fps, mit Ton)

Die Reihenfolge ergibt die Geschichte. Ende und Anfang der Clips passen fast genau aufeinander.

| Nr | Datei im Ordner `Leonard erwacht` | Was passiert | Liegt im Film bei |
|---|---|---|---|
| 1 | `leonsard_wird_morgens_wach_,_20261024131039.mp4` | Leonard schläft, wacht auf, setzt sich auf die Bettkante, reibt sich die Augen | 0,0 bis 10,0 s |
| 2 | `frame1_geht_zu_frame_2_20261024131039.mp4` | gähnt, steht auf, geht zum Schrank, kratzt sich am Kopf | 9,7 bis 19,7 s |
| 3 | `er_dreht_sich_auperschnell_im_20261024131039.mp4` | zieht den grünen Anzug aus der Schublade, dreht sich superschnell (Lichtwirbel), steht verwandelt da, setzt sich staunend aufs Bett | 19,3 bis 29,3 s |
| 4 | `er_ist_sichtbar_ershrocken_steht_20261024131039.mp4` | erschrocken auf dem Bett, geht zum Spiegel, sieht sich, staunt und ruft | 29,0 bis 39,0 s |

Die gleichen Clips liegen noch einmal mit englischen Namen im Ordner `Okt 24 - 10_43 (1)` (gleiche Dateigröße, also identisch). Zum Beispiel ist `Man_waking_up_smiling_…mp4` Clip 1, `Er_dreht_sich_im_Kreis_…mp4` Clip 3 und `Leonard_looks_in_mirror_…mp4` Clip 4.

### Übergänge (damit keine Sprünge zu sehen sind)

| Übergang | Art | Dauer | Warum |
|---|---|---|---|
| Clip 1 → 2 | weiche Überblendung (`fade`) | 0,3 s | Bild passt fast genau, nur leicht verschobener Ausschnitt |
| Clip 2 → 3 | Wisch nach links (`smoothleft`) mit Whoosh-Geräusch | 0,4 s | **echter Sprung**: er kratzt sich am Kopf und hält plötzlich den Anzug. Der Wisch lässt es gewollt wirken. |
| Clip 3 → 4 | weiche Überblendung (`fade`) | 0,3 s | Bild passt fast genau |
| Anfang / Ende | Einblenden 0,6 s, Ausblenden 0,8 s | | |

Durch die Überblendungen überlappen sich die Clips, deshalb ist der Film 39 s lang und nicht 40 s.

### Ton

Der Originalton der Clips bleibt drin (Geräusche, Gähnen, Staunen) und geht an den Übergängen weich ineinander über. Darüber liegt eine eigene Effekt-Spur. Alle Effekte sind **am Rechner erzeugt** (Skript `sfx.py`), nicht aus einer Geräusch-Bibliothek. Deshalb klingen sie etwas künstlich.

| Zeit im Film | Effekt | Zweck |
|---|---|---|
| 0,2 bis 2,2 s | Wecker klingelt (rechts) | er wacht auf |
| 0,6 bis 9 s | leise Vögel (links) | Morgenstimmung |
| 9,5 bis 26,3 s | tiefer Brummton und Puls, der immer schneller wird | Spannung steigt |
| 19,05 s | Whoosh von links nach rechts | Übergang zum Anzug |
| 21,6 bis 26,3 s | ansteigender Ton (Riser) | baut auf die Verwandlung hin |
| 22,0 bis 26,0 s | wirbelnde Whooshes und Glitzern | er dreht sich |
| 26,3 s | tiefer Knall, Crash und Glockenspiel | Verwandlung fertig |
| 32,0 s | dramatischer Schlag mit schiefem Akkord | er sieht sich im Spiegel |
| 35,5 bis 39 s | Helden-Akkord schwillt an, Schlag bei 37,4 s | Finale |

Lautstärke am Ende: auf -16 LUFS gebracht (normales Video-Niveau), Spitze -0,9 dBFS.

---

## 3b. Teaser im Detail

Gebaut mit dem Motion-Skill **social-teaser-video** (Saschas Vorgehen aus dem Lambo-Teaser), Schnitt nach **beat-sync-editing**, geprüft mit **review-loop**. Die Skills liegen auf dem VPS unter `~/.agents/skills/` (Einstieg `motion-hub`).

**Quellen** (Ordner `C:\Users\Neu\Videos\Leonard der Superheld\Neuer Ordner\`):
- `gemini_generated_video_10c15bc5.mp4` = im Skript **A**: Pose im Zimmer, Papa gegen Roboter, BÄÄMMM, Leonard rennt, BOOOMMM, Laser der Schwester, Wand-Explosion, Familie auf dem Dach
- `gemini_generated_video_6af2c6fc.mp4` = **C**: Zimmer, Abheben in Wolken, VROOOM über der Stadt, Papa WHIZZ, Kinder fliegen, Sonnenuntergang
- `gemini_generated_video_ddf18f34.mp4` ist byte-gleich mit 10c15bc5, `Unbenannt_20261024161835.mp4` ist dasselbe Video neu kodiert (nicht gebraucht)
- `bitte_nochmal_neu_machen_._20261024161835.mp4` = **Hafen-Szene mit echten Menschen** (fotorealistisch). Passt nicht zum Pixar-Stil und ist deshalb **noch nicht im Teaser**. Umwandlung per KI-Video (ElevenLabs Kling/Runway) braucht dort einen bezahlten Tarif. Möglichkeiten: in Gemini neu erzeugen (Prompt unten) oder Pixar-Standbilder (ElevenLabs, ca. 0,18 USD je Bild) als schnelle Schnitte.

**Aufbau** (144 BPM, 10 Bilder pro Schlag, jeder Schnitt liegt auf einem Schlag):
| Teil | Zeit | Inhalt | Text |
|---|---|---|---|
| Aufbau | 0 – 4,2 s | Zimmer (Zeitlupe), Power-Pose | „In einer Welt voller Gefahren …“ |
| Steigerung | 4,2 – 11,3 s | Abheben, Papa vs. Roboter, VROOOM, WHIZZ, Leonard rennt, Kinder fliegen | „… braucht es Helden.“ / „Diesmal ist es Familiensache.“ |
| Höhepunkt | 11,3 – 14,6 s | BÄÄMMM, Laser, Wand-Explosion, BOOOMMM (je 2 Schläge, Wackeln, Weißblitz) | – |
| Stille | 14,6 – 15,0 s | ein Schlag schwarz | – |
| Drop | 15,0 – 17,5 s | Familie auf dem Dach in Zeitlupe, größter Einschlag | – |
| Titel | 17,5 – 20,8 s | Sonnenuntergang-Flug | „LEONARD – der Superheld“ |
| Ende | 20,8 – 22,9 s | Standbild | „BALD. – Nur im Familienkino“ |

Ton: Originalgeräusche der Clips (leiser), dazu selbst erzeugt: Braams (d-Moll), Uhr-Ticken, Puls, Streicher-Ostinato, Whoosh vor jedem Schnitt, Einschläge, Riser in den Drop. Lautheit zweipassig auf -14 LUFS (gemessen -14,3, Spitze -0,7 dBFS). Kino-Balken 2.39:1.

**Neu bauen** (auf dem VPS, Projektordner `/root/leonard-teaser/`, Clips liegen dort in `clips/A.mp4` und `clips/C.mp4`):
```bash
ssh sascha-kruss-1
cd /root/leonard-teaser
node text/render.js
/root/sk-werbevideo/.venv/bin/python build.py
```
Ergebnis: `/root/leonard-teaser/out/leonard-teaser-16x9.mp4` (Render ca. 3,5 Minuten). **Danach verschieben, nicht kopieren** (Sascha, 24.10.: keine Mehrfach-Ablagen): `mv out/leonard-teaser-16x9.mp4 /home/sascha-central/htdocs/central.sascha-kruss.de/ausgabe/video/Leonard_Teaser_16x9.mp4`. Ablage ist nur die Central-Station-Ausgabe (plus das Repo). Die Dateien `Teaser/build.py` und `Teaser/text/render.js` im Repo sind dieselben wie auf dem VPS.
- Schnitt ändern: Liste `SHOTS` in `build.py` (Clip, Start, Länge in Schlägen, Tempo, Zufahrt, Blitz, Wackeln, Ton).
- Texte ändern: `blocks()` in `text/render.js`, danach beide Befehle.
- Hafen-Szene einsetzen: Pixar-Fassung als `clips/H.mp4` ablegen und 2 bis 3 Einträge mit `'H'` in die Steigerung setzen.

**Prompt für die Hafen-Szene in Gemini (neu erzeugen, Pixar-Stil):**
> 3D Pixar animation style. A grey-haired bearded father in a green and gold superhero suit with a gold "S" star, his son in a green cap and green-blue suit with an "L" star, and his blonde daughter with pink cat-eye sunglasses in a green-pink suit with a "J" star stand side by side on a sunny container harbor with cranes. The father flexes, the boy shouts and unleashes a glowing green energy blast that lifts the parked cars, the girl turns into green energy and back, then the kids do a martial-arts kick and all three end in a heroic pose. Cinematic camera, warm sunlight, 10 seconds.

## 4. Wo liegt was?

### Im Repo (GitHub `Schoscha/Leonard-der-Superheld`, Zweig `main`)

| Pfad | Inhalt |
|---|---|
| `README.md` | Kurzbeschreibung |
| `memory.md` | diese Datei |
| `Leonard-erwacht/Leonard_erwacht_FINAL.mp4` | fertige Folge 1 |
| `Leonard-erwacht/werkzeuge/sfx.py` | erzeugt die Effekt-Spur als WAV (39 s). Zeiten und Effekte stehen im Skript, Abschnitte 1 bis 9 |
| `Leonard-erwacht/werkzeuge/zusammensetzen.sh` | setzt Clips und Effekt-Spur zum fertigen Film zusammen (der genaue ffmpeg-Befehl) |
| `Leonard-erwacht/werkzeuge/match.py` | Hilfswerkzeug: findet an der Schnittstelle zweier Clips die ähnlichsten Bilder |

**Die Original-Clips und Bilder sind nicht im Repo**, nur auf dem Windows-PC.

### Auf dem Windows-PC (Sascha-Lenovo)

`C:\Users\Neu\Videos\Leonard der Superheld\`
- `Leonard erwacht\` – die 4 Original-Clips von Folge 1 und die fertige `Leonard_erwacht_FINAL.mp4`
- `Okt 24 - 10_43 (1)\` – alle KI-Bilder und Clips (englische Namen), auch Standbilder („Gespeicherter Frame aus …“), Kostüm in der Schublade, Leonard denkt, springt vor Freude, schwört den Bösewicht zu jagen
- `Okt 24 - 10_43\` – drei Bilder (Anzug, Schwur, Fensterbild)
- einzelne Bilder direkt im Ordner (`Download.jpg`, `Boy_vowing_to_hunt_villain_….jpg` usw.) und die ZIP-Dateien, aus denen die Ordner entpackt wurden

### Kopien auf dem VPS (sascha-kruss-1)

- Central Station, Ausgabe › Video: `/home/sascha-central/htdocs/central.sascha-kruss.de/ausgabe/video/Leonard_erwacht_FINAL.mp4`
- Tagebuch-Bericht: `/test-sascha/Leonard-der-Superheld/2026-10-24_1322_leonard-erwacht-schnitt.md` → https://files.sascha-kruss.de/files/srv/test-sascha/Leonard-der-Superheld/2026-10-24_1322_leonard-erwacht-schnitt.md (nur im Tailnet)

---

## 5. So baust du die Folge neu (Schritt für Schritt)

Das brauchst du, wenn du einen Effekt ändern, einen Übergang verschieben oder einen Clip austauschen willst.

### Voraussetzungen (auf dem Windows-PC alles schon da)
- **ffmpeg**: installiert über winget, im PATH (`ffmpeg -version` zum Testen)
- **Python 3.12 mit numpy**: `C:\Users\Neu\AppData\Local\Programs\Python\Python312\python.exe` (das Python im PATH hat kein numpy!)
- **Git Bash** für die `.sh`-Skripte

### Schritte
1. Repo holen oder aktualisieren:
   ```bash
   git clone https://github.com/Schoscha/Leonard-der-Superheld.git
   ```
   oder im vorhandenen Ordner `git pull`.
2. Effekt-Spur erzeugen (dauert ca. 1 Minute):
   ```bash
   /c/Users/Neu/AppData/Local/Programs/Python/Python312/python.exe Leonard-erwacht/werkzeuge/sfx.py sfx.wav
   ```
3. Film zusammensetzen:
   ```bash
   bash Leonard-erwacht/werkzeuge/zusammensetzen.sh "/c/Users/Neu/Videos/Leonard der Superheld/Leonard erwacht" sfx.wav Leonard_erwacht_neu.mp4
   ```
4. Anschauen. Passt es, die neue Datei als `Leonard_erwacht_FINAL.mp4` ins Repo legen, committen und pushen.

### Typische Änderungen
- **Effekt lauter oder leiser:** in `sfx.py` beim passenden `add(...)` den dritten Wert (gain) ändern, z. B. `0.9` beim Knall.
- **Effekt verschieben:** in `sfx.py` die Startzeit im `add(..., ZEIT, ...)` ändern (in Sekunden, Filmzeit).
- **Effekte insgesamt lauter oder leiser:** in `zusammensetzen.sh` bei `[4:a]volume=1.0` den Wert ändern (z. B. `0.7`).
- **Originalton lauter oder leiser:** in `zusammensetzen.sh` `volume=1.4` hinter dem letzten `acrossfade` ändern.
- **Übergang länger:** `duration=` beim `xfade` ändern. Achtung: Dann verschieben sich alle späteren `offset`-Werte und die Effektzeiten. Regel: offset = bisherige Filmlänge minus Übergangsdauer.
- **Andere Übergangsart:** statt `fade` oder `smoothleft` z. B. `fadewhite` (weißer Blitz), `circleopen`, `wipeleft`. Liste: ffmpeg-Doku zu `xfade`.
- **Größer ausgeben (720p):** in `zusammensetzen.sh` in der Zeile mit `fade=t=out:st=38.2:d=0.8[vout]` vor `[vout]` noch `,scale=1280:720:flags=lanczos` einfügen. Schärfer wird es dadurch nicht, nur größer.

---

## 6. Eine neue Folge anlegen

1. Neue Clips mit dem KI-Generator erzeugen. Tipp: Das **letzte Bild** eines Clips als **Startbild** des nächsten verwenden (so wurde es bei Folge 1 gemacht, deshalb passen die Übergänge). Leonards Aussehen aus Abschnitt 1 in den Prompt schreiben.
2. Clips in einen eigenen Ordner legen, z. B. `C:\Users\Neu\Videos\Leonard der Superheld\Folge 2\`.
3. Im Repo einen Ordner `Folge-2-<Titel>/werkzeuge/` anlegen, `sfx.py` und `zusammensetzen.sh` aus Folge 1 hineinkopieren und anpassen: Dateinamen der Clips, Anzahl der Clips, `offset`-Werte, Effektzeiten.
4. Mit `match.py` prüfen, wo zwei Clips am besten zusammenpassen:
   ```bash
   /c/Users/Neu/AppData/Local/Programs/Python/Python312/python.exe Leonard-erwacht/werkzeuge/match.py clipA.mp4 clipB.mp4
   ```
   Es vergleicht die letzten 3 s von Clip A mit den ersten 3 s von Clip B. Kleine Zahl bei `mse` heißt: sehr ähnlich. Liegt der beste Wert weit unter dem Wert für „naive end/start“, lohnt es sich, dort zu schneiden. Ist er hoch (über ca. 800), ist es ein echter Sprung: dann einen Wisch oder Blitz mit Geräusch als Übergang nehmen.
5. Fertigen Film ins Repo, Tabelle in Abschnitt 2 ergänzen, Kopie in die Central-Station-Ausgabe (`ausgabe/video/`) legen, Verlauf unten ergänzen.

Einem Agenten (Claude, Gemini, OpenCode …) reicht als Auftrag: „Lies memory.md im Leonard-Repo und setz Folge 2 aus den Clips im Ordner … zusammen, gleiche Machart wie Folge 1.“

---

## 7. Ideen und offene Punkte

- [ ] Echte Soundeffekte statt der berechneten (z. B. aus einer freien Bibliothek wie freesound.org oder mit ElevenLabs Sound Effects erzeugen) – klingt natürlicher
- [ ] Hintergrundmusik (heldenhaft, leise unter den Effekten)
- [ ] Sprecher oder Untertitel (z. B. „Wow… ich bin ein Superheld!“ beim Spiegel)
- [ ] Ausgabe in 720p oder 1080p (die KI-Clips sind nur 640x360; ein KI-Upscaler wäre besser als einfaches Vergrößern)
- [ ] Original-Clips mit ins Repo nehmen (zusammen ca. 5 MB), damit alles an einem Ort ist
- [ ] Folge 2 planen (Bilder für „Schwur gegen den Bösewicht“ sind schon da)

---

## 8. Gelernt

- KI-Clips, bei denen das Endbild als Startbild des nächsten Clips dient, lassen sich mit 0,3 s Überblendung fast unsichtbar verbinden.
- Wo die Handlung springt, hilft kein Überblenden. Ein schneller Wisch mit Whoosh-Geräusch wirkt dann wie ein gewollter Schnitt.
- Effekte genau auf sichtbare Momente legen (Drehung, Verwandlung, Blick in den Spiegel). Die Zeitpunkte wurden über die Bewegung im Bild ermittelt.

---

## Verlauf

| Datum | Wer | Was |
|---|---|---|
| 2026-10-24 | Claude (Windows-PC) | Folge 1 „Leonard erwacht“ geschnitten, Effekte erzeugt, Repo angelegt, memory.md geschrieben |
| 2026-10-24 | Claude (Windows-PC) | Teaser V1 mit Motion-Skills (social-teaser-video, beat-sync-editing, review-loop) gebaut, Hafen-Szene offen |
