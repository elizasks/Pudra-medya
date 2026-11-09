"""PUDRA GÜNDEM — Met Gala 2027 teması: gündelik kıyafet (10 Kasım 2026)."""
from anim import *
import sys, os
W, H = 1080, 1350
DENIM = (64, 96, 150); DENIM2 = (44, 70, 116)
CAMEL = (196, 150, 98); CAMEL2 = (160, 116, 70)
LEATHER = (34, 26, 30)
OUT = 'out_gm'
os.makedirs(OUT, exist_ok=True)

# ---------------- kıyafet ikonları (cx,cy merkez, s ölçek ~ yükseklik/2)
def tee(d, cx, cy, s, col=CREAM, line=PLUM):
    k = s / 100
    pts = [(-40, -80), (-15, -88), (15, -88), (40, -80), (95, -45), (72, -5), (48, -22), (48, 90), (-48, 90), (-48, -22), (-72, -5), (-95, -45)]
    P = [(cx + x * k, cy + y * k) for x, y in pts]
    d.polygon(P, fill=col, outline=line, width=max(2, int(5 * k)))
    d.arc([cx - 20 * k, cy - 105 * k, cx + 20 * k, cy - 68 * k], 20, 160, fill=line, width=max(2, int(5 * k)))

def jeans(d, cx, cy, s, col=DENIM, line=DENIM2):
    k = s / 100
    d.polygon([(cx - 55 * k, cy - 90 * k), (cx + 55 * k, cy - 90 * k), (cx + 62 * k, cy + 95 * k), (cx + 12 * k, cy + 95 * k),
               (cx, cy - 20 * k), (cx - 12 * k, cy + 95 * k), (cx - 62 * k, cy + 95 * k)], fill=col)
    d.rectangle([cx - 55 * k, cy - 90 * k, cx + 55 * k, cy - 72 * k], fill=line)
    d.line([(cx, cy - 72 * k), (cx, cy - 25 * k)], fill=line, width=max(2, int(4 * k)))
    d.arc([cx - 50 * k, cy - 80 * k, cx - 10 * k, cy - 40 * k], 0, 90, fill=CAMEL, width=max(2, int(4 * k)))
    d.arc([cx + 10 * k, cy - 80 * k, cx + 50 * k, cy - 40 * k], 90, 180, fill=CAMEL, width=max(2, int(4 * k)))
    d.ellipse([cx - 5 * k, cy - 86 * k, cx + 5 * k, cy - 76 * k], fill=CAMEL)

def trench(d, cx, cy, s, col=CAMEL, line=CAMEL2):
    k = s / 100
    d.polygon([(cx - 40 * k, cy - 92 * k), (cx + 40 * k, cy - 92 * k), (cx + 70 * k, cy - 60 * k), (cx + 78 * k, cy + 95 * k),
               (cx - 78 * k, cy + 95 * k), (cx - 70 * k, cy - 60 * k)], fill=col)
    d.polygon([(cx - 40 * k, cy - 92 * k), (cx, cy - 20 * k), (cx - 30 * k, cy - 10 * k), (cx - 55 * k, cy - 60 * k)], fill=line)
    d.polygon([(cx + 40 * k, cy - 92 * k), (cx, cy - 20 * k), (cx + 30 * k, cy - 10 * k), (cx + 55 * k, cy - 60 * k)], fill=line)
    d.rectangle([cx - 76 * k, cy + 5 * k, cx + 76 * k, cy + 20 * k], fill=line)
    for yy in (-5, 35, 65):
        for xx in (-18, 18):
            d.ellipse([cx + xx * k - 5 * k, cy + yy * k - 5 * k, cx + xx * k + 5 * k, cy + yy * k + 5 * k], fill=PLUM)

def hoodie(d, cx, cy, s, col=PINK, line=BERRY):
    k = s / 100
    d.ellipse([cx - 42 * k, cy - 110 * k, cx + 42 * k, cy - 40 * k], fill=col, outline=line, width=max(2, int(4 * k)))
    d.rounded_rectangle([cx - 70 * k, cy - 70 * k, cx + 70 * k, cy + 92 * k], radius=int(26 * k), fill=col, outline=line, width=max(2, int(4 * k)))
    d.rounded_rectangle([cx - 40 * k, cy + 20 * k, cx + 40 * k, cy + 65 * k], radius=int(10 * k), outline=line, width=max(2, int(4 * k)))
    d.line([(cx - 10 * k, cy - 50 * k), (cx - 12 * k, cy - 5 * k)], fill=line, width=max(2, int(4 * k)))
    d.line([(cx + 10 * k, cy - 50 * k), (cx + 12 * k, cy - 5 * k)], fill=line, width=max(2, int(4 * k)))

def puffer(d, cx, cy, s, col=RED, line=BERRY):
    k = s / 100
    for i in range(5):
        y0 = cy - 85 * k + i * 36 * k
        w = 72 + (6 if i in (1, 2, 3) else 0)
        d.rounded_rectangle([cx - w * k, y0, cx + w * k, y0 + 38 * k], radius=int(18 * k), fill=col, outline=line, width=max(2, int(3 * k)))
    d.line([(cx, cy - 85 * k), (cx, cy + 95 * k)], fill=line, width=max(2, int(4 * k)))

def button(d, cx, cy, s, col=BERRY):
    k = s / 100
    d.ellipse([cx - 70 * k, cy - 70 * k, cx + 70 * k, cy + 70 * k], fill=col)
    d.ellipse([cx - 55 * k, cy - 55 * k, cx + 55 * k, cy + 55 * k], outline=PINK, width=max(2, int(4 * k)))
    for dx, dy in ((-16, -16), (16, -16), (-16, 16), (16, 16)):
        d.ellipse([cx + (dx - 8) * k, cy + (dy - 8) * k, cx + (dx + 8) * k, cy + (dy + 8) * k], fill=CREAM)

def jacket(d, cx, cy, s, col=LEATHER, line=(90, 80, 86)):
    k = s / 100
    d.polygon([(cx - 45 * k, cy - 90 * k), (cx + 45 * k, cy - 90 * k), (cx + 78 * k, cy - 55 * k), (cx + 72 * k, cy + 80 * k),
               (cx - 72 * k, cy + 80 * k), (cx - 78 * k, cy - 55 * k)], fill=col)
    d.polygon([(cx - 45 * k, cy - 90 * k), (cx + 10 * k, cy - 30 * k), (cx - 20 * k, cy + 10 * k), (cx - 60 * k, cy - 55 * k)], fill=line)
    d.line([(cx + 20 * k, cy - 70 * k), (cx - 5 * k, cy + 80 * k)], fill=(200, 200, 205), width=max(2, int(4 * k)))
    d.rectangle([cx - 72 * k, cy + 62 * k, cx + 72 * k, cy + 80 * k], fill=line)

ICONS = {'tee': tee, 'jeans': jeans, 'trench': trench, 'hoodie': hoodie, 'puffer': puffer, 'button': button, 'jacket': jacket}

def hanger_swing(c, t, cx, top, s, fn, phase=0.0):
    """Askıda sallanan kıyafet (ayrı katmanda döndürülür)."""
    lay = Image.new('RGBA', (int(s * 2.6), int(s * 3.0)), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    hx = lay.width // 2
    ld.arc([hx - 16, 0, hx + 16, 34], 180, 90, fill=PLUM, width=6)
    ld.line([(hx, 34), (hx - s * 0.75, s * 0.42), (hx + s * 0.75, s * 0.42), (hx, 34)], fill=PLUM, width=7)
    fn(ld, hx, s * 0.42 + s * 0.95, s)
    ang = math.sin(t * 2.2 + phase) * 6
    lay = lay.rotate(ang, center=(hx, 0), resample=Image.BICUBIC)
    c.paste(lay, (int(cx - hx), int(top)), lay)

def frame(d, x0, y0, x1, y1, k, col=PLUM, mat=CREAM):
    """Müze çerçevesi; k 0→1 kenarları çizer."""
    if k <= 0: return
    w = 18
    L = [((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)), ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))]
    for i, (a, b) in enumerate(L):
        f = max(0, min(1, k * 4 - i))
        if f > 0: d.line([a, (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f)], fill=col, width=w)

def label_card(c, x, y, a, title, sub):
    if a <= 0: return
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    al = int(255 * a)
    ld.rectangle([x, y, x + 300, y + 96], fill=CREAM + (al,), outline=PLUM + (al,), width=3)
    ld.text((x + 18, y + 14), title, font=F(BOLD, 28), fill=PLUM + (al,))
    ld.text((x + 18, y + 54), sub, font=F(REG, 22), fill=BERRY + (al,))
    c.paste(lay, (0, 0), lay)

def sparkles(d, t, pts):
    for (x, y, r, st, col) in pts:
        k = back((t - st) / 0.4)
        if k > 0: sparkle(d, x, y, r * k * (1 + 0.12 * math.sin(t * 5 + x)), col)

def footer(c, i, col):
    text_a(c, (80, 1280), 'PUDRA DERGİ', F(BOLD, 22), col, 1)
    text_a(c, (W - 80, 1278), f'{i}/5', F(MED, 24), col, 1, anchor='ra')

# ---------------- 1 · KAPAK
def p1(t):
    c = Image.new('RGB', (W, H), BERRY); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 18; s = ease(t / 0.8)
    r = int(520 * s); d.ellipse([1060 - r - p, 1180 - r - p, 1060 + r + p, 1180 + r + p], fill=PINK)
    r2 = int(240 * s); d.ellipse([-60 - r2, 600 - r2, -60 + r2, 600 + r2], fill=RED)
    dots(d, 830, 120, 5, 4, 44, 7, (176, 60, 110))
    sticker(c, (330, 300), 'PUDRA GÜNDEM · MET GALA 2027', F(BOLD, 30), CREAM, BERRY, -4, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Kotun, tişörtün,', F(BOLD, 88), 380, 0.35, CREAM),
                                  ('trençkotun…', F(BOLD, 88), 485, 0.6, CREAM),
                                  ('artık müzelik.', F(ACC, 118), 600, 0.9, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(40 * (1 - a)))
    # çerçeve içinde sallanan tişört + kot
    fx0, fy0, fx1, fy1 = 470, 790, 960, 1210
    k = ease((t - 1.2) / 0.9)
    if k > 0:
        lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rectangle([fx0, fy0, fx1, fy1], fill=CREAM + (int(255 * k),)); c.paste(lay, (0, 0), lay)
    frame(d, fx0, fy0, fx1, fy1, k)
    a = ease((t - 1.5) / 0.5)
    if a > 0:
        hanger_swing(c, t, 590, fy0 + 25 - int(40 * (1 - a)), 108, tee, 0)
        hanger_swing(c, t, 840, fy0 + 25 - int(40 * (1 - a)), 108, jeans, 1.2)
    label_card(c, 120, 1060, ease((t - 2.3) / 0.4), 'Gündelik No. 1', 'Pamuk & denim, 2027')
    sparkles(d, t, [(960, 760, 40, 2.6, CREAM), (440, 800, 26, 2.9, PINK), (1000, 1230, 30, 3.1, CREAM)])
    a = ease((t - 3.0) / 0.4)
    if a > 0: text_a(c, (70 + int(10 * math.sin(t * 6)), 1270), 'kaydır  ›', F(BOLD, 40), CREAM, a)
    logo(c, 'B'); return c

# ---------------- 2 · HABER
def p2(t):
    c = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.4) * 14; r = int(380 * ease(t / 0.7))
    d.ellipse([W + 40 - r - p, 140 - r - p, W + 40 + r + p, 140 + r + p], fill=PINK)
    sticker(c, (300, 250), 'NE OLDU?', F(BOLD, 30), BERRY, CREAM, -5, back((t - 0.2) / 0.4))
    lines = [('Met Müzesi 2027 sergisinin', F(BOLD, 58), PLUM), ('temasını açıkladı:', F(BOLD, 58), PLUM)]
    y = 340
    for j, (ln, fnt, col) in enumerate(lines):
        a = ease((t - 0.4 - j * 0.15) / 0.45); text_a(c, (70, y), ln, fnt, col, a, int(30 * (1 - a))); y += 72
    a = ease((t - 0.8) / 0.5)
    text_a(c, (70, y + 10), 'extraORDINARY', F(BOLD, 104), BERRY, a, int(30 * (1 - a)))
    text_a(c, (74, y + 140), 'gündelik olanın şiiri', F(ACC, 56), RED, ease((t - 1.1) / 0.5))
    y2 = y + 230
    a = ease((t - 1.4) / 0.5)
    for ln in wrap(F(REG, 36), 'Kot, beyaz tişört, kapüşonlu… Tasarımcıların her gün giydiğimiz parçaları nasıl sanata dönüştürdüğü anlatılacak.', W - 160):
        text_a(c, (70, y2), ln, F(REG, 36), PLUM, a); y2 += 48
    # müze binası illüstrasyonu + tarih kartları
    bx, by = 290, 1150
    k = ease((t - 1.0) / 0.7)
    if k > 0:
        h = 150 * k
        d.polygon([(bx - 200, by - h - 10), (bx + 200, by - h - 10), (bx, by - h - 95 * k)], fill=BERRY)
        d.rectangle([bx - 210, by - h - 10, bx + 210, by - h + 6], fill=PLUM)
        for i in range(5):
            xx = bx - 160 + i * 80
            d.rectangle([xx - 16, by - h + 6, xx + 16, by], fill=PINK)
        d.rectangle([bx - 230, by, bx + 230, by + 22], fill=PLUM)
        d.rectangle([bx - 250, by + 22, bx + 250, by + 42], fill=BERRY)
    for j, (big, sm, col, fg) in enumerate([('3 MAYIS 2027', 'Met Gala gecesi', RED, CREAM), ('9 MAYIS 2027', 'Sergi açılıyor', PLUM, CREAM)]):
        s = back((t - 1.9 - j * 0.35) / 0.45)
        if s > 0:
            cx, cy = 790, 1010 + j * 145
            cw, ch = int(400 * s), int(122 * s)
            lay = Image.new('RGBA', (cw + 4, ch + 4), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
            ld.rounded_rectangle([0, 0, cw, ch], radius=int(24 * s), fill=col)
            if s > 0.6:
                ld.text((cw // 2, int(52 * s)), big, font=F(BOLD, max(8, int(42 * s))), fill=fg, anchor='ms')
                ld.text((cw // 2, int(96 * s)), sm, font=F(MED, max(8, int(28 * s))), fill=PINK if col != PINK else PLUM, anchor='ms')
            lay = lay.rotate(-3 + j * 5, expand=True, resample=Image.BICUBIC)
            c.paste(lay, (cx - lay.width // 2, cy - lay.height // 2), lay)
    sparkles(d, t, [(560, 900, 30, 2.8, BERRY), (1010, 1190, 26, 3.1, RED)])
    footer(c, 2, BERRY)
    logo(c, 'B'); return c

# ---------------- 3 · NELER VAR
GRID = [('jeans', 'Kot'), ('tee', 'Beyaz tişört'), ('trench', 'Trençkot'),
        ('hoodie', 'Kapüşonlu'), ('puffer', 'Şişme mont'), ('jacket', 'Deri ceket')]
def p3(t):
    c = Image.new('RGB', (W, H), PINK); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 16; r = int(330 * ease(t / 0.7))
    d.ellipse([W + 60 - r - p, 120 - r - p, W + 60 + r + p, 120 + r + p], fill=CREAM)
    sticker(c, (330, 250), 'SERGİDE NELER VAR?', F(BOLD, 30), PLUM, PINK, -4, back((t - 0.2) / 0.4))
    a = ease((t - 0.4) / 0.5)
    text_a(c, (70, 330), 'Dolabının', F(BOLD, 80), PLUM, a, int(30 * (1 - a)))
    a = ease((t - 0.6) / 0.5)
    text_a(c, (70, 425), 'en sade parçaları.', F(ACC, 76), BERRY, a, int(30 * (1 - a)))
    cw, chh = 290, 270
    for i, (ic, lab) in enumerate(GRID):
        s = back((t - 0.9 - i * 0.2) / 0.45)
        if s <= 0: continue
        col, row = i % 3, i // 3
        cx = 70 + cw // 2 + col * (cw + 25); cy = 560 + chh // 2 + row * (chh + 25)
        lay = Image.new('RGBA', (cw, chh), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ld.rounded_rectangle([0, 0, cw - 1, chh - 1], radius=30, fill=CREAM)
        bob = math.sin(t * 3 + i) * 5
        ICONS[ic](ld, cw // 2, 112 + bob, 72)
        ld.text((cw // 2, chh - 26), lab, font=F(BOLD, 30), fill=PLUM, anchor='ms')
        if s != 1: lay = lay.resize((max(1, int(cw * s)), max(1, int(chh * s))), Image.LANCZOS)
        lay = lay.rotate(math.sin(i * 1.7) * 3, expand=True, resample=Image.BICUBIC)
        c.paste(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)), lay)
    a = ease((t - 2.4) / 0.5)
    text_a(c, (70, 1160), '…ve kâğıt, plastik, düğme, çatal-bıçak,', F(MED, 32), PLUM, a)
    text_a(c, (70, 1202), 'hatta kırık porselen bile.', F(MED, 32), PLUM, a)
    footer(c, 3, PLUM)
    logo(c, 'B'); return c

# ---------------- 4 · SANA NE DEMEK
def p4(t):
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.4) * 16; r = int(360 * ease(t / 0.7))
    d.ellipse([W - 40 - r - p, 230 - r - p, W - 40 + r + p, 230 + r + p], fill=BERRY)
    sticker(c, (300, 250), 'SANA NE DEMEK?', F(BOLD, 30), PINK, PLUM, -5, back((t - 0.2) / 0.4))
    for txt, font, y, st, col in [('Stil, en çok', F(BOLD, 84), 340, 0.4, CREAM),
                                  ('giydiğin parçada', F(BOLD, 84), 440, 0.6, CREAM),
                                  ('saklı.', F(ACC, 96), 545, 0.85, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    # spot ışığı altında kaide üstündeki tişört
    k = ease((t - 1.0) / 0.6)
    if k > 0:
        lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        fl = 0.85 + 0.15 * math.sin(t * 7)
        ld.polygon([(860, 690), (690, 1180), (1030, 1180)], fill=(255, 240, 220, int(70 * k * fl)))
        c.paste(lay, (0, 0), lay)
        d.rectangle([760, 1110, 960, 1190], fill=BERRY); d.rectangle([740, 1095, 980, 1115], fill=PINK)
        d.rectangle([815, 680, 905, 700], fill=PINK)
        tee(d, 860, 1000 - int(30 * (1 - k)), 80)
    rows = [('DENE', 'En sevdiğin kotu, beyaz gömlek ve blazerla "yeni" gibi giy.', RED),
            ('DENEME', 'Trend diye yeni "basic" alma. Dolabındaki zaten hazır.', CREAM)]
    y = 720
    for j, (tag, txt, col) in enumerate(rows):
        a = ease((t - 1.6 - j * 0.5) / 0.5)
        if a <= 0: continue
        sticker(c, (150, y + 30), tag, F(BOLD, 32), col, PLUM if col == CREAM else CREAM, -3 + j * 5, back((t - 1.6 - j * 0.5) / 0.45))
        yy = y + 85
        for ln in wrap(F(MED, 36), txt, 560):
            text_a(c, (70, yy), ln, F(MED, 36), CREAM, a, int(20 * (1 - a))); yy += 48
        y = yy + 40
    sparkles(d, t, [(980, 700, 30, 2.4, PINK), (700, 760, 20, 2.7, CREAM)])
    footer(c, 4, PINK)
    logo(c, 'B'); return c

# ---------------- 5 · CTA
OPTS = [('jeans', 'Kotum'), ('tee', 'Beyaz tişörtüm'), ('trench', 'Trençkotum'), ('jacket', 'Deri ceketim')]
def p5(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 18; r = int(300 * ease(t / 0.7))
    d.ellipse([W + 20 - r - p, H + 20 - r - p, W + 20 + r + p, H + 20 + r + p], fill=BERRY)
    dots(d, 840, 130, 5, 3, 44, 7, (236, 100, 110))
    sticker(c, (300, 250), 'SIRA SENDE', F(BOLD, 30), CREAM, RED, -5, back((t - 0.2) / 0.4))
    for txt, font, y, st, col in [('Dolabındaki', F(BOLD, 86), 340, 0.4, CREAM),
                                  ('müzelik parça', F(ACC, 96), 440, 0.65, PINK),
                                  ('hangisi?', F(BOLD, 86), 560, 0.9, CREAM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    for i, (ic, lab) in enumerate(OPTS):
        s = back((t - 1.2 - i * 0.22) / 0.45)
        if s <= 0: continue
        y = 720 + i * 112
        lay = Image.new('RGBA', (900, 96), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ld.rounded_rectangle([0, 0, 899, 95], radius=48, fill=CREAM)
        ld.ellipse([10, 8, 90, 88], fill=PLUM)
        ld.text((50, 64), str(i + 1), font=F(BOLD, 48), fill=CREAM, anchor='ms')
        ld.text((120, 66), lab, font=F(BOLD, 44), fill=PLUM, anchor='ls')
        ICONS[ic](ld, 830, 50 + math.sin(t * 3 + i) * 3, 38)
        if s != 1: lay = lay.resize((max(1, int(900 * s)), max(1, int(96 * s))), Image.LANCZOS)
        c.paste(lay, (int(W / 2 - lay.width / 2), int(y + 48 - lay.height / 2)), lay)
    a = ease((t - 2.4) / 0.5)
    text_a(c, (70, 1172), 'Numarasını yorumlara yaz.', F(BOLD, 38), CREAM, a)
    sticker(c, (W // 2 + 170, 1278), 'Stil ikizine gönder ›', F(BOLD, 36), PLUM, CREAM, -3,
            back((t - 2.9) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 34, 16)
    logo(c, 'A'); return c

# ---------------- STORY
def story(t):
    SW, SH = 1080, 1920
    c = Image.new('RGB', (SW, SH), BERRY); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 22; s = ease(t / 0.8)
    r = int(380 * s); d.ellipse([1100 - r - p, 1920 - r - p, 1100 + r + p, 1920 + r + p], fill=PINK)
    r2 = int(260 * s); d.ellipse([-80 - r2, 420 - r2, -80 + r2, 420 + r2], fill=RED)
    dots(d, 830, 380, 5, 3, 44, 7, (176, 60, 110))
    sticker(c, (360, 420), 'PUDRA GÜNDEM', F(BOLD, 34), CREAM, BERRY, -5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Met Gala 2027', F(BOLD, 96), 520, 0.35, CREAM),
                                  ('teması belli:', F(BOLD, 96), 630, 0.6, CREAM),
                                  ('gündelik kıyafet.', F(ACC, 100), 750, 0.9, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(40 * (1 - a)))
    fx0, fy0, fx1, fy1 = 200, 940, 880, 1440
    k = ease((t - 1.2) / 0.9)
    if k > 0:
        lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rectangle([fx0, fy0, fx1, fy1], fill=CREAM + (int(255 * k),)); c.paste(lay, (0, 0), lay)
    frame(d, fx0, fy0, fx1, fy1, k)
    a = ease((t - 1.5) / 0.5)
    if a > 0:
        hanger_swing(c, t, 345, fy0 + 30, 112, tee, 0)
        hanger_swing(c, t, 540, fy0 + 30, 112, jeans, 1.1)
        hanger_swing(c, t, 740, fy0 + 30, 112, trench, 2.2)
    a = ease((t - 2.4) / 0.5)
    text_a(c, (SW // 2, 1525), 'Senin dolabın da müzelik mi?', F(MED, 44), CREAM, a, anchor='ms')
    s2 = back((t - 2.9) / 0.45)
    if s2 > 0: sticker(c, (SW // 2 + int(8 * math.sin(t * 6)), 1595), 'Yeni postta ›', F(BOLD, 44), PLUM, CREAM, 0, s2, 44, 22)
    sparkles(d, t, [(930, 920, 44, 2.6, CREAM), (160, 960, 30, 2.9, PINK)])
    logo(c, 'B', True); return c

PAGES = [p1, p2, p3, p4, p5]
if __name__ == '__main__':
    arg = sys.argv[1]
    if arg == 'preview':
        tt = float(sys.argv[2]) if len(sys.argv) > 2 else 5
        for i, f in enumerate(PAGES): f(tt).save(f'{OUT}/prev_{i+1}.jpg', quality=85)
        story(tt).save(f'{OUT}/prev_story.jpg', quality=85)
    elif arg == 'story':
        render(story, f'{OUT}/story.mp4', 6, (1080, 1920), f'{OUT}/story.jpg')
    else:
        i = int(arg); render(PAGES[i - 1], f'{OUT}/p{i}.mp4', 6, (W, H), f'{OUT}/p{i}.jpg')
