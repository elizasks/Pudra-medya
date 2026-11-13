"""PUDRA GÜNDEM — Göz altına kapatıcı yerine aydınlatıcı: viral trend, dürüst cevap (15 Kasım 2026)."""
from anim import *
from illus import bubble
import sys, os
W, H = 1080, 1350
OUT = 'out_1115'; os.makedirs(OUT, exist_ok=True)
GOLD = (232, 196, 120)
CHAMP = (247, 226, 182)
SHADOW = (120, 80, 130)


# ---------- illüstrasyonlar
def eye(c, t, cx, cy, s=1.0, white=CREAM, line=PLUM, iris=BERRY, glow=True, shadow=True):
    """Stilize göz: göz kırpar; altında gölge, üstüne aydınlatıcı çizgisi çizilir + parıltılar."""
    d = ImageDraw.Draw(c)
    hw, hh = 210 * s, 92 * s
    ph = (t % 3.4)
    op = 1.0 if ph > 0.22 else abs(ph - 0.11) / 0.11
    op = max(0.08, op)
    # göz altı gölgesi
    if shadow:
        sh = Image.new('RGBA', c.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
        k = 1 - 0.55 * ease((t - 1.0) / 1.2) if glow else 1
        sd.arc([cx - hw * 0.95, cy - hh * 0.4, cx + hw * 0.85, cy + hh * 1.55], 25, 155,
               fill=SHADOW + (int(150 * k),), width=int(26 * s))
        c.paste(sh, (0, 0), sh)
    # göz şekli
    up = [(cx + x * hw, cy - hh * (1 - x * x) * op) for x in [i / 20 - 1 for i in range(41)]]
    lo = [(cx + x * hw, cy + hh * 0.72 * (1 - x * x)) for x in [1 - i / 20 for i in range(41)]]
    m = Image.new('L', c.size, 0); ImageDraw.Draw(m).polygon(up + lo, fill=255)
    lay = Image.new('RGB', c.size, white); ld = ImageDraw.Draw(lay)
    ix = cx + 14 * s * math.sin(t * 0.9)
    r = 66 * s; ld.ellipse([ix - r, cy - r + 6 * s, ix + r, cy + r + 6 * s], fill=iris)
    r = 30 * s; ld.ellipse([ix - r, cy - r + 6 * s, ix + r, cy + r + 6 * s], fill=line)
    r = 13 * s; ld.ellipse([ix + 18 * s - r, cy - 18 * s - r, ix + 18 * s + r, cy - 18 * s + r], fill=CREAM)
    c.paste(lay, (0, 0), m)
    d.line(up, fill=line, width=int(9 * s), joint='curve')
    d.line(lo, fill=line, width=int(5 * s), joint='curve')
    for k in range(5):  # kirpikler
        x = -0.75 + k * 0.32
        px, py = cx + x * hw, cy - hh * (1 - x * x) * op
        ang = math.atan2(-1, x * 0.9)
        d.line([(px, py), (px + math.cos(ang) * 46 * s, py + math.sin(ang) * 46 * s)], fill=line, width=int(8 * s))
    # aydınlatıcı darbesi (soldan sağa çizilir)
    if glow:
        k = ease((t - 0.8) / 1.0)
        if k > 0:
            pts = []
            for i in range(int(30 * k) + 1):
                x = -0.7 + 1.1 * i / 30
                pts.append((cx + x * hw, cy + hh * 0.72 * (1 - x * x) + 34 * s))
            if len(pts) > 1:
                d.line(pts, fill=CHAMP, width=int(20 * s), joint='curve')
                d.line(pts, fill=(255, 248, 230), width=int(7 * s), joint='curve')
        for j, (dx, dy, rr) in enumerate([(-0.55, 1.15, 26), (0.05, 1.35, 20), (0.5, 1.05, 30)]):
            f = back((t - 1.6 - j * 0.25) / 0.4)
            if f > 0:
                sparkle(d, cx + dx * hw, cy + dy * hh, (rr + 5 * math.sin(t * 5 + j)) * s * f, GOLD)


def wand(d, t, cx, cy, s=1.0, body=CHAMP, cap=PLUM):
    """Sıvı aydınlatıcı şişesi + damla."""
    tilt = math.sin(t * 2) * 4
    d.rounded_rectangle([cx - 46 * s, cy - 40 * s, cx + 46 * s, cy + 140 * s], radius=22 * s, fill=body)
    d.rounded_rectangle([cx - 46 * s, cy + 20 * s, cx + 46 * s, cy + 140 * s], radius=22 * s, fill=GOLD)
    d.rounded_rectangle([cx - 30 * s, cy - 150 * s + tilt, cx + 30 * s, cy - 38 * s], radius=12 * s, fill=cap)
    k = (t * 0.8) % 1
    dy = cy + 160 * s + k * 60 * s
    r = 14 * s * (1 - k * 0.4)
    d.ellipse([cx - r, dy - r, cx + r, dy + r], fill=CHAMP)


def pearl_vs_glitter(c, t, cx, cy, fg=PLUM):
    d = ImageDraw.Draw(c)
    # inci (iyi)
    k = back((t - 0.2) / 0.45)
    if k > 0:
        x = cx - 200; r = 90 * k
        d.ellipse([x - r, cy - r, x + r, cy + r], fill=CHAMP)
        r2 = 34 * k; d.ellipse([x - 40 * k - r2, cy - 40 * k - r2, x - 40 * k + r2, cy - 40 * k + r2], fill=(255, 250, 238))
        d.text((x, cy + 150), 'inci bitiş', font=F(BOLD, 34), fill=fg, anchor='ms')
        # tik işareti
        if t > 0.8:
            q = ease((t - 0.8) / 0.4)
            p1, p2, p3 = (x + 60, cy - 80), (x + 85, cy - 55), (x + 135, cy - 115)
            d.line([p1, p2], fill=BERRY, width=12)
            if q > 0.4: d.line([p2, (p2[0] + (p3[0] - p2[0]) * q, p2[1] + (p3[1] - p2[1]) * q)], fill=BERRY, width=12)
    # iri sim (kaçın)
    k = back((t - 0.6) / 0.45)
    if k > 0:
        x = cx + 200
        for j in range(9):
            a = j * 0.7 + t * 0.5
            rr = (40 + 30 * (j % 3)) * k
            sparkle(d, x + math.cos(a * 2.3) * rr * 0.9, cy + math.sin(a * 1.7) * rr * 0.9,
                    (16 + 8 * (j % 2)) * k * (1 + 0.2 * math.sin(t * 6 + j)), GOLD)
        d.text((x, cy + 150), 'iri sim', font=F(BOLD, 34), fill=fg, anchor='ms')
        if t > 1.2:
            q = ease((t - 1.2) / 0.4)
            L = 50 * q
            d.line([(x + 70 - L, cy - 110 - L), (x + 70 + L, cy - 110 + L)], fill=RED, width=12)
            d.line([(x + 70 - L, cy - 110 + L), (x + 70 + L, cy - 110 - L)], fill=RED, width=12)


def mark(d, x, y, ok, col, k=1.0):
    """Daire içinde tik ya da çarpı."""
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
    blobs(c, t, (120, 12, 60), (W - 40, 1130), 420)
    dots(d, 830, 230, 5, 3, 44, 6, (180, 60, 110))
    sticker(c, (390, 250), 'PUDRA GÜNDEM · VİRAL TREND', F(BOLD, 30), CREAM, BERRY, -4, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Göz altına', F(BOLD, 100), 320, 0.3, CREAM),
                                  ('kapatıcı değil,', F(BOLD, 100), 432, 0.5, CREAM),
                                  ('aydınlatıcı?', F(ACC, 128), 548, 0.75, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(36 * (1 - a)))
    a = ease((t - 1.3) / 0.5)
    text_a(c, (70, 740), 'Sosyal medyanın yeni göz altı hilesi.', F(MED, 38), CREAM, a)
    text_a(c, (70, 792), 'Herkese uyar mı?', F(MED, 38), CREAM, a)
    eye(c, max(0, t - 0.4), 640, 1040, 1.0, CREAM, PLUM, BERRY)
    a = ease((t - 2.0) / 0.4)
    if a > 0:
        sticker(c, (250, 905), 'Dürüst cevap', F(BOLD, 40), RED, CREAM, -6, back((t - 2.0) / 0.4), 30, 14)
        text_a(c, (70 + int(8 * math.sin(t * 6)), 1240), 'kaydır  ›', F(BOLD, 38), CREAM, a)
    logo(c, 'A'); return c


# ---------- 2 · NE OLUYOR
def p2(t):
    c = Image.new('RGB', (W, H), PINK); d = ImageDraw.Draw(c)
    blobs(c, t, (236, 170, 192), (W - 80, 1180), 320)
    sticker(c, (W - 300, 110), 'NE OLUYOR?', F(BOLD, 30), BERRY, CREAM, 5, back((t - 0.2) / 0.4))
    for txt, font, y, st, col in [('Kapatma,', F(BOLD, 110), 210, 0.3, BERRY),
                                  ('aydınlat.', F(ACC, 120), 330, 0.55, PLUM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    body = ['Göz altına önce sıvı ya da krem aydınlatıcı',
            'sürülüyor; kapatıcı sadece gereken yere',
            'ya da hiç. Akım TikTok ve Instagram\'da yayıldı.']
    a = ease((t - 1.0) / 0.5); y = 510
    for ln in body: text_a(c, (72, y), ln, F(REG, 36), PLUM, a); y += 50
    a = ease((t - 1.5) / 0.5); y += 24
    for ln in ['Mantık: Işığı yansıtan ürün gölgeyi', 'yumuşatır. Morluk gitmez, sadece', 'daha az görünür. Bir optik illüzyon.']:
        text_a(c, (72, y), ln, F(BOLD, 38), BERRY, a); y += 52
    wave_line(d, 0, W * ease((t - 1.2) / 0.8), y + 26, 12, 170, BERRY, 5, -t * 2)
    eye(c, max(0, t - 0.6), 400, 1070, 0.8, CREAM, PLUM, BERRY)
    wand(d, max(0, t - 0.6), 850, 1010, 0.9)
    footer(c, 2, PLUM)
    logo(c, 'B'); return c


# ---------- 3 · SANA NE DEMEK
def p3(t):
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1200), 300)
    sticker(c, (W - 290, 110), 'SANA NE DEMEK?', F(BOLD, 30), RED, CREAM, -5, back((t - 0.2) / 0.4))
    groups = [('DENE', True, PINK, BERRY, [
                  ('Göz altında çöküklük, gölge varsa', 'Işık gölgeli bölgeyi öne çıkarır.'),
                  ('Hafif makyaj seviyorsan', 'Örtmeden canlı, uyanık bir görünüm.')]),
              ('DİKKAT', False, PINK, RED, [
                  ('Morluğun koyuysa', 'Açık ton gri gösterebilir. Şeftali ya da turuncu düzeltici daha iyi iş görür.'),
                  ('Şişlik ya da ince çizgi varsa', 'Parıltı, gizlemek istediğini öne çıkarabilir.')])]
    y = 210; st = 0.3
    for title, ok, tc, mc, items in groups:
        a = ease((t - st) / 0.45)
        text_a(c, (70, y), title, F(BOLD, 64), tc if ok else (255, 150, 160), a, int(20 * (1 - a)))
        y += 92; st += 0.3
        for head, body in items:
            k = back((t - st) / 0.4)
            mark(d, 102, y + 30, ok, mc, k)
            aa = ease((t - st - 0.1) / 0.45)
            text_a(c, (160, y + 4), head, F(BOLD, 40), CREAM, aa, int(16 * (1 - aa)))
            yy = y + 60
            for ln in wrap(F(REG, 32), body, W - 240):
                text_a(c, (160, yy), ln, F(REG, 32), PINK, aa); yy += 44
            y = yy + 26; st += 0.45
        y += 26
    eye(c, max(0, t - 1.8), 330, 1150, 0.6, CREAM, PLUM, BERRY)
    footer(c, 3, PINK)
    logo(c, 'B'); return c


# ---------- 4 · PUDRA USULÜ
def p4(t):
    c = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(c)
    blobs(c, t, PINK, (W - 90, 1160), 330)
    sticker(c, (W - 300, 110), 'DENEYECEKSEN', F(BOLD, 30), BERRY, CREAM, 5, back((t - 0.2) / 0.4))
    a = ease((t - 0.2) / 0.5); text_a(c, (70, 200), 'Pudra usulü', F(BOLD, 84), PLUM, a, int(24 * (1 - a)))
    a = ease((t - 0.4) / 0.5); text_a(c, (70, 296), '3 adım', F(ACC, 96), BERRY, a, int(24 * (1 - a)))
    steps = [('01', 'Önce nem', 'Kuru göz altında aydınlatıcı dokuyu büyütür.'),
             ('02', 'Minicik bir damla', 'İri sim değil, inci bitiş. Ton teninle aynı olsun.'),
             ('03', 'Kapatıcı en son', 'Sadece gereken yere, ince bir kat.')]
    y = 440
    for j, (n, h, b) in enumerate(steps):
        st = 0.8 + j * 0.5
        a = ease((t - st) / 0.45)
        text_a(c, (70 - int(40 * (1 - a)), y - 6), n, F(BOLD, 70), RED, a)
        text_a(c, (210, y), h, F(BOLD, 44), PLUM, a, int(16 * (1 - a)))
        yy = y + 58
        for ln in wrap(F(REG, 32), b, W - 290):
            text_a(c, (210, yy), ln, F(REG, 32), PLUM, a); yy += 44
        y = yy + 34
    pearl_vs_glitter(c, max(0, t - 2.2), W // 2, 1090)
    footer(c, 4, PLUM)
    logo(c, 'A'); return c


# ---------- 5 · SORU
def p5(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1220), 380)
    sparkle(d, 930, 300, 30 + 6 * math.sin(t * 4), PINK)
    for txt, font, y, st, col in [('Sen hangi', F(BOLD, 96), 210, 0.2, CREAM),
                                  ('takımdasın?', F(ACC, 120), 318, 0.5, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    opts = [('A', 'Aydınlatıcı takımı'), ('B', 'Kapatıcıdan vazgeçmem'), ('C', 'İkisi bir arada')]
    y = 540
    for k, (l, txt) in enumerate(opts):
        s = ease((t - 0.9 - k * 0.3) / 0.45)
        if s > 0:
            x = 70 - int(60 * (1 - s))
            d.rounded_rectangle([x, y, x + 760, y + 104], radius=52, fill=CREAM)
            d.ellipse([x + 14, y + 12, x + 94, y + 92], fill=PLUM)
            d.text((x + 54, y + 70), l, font=F(BOLD, 48), fill=CREAM, anchor='ms')
            d.text((x + 120, y + 70), txt, font=F(BOLD, 40), fill=PLUM, anchor='ls')
        y += 130
    sticker(c, (360, 1000), 'Harfini yorumlara yaz ›', F(BOLD, 42), PLUM, CREAM, -3,
            back((t - 2.0) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 36, 18)
    a = ease((t - 2.5) / 0.4)
    text_a(c, (72, 1110), 'Göz altı derdini bilen', F(BOLD, 40), CREAM, a)
    text_a(c, (72, 1162), 'arkadaşına gönder.', F(ACC, 52), PINK, a)
    eye(c, max(0, t - 1.4), 870, 1090, 0.5, CREAM, PLUM, BERRY, shadow=False)
    footer(c, 5, CREAM)
    logo(c, 'A'); return c


# ---------- STORY
def story(t):
    SW, SH = 1080, 1920
    c = Image.new('RGB', (SW, SH), BERRY); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 22; r = int(360 * ease(t / 0.8))
    d.ellipse([1080 - r - p, 1500 - r - p, 1080 + r + p, 1500 + r + p], fill=(120, 12, 60))
    dots(d, 800, 430, 5, 3, 44, 6, (180, 60, 110))
    sticker(c, (300, 420), 'PUDRA GÜNDEM', F(BOLD, 34), CREAM, BERRY, -5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Göz altına', F(BOLD, 104), 500, 0.3, CREAM),
                                  ('aydınlatıcı?', F(ACC, 128), 616, 0.55, PINK),
                                  ('Dene mi, deneme mi?', F(BOLD, 60), 820, 0.9, CREAM),
                                  ('Dürüst cevap hazır.', F(MED, 48), 900, 1.1, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    eye(c, max(0, t - 0.6), SW // 2, 1240, 1.15, CREAM, PLUM, BERRY)
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
