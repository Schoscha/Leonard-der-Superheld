"""Leonard der Superheld – Hollywood-Teaser (Skill social-teaser-video, Schnitt nach beat-sync-editing).

Schnitte liegen im Takt: 144 BPM bei 24 fps = genau 10 Bilder pro Schlag.
Bogen: Aufbau (lange Einstellungen, Texte) -> Steigerung (kürzer) -> Höhepunkt (2 Schläge je Schnitt,
Comic-Einschläge) -> Stille -> Drop (Dach-Pose in Zeitlupe) -> Titel -> "BALD."
Aufruf (VPS): /root/sk-werbevideo/.venv/bin/python build.py      (vorher: node text/render.js)
"""
import json
import subprocess
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

ROOT = Path(__file__).parent
CLIPS = ROOT / 'clips'          # A.mp4 = gemini_generated_video_10c15bc5, C.mp4 = gemini_generated_video_6af2c6fc
OUT = ROOT / 'out'
TMP = ROOT / 'audio'
FPS = 24
SR = 48000
BPM = 144
BEAT = 60 / BPM                 # 0,4167 s = 10 Bilder
W, H = 1920, 1080

# (Clip, Start in der Quelle, Länge in Schlägen, Tempo, Zufahrt %, Weißblitz, Wackeln, Ton-Pegel)
SHOTS = [
    ('C', 0.00, 6, 0.55, 5, False, False, 0.6),   # Zimmer, Familie steht da
    ('A', 0.45, 4, 0.90, 4, True, False, 0.8),    # Power-Pose mit Speedlines
    ('C', 1.45, 3, 1.00, 5, True, False, 0.8),    # Abheben in Wolken
    ('A', 2.00, 3, 0.80, 6, False, False, 0.8),   # Papa gegen Roboter
    ('C', 3.00, 3, 1.00, 7, False, False, 0.8),   # VROOOM über der Stadt
    ('C', 4.30, 4, 1.00, 5, False, False, 0.8),   # Papa WHIZZ
    ('A', 5.00, 1, 1.00, 4, False, False, 0.8),   # Leonard rennt
    ('C', 6.00, 3, 1.00, 5, False, False, 0.8),   # Kinder fliegen, BOING CLANG
    ('A', 3.05, 2, 1.00, 3, True, True, 1.0),     # BÄÄMMM
    ('A', 6.45, 2, 1.00, 4, False, False, 0.9),   # Laser der Schwester
    ('A', 7.40, 2, 1.00, 3, True, True, 1.0),     # Wand-Explosion BAAANNNGGG
    ('A', 5.50, 2, 1.00, 3, True, True, 1.0),     # BOOOMMM
    (None, 0, 1, 1, 0, False, False, 0.0),        # Schwarz: ein Schlag Stille vor dem Drop
    ('A', 8.40, 6, 0.60, 6, True, False, 0.7),    # DROP: Dach-Pose, Zeitlupe
    ('C', 7.45, 8, 0.75, 5, False, False, 0.6),   # Sonnenuntergang-Flug + Titel
    ('END', 9.90, 5, 1.00, 0, False, False, 0.0), # Standbild "BALD."
]
CUTS = np.cumsum([0] + [s[2] for s in SHOTS]) * BEAT
TOTAL = float(CUTS[-1])
I_DROP, I_TITLE, I_END = 13, 14, 15
# Texte (je >= 3 s Standzeit), Zeiten auf Schnitte bezogen
TEXT = [('tA', CUTS[0] + 0.25, CUTS[2]), ('tB', CUTS[2] + 0.1, CUTS[5]), ('tC', CUTS[5] + 0.1, CUTS[8]),
        ('ti', CUTS[I_TITLE] + 0.6, CUTS[I_END]), ('en', CUTS[I_END] + 0.15, TOTAL)]


def run(cmd):
    subprocess.run(cmd, check=True)


# ---------------------------------------------------------------- Bild

def build_video(name='16x9'):
    inputs, chains, labels = [], [], []
    for i, (clip, ss, beats, tempo, zoom, flash, shake, _) in enumerate(SHOTS):
        dur = beats * BEAT
        if clip is None:
            inputs += ['-f', 'lavfi', '-t', f'{dur:.4f}', '-i', f'color=black:s={W}x{H}:r={FPS}']
            chains.append(f'[{i}:v]format=yuv420p,setsar=1[s{i}]')
            labels.append(f'[s{i}]')
            continue
        src = 'C' if clip == 'END' else clip
        src_dur = 0.06 if clip == 'END' else dur * tempo
        inputs += ['-ss', str(ss), '-t', f'{src_dur:.4f}', '-i', str(CLIPS / f'{src}.mp4')]
        z = zoom / 100
        chain = f'[{i}:v]setpts=(PTS-STARTPTS)/{tempo},'
        if tempo < 1:
            chain += f'minterpolate=fps={FPS}:mi_mode=blend,'          # weiche Zeitlupe
        chain += f'fps={FPS},'
        if i == I_TITLE:
            chain += 'eq=brightness=-0.07,'
        if clip == 'END':
            chain += f'tpad=stop_mode=clone:stop_duration={dur:.3f},eq=brightness=-0.18:saturation=0.8,'
        chain += (f"scale=w='2*trunc({W}*(1.02+{z}*t/{dur:.3f})/2)':h=-2:eval=frame:flags=lanczos,"
                  + (f"crop={W}:{H}:x='(iw-ow)/2+22*sin(t*95)*exp(-t*7)':y='(ih-oh)/2+16*cos(t*80)*exp(-t*7)',"
                     if shake else f'crop={W}:{H},')
                  + f'eq=contrast=1.08:saturation=1.12,setsar=1,format=yuv420p,trim=duration={dur:.4f}')
        if flash:
            chain += ',fade=in:st=0:d=0.14:color=white'
        if clip == 'END':
            chain += f',fade=out:st={dur - 0.6:.2f}:d=0.6'
        chains.append(chain + f'[s{i}]')
        labels.append(f'[s{i}]')
    n = len(SHOTS)
    chains.append(''.join(labels) + f'concat=n={n}:v=1:a=0,vignette=PI/5[v00]')
    # Verlauf unten für Lesbarkeit der Texte (wie im Lambo-Teaser), nur im Textteil
    inputs += ['-f', 'lavfi', '-t', f'{CUTS[8]:.3f}', '-i', f'color=black:s={W}x{H}:r={FPS}']
    chains.append(f"[{n}:v]format=rgba,geq=r=0:g=0:b=0:a='255*0.75*pow(max(0,(Y-{H}*0.5)/({H}*0.5)),1.2)'[grad]")
    chains.append('[v00][grad]overlay=eof_action=pass[v0]')
    cur, idx = 'v0', n + 1
    for tid, t0, t1 in TEXT:
        inputs += ['-loop', '1', '-t', f'{TOTAL:.3f}', '-i', str(ROOT / f'text/{name}_{tid}.png')]
        chains.append(f'[{idx}:v]format=rgba,fade=in:st={t0:.3f}:d=0.3:alpha=1,'
                      f'fade=out:st={t1 - 0.2:.3f}:d=0.2:alpha=1[t{idx}]')
        chains.append(f"[{cur}][t{idx}]overlay=x=0:y='if(lt(t,{t0:.3f}),30,max(0,30*(1-(t-{t0:.3f})/0.4)))'"
                      f':enable=between(t\\,{t0:.3f}\\,{t1:.3f})[v{idx}]')
        cur, idx = f'v{idx}', idx + 1
    bar = round((H - W / 2.39) / 2)          # Kino-Balken 2.39:1
    chains.append(f'[{cur}]drawbox=x=0:y=0:w=iw:h={bar}:color=black:t=fill,'
                  f'drawbox=x=0:y=ih-{bar}:w=iw:h={bar}:color=black:t=fill,format=yuv420p[v]')
    silent = OUT / f'leonard-teaser-{name}-stumm.mp4'
    run(['ffmpeg', '-nostdin', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(chains),
         '-map', '[v]', '-c:v', 'libx264', '-crf', '17', '-preset', 'slow', '-pix_fmt', 'yuv420p',
         '-r', str(FPS), '-t', f'{TOTAL:.3f}', str(silent)])
    return silent


# ---------------------------------------------------------------- Ton (aus dem Lambo-Teaser übernommen)

def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], btype='band', fs=SR, output='sos'), x)
def lp(x, fc): return sosfilt(butter(2, fc, btype='low', fs=SR, output='sos'), x)
def hp(x, fc): return sosfilt(butter(2, fc, btype='high', fs=SR, output='sos'), x)


def place(buf, sig, t0, gain=1.0):
    i = int(t0 * SR)
    if 0 <= i < len(buf):
        sig = sig[: len(buf) - i]
        buf[i:i + len(sig)] += sig * gain


rng = np.random.default_rng(7)


def impact(size=1.0):
    """Trailer-Einschlag: Sub-Thump mit Pitch-Drop + Rauschschlag + Hall-Schwanz."""
    n = int(SR * 2.6 * size); t = np.arange(n) / SR
    f = 30 + 90 * np.exp(-t * 18)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.2 / size)
    noise = rng.standard_normal(n)
    crack = hp(noise, 1500) * np.exp(-t * 35)
    tail = lp(noise, 900) * np.exp(-t * 2.8 / size) * 0.25
    return np.tanh(1.6 * (sub + crack * 0.5 + tail))


def braam(dur=2.6, root=36.7):
    """Tiefes Kino-Blech, Tonart d-Moll (D1 = 36,7 Hz)."""
    n = int(SR * dur); t = np.arange(n) / SR; sig = np.zeros(n)
    for mult, g in [(1, 1.0), (1.5, 0.6), (2, 0.5), (3, 0.25)]:
        for det in (-0.3, 0.3):
            sig += g * (2 * (((root * mult + det) * t) % 1) - 1)
    env = np.minimum(1, t / 0.04) * np.exp(-t * 1.0)
    return np.tanh(2.2 * lp(sig, 700) * env) * 0.8


def whoosh(dur=0.32):
    n = int(SR * dur); t = np.arange(n) / SR; noise = rng.standard_normal(n); sig = np.zeros(n)
    for c in range(16):
        a, b = c * n // 16, (c + 1) * n // 16
        fc = 400 + 5000 * (c / 16) ** 2
        sig[a:b] = bp(noise, fc, min(fc * 2.2, 20000))[a:b]
    return sig * np.sin(np.pi * t / dur) ** 2


def riser(dur):
    n = int(SR * dur); t = np.arange(n) / SR
    noise = hp(rng.standard_normal(n), 800)
    f = 120 * 2 ** (t / dur * 3)
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.5 * np.sin(4 * np.pi * np.cumsum(f) / SR)
    return (noise * 0.6 + tone * 0.35) * (t / dur) ** 2.2


def kick():
    n = int(SR * 0.35); t = np.arange(n) / SR
    return np.sin(2 * np.pi * (45 + 40 * np.exp(-t * 30)) * t) * np.exp(-t * 9)


def tick():
    n = int(SR * 0.05); t = np.arange(n) / SR
    return np.sin(2 * np.pi * 2200 * t) * np.exp(-t * 90)


def strings(dur, notes=(146.8, 174.6, 220.0)):
    """Ostinato in d-Moll (Achtel), treibt die Steigerung."""
    n = int(SR * dur); out = np.zeros(n); step = BEAT / 2; k = 0
    while k * step < dur:
        f = notes[k % len(notes)]; m = int(SR * step); tt = np.arange(m) / SR
        tone = sum(np.sin(2 * np.pi * f * h * tt) / h for h in (1, 2, 3)) * np.exp(-tt * 6)
        place(out, tone, k * step, 0.5); k += 1
    return lp(out, 2500)


def load_audio(src, ss, dur, tempo):
    wav = TMP / f'_seg_{src}_{ss}_{tempo}.wav'
    af = f'atempo={max(0.5, tempo)}' if tempo != 1 else 'anull'
    run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', str(ss), '-t', f'{dur * tempo:.4f}', '-i', str(CLIPS / f'{src}.mp4'),
         '-vn', '-af', af, '-ac', '2', '-ar', str(SR), str(wav)])
    _, data = wavfile.read(wav)
    data = data.astype(np.float64) / 32768.0
    fade = min(int(SR * 0.012), len(data) // 2)
    ramp = np.linspace(0, 1, fade)[:, None]
    data[:fade] *= ramp; data[-fade:] *= ramp[::-1]
    return data


def build_audio():
    n = int(SR * (TOTAL + 0.5)); mix = np.zeros((n, 2)); fx = np.zeros(n)
    # Originalton der Shots (Comic-Geräusche der Clips)
    for (clip, ss, beats, tempo, *_rest, gain), t0 in zip(SHOTS, CUTS[:-1]):
        if clip in (None, 'END') or gain == 0:
            continue
        seg = load_audio(clip, ss, beats * BEAT, tempo)
        i = int(t0 * SR); mix[i:i + len(seg)] += seg[: n - i] * gain * 0.55
    c = CUTS
    # Aufbau: Braam, Uhr-Ticken im Takt
    place(fx, braam(3.2), 0.0, 0.9); place(fx, impact(1.0), c[1], 0.7)
    for k in range(int(c[2] / BEAT)):
        place(fx, tick(), k * BEAT, 0.25)
    # Steigerung: Puls auf jedem Schlag, Streicher-Ostinato, Braam auf "Helden"
    for k in range(int((c[8] - c[2]) / BEAT)):
        place(fx, kick(), c[2] + k * BEAT, 0.55 if k % 2 == 0 else 0.35)
    place(fx, strings(c[8] - c[2]), c[2], 0.35)
    place(fx, braam(2.4), c[2], 0.7); place(fx, impact(0.8), c[5], 0.6)
    # Höhepunkt: doppelter Puls, Einschlag auf jedem Schnitt, Riser in den Drop
    for k in range(int((c[I_DROP - 1] - c[8]) / (BEAT / 2))):
        place(fx, kick(), c[8] + k * BEAT / 2, 0.5)
    place(fx, strings(c[I_DROP - 1] - c[8], (146.8, 220.0, 293.7)), c[8], 0.45)
    for j in range(8, I_DROP - 1):
        place(fx, impact(0.7), c[j], 0.75)
    place(fx, riser(c[I_DROP - 1] - c[6]), c[6], 0.6)
    # Whoosh vor jedem Schnitt (außer in die Stille)
    for j in range(1, I_END + 1):
        if j != I_DROP - 1:
            place(fx, whoosh(), c[j] - 0.28, 0.35)
    # Stille, dann DROP: größter Einschlag + Braam
    place(fx, impact(1.5), c[I_DROP], 1.0); place(fx, braam(3.0), c[I_DROP], 0.8)
    # Titel: Braam + Einschlag, BALD: letzter Schlag
    place(fx, braam(3.5, 43.65), c[I_TITLE], 0.8); place(fx, impact(1.2), c[I_TITLE] + 0.6, 0.85)
    place(fx, impact(1.3), c[I_END] + 0.15, 0.9)
    mix += fx[:, None]
    mix = mix[: int(SR * TOTAL)]
    fo = int(SR * 0.8); mix[-fo:] *= np.linspace(1, 0, fo)[:, None]
    mix /= max(1e-9, np.abs(mix).max()) / 0.95
    out = TMP / 'teaser-mix.wav'
    wavfile.write(out, SR, (mix * 32767).astype(np.int16))
    return out


def loudnorm_filter(wav):
    """Zweipassiges loudnorm auf -14 LUFS."""
    res = subprocess.run(['ffmpeg', '-nostdin', '-hide_banner', '-i', str(wav), '-af',
                          'loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'],
                         capture_output=True, text=True, check=True)
    m = json.loads(res.stderr[res.stderr.rindex('{'):])
    return (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
            f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")


def mux(name, silent, wav):
    final = OUT / f'leonard-teaser-{name}.mp4'
    run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', str(silent), '-i', str(wav), '-af', loudnorm_filter(wav),
         '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', str(SR),
         '-t', f'{TOTAL:.3f}', '-movflags', '+faststart', str(final)])
    return final


if __name__ == '__main__':
    OUT.mkdir(exist_ok=True); TMP.mkdir(exist_ok=True)
    wav = build_audio()
    print(mux('16x9', build_video('16x9'), wav))
    print(json.dumps({'laenge': round(TOTAL, 2), 'schnitte': [round(x, 2) for x in CUTS]}))
