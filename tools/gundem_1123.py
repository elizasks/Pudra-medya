"""PUDRA GÜNDEM — Kusursuz oje bitti, sıra kusurlu incide (23 Kasım 2026; yayın 28 Kasım 18:00).
Kaynaklar: Marie Claire (5 Kasım 2026, Samantha Holender; Miss Pop, Jin Soon Choi),
NewBeauty (16 Kasım 2026, Marisa Petrarca; Miss Pop, Nicole Wong)."""
from anim import *
from PIL import ImageFilter
import sys, os, random
W, H = 1080, 1350
OUT = 'out_1123'; os.makedirs(OUT, exist_ok=True)

SKIN = (240, 200, 180)
SKIN_D = (222, 176, 154)
PEARL = (240, 232, 228)
SAGE = (128, 172, 140)
BROWN = (112, 66, 44)
GOLD = (232, 190, 110)
BLACKBERRY = (78, 22, 52)

FIN = {
    'pearl': PEARL, 'sage': SAGE, 'brown': BROWN, 'berry': BLACKBERRY,
}


def nail_layer(t, w, h, finish, seed=0):
    """Tek tırnak katmanı (RGBA)."""
    lay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    m = Image.new('L', (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=w // 2, fill=255)
    base = Image.new('RGBA', (w, h), FIN[finish] + (255,))
    bd = ImageDraw.Draw(base)
    rnd = random.Random(seed)
    if finish == 'pearl':
        # kayan sedef parıltısı (pembe → altın → mavi)
        for y in range(h):
            u = y / h + t * 0.35
            r = 236 + 14 * math.sin(u * 6.28)
            g = 226 + 12 * math.sin(u * 6.28 + 2.1)
            b = 226 + 18 * math.sin(u * 6.28 + 4.2)
            bd.line([(0, y), (w, y)], fill=(int(r), int(g), int(b), 255))
        for k in range(int(w * h / 90)):
            x, y = rnd.uniform(0, w), rnd.uniform(0, h)
            tw = 0.5 + 0.5 * math.sin(t * 5 + k * 1.7)
            col = [(255, 255, 255), (250, 210, 220), (210, 220, 250), (245, 225, 180)][k % 4]
            rr = 1.2 + 1.6 * tw
            bd.ellipse([x - rr, y - rr, x + rr, y + rr], fill=col + (int(120 + 135 * tw),))
    elif finish == 'brown':
        for k in range(int(w * h / 60)):
            x, y = rnd.uniform(0, w), rnd.uniform(0, h)
            tw = 0.5 + 0.5 * math.sin(t * 6 + k * 2.3)
            rr = 1.4 + 1.8 * tw
            bd.ellipse([x - rr, y - rr, x + rr, y + rr], fill=GOLD + (int(90 + 165 * tw),))
    elif finish == 'sage':
        base.putalpha(200)
    # parlaklık çizgisi
    hl = Image.new('RGBA', (w, h), (0, 0, 0, 0)); hd = ImageDraw.Draw(hl)
    sx = w * 0.22 + w * 0.08 * math.sin(t * 1.5 + seed)
    hd.rounded_rectangle([sx, h * 0.14, sx + w * 0.16, h * 0.62], radius=int(w * 0.08), fill=(255, 255, 255, 150))
    base.alpha_composite(hl)
    lay.paste(base, (0, 0), Image.composite(base, Image.new('RGBA', (w, h), (0, 0, 0, 0)), m).split()[3])
    return lay


def hand(c, t, cx, cy, s=1.0, finish='pearl', wiggle=True, k=1.0):
    """Stilize el (üstten), 4 parmak + başparmak; tırnaklar seçilen bitişte."""
    if k <= 0.02: return
    s = s * k
    Wl, Hl = int(720 * s), int(820 * s)
    lay = Image.new('RGBA', (Wl, Hl), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    px, py = Wl / 2, Hl * 0.78
    # bilek + avuç
    d.rounded_rectangle([px - 150 * s, py - 40 * s, px + 150 * s, Hl + 40 * s], radius=int(120 * s), fill=SKIN)
    d.ellipse([px - 190 * s, py - 220 * s, px + 190 * s, py + 120 * s], fill=SKIN)
    fingers = [(-135, 330, -14), (-48, 390, -5), (42, 400, 3), (128, 340, 12)]
    for j, (dx, L, ang) in enumerate(fingers):
        a = ang + (math.sin(t * 2.2 + j * 0.9) * 2.5 if wiggle else 0)
        fw = int(86 * s); fl = int(L * s)
        fl_ = Image.new('RGBA', (fw, fl), (0, 0, 0, 0)); fd = ImageDraw.Draw(fl_)
        fd.rounded_rectangle([0, 0, fw - 1, fl - 1], radius=fw // 2, fill=SKIN)
        fd.line([(fw * 0.3, fl * 0.45), (fw * 0.7, fl * 0.45)], fill=SKIN_D, width=max(1, int(3 * s)))
        nw, nh = int(fw * 0.74), int(fw * 1.08)
        fl_.alpha_composite(nail_layer(t, nw, nh, finish, seed=j + 1), ((fw - nw) // 2, int(fw * 0.12)))
        # rotate around base
        big = Image.new('RGBA', (fl * 2, fl * 2), (0, 0, 0, 0))
        big.paste(fl_, (fl - fw // 2, 0))
        big = big.rotate(-a, resample=Image.BICUBIC)
        bx = px + dx * s - fl; by = py - 80 * s - fl
        lay.alpha_composite(big, (int(bx), int(by)))
    # başparmak
    tw_, tl = int(92 * s), int(250 * s)
    th = Image.new('RGBA', (tw_, tl), (0, 0, 0, 0)); tdr = ImageDraw.Draw(th)
    tdr.rounded_rectangle([0, 0, tw_ - 1, tl - 1], radius=tw_ // 2, fill=SKIN)
    nw, nh = int(tw_ * 0.64), int(tw_ * 0.9)
    th.alpha_composite(nail_layer(t, nw, nh, finish, seed=9), ((tw_ - nw) // 2, int(tw_ * 0.12)))
    big = Image.new('RGBA', (tl * 2, tl * 2), (0, 0, 0, 0)); big.paste(th, (tl - tw_ // 2, 0))
    big = big.rotate(52 + (math.sin(t * 2) * 3 if wiggle else 0), resample=Image.BICUBIC)
    lay.alpha_composite(big, (int(px - 170 * s - tl), int(py + 10 * s - tl)))
    c.paste(lay, (int(cx - Wl / 2), int(cy - Hl / 2)), lay)


def bottle(c, t, cx, cy, s, col, k=1.0, label=None, finish=None):
    if k <= 0.02: return
    s = s * k
    d = ImageDraw.Draw(c)
    bw, bh = 170 * s, 190 * s
    top = cy - bh / 2
    d.rounded_rectangle([cx - bw / 2, top, cx + bw / 2, top + bh], radius=int(40 * s), fill=col)
    if finish:
        nl = nail_layer(t, int(bw * 0.8), int(bh * 0.7), finish, seed=21)
        c.paste(nl, (int(cx - bw * 0.4), int(top + bh * 0.12)), nl)
    d.rounded_rectangle([cx - bw / 2 + 16 * s, top + 18 * s, cx - bw / 2 + 36 * s, top + bh - 40 * s], radius=int(10 * s), fill=(255, 255, 255))
    d.rectangle([cx - 30 * s, top - 26 * s, cx + 30 * s, top], fill=(210, 200, 196))
    d.rounded_rectangle([cx - 38 * s, top - 190 * s, cx + 38 * s, top - 22 * s], radius=int(14 * s), fill=PLUM)
    if label:
        d.text((cx, top + bh + 34 * s), label, font=F(BOLD, max(8, int(24 * s))), fill=PLUM, anchor='mm')


def pearl_orb(c, t, cx, cy, R, k=1.0):
    if k <= 0.02: return
    R = R * k
    lay = nail_layer(t, int(2 * R), int(2 * R), 'pearl', seed=5)
    m = Image.new('L', lay.size, 0); ImageDraw.Draw(m).ellipse([0, 0, 2 * R - 1, 2 * R - 1], fill=255)
    sh = Image.new('RGBA', lay.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    sd.ellipse([R * 0.35, R * 0.25, R * 0.95, R * 0.75], fill=(255, 255, 255, 170))
    sh = sh.filter(ImageFilter.GaussianBlur(R * 0.12))
    lay.alpha_composite(sh)
    dk = Image.new('RGBA', lay.size, (0, 0, 0, 0)); dd = ImageDraw.Draw(dk)
    dd.ellipse([R * 0.6, R * 0.7, R * 2.2, R * 2.3], fill=(150, 120, 140, 90))
    dk = dk.filter(ImageFilter.GaussianBlur(R * 0.3)); lay.alpha_composite(dk)
    c.paste(lay, (int(cx - R), int(cy - R)), Image.composite(lay, Image.new('RGBA', lay.size, (0, 0, 0, 0)), m).split()[3])


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


def blobs(c, t, col, pos=(W - 110, 1120), R=380):
    d = ImageDraw.Draw(c); s = ease(t / 0.7); p = math.sin(t * 1.4) * 14
    r = int(R * s); d.ellipse([pos[0] - r - p, pos[1] - r - p, pos[0] + r + p, pos[1] + r + p], fill=col)


def footer(c, i, col):
    text_a(c, (70, 1290), 'PUDRA DERGİ', F(BOLD, 22), col, 1)
    text_a(c, (W - 70, 1288), f'{i}/5', F(MED, 24), col, 1, anchor='ra')


# ---------- 1 · KAPAK
def p1(t):
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 40, 1120), 470)
    dots(d, 860, 230, 4, 3, 44, 6, (90, 50, 72))
    sticker(c, (400, 250), 'PUDRA GÜNDEM · TIRNAK', F(BOLD, 30), PINK, PLUM, -4, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Kusursuz oje', F(BOLD, 108), 316, 0.3, CREAM),
                                  ('modası geçti.', F(BOLD, 96), 436, 0.5, CREAM),
                                  ('Sıra kusurlu incide.', F(ACC, 88), 552, 0.75, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(36 * (1 - a)))
    a = ease((t - 1.3) / 0.5)
    text_a(c, (70, 706), 'Manikür ustası diyor ki: Bu doku,', F(MED, 36), CREAM, a)
    text_a(c, (70, 756), 'yapay zekânın kusursuzluğuna tepki.', F(MED, 36), CREAM, a)
    hand(c, t, 700, 1100, 0.9, 'pearl')
    pearl_orb(c, t, 950, 860, 46, back((t - 1.2) / 0.5))
    a = ease((t - 2.0) / 0.4)
    if a > 0:
        sticker(c, (190, 930), 'Kaydet', F(BOLD, 42), RED, CREAM, -6, back((t - 2.0) / 0.4), 34, 14)
        text_a(c, (70 + int(8 * math.sin(t * 6)), 1230), 'kaydır  ›', F(BOLD, 38), CREAM, a)
    sparkle(d, 300, 1080, 24 + 6 * math.sin(t * 4), PINK)
    sparkle(d, 1000, 650, 18 + 5 * math.sin(t * 5 + 1), CREAM)
    logo(c, 'A'); return c


# ---------- 2 · NE OLDU
def p2(t):
    c = Image.new('RGB', (W, H), PINK); d = ImageDraw.Draw(c)
    blobs(c, t, (236, 170, 192), (W - 80, 1200), 320)
    sticker(c, (W - 260, 110), 'NE OLDU?', F(BOLD, 30), BERRY, CREAM, 5, back((t - 0.2) / 0.4))
    for txt, font, y, st, col in [('Pürüzsüz krom değil,', F(BOLD, 72), 200, 0.3, BERRY),
                                  ('zerrecikli inci.', F(ACC, 92), 292, 0.55, PLUM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    body = ['New York\'lu manikür sanatçısı Miss Pop,',
            'kasımın gözdesini Marie Claire ve',
            'NewBeauty\'ye anlattı: ayna gibi krom',
            'değil, minik zerrecikli, hafif "kumlu"',
            'dokulu, ışıkta renk değiştiren inci.']
    a = ease((t - 0.9) / 0.5); y = 440
    for ln in body: text_a(c, (72, y), ln, F(REG, 34), PLUM, a); y += 48
    a = ease((t - 1.5) / 0.5); y += 24
    text_a(c, (72, y), 'Neden? Ona göre bu kusur,', F(MED, 34), BERRY, a); y += 50
    a = ease((t - 1.9) / 0.5)
    text_a(c, (72, y), 'yapay zekâya bir tepki.', F(ACC, 44), PLUM, a)
    if t > 1.6:
        tt = t - 1.6
        pearl_orb(c, tt, 300, 1110, 120, back(tt / 0.6))
        pearl_orb(c, tt + 1, 470, 1170, 60, back((tt - 0.2) / 0.6))
        bottle(c, tt, 740, 1110, 0.95, (232, 222, 220), back((tt - 0.3) / 0.6), finish='pearl')
        sparkle(d, 420, 990, 22 + 6 * math.sin(t * 5), CREAM)
    footer(c, 2, PLUM)
    logo(c, 'B'); return c


# ---------- 3 · KASIMIN DİĞER RENKLERİ
def p3(t):
    c = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(c)
    blobs(c, t, PINK, (W - 60, 1220), 300)
    sticker(c, (W - 300, 110), 'KASIM PALETİ', F(BOLD, 30), BERRY, CREAM, -5, back((t - 0.2) / 0.4))
    a = ease((t - 0.2) / 0.5); text_a(c, (70, 190), 'İnciden sıkıldıysan', F(BOLD, 72), PLUM, a, int(24 * (1 - a)))
    a = ease((t - 0.4) / 0.5); text_a(c, (70, 280), '3 renk daha.', F(ACC, 92), BERRY, a, int(24 * (1 - a)))
    rows = [('sage', 'Adaçayı yeşili, jöle', 'Yarı şeffaf, yeşim taşı gibi.'),
            ('brown', 'Işıltılı kahve', 'Çikolata, kestane, karamel + sim.'),
            ('berry', 'Böğürtlen', 'Koyu, sade, süssüz. Yeni "vamp".')]
    y = 450
    for j, (fin, l1, l2) in enumerate(rows):
        st = 0.7 + j * 0.4
        k = back((t - st) / 0.45)
        if k > 0.02:
            nl = nail_layer(t, int(96 * k) + 1, int(140 * k) + 1, fin, seed=j + 3)
            c.paste(nl, (int(110 - 48 * k), int(y + 70 - 70 * k)), nl)
        aa = ease((t - st - 0.1) / 0.45)
        text_a(c, (200, y + 8), l1, F(BOLD, 44), PLUM, aa, int(16 * (1 - aa)))
        text_a(c, (200, y + 70), l2, F(REG, 34), BERRY, aa, int(16 * (1 - aa)))
        y += 200
    for j, (col, fin) in enumerate([(SAGE, None), (BROWN, 'brown'), (BLACKBERRY, None)]):
        bottle(c, t, 200 + j * 240, 1195, 0.55, col, back((t - 1.9 - j * 0.2) / 0.5), finish=fin)
    sparkle(d, 860, 1040, 22 + 6 * math.sin(t * 5), BERRY)
    footer(c, 3, PLUM)
    logo(c, 'B'); return c


# ---------- 4 · DENE / DENEME
def p4(t):
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1230), 300)
    sticker(c, (W - 300, 110), 'DENE / DENEME', F(BOLD, 30), RED, CREAM, 5, back((t - 0.2) / 0.4))
    a = ease((t - 0.2) / 0.5); text_a(c, (70, 190), 'Evde salon işi', F(BOLD, 80), CREAM, a, int(24 * (1 - a)))
    a = ease((t - 0.4) / 0.5); text_a(c, (70, 286), 'tırnak.', F(ACC, 96), PINK, a, int(24 * (1 - a)))
    rows = [(True, 'Jöle için tek ince kat renk, üstüne bol parlak üst kat. Bu kadar.'),
            (True, 'Kahvene ışıltı: Üst katına bir damla simli oje karıştır.'),
            (True, 'Koyu renk kısa tırnakta çok şık durur, desen ekleme.'),
            (False, 'İnciyi kusursuz parlatmaya çalışma. Zerrecik, işin özü.')]
    y = 430
    for j, (ok, txt) in enumerate(rows):
        st = 0.7 + j * 0.35
        k = back((t - st) / 0.4); mark(d, 102, y + 28, ok, (120, 172, 136) if ok else RED, k)
        aa = ease((t - st - 0.1) / 0.45); yy = y
        for ln in wrap(F(MED, 34), txt, W - 420):
            text_a(c, (160, yy + 2), ln, F(MED, 34), CREAM, aa, int(14 * (1 - aa))); yy += 46
        y = yy + 26
    if t > 1.6:
        tt = t - 1.6
        bottle(c, tt, 900, 640, 0.75, SAGE, back(tt / 0.5))
        bottle(c, tt, 900, 1000, 0.75, BROWN, back((tt - 0.25) / 0.5), finish='brown')
    footer(c, 4, PINK)
    logo(c, 'A'); return c


# ---------- 5 · SORU
def p5(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1220), 380)
    sparkle(d, 950, 300, 30 + 6 * math.sin(t * 4), PINK)
    for txt, font, y, st, col in [('Bu kasım', F(BOLD, 96), 200, 0.2, CREAM),
                                  ('tırnağında', F(BOLD, 96), 306, 0.35, CREAM),
                                  ('hangisi?', F(ACC, 120), 410, 0.5, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    opts = [('A', 'Kusurlu inci', 'pearl'), ('B', 'Adaçayı jöle', 'sage'),
            ('C', 'Işıltılı kahve', 'brown'), ('D', 'Böğürtlen', 'berry')]
    y = 590
    for k, (l, txt, fin) in enumerate(opts):
        s = ease((t - 0.9 - k * 0.25) / 0.45)
        if s > 0:
            x = 70 - int(60 * (1 - s))
            d.rounded_rectangle([x, y, x + 560, y + 88], radius=44, fill=CREAM)
            d.ellipse([x + 10, y + 8, x + 86, y + 84], fill=PLUM)
            d.text((x + 48, y + 64), l, font=F(BOLD, 44), fill=CREAM, anchor='ms')
            d.text((x + 108, y + 61), txt, font=F(BOLD, 34), fill=PLUM, anchor='ls')
            nl = nail_layer(t, 40, 60, fin, seed=k)
            c.paste(nl, (x + 500, y + 16), nl)
        y += 100
    sticker(c, (330, 1050), 'Harfini yorumlara yaz ›', F(BOLD, 40), PLUM, CREAM, -3,
            back((t - 2.0) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 34, 18)
    a = ease((t - 2.5) / 0.4)
    text_a(c, (72, 1122), 'Manikür arkadaşına', F(BOLD, 40), CREAM, a)
    text_a(c, (72, 1172), 'gönder.', F(ACC, 52), PINK, a)
    if t > 0.8:
        hand(c, t - 0.8, 880, 980, 0.5, 'pearl', k=back((t - 0.8) / 0.5))
    footer(c, 5, CREAM)
    logo(c, 'A'); return c


# ---------- STORY
def story(t):
    SW, SH = 1080, 1920
    c = Image.new('RGB', (SW, SH), BERRY); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 22; r = int(420 * ease(t / 0.8))
    d.ellipse([1080 - r - p, 1420 - r - p, 1080 + r + p, 1420 + r + p], fill=(120, 12, 60))
    dots(d, 820, 430, 5, 3, 44, 6, (180, 60, 110))
    sticker(c, (300, 420), 'PUDRA GÜNDEM', F(BOLD, 34), CREAM, BERRY, -5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Kusursuz oje', F(BOLD, 108), 500, 0.3, CREAM),
                                  ('modası geçti.', F(BOLD, 96), 620, 0.5, CREAM),
                                  ('Sıra kusurlu incide.', F(ACC, 84), 736, 0.75, PINK),
                                  ('+ kasımın 3 rengi', F(MED, 50), 880, 1.1, CREAM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    hand(c, t, SW // 2 + 40, 1260, 0.82, 'pearl')
    pearl_orb(c, t, 220, 1120, 60, back((t - 1.0) / 0.5))
    s2 = back((t - 2.2) / 0.45)
    if s2 > 0: sticker(c, (SW // 2 + int(8 * math.sin(t * 6)), 1580), 'Yeni gönderide ›', F(BOLD, 46), PLUM, CREAM, -2, s2, 42, 22)
    logo(c, 'A', True); return c


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
