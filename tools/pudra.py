"""Pudra Instagram tasarım yardımcıları."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

FD = '/mnt/skills/examples/canvas-design/canvas-fonts/'
SERIF_I = FD + 'InstrumentSerif-Italic.ttf'
SERIF = FD + 'InstrumentSerif-Regular.ttf'
SANS = FD + 'InstrumentSans-Regular.ttf'
SANS_B = FD + 'InstrumentSans-Bold.ttf'

BERRY = (142, 16, 72)
CREAM = (251, 246, 247)
PLUM = (42, 21, 32)
PINK = (244, 198, 212)

LOGO_A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'logo_A_klasik.png')
LOGO_B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'logo_B_berry.png')

LOGO_SIZE = 92
LOGO_X = 56
LOGO_Y_POST = 56
LOGO_Y_STORY = 210  # Instagram story üst arayüzünün altında


def f(path, size):
    return ImageFont.truetype(path, size)


def load(path):
    return ImageOps.exif_transpose(Image.open(path)).convert('RGB')


def fit(img, size, centering=(0.5, 0.5)):
    """Kırp + gerekirse kaliteli büyüt + keskinleştir."""
    w, h = size
    scale = max(w / img.width, h / img.height)
    out = ImageOps.fit(img, size, Image.LANCZOS, centering=centering)
    if scale > 1.15:  # düşük çözünürlük: netleştir
        out = out.filter(ImageFilter.UnsharpMask(radius=2, percent=90, threshold=2))
    return out


def logo(canvas, variant='B', story=False):
    lg = load(LOGO_B if variant == 'B' else LOGO_A).resize((LOGO_SIZE, LOGO_SIZE), Image.LANCZOS)
    canvas.paste(lg, (LOGO_X, LOGO_Y_STORY if story else LOGO_Y_POST))


def spaced(d, xy, text, font, fill, tracking=4, anchor='la'):
    x, y = xy
    if anchor[0] == 'm':
        total = sum(d.textlength(c, font=font) + tracking for c in text) - tracking
        x -= total / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += d.textlength(c, font=font) + tracking


def gradient(canvas, top, height, color=(0, 0, 0), max_alpha=170):
    ov = Image.new('L', (1, height))
    for i in range(height):
        ov.putpixel((0, i), int(max_alpha * (i / height) ** 1.6))
    ov = ov.resize((canvas.width, height))
    solid = Image.new('RGB', (canvas.width, height), color)
    region = canvas.crop((0, top, canvas.width, top + height))
    canvas.paste(Image.composite(solid, region, ov), (0, top))


# ---- dekor yardımcıları
import math
RED = (214, 40, 57)
def sparkle(d, x, y, r, col):
    pts = []
    for i in range(8):
        a = math.pi / 4 * i - math.pi / 2
        rr = r if i % 2 == 0 else r * 0.28
        pts.append((x + rr * math.cos(a), y + rr * math.sin(a)))
    d.polygon(pts, fill=col)

def flag_shape(d, x, y, s, col=RED, pole=PLUM):
    d.rectangle([x, y, x + int(s * 0.07), y + s], fill=pole)
    p = x + int(s * 0.07)
    d.polygon([(p, y), (p + int(s * 0.75), y + int(s * 0.05)), (p + int(s * 0.55), y + int(s * 0.22)),
               (p + int(s * 0.78), y + int(s * 0.42)), (p, y + int(s * 0.45))], fill=col)

def wave(d, x0, x1, y, amp, period, col, width=6):
    pts = [(x, y + amp * math.sin((x - x0) / period * 2 * math.pi)) for x in range(x0, x1, 4)]
    d.line(pts, fill=col, width=width, joint='curve')

def sticker(canvas, center, text, font, bg, fg, angle=-6, padx=34, pady=18):
    tmp = Image.new('RGBA', (10, 10)); td = ImageDraw.Draw(tmp)
    tw = td.textlength(text, font=font); bb = font.getbbox(text)
    th = bb[3] - bb[1]
    w, h = int(tw + 2 * padx), int(th + 2 * pady)
    s = Image.new('RGBA', (w, h), (0, 0, 0, 0)); sd = ImageDraw.Draw(s)
    sd.rounded_rectangle([0, 0, w - 1, h - 1], radius=h // 2, fill=bg)
    sd.text((padx, pady - bb[1]), text, font=font, fill=fg)
    s = s.rotate(angle, expand=True, resample=Image.BICUBIC)
    canvas.paste(s, (int(center[0] - s.width / 2), int(center[1] - s.height / 2)), s)

def dots(d, x0, y0, cols, rows, gap, r, col):
    for i in range(cols):
        for j in range(rows):
            d.ellipse([x0 + i * gap - r, y0 + j * gap - r, x0 + i * gap + r, y0 + j * gap + r], fill=col)
