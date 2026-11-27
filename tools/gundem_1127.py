"""PUDRA GÜNDEM — Bugün herkes indirimde, bir marka kapıyı kapattı (27 Kasım 2026; yayın 27 Kasım 18:00).
Kaynaklar: Marketing Türkiye (18 Kasım 2026), Campaign Türkiye (18 Kasım 2026),
Madeline Levin · The Beauty Brief (20 Kasım 2026)."""
from anim import *
import sys, os
W, H = 1080, 1350
OUT = 'out_1127'; os.makedirs(OUT, exist_ok=True)
BLACK = (22, 14, 18)
INK2 = (58, 40, 48)
GREEN = (70, 140, 96)


def lerp(a, b, u):
    return tuple(int(a[i] + (b[i] - a[i]) * u) for i in range(3))


def blobs(c, t, col, pos=(W - 110, 1120), R=380):
    d = ImageDraw.Draw(c); s = ease(t / 0.7); p = math.sin(t * 1.4) * 14
    r = int(R * s); d.ellipse([pos[0] - r - p, pos[1] - r - p, pos[0] + r + p, pos[1] + r + p], fill=col)


def footer(c, i, col):
    text_a(c, (70, 1290), 'PUDRA DERGİ', F(BOLD, 22), col, 1)
    text_a(c, (W - 70, 1288), f'{i}/5', F(MED, 24), col, 1, anchor='ra')


# ---------- illüstrasyonlar
def shop(c, t, cx, cy, s, k=1.0, wall=CREAM, awn=BERRY):
    """Mağaza cephesi + ipte sallanan KAPALI tabelası."""
    if k <= 0.02: return
    s = s * k; d = ImageDraw.Draw(c)
    w, h = 300 * s, 330 * s
    x0, y0 = cx - w, cy - h
    d.rounded_rectangle([x0, y0, cx + w, cy + h], radius=int(26 * s), fill=wall)
    # tente (çizgili, dalgalı alt kenar)
    n = 8; sw = 2 * w / n
    for j in range(n):
        col = awn if j % 2 == 0 else PINK
        xa = x0 + j * sw
        d.rectangle([xa, y0 - 40 * s, xa + sw, y0 + 70 * s], fill=col)
        d.pieslice([xa, y0 + 40 * s, xa + sw, y0 + 100 * s], 0, 180, fill=col)
    d.rounded_rectangle([x0 - 16 * s, y0 - 70 * s, cx + w + 16 * s, y0 - 30 * s], radius=int(16 * s), fill=PLUM)
    # vitrin
    d.rounded_rectangle([x0 + 40 * s, y0 + 140 * s, cx - 60 * s, cy + 90 * s], radius=int(18 * s), fill=(226, 214, 220))
    for j, (dx, hh, col) in enumerate([(70, 90, BERRY), (150, 120, RED), (225, 70, PLUM)]):
        b = math.sin(t * 2 + j) * 3 * s
        bx = x0 + dx * s
        d.rounded_rectangle([bx, cy + 90 * s - hh * s + b, bx + 46 * s, cy + 90 * s], radius=int(10 * s), fill=col)
        d.rounded_rectangle([bx + 12 * s, cy + 90 * s - hh * s - 22 * s + b, bx + 34 * s, cy + 90 * s - hh * s + 2 * s + b],
                            radius=int(5 * s), fill=PLUM)
    # kapı
    dx0 = cx + 10 * s
    d.rounded_rectangle([dx0, y0 + 140 * s, cx + w - 40 * s, cy + h], radius=int(14 * s), fill=PLUM)
    d.ellipse([cx + w - 90 * s, cy + 60 * s, cx + w - 66 * s, cy + 84 * s], fill=PINK)
    # sallanan tabela
    ang = math.sin(t * 2.4) * 9
    sg = Image.new('RGBA', (int(240 * s), int(200 * s)), (0, 0, 0, 0)); sd = ImageDraw.Draw(sg)
    pw = 240 * s
    sd.line([(pw / 2, 4 * s), (30 * s, 80 * s)], fill=CREAM, width=max(2, int(5 * s)))
    sd.line([(pw / 2, 4 * s), (pw - 30 * s, 80 * s)], fill=CREAM, width=max(2, int(5 * s)))
    sd.ellipse([pw / 2 - 9 * s, 0, pw / 2 + 9 * s, 18 * s], fill=PINK)
    sd.rounded_rectangle([10 * s, 76 * s, pw - 10 * s, 176 * s], radius=int(18 * s), fill=RED)
    sd.text((pw / 2, 140 * s), 'KAPALI', font=F(BOLD, max(10, int(46 * s))), fill=CREAM, anchor='ms')
    sg = sg.rotate(ang, center=(pw / 2, 9 * s), resample=Image.BICUBIC)
    door_cx = (dx0 + cx + w - 40 * s) / 2
    c.paste(sg, (int(door_cx - pw / 2), int(y0 + 175 * s)), sg)


def drop(c, t, cx, cy, s, k=1.0, col=RED):
    """Kalpli damla (kan bağışı) — nabız gibi atar."""
    if k <= 0.02: return
    p = 1 + 0.05 * math.sin(t * 6)
    s = s * k * p; d = ImageDraw.Draw(c)
    R = 110 * s
    d.ellipse([cx - R, cy - R * 0.4, cx + R, cy + R * 1.6], fill=col)
    d.polygon([(cx, cy - R * 1.5), (cx - R * 0.93, cy + R * 0.25), (cx + R * 0.93, cy + R * 0.25)], fill=col)
    # kalp
    hs = 30 * s
    d.ellipse([cx - hs * 1.9, cy + R * 0.2, cx, cy + R * 0.2 + hs * 1.8], fill=CREAM)
    d.ellipse([cx, cy + R * 0.2, cx + hs * 1.9, cy + R * 0.2 + hs * 1.8], fill=CREAM)
    d.polygon([(cx - hs * 1.85, cy + R * 0.2 + hs * 1.15), (cx + hs * 1.85, cy + R * 0.2 + hs * 1.15),
               (cx, cy + R * 0.2 + hs * 3.2)], fill=CREAM)
    d.ellipse([cx - R * 0.6, cy + R * 0.1, cx - R * 0.35, cy + R * 0.6], fill=lerp(col, (255, 255, 255), 0.35))


def cart(c, t, cx, cy, s, k=1.0, col=CREAM, items=(PINK, RED, BERRY)):
    """Alışveriş sepeti — ürünler tek tek uçup gidiyor, sepet boşalıyor."""
    if k <= 0.02: return
    s = s * k; d = ImageDraw.Draw(c)
    # ürünler (döngü 4 sn)
    ph = t % 4.0
    for j, ic in enumerate(items):
        st = 0.6 + j * 0.7
        u = max(0.0, min(1.0, (ph - st) / 0.8))
        if ph < 0.3: u = 0
        x = cx - 90 * s + j * 85 * s + u * 260 * s
        y = cy - 70 * s - math.sin(u * math.pi) * 110 * s + u * 40 * s
        if u >= 1: continue
        hh = (70 + 25 * (j % 2)) * s
        d.rounded_rectangle([x - 28 * s, y - hh, x + 28 * s, y], radius=int(10 * s), fill=ic)
        d.rounded_rectangle([x - 12 * s, y - hh - 20 * s, x + 12 * s, y - hh + 2], radius=int(5 * s), fill=PLUM if ic != PLUM else CREAM)
    # sepet gövdesi
    w = 170 * s
    d.polygon([(cx - w, cy - 60 * s), (cx + w, cy - 60 * s), (cx + w * 0.78, cy + 80 * s), (cx - w * 0.72, cy + 80 * s)],
              outline=col, width=max(3, int(12 * s)))
    for j in range(1, 4):
        xx = cx - w + j * 2 * w / 4
        d.line([(xx, cy - 60 * s), (xx - 10 * s, cy + 80 * s)], fill=col, width=max(2, int(7 * s)))
    d.line([(cx - w * 0.85, cy + 10 * s), (cx + w * 0.88, cy + 10 * s)], fill=col, width=max(2, int(7 * s)))
    d.line([(cx - w, cy - 60 * s), (cx - w - 50 * s, cy - 120 * s), (cx - w - 90 * s, cy - 120 * s)],
           fill=col, width=max(3, int(12 * s)), joint='curve')
    d.line([(cx - w * 0.72, cy + 80 * s), (cx - w * 0.78, cy + 120 * s), (cx + w * 0.8, cy + 120 * s)],
           fill=col, width=max(3, int(10 * s)))
    roll = t * 3
    for wx in (cx - w * 0.6, cx + w * 0.6):
        r = 24 * s
        d.ellipse([wx - r, cy + 130 * s, wx + r, cy + 130 * s + 2 * r], fill=col)
        a = roll
        d.line([(wx, cy + 130 * s + r), (wx + r * 0.8 * math.cos(a), cy + 130 * s + r + r * 0.8 * math.sin(a))],
               fill=PLUM, width=max(2, int(5 * s)))


def jar(c, t, cx, cy, s, k=1.0):
    """Açık kavanoz simgesi (PAO) — kapak açılıp kapanıyor, 12M yazısı."""
    if k <= 0.02: return
    s = s * k; d = ImageDraw.Draw(c)
    w = 120 * s
    d.rounded_rectangle([cx - w, cy - 40 * s, cx + w, cy + 140 * s], radius=int(30 * s), outline=PLUM, width=max(3, int(12 * s)), fill=PINK)
    d.text((cx, cy + 92 * s), '12M', font=F(BOLD, max(10, int(76 * s))), fill=PLUM, anchor='ms')
    op = 0.5 + 0.5 * math.sin(t * 2.2)
    ang = -10 - 28 * op
    lid = Image.new('RGBA', (int(2 * w + 60 * s), int(80 * s)), (0, 0, 0, 0)); ld = ImageDraw.Draw(lid)
    ld.rounded_rectangle([10 * s, 20 * s, 2 * w + 50 * s, 64 * s], radius=int(14 * s), fill=BERRY)
    lid = lid.rotate(-ang, center=(10 * s, 64 * s), expand=False, resample=Image.BICUBIC)
    c.paste(lid, (int(cx - w - 30 * s), int(cy - 104 * s - op * 12 * s)), lid)
    sparkle(d, cx + w + 40 * s, cy - 90 * s, (18 + 6 * math.sin(t * 5)) * s, RED)


def tick(d, x, y, s, col, a=1.0):
    d.line([(x, y + 14 * s), (x + 12 * s, y + 27 * s), (x + 32 * s, y)], fill=col, width=max(3, int(8 * s)), joint='curve')


def cross(d, x, y, s, col):
    d.line([(x, y), (x + 26 * s, y + 26 * s)], fill=col, width=max(3, int(8 * s)))
    d.line([(x + 26 * s, y), (x, y + 26 * s)], fill=col, width=max(3, int(8 * s)))


# ---------- 1 · KAPAK
def p1(t):
    c = Image.new('RGB', (W, H), BLACK); d = ImageDraw.Draw(c)
    blobs(c, t, (64, 16, 40), (W - 40, 1160), 460)
    dots(d, 860, 230, 4, 3, 44, 6, (80, 50, 64))
    sticker(c, (420, 250), 'PUDRA GÜNDEM · BLACK FRIDAY', F(BOLD, 28), PINK, PLUM, -4, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Bugün herkes', F(BOLD, 104), 316, 0.3, CREAM),
                                  ('indirimde.', F(BOLD, 104), 432, 0.5, CREAM),
                                  ('Bir marka kapıyı kapattı.', F(ACC, 74), 560, 0.75, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(36 * (1 - a)))
    a = ease((t - 1.3) / 0.5)
    text_a(c, (70, 690), 'Yedinci yıl: indirim yok,', F(MED, 36), CREAM, a)
    text_a(c, (70, 740), 'mağaza kapalı. Neden?', F(MED, 36), CREAM, a)
    shop(c, t, 760, 1050, 0.62)
    a = ease((t - 2.0) / 0.4)
    if a > 0:
        sticker(c, (190, 930), 'Kaydet', F(BOLD, 42), RED, CREAM, -6, back((t - 2.0) / 0.4), 34, 14)
        text_a(c, (70 + int(8 * math.sin(t * 6)), 1230), 'kaydır  ›', F(BOLD, 38), CREAM, a)
    sparkle(d, 300, 1090, 24 + 6 * math.sin(t * 4), PINK)
    sparkle(d, 1010, 640, 18 + 5 * math.sin(t * 5 + 1), CREAM)
    logo(c, 'A'); return c


def p1_cover(t):
    # Instagram ızgara kapağı = ilk videonun İLK karesi; 0. saniyede tam dolu.
    return p1(t + 3.5)


# ---------- 2 · NE OLDU?
def p2(t):
    c = Image.new('RGB', (W, H), PINK); d = ImageDraw.Draw(c)
    blobs(c, t, (236, 170, 192), (W - 80, 1210), 330)
    sticker(c, (W - 250, 110), 'NE OLDU?', F(BOLD, 30), PLUM, CREAM, 5, back((t - 0.2) / 0.4))
    a = ease((t - 0.25) / 0.5); text_a(c, (70, 200), '7. yıl,', F(BOLD, 96), PLUM, a, int(28 * (1 - a)))
    a = ease((t - 0.45) / 0.5); text_a(c, (70, 305), 'yine kapalı.', F(ACC, 96), BERRY, a, int(28 * (1 - a)))
    a = ease((t - 0.9) / 0.5); y = 460
    body = "The Ordinary, Black Friday'de indirim yapmak yerine yine mağazalarını kapatıyor. Bu yılın sloganı:"
    for ln in wrap(F(REG, 34), body, 640):
        text_a(c, (72, y), ln, F(REG, 34), PLUM, a); y += 48
    a = ease((t - 1.3) / 0.5); y += 10
    for ln in ['“İhtiyacımız olan her şey', 'satılık değil.”']:
        text_a(c, (72, y), ln, F(ACC, 46), BERRY, a, int(20 * (1 - a))); y += 60
    y += 24
    items = ['New York ve Toronto’da bazı mağazalar bugün kan bağışı noktası.',
             'Londra ve Kopenhag’da kan grubunu öğrenebileceğin etkinlikler.']
    for j, it in enumerate(items):
        s = ease((t - 1.8 - j * 0.35) / 0.45)
        if s <= 0: continue
        x = 72 - int(50 * (1 - s))
        d.ellipse([x, y + 8, x + 26, y + 34], fill=RED)
        yy = y
        for ln in wrap(F(MED, 32), it, 560):
            text_a(c, (x + 44, yy), ln, F(MED, 32), PLUM, s); yy += 44
        y = yy + 18
    drop(c, t, 860, 1060, 0.95, back((t - 0.7) / 0.5))
    footer(c, 2, PLUM)
    logo(c, 'B'); return c


# ---------- 3 · SANA NE DEMEK?
def p3(t):
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 80, 1210), 330)
    sticker(c, (W - 290, 110), 'SANA NE DEMEK?', F(BOLD, 30), PINK, PLUM, 5, back((t - 0.2) / 0.4))
    a = ease((t - 0.25) / 0.5); text_a(c, (70, 200), 'Son fırsat', F(BOLD, 92), CREAM, a, int(28 * (1 - a)))
    a = ease((t - 0.45) / 0.5); text_a(c, (70, 302), 'ihtiyaç değil.', F(ACC, 92), PINK, a, int(28 * (1 - a)))
    a = ease((t - 0.9) / 0.5); y = 450
    body = 'İndirim baskısı gerçek. Ama geri sayan saat, senin cildinin neye ihtiyacı olduğunu bilmiyor. Bugün en kârlı alışveriş: bitirdiğin ürünü yenilemek.'
    for ln in wrap(F(REG, 34), body, 640):
        text_a(c, (72, y), ln, F(REG, 34), CREAM, a); y += 48
    k = back((t - 1.6) / 0.5)
    if k > 0.02:
        tip = 'Sepette 24 saat beklet. Hâlâ aklındaysa al. Unuttuysan zaten ihtiyacın değilmiş.'
        lines = wrap(F(MED, 33), tip, 560)
        bh = 90 + len(lines) * 46
        box = Image.new('RGBA', (640, bh + 10), (0, 0, 0, 0)); bd = ImageDraw.Draw(box)
        bd.rounded_rectangle([0, 0, 630, bh], radius=34, fill=PINK)
        bd.text((34, 28), 'PUDRA DİYOR Kİ', font=F(BOLD, 26), fill=BERRY)
        yy = 70
        for ln in lines: bd.text((34, yy), ln, font=F(MED, 33), fill=PLUM); yy += 46
        if k != 1: box = box.resize((max(1, int(640 * k)), max(1, int((bh + 10) * k))))
        c.paste(box, (66, y + 34), box)
    cart(c, t, 660, 1150, 0.8, back((t - 0.7) / 0.5), CREAM, (PINK, RED, CREAM))
    sparkle(d, 990, 420, 22 + 6 * math.sin(t * 4), PINK)
    footer(c, 3, CREAM)
    logo(c, 'A'); return c


# ---------- 4 · DENE / DENEME
def p4(t):
    c = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(c)
    blobs(c, t, PINK, (W - 60, 1220), 330)
    sticker(c, (W - 270, 110), 'DENE · DENEME', F(BOLD, 30), BERRY, CREAM, 5, back((t - 0.2) / 0.4))
    a = ease((t - 0.25) / 0.5); text_a(c, (70, 196), 'Sepeti', F(BOLD, 92), PLUM, a, int(28 * (1 - a)))
    a = ease((t - 0.45) / 0.5); text_a(c, (70, 298), 'akıllı doldur.', F(ACC, 92), BERRY, a, int(28 * (1 - a)))
    y = 452
    a = ease((t - 0.8) / 0.4); text_a(c, (72, y), 'DENE', F(BOLD, 34), GREEN, a); y += 58
    dene = ['Kavanoz simgesine bak: “12M”, açıldıktan sonra 12 ay demek.',
            'Elindekini bitir, sonra yenile.',
            'Listeyle gir, listeyle çık.']
    for j, it in enumerate(dene):
        s = ease((t - 1.0 - j * 0.3) / 0.4)
        if s <= 0: continue
        x = 72 - int(40 * (1 - s))
        tick(d, x, y + 6, 1.0, GREEN)
        yy = y
        for ln in wrap(F(MED, 32), it, 520):
            text_a(c, (x + 54, yy), ln, F(MED, 32), PLUM, s); yy += 44
        y = yy + 14
    y += 18
    a = ease((t - 2.0) / 0.4); text_a(c, (72, y), 'DENEME', F(BOLD, 34), RED, a); y += 58
    deneme = ['Aynı serumdan üç tane stoklamak.',
              'Sırf ücretsiz kargo için sepete bir şey eklemek.']
    for j, it in enumerate(deneme):
        s = ease((t - 2.2 - j * 0.3) / 0.4)
        if s <= 0: continue
        x = 72 - int(40 * (1 - s))
        cross(d, x + 4, y + 8, 1.0, RED)
        yy = y
        for ln in wrap(F(MED, 32), it, 520):
            text_a(c, (x + 54, yy), ln, F(MED, 32), PLUM, s); yy += 44
        y = yy + 14
    jar(c, t, 850, 1080, 0.95, back((t - 0.6) / 0.5))
    footer(c, 4, PLUM)
    logo(c, 'B'); return c


# ---------- 5 · SORU
def p5(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1220), 380)
    sparkle(d, 950, 300, 30 + 6 * math.sin(t * 4), PINK)
    for txt, font, y, st, col in [('Sen bugün', F(BOLD, 96), 200, 0.2, CREAM),
                                  ('hangisisin?', F(ACC, 116), 306, 0.4, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    opts = [('A', 'Sepet çoktan doldu'), ('B', 'Listemdekini aldım, o kadar'),
            ('C', 'Bugün hiçbir şey almıyorum'), ('D', 'Hafta sonunu bekliyorum')]
    y = 480
    for k, (l, txt) in enumerate(opts):
        s = ease((t - 0.9 - k * 0.25) / 0.45)
        if s > 0:
            x = 70 - int(60 * (1 - s))
            d.rounded_rectangle([x, y, x + 680, y + 88], radius=44, fill=CREAM)
            d.ellipse([x + 10, y + 8, x + 86, y + 84], fill=PLUM)
            d.text((x + 48, y + 64), l, font=F(BOLD, 44), fill=CREAM, anchor='ms')
            d.text((x + 108, y + 61), txt, font=F(BOLD, 32), fill=PLUM, anchor='ls')
        y += 100
    sticker(c, (330, 940), 'Harfini yorumlara yaz ›', F(BOLD, 40), PLUM, CREAM, -3,
            back((t - 2.0) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 34, 18)
    a = ease((t - 2.5) / 0.4)
    text_a(c, (72, 1030), 'Alışveriş arkadaşına', F(BOLD, 40), CREAM, a)
    text_a(c, (72, 1080), 'gönder.', F(ACC, 52), PINK, a)
    cart(c, t, 860, 1080, 0.55, back((t - 0.8) / 0.5), CREAM, (PINK, PLUM, CREAM))
    footer(c, 5, CREAM)
    logo(c, 'A'); return c


# ---------- STORY
def story(t):
    SW, SH = 1080, 1920
    c = Image.new('RGB', (SW, SH), BLACK); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 22; r = int(460 * ease(t / 0.8))
    d.ellipse([1080 - r - p, 1420 - r - p, 1080 + r + p, 1420 + r + p], fill=(64, 16, 40))
    dots(d, 820, 430, 5, 3, 44, 6, (80, 50, 64))
    sticker(c, (300, 420), 'PUDRA GÜNDEM', F(BOLD, 34), PINK, PLUM, -5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Bugün herkes', F(BOLD, 104), 500, 0.3, CREAM),
                                  ('indirimde.', F(BOLD, 104), 616, 0.5, CREAM),
                                  ('Bir marka kapıyı kapattı.', F(ACC, 72), 746, 0.75, PINK),
                                  ('Hem de yedinci kez.', F(MED, 46), 860, 1.1, CREAM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    shop(c, t, SW // 2, 1240, 0.72)
    s2 = back((t - 2.2) / 0.45)
    if s2 > 0: sticker(c, (SW // 2 + int(8 * math.sin(t * 6)), 1580), 'Neden? Yeni gönderide ›', F(BOLD, 44), RED, CREAM, -2, s2, 42, 22)
    logo(c, 'A', True); return c


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
