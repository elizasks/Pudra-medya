"""Pudra hareketli tasarım motoru (Poppins + Lora vurgu)."""
import math, os, subprocess, shutil
from PIL import Image, ImageDraw, ImageFont
from pudra import (BERRY, CREAM, PLUM, PINK, RED, LOGO_A, LOGO_B, LOGO_SIZE, LOGO_X,
                   LOGO_Y_POST, LOGO_Y_STORY, load, sparkle, dots)

GF = '/usr/share/fonts/truetype/google-fonts/'
CF = '/mnt/skills/examples/canvas-design/canvas-fonts/'
BOLD = GF + 'Poppins-Bold.ttf'
MED = GF + 'Poppins-Medium.ttf'
REG = GF + 'Poppins-Regular.ttf'
ACC = CF + 'Lora-BoldItalic.ttf'
_fc = {}
def F(p, s):
    k = (p, s)
    if k not in _fc: _fc[k] = ImageFont.truetype(p, s)
    return _fc[k]

FPS = 30
def ease(t): t = max(0.0, min(1.0, t)); return 1 - (1 - t) ** 3
def back(t):
    t = max(0.0, min(1.0, t)); c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2

_logos = {}
def logo(c, v, story=False):
    if v not in _logos:
        _logos[v] = load(LOGO_B if v == 'B' else LOGO_A).resize((LOGO_SIZE, LOGO_SIZE), Image.LANCZOS)
    c.paste(_logos[v], (LOGO_X, LOGO_Y_STORY if story else LOGO_Y_POST))

def text_a(c, xy, txt, font, col, a, dy=0, anchor='la'):
    """Saydamlık + kayma ile metin."""
    if a <= 0: return
    x, y = xy
    if a >= 1 and dy == 0:
        ImageDraw.Draw(c).text((x, y), txt, font=font, fill=col, anchor=anchor); return
    layer = Image.new('RGBA', c.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).text((x, y + dy), txt, font=font, fill=col + (int(255 * a),), anchor=anchor)
    c.paste(layer, (0, 0), layer)

def wrap(font, text, maxw):
    d = ImageDraw.Draw(Image.new('RGB', (1, 1)))
    words = text.split(); lines = []; cur = ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

def waving_flag(d, x, y, s, t, col=RED, pole=PLUM):
    d.rectangle([x, y, x + int(s * 0.07), y + s], fill=pole)
    p = x + int(s * 0.07)
    w = math.sin(t * 5) * s * 0.04
    w2 = math.sin(t * 5 + 1.3) * s * 0.05
    d.polygon([(p, y), (p + s * 0.37, y + s * 0.03 + w), (p + s * 0.75, y + s * 0.05 + w2),
               (p + s * 0.55, y + s * 0.22 + w2 * 0.6), (p + s * 0.78, y + s * 0.42 + w2),
               (p + s * 0.37, y + s * 0.44 + w), (p, y + s * 0.45)], fill=col)

def sticker(c, center, txt, font, bg, fg, angle, scale=1.0, padx=30, pady=16):
    if scale <= 0.02: return
    d0 = ImageDraw.Draw(Image.new('RGB', (1, 1)))
    tw = d0.textlength(txt, font=font); bb = font.getbbox(txt); th = bb[3] - bb[1]
    w, h = int(tw + 2 * padx), int(th + 2 * pady)
    s = Image.new('RGBA', (w, h), (0, 0, 0, 0)); sd = ImageDraw.Draw(s)
    sd.rounded_rectangle([0, 0, w - 1, h - 1], radius=h // 2, fill=bg)
    sd.text((padx, pady - bb[1]), txt, font=font, fill=fg)
    if scale != 1: s = s.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    s = s.rotate(angle, expand=True, resample=Image.BICUBIC)
    c.paste(s, (int(center[0] - s.width / 2), int(center[1] - s.height / 2)), s)

def wave_line(d, x0, x1, y, amp, period, col, width, phase=0.0):
    if x1 - x0 < 8: return
    pts = [(x, y + amp * math.sin((x - x0) / period * 2 * math.pi + phase)) for x in range(x0, int(x1), 4)]
    d.line(pts, fill=col, width=width, joint='curve')

def render(draw_fn, path_mp4, dur, size, path_jpg=None):
    """draw_fn(t) -> Image. mp4 + son kare jpg üretir."""
    tmp = path_mp4 + '_frames'
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    n = int(dur * FPS)
    for k in range(n):
        draw_fn(k / FPS).save(f'{tmp}/{k:04d}.jpg', quality=90)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', f'{tmp}/%04d.jpg',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p',
                    '-movflags', '+faststart', path_mp4], check=True)
    if path_jpg: draw_fn(99).save(path_jpg, quality=92)
    shutil.rmtree(tmp)
