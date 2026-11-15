"""PUDRA GÜNDEM — Kazak sezonu açıldı: 3 yıkamada tüylenmeyen kazak nasıl seçilir? (16 Kasım 2026)."""
from anim import *
import sys, os
W, H = 1080, 1350
OUT = 'out_1116'; os.makedirs(OUT, exist_ok=True)
OAT = (236, 222, 200)
OAT2 = (214, 194, 164)
SNOW = (255, 255, 255)


# ---------- illüstrasyonlar
def snow(d, t, x0, x1, y0, y1, n=14, col=SNOW, seed=3):
    for j in range(n):
        sx = x0 + ((j * 137 + seed * 61) % max(1, (x1 - x0)))
        sp = 40 + (j * 23) % 50
        yy = y0 + ((t * sp + j * 97) % max(1, (y1 - y0)))
        xx = sx + 14 * math.sin(t * 1.5 + j)
        r = 5 + (j % 3) * 3
        d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=col)


def sweater(c, t, cx, cy, s=1.0, body=OAT, rib=OAT2, line=PLUM):
    """Örgü kazak: hafifçe sallanır, örgü desenli."""
    lay = Image.new('RGBA', (int(560 * s), int(520 * s)), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    w, h = lay.size; k = s
    # kollar
    d.polygon([(130 * k, 60 * k), (30 * k, 150 * k), (0, 420 * k), (80 * k, 430 * k), (140 * k, 220 * k)], fill=body)
    d.polygon([(w - 130 * k, 60 * k), (w - 30 * k, 150 * k), (w, 420 * k), (w - 80 * k, 430 * k), (w - 140 * k, 220 * k)], fill=body)
    d.rounded_rectangle([0, 400 * k, 84 * k, 460 * k], radius=12 * k, fill=rib)
    d.rounded_rectangle([w - 84 * k, 400 * k, w, 460 * k], radius=12 * k, fill=rib)
    # gövde
    d.rounded_rectangle([120 * k, 40 * k, w - 120 * k, 470 * k], radius=36 * k, fill=body)
    d.rounded_rectangle([120 * k, 430 * k, w - 120 * k, 505 * k], radius=14 * k, fill=rib)
    # yaka
    d.ellipse([w / 2 - 90 * k, 10 * k, w / 2 + 90 * k, 110 * k], fill=rib)
    d.ellipse([w / 2 - 62 * k, 22 * k, w / 2 + 62 * k, 84 * k], fill=(0, 0, 0, 0))
    # örgü (saç örgüsü) desen
    for col_x in [w / 2 - 110 * k, w / 2, w / 2 + 110 * k]:
        for r in range(7):
            y = 130 * k + r * 42 * k
            d.arc([col_x - 28 * k, y, col_x + 28 * k, y + 50 * k], 200, 340, fill=rib, width=int(9 * k))
    for x in [w / 2 - 55 * k, w / 2 + 55 * k]:
        d.line([(x, 120 * k), (x, 420 * k)], fill=rib, width=int(5 * k))
    for r in range(4):  # kol çizgileri
        d.line([(40 * k + r * 8 * k, 180 * k + r * 60 * k), (110 * k, 200 * k + r * 55 * k)], fill=rib, width=int(5 * k))
    ang = math.sin(t * 1.6) * 3
    lay = lay.rotate(ang, expand=True, resample=Image.BICUBIC)
    c.paste(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)), lay)


def tag(c, t, cx, cy, s=1.0, rows=(('YÜN', 80, BERRY), ('POLİAMİD', 20, RED)), bg=CREAM, fg=PLUM):
    """Sallanan etiket; elyaf yüzdeleri dolan çubuklarla."""
    w, h = int(330 * s), int(400 * s)
    lay = Image.new('RGBA', (w, h + int(80 * s)), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    top = int(80 * s)
    d.line([(w / 2, 0), (w / 2, top + 30 * s)], fill=fg, width=int(5 * s))
    d.rounded_rectangle([0, top, w, top + h], radius=int(26 * s), fill=bg)
    d.ellipse([w / 2 - 16 * s, top + 22 * s, w / 2 + 16 * s, top + 54 * s], fill=fg)
    d.text((w / 2, top + 108 * s), 'İÇERİK', font=F(BOLD, int(34 * s)), fill=fg, anchor='ms')
    y = top + 150 * s
    for j, (name, pct, col) in enumerate(rows):
        q = ease((t - 0.4 - j * 0.35) / 0.8)
        d.text((26 * s, y + 36 * s), f'%{int(pct * q)}', font=F(BOLD, int(46 * s)), fill=col, anchor='ls')
        d.text((w - 26 * s, y + 34 * s), name, font=F(MED, int(26 * s)), fill=fg, anchor='rs')
        d.rounded_rectangle([26 * s, y + 52 * s, w - 26 * s, y + 70 * s], radius=int(9 * s), fill=(230, 214, 220))
        if q > 0.02:
            d.rounded_rectangle([26 * s, y + 52 * s, 26 * s + (w - 52 * s) * pct / 100 * q, y + 70 * s], radius=int(9 * s), fill=col)
        y += 110 * s
    lay = lay.rotate(math.sin(t * 2.2) * 6, expand=True, resample=Image.BICUBIC, center=(w / 2, 0))
    c.paste(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)), lay)


def swatch_pills(c, t, cx, cy, s=1.0, cloth=OAT, rib=OAT2, pill=OAT2, hand=PINK, line=PLUM):
    """Kumaş parçası + ovalayan avuç: zamanla tüy topları belirir."""
    d = ImageDraw.Draw(c)
    w, h = 380 * s, 250 * s
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=int(24 * s), fill=cloth)
    for r in range(5):
        for q in range(8):
            x = cx - w / 2 + 30 * s + q * 46 * s; y = cy - h / 2 + 30 * s + r * 46 * s
            d.arc([x - 14 * s, y - 10 * s, x + 14 * s, y + 18 * s], 200, 340, fill=rib, width=int(5 * s))
    n = int(min(9, max(0, (t - 0.8) * 4)))
    for j in range(n):
        x = cx - w / 2 + 50 * s + ((j * 113) % int(280 * s)); y = cy - h / 2 + 40 * s + ((j * 71) % int(170 * s))
        r = 11 * s
        d.ellipse([x - r, y - r, x + r, y + r], fill=pill, outline=line, width=max(1, int(3 * s)))
    hx = cx + math.sin(t * 6) * 90 * s; hy = cy - 30 * s
    d.ellipse([hx - 95 * s, hy - 60 * s, hx + 95 * s, hy + 60 * s], fill=hand, outline=line, width=int(5 * s))
    for f in range(4):
        fx = hx - 60 * s + f * 40 * s
        d.rounded_rectangle([fx - 16 * s, hy - 120 * s, fx + 16 * s, hy - 30 * s], radius=int(16 * s), fill=hand, outline=line, width=int(5 * s))


def stretch(c, t, cx, cy, s=1.0, cloth=OAT, rib=OAT2, line=PLUM):
    """Kumaş esner ve geri toparlanır."""
    d = ImageDraw.Draw(c)
    ph = (t % 2.0) / 2.0
    k = math.sin(ph * math.pi) ** 2
    w = (240 + 170 * k) * s; h = (210 - 40 * k) * s
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=int(20 * s), fill=cloth)
    for q in range(7):
        x = cx - w / 2 + (q + 0.5) * w / 7
        d.line([(x, cy - h / 2 + 18 * s), (x, cy + h / 2 - 18 * s)], fill=rib, width=int(6 * s))
    for side in (-1, 1):
        ax = cx + side * (w / 2 + 40 * s)
        d.line([(ax - side * 30 * s, cy), (ax + side * 20 * s, cy)], fill=line, width=int(8 * s))
        d.polygon([(ax + side * 40 * s, cy), (ax + side * 12 * s, cy - 20 * s), (ax + side * 12 * s, cy + 20 * s)], fill=line)


def yarn(c, t, cx, cy, s=1.0, col=PINK, line=BERRY):
    d = ImageDraw.Draw(c)
    r = 110 * s
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
    a0 = t * 1.2
    for j in range(6):
        a = a0 + j * 0.52
        d.arc([cx - r * 0.95, cy - r * (0.3 + 0.12 * j), cx + r * 0.95, cy + r * (0.3 + 0.12 * j)],
              int(math.degrees(a)) % 360, (int(math.degrees(a)) + 160) % 360, fill=line, width=int(6 * s))
    pts = [(cx + r * 0.7 + i * 12 * s, cy + r * 0.7 + 18 * s * math.sin(i * 0.6 + t * 3)) for i in range(26)]
    d.line(pts, fill=line, width=int(6 * s), joint='curve')
    # iki kat (2-ply) bükülmüş iplik
    for i in range(0, 26, 3):
        x, y = pts[i]; d.ellipse([x - 4 * s, y - 4 * s, x + 4 * s, y + 4 * s], fill=col)


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
    blobs(c, t, (120, 12, 60), (W - 60, 1110), 430)
    dots(d, 840, 230, 5, 3, 44, 6, (180, 60, 110))
    snow(d, t, 0, 560, 860, 1230, 8, (190, 70, 120))
    sticker(c, (360, 250), 'PUDRA GÜNDEM · KIŞ GELDİ', F(BOLD, 30), CREAM, BERRY, -4, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Kazak sezonu', F(BOLD, 100), 320, 0.3, CREAM),
                                  ('açıldı. Peki', F(BOLD, 100), 432, 0.5, CREAM),
                                  ('tüylenmeyeni?', F(ACC, 120), 548, 0.75, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(36 * (1 - a)))
    a = ease((t - 1.3) / 0.5)
    text_a(c, (70, 740), 'Üç yıkamada top top olan kazağa', F(MED, 38), CREAM, a)
    text_a(c, (70, 792), 'para verme. Mağazada 3 test.', F(MED, 38), CREAM, a)
    sweater(c, t, 700, 1060, 0.78)
    a = ease((t - 2.0) / 0.4)
    if a > 0:
        sticker(c, (230, 915), 'Kaydet', F(BOLD, 42), RED, CREAM, -6, back((t - 2.0) / 0.4), 34, 14)
        text_a(c, (70 + int(8 * math.sin(t * 6)), 1240), 'kaydır  ›', F(BOLD, 38), CREAM, a)
    logo(c, 'A'); return c


# ---------- 2 · NE OLUYOR
def p2(t):
    c = Image.new('RGB', (W, H), PINK); d = ImageDraw.Draw(c)
    blobs(c, t, (236, 170, 192), (W - 80, 1180), 320)
    sticker(c, (W - 300, 110), 'NE OLUYOR?', F(BOLD, 30), BERRY, CREAM, 5, back((t - 0.2) / 0.4))
    for txt, font, y, st, col in [('Soğuk geldi,', F(BOLD, 104), 210, 0.3, BERRY),
                                  ('kazaklar çıktı.', F(ACC, 112), 326, 0.55, PLUM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    body = ['Meteoroloji bu hafta yağış ve yer yer kar',
            'uyarısı verdi; dolaplar kış moduna geçti.',
            'Ama çok tanıdık bir dert var:',
            '"Yeni kazağım hemen tüylendi."']
    a = ease((t - 1.0) / 0.5); y = 500
    for ln in body: text_a(c, (72, y), ln, F(REG, 36), PLUM, a); y += 50
    a = ease((t - 1.5) / 0.5); y += 24
    for ln in ['Uzmanlara göre sebep çoğu zaman', 'etikette: sentetik ağırlıklı karışımlar', 've kısa lifli iplik.']:
        text_a(c, (72, y), ln, F(BOLD, 38), BERRY, a); y += 52
    wave_line(d, 0, W * ease((t - 1.2) / 0.8), y + 26, 12, 170, BERRY, 5, -t * 2)
    sweater(c, max(0, t - 0.4), 330, 1110, 0.5)
    tag(c, max(0, t - 0.8), 800, 1080, 0.62, (('AKRİLİK', 70, RED), ('YÜN', 30, BERRY)))
    footer(c, 2, PLUM)
    logo(c, 'B'); return c


# ---------- 3 · ETİKETİ OKU
def p3(t):
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1200), 300)
    sticker(c, (W - 290, 110), 'SANA NE DEMEK?', F(BOLD, 30), RED, CREAM, -5, back((t - 0.2) / 0.4))
    a = ease((t - 0.2) / 0.5); text_a(c, (70, 190), 'Önce', F(BOLD, 84), CREAM, a, int(24 * (1 - a)))
    a = ease((t - 0.4) / 0.5); text_a(c, (70, 284), 'etiketi oku.', F(ACC, 96), PINK, a, int(24 * (1 - a)))
    items = [(True, BERRY, 'Çoğunluk doğal lif olsun', 'Yün, merinos, kaşmir, alpaka ya da %100 pamuk.'),
             (False, RED, 'Akrilik, polyester ağırlıklıysa', 'Tüylenme riski artar; ucuzluğu kısa sürer.'),
             (False, RED, '"Kaşmirli" yazıyor diye kanma', 'Kaşmir %20\'nin altındaysa farkı pek hissedilmez.')]
    y = 440; st = 0.7
    for ok, mc, head, body in items:
        k = back((t - st) / 0.4)
        mark(d, 102, y + 30, ok, mc, k)
        aa = ease((t - st - 0.1) / 0.45)
        text_a(c, (160, y + 4), head, F(BOLD, 40), CREAM, aa, int(16 * (1 - aa)))
        yy = y + 60
        for ln in wrap(F(REG, 32), body, W - 240):
            text_a(c, (160, yy), ln, F(REG, 32), PINK, aa); yy += 44
        y = yy + 34; st += 0.45
    tag(c, max(0, t - 1.6), 300, 1080, 0.66, (('MERİNOS', 90, BERRY), ('POLİAMİD', 10, RED)))
    yarn(c, max(0, t - 1.6), 760, 1130, 0.9)
    footer(c, 3, PINK)
    logo(c, 'B'); return c


# ---------- 4 · MAĞAZADA 3 TEST
def p4(t):
    c = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(c)
    blobs(c, t, PINK, (W - 90, 1160), 330)
    sticker(c, (W - 290, 110), 'DENE', F(BOLD, 30), BERRY, CREAM, 5, back((t - 0.2) / 0.4))
    a = ease((t - 0.2) / 0.5); text_a(c, (70, 200), 'Mağazada', F(BOLD, 84), PLUM, a, int(24 * (1 - a)))
    a = ease((t - 0.4) / 0.5); text_a(c, (70, 296), '3 test', F(ACC, 96), BERRY, a, int(24 * (1 - a)))
    steps = [('01', 'Avucunla ovala', 'Hemen top top oluyorsa yerine bırak.'),
             ('02', 'Hafifçe esnet', 'Kalite eski haline döner; dönmüyorsa sarkar.'),
             ('03', 'Örgüye bak', 'Gevşek, cansız örgü ucuz işçilik demek. İki katlı bükümlü iplik daha dayanıklı.')]
    y = 440
    for j, (n, h, b) in enumerate(steps):
        st = 0.8 + j * 0.5
        a = ease((t - st) / 0.45)
        text_a(c, (70 - int(40 * (1 - a)), y - 6), n, F(BOLD, 70), RED, a)
        text_a(c, (210, y), h, F(BOLD, 44), PLUM, a, int(16 * (1 - a)))
        yy = y + 58
        for ln in wrap(F(REG, 32), b, W - 290):
            text_a(c, (210, yy), ln, F(REG, 32), PLUM, a); yy += 44
        y = yy + 30
    if t > 2.0:
        swatch_pills(c, t - 2.0, 300, 1110, 0.62)
        stretch(c, t - 2.0, 790, 1110, 0.7)
    footer(c, 4, PLUM)
    logo(c, 'A'); return c


# ---------- 5 · SORU
def p5(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1220), 380)
    sparkle(d, 930, 300, 30 + 6 * math.sin(t * 4), PINK)
    for txt, font, y, st, col in [('Dolabındaki en', F(BOLD, 88), 200, 0.2, CREAM),
                                  ('eski kazak', F(BOLD, 88), 300, 0.35, CREAM),
                                  ('kaç yaşında?', F(ACC, 112), 400, 0.5, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    opts = [('A', '1–2 yıl'), ('B', '5 yıl ve üstü'), ('C', 'Annemden kaldı')]
    y = 600
    for k, (l, txt) in enumerate(opts):
        s = ease((t - 0.9 - k * 0.3) / 0.45)
        if s > 0:
            x = 70 - int(60 * (1 - s))
            d.rounded_rectangle([x, y, x + 620, y + 100], radius=50, fill=CREAM)
            d.ellipse([x + 12, y + 10, x + 92, y + 90], fill=PLUM)
            d.text((x + 52, y + 68), l, font=F(BOLD, 48), fill=CREAM, anchor='ms')
            d.text((x + 118, y + 68), txt, font=F(BOLD, 40), fill=PLUM, anchor='ls')
        y += 116
    sticker(c, (350, 1018), 'Harfini yorumlara yaz ›', F(BOLD, 42), PLUM, CREAM, -3,
            back((t - 2.0) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 36, 18)
    a = ease((t - 2.5) / 0.4)
    text_a(c, (72, 1110), 'Kazak alacak', F(BOLD, 40), CREAM, a)
    text_a(c, (72, 1162), 'arkadaşına gönder.', F(ACC, 52), PINK, a)
    sweater(c, max(0, t - 1.0), 870, 760, 0.42, OAT, OAT2)
    footer(c, 5, CREAM)
    logo(c, 'A'); return c


# ---------- STORY
def story(t):
    SW, SH = 1080, 1920
    c = Image.new('RGB', (SW, SH), BERRY); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 22; r = int(360 * ease(t / 0.8))
    d.ellipse([1080 - r - p, 1500 - r - p, 1080 + r + p, 1500 + r + p], fill=(120, 12, 60))
    dots(d, 800, 430, 5, 3, 44, 6, (180, 60, 110))
    snow(d, t, 0, SW, 1040, 1620, 14, (190, 70, 120))
    sticker(c, (300, 420), 'PUDRA GÜNDEM', F(BOLD, 34), CREAM, BERRY, -5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Kazak', F(BOLD, 110), 500, 0.3, CREAM),
                                  ('tüylenmesin.', F(ACC, 124), 620, 0.55, PINK),
                                  ('Mağazada 3 test,', F(BOLD, 60), 830, 0.9, CREAM),
                                  ('etikette 1 kural.', F(MED, 52), 910, 1.1, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    sweater(c, t, SW // 2, 1260, 0.82)
    s2 = back((t - 2.2) / 0.45)
    if s2 > 0: sticker(c, (SW // 2 + int(8 * math.sin(t * 6)), 1580), 'Yeni gönderide ›', F(BOLD, 46), PLUM, CREAM, -2, s2, 42, 22)
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
