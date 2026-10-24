#!/usr/bin/env bash
# Setzt "Leonard erwacht" aus den 4 Original-Clips und der Soundeffekt-Spur zusammen.
# Aufruf (Git Bash):  bash zusammensetzen.sh "<Ordner mit den 4 Clips>" <sfx.wav> <ausgabe.mp4>
# Beispiel:           bash zusammensetzen.sh "/c/Users/Neu/Videos/Leonard der Superheld/Leonard erwacht" sfx.wav test.mp4
# Die sfx.wav vorher mit sfx.py erzeugen (siehe memory.md).
set -euo pipefail
ORDNER="$1"; SFX="$2"; AUS="$3"
cd "$ORDNER"
# Reihenfolge der Geschichte: Aufwachen -> zum Schrank -> Verwandlung -> Spiegel
C1=$(ls leonsard*.mp4); C2=$(ls frame1*.mp4); C3=$(ls er_dreht*.mp4); C4=$(ls er_ist*.mp4)
ffmpeg -v error -y -i "$C1" -i "$C2" -i "$C3" -i "$C4" -i "$SFX" -filter_complex "
[0:v]settb=AVTB,fps=24,format=yuv420p[v0];[1:v]settb=AVTB,fps=24,format=yuv420p[v1];[2:v]settb=AVTB,fps=24,format=yuv420p[v2];[3:v]settb=AVTB,fps=24,format=yuv420p[v3];
[v0][v1]xfade=transition=fade:duration=0.3:offset=9.7[x1];
[x1][v2]xfade=transition=smoothleft:duration=0.4:offset=19.3[x2];
[x2][v3]xfade=transition=fade:duration=0.3:offset=29.0,fade=t=in:st=0:d=0.6,fade=t=out:st=38.2:d=0.8[vout];
[0:a]atrim=0:10,asetpts=PTS-STARTPTS[a0];[1:a]atrim=0:10,asetpts=PTS-STARTPTS[a1];[2:a]atrim=0:10,asetpts=PTS-STARTPTS[a2];[3:a]atrim=0:10,asetpts=PTS-STARTPTS[a3];
[a0][a1]acrossfade=d=0.3[b1];[b1][a2]acrossfade=d=0.4[b2];[b2][a3]acrossfade=d=0.3,volume=1.4[orig];
[4:a]volume=1.0[fx];
[orig][fx]amix=inputs=2:normalize=0:duration=longest,atrim=0:39,afade=t=out:st=38.0:d=1.0,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[aout]" \
  -map "[vout]" -map "[aout]" -c:v libx264 -crf 17 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -t 39 "$AUS"
echo "fertig: $AUS"
