"""PUDRA GÜNDEM — Smoky göz geri döndü, bu kez dağınık (19 Kasım 2026; yayın 26 Kasım 18:00).
Kaynaklar: WWD/Yahoo 18 Kasım (British GQ Men of the Year, 17 Kasım Londra; makyaj Kelly Cornwell),
evoke.ie 13 Kasım (parti sezonu 'soft grunge' 90'lar makyajı)."""
from anim import *
from PIL import ImageFilter
import sys, os
W, H = 1080, 1350
OUT = 'out_1119'; os.makedirs(OUT, exist_ok=True)
BROWN = (110, 62, 40)
AMBER = (186, 100, 44)
COPPER = (214, 128, 72)
CHAR = (66, 56, 62)
SKIN = (246, 214, 196)
SCLERA = (255, 250, 246)


# ---------- illüstrasyonlar
def eye(c, t, cx, cy, s=1.0, smudge=1.0, sharp=False, finger=False, pencil=False, skin=SKIN):
    """Göz: sıcak tonlu, bulanık smoky gölge (smudge 0→1 yayılır), kirpikler, ara sıra göz kırpma.
    sharp=True → keskin siyah eyeliner kanadı (karşılaştırma için)."""
    a, hh, hl = 190 * s, 92 * s, 58 * s
    pad = int(200 * s)
    Wl, Hl = int(2 * a + 2 * pad), int(2 * hh + 2 * pad)
    lay = Image.new('RGBA', (Wl, Hl), (0, 0, 0, 0))
    ox, oy = Wl / 2, Hl / 2
    # ten zemini (yumuşak oval)
    d = ImageDraw.Draw(lay)
    d.ellipse([ox - a - 120 * s, oy - hh - 130 * s, ox + a + 120 * s, oy + hh + 110 * s], fill=skin)
    # göz kırpma
    bl = 1.0
    ph = t % 3.2
    if 2.9 < ph < 3.15: bl = max(0.08, abs(ph - 3.025) / 0.125)
    def up(u): return oy - hh * bl * math.sin(math.pi * u) + 6 * s * u
    def lo(u): return oy + hl * bl * math.sin(math.pi * u) + 6 * s * u
    N = 40
    upper = [(ox - a + 2 * a * k / N, up(k / N)) for k in range(N + 1)]
    lower = [(ox - a + 2 * a * k / N, lo(k / N)) for k in range(N + 1)]
    if not sharp and smudge > 0:
        sm = Image.new('RGBA', (Wl, Hl), (0, 0, 0, 0)); sd = ImageDraw.Draw(sm)
        al = int(235 * min(1, smudge))
        sp = 0.55 + 0.45 * smudge
        sd.ellipse([ox - a * 0.95, oy - hh - 70 * s * sp, ox + a * 1.05, oy + 20 * s], fill=BROWN + (al,))
        sd.ellipse([ox - a * 0.3, oy - hh - 50 * s * sp, ox + a * 1.15, oy + 10 * s], fill=AMBER + (al,))
        # bulanık kanat (dışa ve yukarı)
        sd.polygon([(ox + a * 0.6, oy - 30 * s), (ox + a + 120 * s * sp, oy - hh * 0.9 - 30 * s * sp),
                    (ox + a + 40 * s, oy + 20 * s)], fill=COPPER + (al,))
        # alt kirpik dibi dağınık kalem
        sd.ellipse([ox - a * 0.2, oy + hl * 0.4, ox + a * 1.1, oy + hl + 26 * s * sp], fill=CHAR + (int(al * 0.75),))
        sm = sm.filter(ImageFilter.GaussianBlur(max(2, 26 * s * (0.4 + 0.6 * smudge))))
        lay.alpha_composite(sm)
    d = ImageDraw.Draw(lay)
    # göz akı
    poly = upper + lower[::-1]
    d.polygon(poly, fill=SCLERA)
    # iris (göz şekline maskeli)
    look = math.sin(t * 0.9) * 26 * s
    ir = 62 * s
    irl = Image.new('RGBA', (Wl, Hl), (0, 0, 0, 0)); idr = ImageDraw.Draw(irl)
    ix, iy = ox + look, oy + 4 * s
    idr.ellipse([ix - ir, iy - ir, ix + ir, iy + ir], fill=(120, 74, 44))
    idr.ellipse([ix - ir * 0.62, iy - ir * 0.62, ix + ir * 0.62, iy + ir * 0.62], fill=(86, 50, 30))
    idr.ellipse([ix - ir * 0.36, iy - ir * 0.36, ix + ir * 0.36, iy + ir * 0.36], fill=(24, 14, 18))
    idr.ellipse([ix + ir * 0.18, iy - ir * 0.5, ix + ir * 0.46, iy - ir * 0.22], fill=(255, 255, 255))
    m = Image.new('L', (Wl, Hl), 0); ImageDraw.Draw(m).polygon(poly, fill=255)
    lay.paste(irl, (0, 0), Image.composite(irl, Image.new('RGBA', (Wl, Hl), (0, 0, 0, 0)), m).split()[3])
    # üst kapak çizgisi + kirpikler
    lc = PLUM if not sharp else (16, 10, 14)
    d.line(upper, fill=lc, width=max(2, int((12 if sharp else 7) * s)), joint='curve')
    d.line(lower, fill=(150, 100, 90) if sharp else CHAR, width=max(1, int(4 * s)), joint='curve')
    if sharp:
        ex, ey = upper[-1]
        d.polygon([(ex - 40 * s, ey - 16 * s), (ex + 90 * s, ey - 70 * s), (ex, ey + 4 * s)], fill=(16, 10, 14))
    for k in range(4, N - 1, 4):
        x, y = upper[k]
        u = k / N
        ang = -math.pi / 2 + (u - 0.45) * 1.6
        L = (26 + 18 * math.sin(math.pi * u)) * s * bl
        d.line([(x, y), (x + math.cos(ang) * L, y + math.sin(ang) * L)], fill=lc, width=max(1, int(5 * s)))
    # parmak (dağıtma hareketi)
    if finger:
        fx = ox + a * 0.75 + math.sin(t * 4) * 40 * s
        fy = oy + hl + 50 * s
        fl = Image.new('RGBA', (Wl, Hl), (0, 0, 0, 0)); fd = ImageDraw.Draw(fl)
        fd.rounded_rectangle([fx - 34 * s, fy - 30 * s, fx + 34 * s, fy + 200 * s], radius=int(34 * s), fill=(236, 186, 164))
        fd.rounded_rectangle([fx - 20 * s, fy - 18 * s, fx + 20 * s, fy + 30 * s], radius=int(16 * s), fill=(250, 214, 204))
        lay.alpha_composite(fl)
    if pencil:
        u = (t * 0.45) % 1
        px = ox - a * 0.4 + u * a * 1.5
        py = up(min(1, 0.3 + u * 0.7)) - 6 * s
        pl = Image.new('RGBA', (int(300 * s), int(60 * s)), (0, 0, 0, 0)); pd = ImageDraw.Draw(pl)
        pd.rectangle([0, 14 * s, 230 * s, 46 * s], fill=BERRY)
        pd.rectangle([230 * s, 14 * s, 262 * s, 46 * s], fill=(230, 200, 160))
        pd.polygon([(262 * s, 14 * s), (296 * s, 30 * s), (262 * s, 46 * s)], fill=CHAR)
        pl = pl.rotate(-38, expand=True, resample=Image.BICUBIC)
        lay.alpha_composite(pl, (int(px - pl.width * 0.86), int(py - pl.height * 0.86)))
    c.paste(lay, (int(cx - Wl / 2), int(cy - Hl / 2)), lay)


def palette(c, t, cx, cy, s=1.0, labels=True):
    """Far paleti: 4 sıcak ton sırayla zıplar, fırça dolaşır."""
    d = ImageDraw.Draw(c)
    w, h = 560 * s, 210 * s
    k0 = back(t / 0.5)
    if k0 <= 0.02: return
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=int(36 * s), fill=PLUM)
    tones = [(BROWN, 'KAHVE'), (AMBER, 'AMBER'), (COPPER, 'BAKIR'), (CHAR, 'ANTRASİT')]
    for j, (col, lab) in enumerate(tones):
        k = back((t - 0.3 - j * 0.25) / 0.4)
        if k <= 0.02: continue
        x = cx - w / 2 + 75 * s + j * 137 * s
        r = 52 * s * k * (1 + 0.04 * math.sin(t * 5 + j))
        d.ellipse([x - r, cy - 20 * s - r, x + r, cy - 20 * s + r], fill=col)
        d.ellipse([x - r * 0.5, cy - 20 * s - r * 0.7, x - r * 0.1, cy - 20 * s - r * 0.3], fill=tuple(min(255, v + 50) for v in col))
        if labels:
            d.text((x, cy + 66 * s), lab, font=F(BOLD, max(8, int(19 * s * k))), fill=CREAM, anchor='mm')
    # fırça
    if t > 1.4:
        u = (t - 1.4) * 1.1
        bx = cx - w / 2 + 75 * s + (math.sin(u) * 0.5 + 0.5) * 3 * 137 * s
        by = cy - 30 * s + math.sin(u * 3) * 8 * s
        s = s * 0.75
        bl = Image.new('RGBA', (int(70 * s), int(330 * s)), (0, 0, 0, 0)); bd = ImageDraw.Draw(bl)
        bd.ellipse([8 * s, 0, 62 * s, 90 * s], fill=COPPER)
        bd.rectangle([18 * s, 70 * s, 52 * s, 120 * s], fill=(200, 200, 205))
        bd.rounded_rectangle([24 * s, 116 * s, 46 * s, 330 * s], radius=int(10 * s), fill=CREAM)
        bl = bl.rotate(20, expand=True, resample=Image.BICUBIC)
        c.paste(bl, (int(bx - bl.width / 2), int(by - bl.height * 0.75)), bl)


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
    c = Image.new('RGB', (W, H), BERRY); d = ImageDraw.Draw(c)
    blobs(c, t, (120, 12, 60), (W - 60, 1100), 450)
    dots(d, 870, 230, 4, 3, 44, 6, (180, 60, 110))
    sticker(c, (390, 250), 'PUDRA GÜNDEM · PARTİ SEZONU', F(BOLD, 30), CREAM, BERRY, -4, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Smoky göz', F(BOLD, 112), 316, 0.3, CREAM),
                                  ('geri döndü.', F(BOLD, 96), 438, 0.5, CREAM),
                                  ('Bu kez dağınık.', F(ACC, 108), 548, 0.75, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(36 * (1 - a)))
    a = ease((t - 1.3) / 0.5)
    text_a(c, (70, 728), 'Keskin eyeliner kenara: bakır tonlar', F(MED, 36), CREAM, a)
    text_a(c, (70, 778), 've parmakla dağıtılmış kalem.', F(MED, 36), CREAM, a)
    eye(c, t, 680, 1060, 0.95, smudge=min(1, 0.6 + t * 0.2), finger=True)
    a = ease((t - 2.0) / 0.4)
    if a > 0:
        sticker(c, (200, 920), 'Kaydet', F(BOLD, 42), RED, CREAM, -6, back((t - 2.0) / 0.4), 34, 14)
        text_a(c, (70 + int(8 * math.sin(t * 6)), 1240), 'kaydır  ›', F(BOLD, 38), CREAM, a)
    sparkle(d, 990, 640, 26 + 6 * math.sin(t * 4), PINK)
    logo(c, 'A'); return c


# ---------- 2 · NE OLDU
def p2(t):
    c = Image.new('RGB', (W, H), PINK); d = ImageDraw.Draw(c)
    blobs(c, t, (236, 170, 192), (W - 80, 1200), 300)
    sticker(c, (W - 260, 110), 'NE OLDU?', F(BOLD, 30), BERRY, CREAM, 5, back((t - 0.2) / 0.4))
    for txt, font, y, st, col in [('Londra, 17 Kasım.', F(BOLD, 84), 200, 0.3, BERRY),
                                  ('Kırmızı halıda', F(ACC, 92), 304, 0.55, PLUM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    body = ['British GQ ödüllerinde Olivia Cooke\'un',
            'makyajı konuşuldu: sıcak kahve ve yanık',
            'amber far, dışa doğru bulanık bir kanat,',
            'kahve kalemle çevrili gözler.']
    a = ease((t - 0.9) / 0.5); y = 460
    for ln in body: text_a(c, (72, y), ln, F(REG, 34), PLUM, a); y += 48
    a = ease((t - 1.4) / 0.5); y += 26
    for ln in ['Güzellik editörlerine göre parti sezonunun',
               'gözdesi 90\'lar esintili "soft grunge":']:
        text_a(c, (72, y), ln, F(MED, 34), BERRY, a); y += 48
    a = ease((t - 1.8) / 0.5)
    text_a(c, (72, y + 6), 'biraz dağınık, sanki dünden kalmış.', F(ACC, 40), PLUM, a)
    if t > 1.9:
        palette(c, t - 1.9, 540, 1150, 1.05)
    footer(c, 2, PLUM)
    logo(c, 'B'); return c


# ---------- 3 · SANA NE DEMEK / 3 ADIM
def p3(t):
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1220), 300)
    sticker(c, (W - 290, 110), 'SANA NE DEMEK?', F(BOLD, 30), RED, CREAM, -5, back((t - 0.2) / 0.4))
    a = ease((t - 0.2) / 0.5); text_a(c, (70, 190), 'Kusursuz olmak', F(BOLD, 84), CREAM, a, int(24 * (1 - a)))
    a = ease((t - 0.4) / 0.5); text_a(c, (70, 290), 'zorunda değil.', F(ACC, 96), PINK, a, int(24 * (1 - a)))
    steps = [('01', 'Mat taba ya da bronz farı', 'tüm kapağa yay, kenar bırakma.'),
             ('02', 'Kalemi kirpik dibine karala,', 'sonra parmağınla dağıt.'),
             ('03', 'Rimel + kahve tonlu ruj.', 'Bu kadar.')]
    y = 440; st = 0.7
    for num, l1, l2 in steps:
        k = back((t - st) / 0.4)
        if k > 0.02:
            r = 34 * k
            d.ellipse([102 - r, y + 32 - r, 102 + r, y + 32 + r], fill=PINK)
            d.text((102, y + 33), num, font=F(BOLD, max(8, int(28 * k))), fill=PLUM, anchor='mm')
        aa = ease((t - st - 0.1) / 0.45)
        text_a(c, (164, y + 4), l1, F(BOLD, 38), CREAM, aa, int(16 * (1 - aa)))
        text_a(c, (164, y + 56), l2, F(REG, 34), PINK, aa, int(16 * (1 - aa)))
        y += 138; st += 0.4
    if t > 1.5:
        tt = t - 1.5
        eye(c, tt, 560, 1085, 0.72, smudge=min(1, 0.15 + tt * 0.35), pencil=tt < 2.2, finger=tt >= 2.2)
    footer(c, 3, PINK)
    logo(c, 'B'); return c


# ---------- 4 · DENE / DENEME
def p4(t):
    c = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(c)
    blobs(c, t, PINK, (W - 90, 1190), 320)
    sticker(c, (W - 300, 110), 'DENE / DENEME', F(BOLD, 30), BERRY, CREAM, 5, back((t - 0.2) / 0.4))
    a = ease((t - 0.2) / 0.5); text_a(c, (70, 190), 'Dağınık ama', F(BOLD, 84), PLUM, a, int(24 * (1 - a)))
    a = ease((t - 0.4) / 0.5); text_a(c, (70, 286), 'yorgun değil.', F(ACC, 96), BERRY, a, int(24 * (1 - a)))
    rows = [(True, BERRY, 'Siyah yerine kahve ya da antrasit kalem: daha yumuşak durur.'),
            (True, BERRY, '40+ ipucu: Kanadı yukarı doğru dağıt, göz kalkık görünür.'),
            (False, RED, 'Alt kirpik dibini baştan sona kalın siyahla doldurma.'),
            (False, RED, 'Her yere simli far sürme; matla başla, simi kapağın ortasına.')]
    y = 430
    for j, (ok, mc, txt) in enumerate(rows):
        st = 0.7 + j * 0.35
        k = back((t - st) / 0.4); mark(d, 102, y + 28, ok, mc, k)
        aa = ease((t - st - 0.1) / 0.45); yy = y
        for ln in wrap(F(MED, 34), txt, W - 250):
            text_a(c, (160, yy + 2), ln, F(MED, 34), PLUM, aa, int(14 * (1 - aa))); yy += 46
        y = yy + 24
    if t > 1.9:
        palette(c, t - 1.9, 400, 1130, 0.78, labels=True)
    footer(c, 4, PLUM)
    logo(c, 'A'); return c


# ---------- 5 · SORU
def p5(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1220), 380)
    sparkle(d, 950, 300, 30 + 6 * math.sin(t * 4), PINK)
    for txt, font, y, st, col in [('Partide', F(BOLD, 96), 200, 0.2, CREAM),
                                  ('hangi göz', F(BOLD, 96), 306, 0.35, CREAM),
                                  ('senin?', F(ACC, 120), 410, 0.5, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    opts = [('A', 'Keskin eyeliner'), ('B', 'Dağınık smoky'), ('C', 'Sadece rimel, yeter')]
    y = 610
    for k, (l, txt) in enumerate(opts):
        s = ease((t - 0.9 - k * 0.3) / 0.45)
        if s > 0:
            x = 70 - int(60 * (1 - s))
            d.rounded_rectangle([x, y, x + 600, y + 100], radius=50, fill=CREAM)
            d.ellipse([x + 12, y + 10, x + 92, y + 90], fill=PLUM)
            d.text((x + 52, y + 68), l, font=F(BOLD, 48), fill=CREAM, anchor='ms')
            d.text((x + 118, y + 66), txt, font=F(BOLD, 36), fill=PLUM, anchor='ls')
        y += 116
    sticker(c, (350, 1018), 'Harfini yorumlara yaz ›', F(BOLD, 42), PLUM, CREAM, -3,
            back((t - 2.0) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 36, 18)
    a = ease((t - 2.5) / 0.4)
    text_a(c, (72, 1110), 'Parti arkadaşına', F(BOLD, 40), CREAM, a)
    text_a(c, (72, 1162), 'gönder.', F(ACC, 52), PINK, a)
    if t > 0.8:
        eye(c, t - 0.8, 870, 1090, 0.42, smudge=1.0)
        eye(c, t - 0.5, 900, 760, 0.42, sharp=True)
    footer(c, 5, CREAM)
    logo(c, 'A'); return c


# ---------- STORY
def story(t):
    SW, SH = 1080, 1920
    c = Image.new('RGB', (SW, SH), BERRY); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 22; r = int(400 * ease(t / 0.8))
    d.ellipse([1080 - r - p, 1400 - r - p, 1080 + r + p, 1400 + r + p], fill=(120, 12, 60))
    dots(d, 820, 430, 5, 3, 44, 6, (180, 60, 110))
    sticker(c, (300, 420), 'PUDRA GÜNDEM', F(BOLD, 34), CREAM, BERRY, -5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Smoky göz', F(BOLD, 112), 500, 0.3, CREAM),
                                  ('geri döndü.', F(BOLD, 96), 622, 0.5, CREAM),
                                  ('Bu kez dağınık.', F(ACC, 104), 734, 0.75, PINK),
                                  ('3 adımda parti makyajı', F(MED, 50), 920, 1.1, CREAM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    eye(c, t, SW // 2 + 60, 1260, 0.95, smudge=min(1, 0.3 + t * 0.3), finger=True)
    s2 = back((t - 2.2) / 0.45)
    if s2 > 0: sticker(c, (SW // 2 + int(8 * math.sin(t * 6)), 1560), 'Yeni gönderide ›', F(BOLD, 46), PLUM, CREAM, -2, s2, 42, 22)
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
