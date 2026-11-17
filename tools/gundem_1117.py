"""PUDRA GÜNDEM — 'Cam cilt' videolarının dürüst hali: 38 viral videodan 36'sı yanıltıcı (17 Kasım 2026).
Kaynak: EADV 2026 kongresi çalışması; Türkiye basını 16 Kasım (Prof. Dr. Aslı Tatlıparmak yorumu)."""
from anim import *
import sys, os
W, H = 1080, 1350
OUT = 'out_1117'; os.makedirs(OUT, exist_ok=True)
GLASS = (226, 240, 246)
SKIN = (246, 214, 196)
SKIN2 = (232, 190, 170)


# ---------- illüstrasyonlar
def phone(c, t, cx, cy, s=1.0, frame=PLUM, screen=PINK, badge=True):
    """Telefon: içinde parlayan 'cam cilt' yüzü, kayan parıltı şeridi, oynat simgesi ve uyarı rozeti."""
    w, h = int(340 * s), int(620 * s)
    lay = Image.new('RGBA', (w + int(120 * s), h + int(120 * s)), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    ox, oy = int(60 * s), int(60 * s)
    d.rounded_rectangle([ox, oy, ox + w, oy + h], radius=int(54 * s), fill=frame)
    d.rounded_rectangle([ox + 18 * s, oy + 18 * s, ox + w - 18 * s, oy + h - 18 * s], radius=int(40 * s), fill=screen)
    d.rounded_rectangle([ox + w / 2 - 50 * s, oy + 30 * s, ox + w / 2 + 50 * s, oy + 48 * s], radius=int(9 * s), fill=frame)
    # yüz
    fx, fy = ox + w / 2, oy + h * 0.44
    d.ellipse([fx - 100 * s, fy - 130 * s, fx + 100 * s, fy + 130 * s], fill=SKIN)
    d.arc([fx - 40 * s, fy + 40 * s, fx + 40 * s, fy + 80 * s], 20, 160, fill=BERRY, width=int(8 * s))
    for ex in (-38, 38):
        d.arc([fx + ex * s - 18 * s, fy - 30 * s, fx + ex * s + 18 * s, fy - 6 * s], 200, 340, fill=frame, width=int(6 * s))
    # kayan parıltı (cam etkisi)
    ph = (t * 0.6) % 1.0
    gx = fx - 160 * s + ph * 320 * s
    shine = Image.new('RGBA', lay.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(shine)
    sd.polygon([(gx, fy - 140 * s), (gx + 34 * s, fy - 140 * s), (gx - 26 * s, fy + 140 * s), (gx - 60 * s, fy + 140 * s)],
               fill=(255, 255, 255, 150))
    mask = Image.new('L', lay.size, 0)
    ImageDraw.Draw(mask).ellipse([fx - 100 * s, fy - 130 * s, fx + 100 * s, fy + 130 * s], fill=255)
    lay.paste(shine, (0, 0), Image.composite(shine, Image.new('RGBA', lay.size, (0, 0, 0, 0)), mask))
    sparkle(d, fx + 70 * s, fy - 90 * s, (16 + 6 * math.sin(t * 5)) * s, (255, 255, 255))
    sparkle(d, fx - 76 * s, fy + 10 * s, (10 + 4 * math.sin(t * 5 + 1)) * s, (255, 255, 255))
    # oynat + kalp sayaç
    py = oy + h - 110 * s
    d.polygon([(ox + 50 * s, py - 22 * s), (ox + 50 * s, py + 22 * s), (ox + 86 * s, py)], fill=frame)
    d.rounded_rectangle([ox + 110 * s, py - 8 * s, ox + w - 50 * s, py + 8 * s], radius=int(8 * s), fill=(255, 255, 255))
    d.rounded_rectangle([ox + 110 * s, py - 8 * s, ox + 110 * s + (w - 160 * s) * ((t * 0.25) % 1), py + 8 * s],
                        radius=int(8 * s), fill=BERRY)
    if badge:
        k = back((t - 0.6) / 0.4)
        if k > 0.02:
            r = 62 * s * k * (1 + 0.05 * math.sin(t * 6))
            bx, by = ox + w - 10 * s, oy + 70 * s
            d.ellipse([bx - r, by - r, bx + r, by + r], fill=RED)
            d.text((bx, by + 4 * s * k), '!', font=F(BOLD, max(8, int(80 * s * k))), fill=CREAM, anchor='mm')
    lay = lay.rotate(math.sin(t * 1.4) * 4, expand=True, resample=Image.BICUBIC)
    c.paste(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)), lay)


def bottles(c, t, cx, cy, s=1.0, warn=True):
    """Aktif şişeleri tek tek düşüp üst üste yığılır; en sonda uyarı rozeti."""
    d = ImageDraw.Draw(c)
    items = [('RETİNOL', BERRY), ('AHA', RED), ('BHA', PLUM), ('C VİT.', (230, 140, 60))]
    for j, (lab, col) in enumerate(items):
        st = 0.2 + j * 0.45
        q = max(0.0, min(1.0, (t - st) / 0.5))
        if q <= 0: continue
        bounce = abs(math.sin(q * math.pi * 2)) * (1 - q) * 30
        x = cx + (j - 1.5) * 118 * s
        base = cy + 150 * s
        y = base - 600 * (1 - ease(q)) * s - bounce * s
        tilt = (j - 1.5) * 4 * math.sin(t * 3) if q >= 1 else 0
        bw, bh = 90 * s, 170 * s
        lay = Image.new('RGBA', (int(bw + 20 * s), int(bh + 110 * s)), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ox = 10 * s
        ld.rounded_rectangle([ox, 100 * s, ox + bw, 100 * s + bh], radius=int(22 * s), fill=col)
        ld.rectangle([ox + bw / 2 - 18 * s, 66 * s, ox + bw / 2 + 18 * s, 104 * s], fill=CREAM)
        ld.ellipse([ox + bw / 2 - 26 * s, 6 * s, ox + bw / 2 + 26 * s, 76 * s], fill=PLUM)
        ld.rounded_rectangle([ox + 8 * s, 150 * s, ox + bw - 8 * s, 200 * s], radius=int(10 * s), fill=CREAM)
        fs = int((17 if len(lab) > 6 else 22 if len(lab) > 4 else 28) * s)
        ld.text((ox + bw / 2, 176 * s), lab, font=F(BOLD, fs), fill=col, anchor='mm')
        lay = lay.rotate(tilt, expand=True, resample=Image.BICUBIC)
        c.paste(lay, (int(x - lay.width / 2), int(y - lay.height + 60 * s)), lay)
    if warn:
        k = back((t - 2.3) / 0.4)
        if k > 0.02:
            sticker(c, (cx, cy - 260 * s), 'Hepsi aynı akşam?', F(BOLD, int(34 * s)), RED, CREAM, -5, k, 28, 14)


def ringlight(c, t, cx, cy, s=1.0):
    """Halka ışık + yüz: ışık yanıp sönerken yüz 'cam'laşır."""
    d = ImageDraw.Draw(c)
    on = 0.5 + 0.5 * math.sin(t * 2.2)
    R = 190 * s
    glow = tuple(int(a + (b - a) * on) for a, b in zip((120, 40, 80), (255, 236, 200)))
    d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=glow, width=int(30 * s))
    d.line([(cx, cy + R), (cx, cy + R + 160 * s)], fill=CREAM, width=int(10 * s))
    d.line([(cx - 70 * s, cy + R + 160 * s), (cx + 70 * s, cy + R + 160 * s)], fill=CREAM, width=int(10 * s))
    skin = tuple(int(a + (b - a) * on) for a, b in zip(SKIN2, (252, 234, 224)))
    d.ellipse([cx - 92 * s, cy - 120 * s, cx + 92 * s, cy + 120 * s], fill=skin)
    d.arc([cx - 36 * s, cy + 36 * s, cx + 36 * s, cy + 74 * s], 20, 160, fill=BERRY, width=int(7 * s))
    for ex in (-34, 34):
        d.arc([cx + ex * s - 16 * s, cy - 28 * s, cx + ex * s + 16 * s, cy - 6 * s], 200, 340, fill=PLUM, width=int(6 * s))
    if on > 0.6:
        sparkle(d, cx + 52 * s, cy - 70 * s, 18 * s * on, (255, 255, 255))
        sparkle(d, cx - 58 * s, cy + 6 * s, 11 * s * on, (255, 255, 255))
    # 'FİLTRE' sürgüsü
    k = ease((t - 0.8) / 0.6)
    if k > 0:
        sticker(c, (cx + 170 * s, cy - 200 * s), 'FİLTRE: AÇIK', F(BOLD, int(26 * s)), PINK, PLUM, 8, k, 22, 12)


def basics(c, t, cx, cy, s=1.0):
    """Temel üçlü: temizleyici, krem kavanozu, güneş (SPF) — sırayla zıplar."""
    d = ImageDraw.Draw(c)
    gap = 220 * s
    for j in range(3):
        k = back((t - 0.3 - j * 0.3) / 0.45)
        if k <= 0.02: continue
        x = cx + (j - 1) * gap; y = cy - abs(math.sin(t * 3 + j)) * 10 * s
        if j == 0:  # pompalı temizleyici
            d.rounded_rectangle([x - 46 * s * k, y - 60 * s * k, x + 46 * s * k, y + 90 * s * k], radius=int(20 * s * k), fill=(236, 160, 186))
            d.rectangle([x - 10 * s * k, y - 96 * s * k, x + 10 * s * k, y - 60 * s * k], fill=PLUM)
            d.rectangle([x - 10 * s * k, y - 100 * s * k, x + 40 * s * k, y - 88 * s * k], fill=PLUM)
            for b in range(3):
                bx = x + 50 * s + b * 16 * s; by = y - 110 * s - ((t * 40 + b * 25) % 60) * s
                d.ellipse([bx - 7 * s, by - 7 * s, bx + 7 * s, by + 7 * s], outline=BERRY, width=max(1, int(3 * s)))
        elif j == 1:  # krem kavanozu
            d.rounded_rectangle([x - 70 * s * k, y - 10 * s * k, x + 70 * s * k, y + 80 * s * k], radius=int(18 * s * k), fill=CREAM, outline=PLUM, width=max(1, int(5 * s)))
            d.rounded_rectangle([x - 76 * s * k, y - 44 * s * k, x + 76 * s * k, y - 6 * s * k], radius=int(12 * s * k), fill=BERRY)
            d.text((x, y + 40 * s * k), 'NEM', font=F(BOLD, max(8, int(28 * s * k))), fill=PLUM, anchor='mm')
        else:  # güneş
            r = 52 * s * k
            for a in range(8):
                ang = a * math.pi / 4 + t * 0.8
                d.line([(x + math.cos(ang) * (r + 12 * s), y + math.sin(ang) * (r + 12 * s)),
                        (x + math.cos(ang) * (r + 40 * s), y + math.sin(ang) * (r + 40 * s))], fill=(240, 150, 40), width=int(8 * s))
            d.ellipse([x - r, y - r, x + r, y + r], fill=(250, 190, 60))
            d.text((x, y + 2), 'SPF', font=F(BOLD, max(8, int(30 * s * k))), fill=PLUM, anchor='mm')


def mark(d, x, y, ok, col, k=1.0):
    if k <= 0: return
    r = 30 * k
    d.ellipse([x - r, y - r, x + r, y + r], fill=col)
    if ok:
        d.line([(x - 13 * k, y), (x - 3 * k, y + 11 * k), (x + 15 * k, y - 11 * k)], fill=CREAM, width=int(7 * k) + 1, joint='curve')
    else:
        L = 11 * k
        d.line([(x - L, y - L), (x + L, y + L)], fill=CREAM, width=int(7 * k) + 1)
        d.line([(x - L, y + L), (x + L, y - L)], fill=CREAM, width=int(7 * k) + 1)


# ---------- ortak
def blobs(c, t, col, pos=(W - 110, 1120), R=380):
    d = ImageDraw.Draw(c); s = ease(t / 0.7); p = math.sin(t * 1.4) * 14
    r = int(R * s); d.ellipse([pos[0] - r - p, pos[1] - r - p, pos[0] + r + p, pos[1] + r + p], fill=col)


def footer(c, i, col):
    text_a(c, (70, 1290), 'PUDRA DERGİ', F(BOLD, 22), col, 1)
    text_a(c, (W - 70, 1288), f'{i}/5', F(MED, 24), col, 1, anchor='ra')


# ---------- 1 · KAPAK
def p1(t):
    c = Image.new('RGB', (W, H), BERRY); d = ImageDraw.Draw(c)
    blobs(c, t, (120, 12, 60), (W - 60, 1110), 440)
    dots(d, 860, 240, 4, 3, 44, 6, (180, 60, 110))
    sticker(c, (370, 250), 'PUDRA GÜNDEM · CAM CİLT', F(BOLD, 30), CREAM, BERRY, -4, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('38 viral', F(BOLD, 104), 316, 0.3, CREAM),
                                  ('cam cilt videosu.', F(BOLD, 84), 432, 0.5, CREAM),
                                  ('36\'sı yanıltıcı.', F(ACC, 116), 540, 0.75, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(36 * (1 - a)))
    a = ease((t - 1.3) / 0.5)
    text_a(c, (70, 732), 'Dermatologlar en popüler TikTok\'ları', F(MED, 36), CREAM, a)
    text_a(c, (70, 782), 'inceledi. Filtre çok, uyarı yok.', F(MED, 36), CREAM, a)
    phone(c, t, 790, 1050, 0.68)
    a = ease((t - 2.0) / 0.4)
    if a > 0:
        sticker(c, (220, 930), 'Kaydet', F(BOLD, 42), RED, CREAM, -6, back((t - 2.0) / 0.4), 34, 14)
        text_a(c, (70 + int(8 * math.sin(t * 6)), 1240), 'kaydır  ›', F(BOLD, 38), CREAM, a)
    logo(c, 'A'); return c


# ---------- 2 · NE OLUYOR
def p2(t):
    c = Image.new('RGB', (W, H), PINK); d = ImageDraw.Draw(c)
    blobs(c, t, (236, 170, 192), (W - 80, 1200), 300)
    sticker(c, (W - 300, 110), 'NE OLUYOR?', F(BOLD, 30), BERRY, CREAM, 5, back((t - 0.2) / 0.4))
    for txt, font, y, st, col in [('Dermatologlar', F(BOLD, 96), 200, 0.3, BERRY),
                                  ('videoları izledi.', F(ACC, 100), 310, 0.55, PLUM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    body = ['Avrupa Dermatoloji Akademisi (EADV)',
            'kongresinde sunulan çalışma, en popüler',
            '38 Kore bakımı / cam cilt videosuna baktı:']
    a = ease((t - 0.9) / 0.5); y = 470
    for ln in body: text_a(c, (72, y), ln, F(REG, 34), PLUM, a); y += 48
    stats = [(84, 'cilt tipi farkını yok sayıyor'),
             (45, 'aktifleri uyarısız karıştırıyor'),
             (32, '"anında sonuç" vaat ediyor'),
             (0, 'bilimsel kaynak göstermiyor')]
    y += 36
    for j, (pct, lab) in enumerate(stats):
        st = 1.3 + j * 0.35
        q = ease((t - st) / 0.8)
        if q <= 0: y += 150; continue
        num = f'%{int(pct * q)}' if pct else 'Hiçbiri'
        text_a(c, (72, y), num, F(BOLD, 58), BERRY if pct else RED, q)
        text_a(c, (300, y + 16), lab, F(MED, 34), PLUM, q)
        d.rounded_rectangle([72, y + 82, 1008, y + 100], radius=9, fill=(236, 170, 192))
        if pct and q > 0.02:
            d.rounded_rectangle([72, y + 82, 72 + 936 * pct / 100 * q, y + 100], radius=9, fill=BERRY)
        y += 150
    footer(c, 2, PLUM)
    logo(c, 'B'); return c


# ---------- 3 · SANA NE DEMEK
def p3(t):
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1220), 300)
    sticker(c, (W - 290, 110), 'SANA NE DEMEK?', F(BOLD, 30), RED, CREAM, -5, back((t - 0.2) / 0.4))
    a = ease((t - 0.2) / 0.5); text_a(c, (70, 190), 'Çok ürün', F(BOLD, 88), CREAM, a, int(24 * (1 - a)))
    a = ease((t - 0.4) / 0.5); text_a(c, (70, 290), '≠ iyi cilt.', F(ACC, 100), PINK, a, int(24 * (1 - a)))
    items = [(True, BERRY, 'Sorun Kore bakımı değil', 'Sorun, herkese aynı rutinin satılması.'),
             (False, RED, 'Parlaklık ışıktan olabilir', 'Halka ışık, açı ve filtre cildi cam gibi gösterir.'),
             (False, RED, '"Viral" = güvenli değil', '38 videonun yalnızca 2\'si güneş korumasından söz etti.')]
    y = 440; st = 0.7
    for ok, mc, head, body in items:
        k = back((t - st) / 0.4)
        mark(d, 102, y + 30, ok, mc, k)
        aa = ease((t - st - 0.1) / 0.45)
        text_a(c, (160, y + 4), head, F(BOLD, 40), CREAM, aa, int(16 * (1 - aa)))
        yy = y + 60
        for ln in wrap(F(REG, 32), body, W - 240):
            text_a(c, (160, yy), ln, F(REG, 32), PINK, aa); yy += 44
        y = yy + 30; st += 0.45
    if t > 1.6:
        ringlight(c, t - 1.6, 540, 1040, 0.62)
    footer(c, 3, PINK)
    logo(c, 'B'); return c


# ---------- 4 · DENE / DENEME
def p4(t):
    c = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(c)
    blobs(c, t, PINK, (W - 90, 1180), 320)
    sticker(c, (W - 300, 110), 'DENE / DENEME', F(BOLD, 30), BERRY, CREAM, 5, back((t - 0.2) / 0.4))
    a = ease((t - 0.2) / 0.5); text_a(c, (70, 190), 'Cam cildin', F(BOLD, 84), PLUM, a, int(24 * (1 - a)))
    a = ease((t - 0.4) / 0.5); text_a(c, (70, 286), 'dürüst hali', F(ACC, 96), BERRY, a, int(24 * (1 - a)))
    rows = [(True, BERRY, 'Yeni ürünü tek tek ekle, birkaç hafta izle.'),
            (True, BERRY, 'Temel üçlü: temizle, nemlendir, güneş koru.'),
            (False, RED, 'Retinol + AHA + BHA\'yı aynı akşam üst üste sürme.'),
            (False, RED, '"1 haftada cam cilt" vaadine inanma.')]
    y = 440
    for j, (ok, mc, txt) in enumerate(rows):
        st = 0.7 + j * 0.35
        k = back((t - st) / 0.4); mark(d, 102, y + 28, ok, mc, k)
        aa = ease((t - st - 0.1) / 0.45); yy = y
        for ln in wrap(F(MED, 34), txt, W - 250):
            text_a(c, (160, yy + 2), ln, F(MED, 34), PLUM, aa, int(14 * (1 - aa))); yy += 46
        y = yy + 26
    a = ease((t - 2.2) / 0.4)
    text_a(c, (160, y), 'Kızarıklık, yanma olursa: dermatoloğa danış.', F(REG, 28), BERRY, a)
    if t > 1.8:
        basics(c, t - 1.8, 300, 1100, 0.62)
        bottles(c, t - 1.8, 790, 1060, 0.55, warn=True)
    footer(c, 4, PLUM)
    logo(c, 'A'); return c


# ---------- 5 · SORU
def p5(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1220), 380)
    sparkle(d, 930, 300, 30 + 6 * math.sin(t * 4), PINK)
    for txt, font, y, st, col in [('Senin cilt', F(BOLD, 92), 200, 0.2, CREAM),
                                  ('bakım rutinin', F(BOLD, 92), 304, 0.35, CREAM),
                                  ('kaç adım?', F(ACC, 116), 408, 0.5, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    opts = [('A', '1–3 adım, sade'), ('B', '4–6 adım'), ('C', '7+ adım, cam cilt modu')]
    y = 610
    for k, (l, txt) in enumerate(opts):
        s = ease((t - 0.9 - k * 0.3) / 0.45)
        if s > 0:
            x = 70 - int(60 * (1 - s))
            d.rounded_rectangle([x, y, x + 660, y + 100], radius=50, fill=CREAM)
            d.ellipse([x + 12, y + 10, x + 92, y + 90], fill=PLUM)
            d.text((x + 52, y + 68), l, font=F(BOLD, 48), fill=CREAM, anchor='ms')
            d.text((x + 118, y + 66), txt, font=F(BOLD, 36), fill=PLUM, anchor='ls')
        y += 116
    sticker(c, (350, 1018), 'Harfini yorumlara yaz ›', F(BOLD, 42), PLUM, CREAM, -3,
            back((t - 2.0) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 36, 18)
    a = ease((t - 2.5) / 0.4)
    text_a(c, (72, 1110), 'Her videoyu deneyen', F(BOLD, 40), CREAM, a)
    text_a(c, (72, 1162), 'arkadaşına gönder.', F(ACC, 52), PINK, a)
    bottles(c, max(0, t - 1.0), 850, 1080, 0.5, warn=False)
    footer(c, 5, CREAM)
    logo(c, 'A'); return c


# ---------- STORY
def story(t):
    SW, SH = 1080, 1920
    c = Image.new('RGB', (SW, SH), BERRY); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 22; r = int(380 * ease(t / 0.8))
    d.ellipse([1080 - r - p, 1460 - r - p, 1080 + r + p, 1460 + r + p], fill=(120, 12, 60))
    dots(d, 820, 430, 5, 3, 44, 6, (180, 60, 110))
    sticker(c, (300, 420), 'PUDRA GÜNDEM', F(BOLD, 34), CREAM, BERRY, -5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Cam cilt', F(BOLD, 112), 500, 0.3, CREAM),
                                  ('videoları?', F(ACC, 124), 622, 0.55, PINK),
                                  ('38 videodan 36\'sı', F(BOLD, 60), 830, 0.9, CREAM),
                                  ('yanıltıcı çıktı.', F(MED, 56), 908, 1.1, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    phone(c, t, SW // 2 + 160, 1230, 0.62)
    s2 = back((t - 2.2) / 0.45)
    if s2 > 0: sticker(c, (SW // 2 + int(8 * math.sin(t * 6)), 1600), 'Yeni gönderide ›', F(BOLD, 46), PLUM, CREAM, -2, s2, 42, 22)
    logo(c, 'B', True); return c


def p1_cover(t):
    # Instagram ızgara kapağı = ilk videonun İLK karesi. Kapak 0. saniyede tam dolu başlamalı.
    return p1(t + 3.5)

PAGES = [p1_cover, p2, p3, p4, p5]
if __name__ == '__main__':
    arg = sys.argv[1]
    if arg == 'preview':
        tt = float(sys.argv[2]) if len(sys.argv) > 2 else 5
        fr = [f(tt) for f in PAGES]
        s = Image.new('RGB', (3 * 550 + 10, 2 * 685 + 10), (230, 230, 230))
        for k, im in enumerate(fr): s.paste(im.resize((540, 675)), ((k % 3) * 550 + 10, (k // 3) * 685 + 10))
        s.paste(story(tt).resize((380, 675)), (2 * 550 + 90, 685 + 10))
        s.save(f'{OUT}/sheet.jpg', quality=85)
    elif arg == 'story':
        render(story, f'{OUT}/story.mp4', 6, (1080, 1920), f'{OUT}/story.jpg')
    else:
        i = int(arg); render(PAGES[i - 1], f'{OUT}/p{i}.mp4', 6, (W, H), f'{OUT}/p{i}.jpg')
