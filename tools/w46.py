"""46. hafta (11–15 Kasım 2026) story'leri."""
import os, sys, math
from anim import *
from pudra import fit
W, H = 1080, 1920
P = os.environ.get('PUDRA_PHOTOS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'photos') + '/')
_ph = {}
def photo(name):
    if name not in _ph: _ph[name] = load(P + name)
    return _ph[name]
def kb(name, box, t, zoom=0.07, cen=(0.5, 0.5)):
    w, h = box; z = 1 + zoom * min(t, 6) / 6
    im = fit(photo(name), (int(w * z), int(h * z)), cen)
    ox = (im.width - w) // 2; oy = (im.height - h) // 2
    return im.crop((ox, oy, ox + w, oy + h))
def rounded(im, r):
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width - 1, im.height - 1], radius=r, fill=255)
    out = Image.new('RGBA', im.size); out.paste(im, (0, 0), m); return out
def grad(c, top, h, col, amax):
    g = Image.new('L', (1, h))
    for i in range(h): g.putpixel((0, i), int(amax * (i / h) ** 1.5))
    g = g.resize((W, h)); solid = Image.new('RGB', (W, h), col)
    reg = c.crop((0, top, W, top + h)); c.paste(Image.composite(solid, reg, g), (0, top))
def blob(d, cx, cy, R, t, col, st=0.0):
    p = math.sin(t * 1.5) * 18; r = int(R * ease((t - st) / 0.8))
    if r > 0: d.ellipse([cx - r - p, cy - r - p, cx + r + p, cy + r + p], fill=col)
def lines_in(c, items, x, t0, step=0.3, anchor='la'):
    for j, (txt, font, y, col) in enumerate(items):
        a = ease((t - t0 - j * step) / 0.5) if False else None
def stack(c, t, items, x=70, t0=0.6, step=0.3, anchor='la'):
    for j, (txt, font, y, col) in enumerate(items):
        a = ease((t - t0 - j * step) / 0.5)
        text_a(c, (x, y), txt, font, col, a, int(45 * (1 - a)), anchor=anchor)
def cta(c, t, xy, txt, bg, fg, st, size=38, angle=0):
    a = ease((t - st) / 0.4)
    if a > 0: sticker(c, (xy[0] + int(7 * math.sin(t * 6)), xy[1]), txt, F(BOLD, size), bg, fg, angle, a, 38, 20)
def sparks(d, t, pts, col):
    for (x, y, r, st) in pts:
        k = back((t - st) / 0.4)
        if k > 0: sparkle(d, x, y, r * k * (1 + 0.12 * math.sin(t * 5 + x)), col)

# ---------- ortak kalıplar
def photo_story(t, name, cen, stk, stk_col, items, sub, cta_txt, lg='B', gtop=760):
    c = Image.new('RGB', (W, H), PLUM)
    c.paste(kb(name, (W, 1180), t, 0.08, cen), (0, 0))
    g = Image.new('L', (1, 560))
    for i in range(560): g.putpixel((0, i), int(255 * min(1, (i / 560) ** 0.8)))
    g = g.resize((W, 560)); reg = c.crop((0, 620, W, 1180))
    c.paste(Image.composite(Image.new('RGB', (W, 560), PLUM), reg, g), (0, 620))
    d = ImageDraw.Draw(c)
    y0 = items[0][2]
    sticker(c, (60 + F(BOLD, 32).getlength(stk) / 2 + 30, y0 - 70), stk, F(BOLD, 32), stk_col[0], stk_col[1], -5, back((t - 0.3) / 0.4))
    stack(c, t, items)
    if sub: text_a(c, (76, sub[1]), sub[0], F(MED, 40), CREAM, ease((t - 1.6) / 0.5))
    cta(c, t, (70 + F(BOLD, 38).getlength(cta_txt) / 2 + 38, 1600), cta_txt, CREAM, BERRY, 2.0)
    sparks(d, t, [(930, y0 + 60, 40, 1.3), (1000, y0 + 220, 24, 1.6)], PINK)
    logo(c, lg, True); return c

def duel(t, bg, circ, title, q, a_img, b_img, la, lb, cen=((0.5, 0.5), (0.5, 0.5)), txt=PLUM):
    c = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(c)
    blob(d, W // 2, 2080, 420, t, circ)
    dots(d, 760, 250, 6, 2, 44, 7, circ)
    text_a(c, (W // 2, 420), title, F(BOLD, 32), circ if circ != RED else RED, ease((t - 0.1) / 0.4), anchor='ms')
    a = ease((t - 0.3) / 0.5)
    text_a(c, (W // 2, 520), q, F(BOLD, 80), txt, a, int(30 * (1 - a)), anchor='ms')
    bw, bh = 470, 760
    for k, (name, lab, cap, x0, dr) in enumerate([(a_img, 'A', la, 50, -1), (b_img, 'B', lb, W - 50 - bw, 1)]):
        a = ease((t - 0.6 - k * 0.25) / 0.6)
        if a <= 0: continue
        im = rounded(kb(name, (bw, bh), t, 0.05, cen[k]), 36)
        x = int(x0 + dr * (1 - a) * 500); y = 610 + int(18 * math.sin(t * 2 + k))
        c.paste(im, (x, y), im)
        s = back((t - 1.3 - k * 0.2) / 0.4)
        if s > 0:
            cx = x + bw // 2; cy = y + bh - 10; rr = int(66 * s)
            d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=RED if k == 0 else PLUM)
            text_a(c, (cx, cy + 30 * s), lab, F(BOLD, int(84 * s) + 1), CREAM, 1, anchor='ms')
        text_a(c, (x + bw // 2, y + bh + 110), cap, F(BOLD, 36), txt, ease((t - 1.6 - k * 0.2) / 0.4), anchor='ms')
    text_a(c, (W // 2, 1575), 'A mı, B mi? Harfini yanıtla.', F(MED, 42), txt, ease((t - 2.2) / 0.5), anchor='ms')
    logo(c, 'B', True); return c

def truefalse(t, bg1, bg2, c1, c2, label, stmt, ans, body, fg1=CREAM):
    flip = t > 3.0
    c = Image.new('RGB', (W, H), bg2 if flip else bg1); d = ImageDraw.Draw(c)
    blob(d, W - 60, 380, 380, t, c2 if flip else c1)
    dots(d, 90, 1640, 6, 3, 46, 7, PINK if flip else c1)
    sticker(c, (W // 2, 580), label, F(BOLD, 32), PINK, PLUM, -4, back((t - 0.1) / 0.4))
    if not flip:
        for j, ln in enumerate(stmt):
            a = ease((t - 0.4 - j * 0.2) / 0.5); text_a(c, (W // 2, 820 + j * 125), ln, F(BOLD, 88), fg1, a, int(40 * (1 - a)), anchor='ms')
        a = ease((t - 1.3) / 0.4)
        text_a(c, (W // 2, 1270), 'Doğru mu, yanlış mı?', F(ACC, 78), PINK if fg1 == CREAM else BERRY, a, anchor='ms')
        k = t - 1.8
        if k > 0:
            cnt = 3 - int(k / 0.4)
            if cnt > 0: text_a(c, (W // 2, 1500), str(cnt), F(BOLD, 160), PINK if fg1 == CREAM else BERRY, 1, anchor='ms')
    else:
        k = back((t - 3.0) / 0.4)
        text_a(c, (W // 2, 860), ans, F(BOLD, int(170 * max(k, 0.01))), CREAM, 1, anchor='ms')
        a = ease((t - 3.4) / 0.5)
        for j, ln in enumerate(body):
            text_a(c, (W // 2, 1010 + j * 68), ln, F(MED, 46), CREAM, a, int(20 * (1 - a)), anchor='ms')
        cta(c, t, (W // 2, 1060 + len(body) * 68 + 90), 'Bilmeyen arkadaşına gönder ›', CREAM, bg2, 4.2)
    logo(c, 'B', True); return c

# ---------- Çarşamba 11
def w1(t):  # 10:30 Kırmızı bayrak carousel'ine yönlendirme
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blob(d, W - 20, 1560, 460, t, PLUM)
    r2 = int(230 * ease(t / 0.8)); d.ellipse([-80 - r2, 420 - r2, -80 + r2, 420 + r2], fill=(232, 80, 96))
    fy = int(1960 - 780 * ease((t - 0.5) / 0.9)); waving_flag(d, 680, fy, 380, t, CREAM, PLUM)
    sticker(c, (270, 540), 'KIRMIZI BAYRAK', F(BOLD, 32), CREAM, RED, -6, back((t - 0.2) / 0.4))
    stack(c, t, [('İlk buluşmada', F(BOLD, 96), 620, CREAM), ('5 kırmızı', F(ACC, 130), 745, PLUM), ('bayrak.', F(BOLD, 96), 905, CREAM)])
    text_a(c, (76, 1060), 'Görürsen kahveni bitirme, kalk.', F(MED, 42), CREAM, ease((t - 1.6) / 0.5))
    cta(c, t, (320, 1290), 'Yeni gönderi profilde ›', CREAM, RED, 2.0)
    logo(c, 'A', True); return c

def w2(t):  # 13:00 Doğru/yanlış — saç
    return truefalse(t, PINK, BERRY, BERRY, PLUM, 'SAÇ TESTİ', ['"Saçını sık kestir,', 'daha hızlı', 'uzasın."'], 'YANLIŞ!',
                     ['Saç kökten, folikülden uzar.', 'Uç kesimi hızı değiştirmez;', 'ama kırık uçları azaltır,', 'saç daha gür görünür.'], fg1=PLUM)

def sun(d, cx, cy, R, t, col, ray):
    k = ease(t / 0.8); r = R * k
    for i in range(12):
        a = t * 0.6 + i * math.pi / 6
        r1 = r * 1.25; r2 = r * (1.55 + 0.08 * math.sin(t * 4 + i))
        d.line([(cx + r1 * math.cos(a), cy + r1 * math.sin(a)), (cx + r2 * math.cos(a), cy + r2 * math.sin(a))], fill=ray, width=14)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)

def w3(t):  # 19:00 20'lere not — SPF
    c = Image.new('RGB', (W, H), BERRY); d = ImageDraw.Draw(c)
    blob(d, -40, 1700, 360, t, (168, 30, 90))
    sun(d, 820, 560, 150, t, (255, 196, 92), PINK)
    sticker(c, (230, 800), "20'LERE NOT", F(BOLD, 32), PINK, PLUM, -6, back((t - 0.3) / 0.4))
    stack(c, t, [('En ucuz', F(BOLD, 110), 860, CREAM), ('anti-aging:', F(ACC, 120), 990, PINK), ('güneş kremi.', F(BOLD, 110), 1140, CREAM)])
    a = ease((t - 1.7) / 0.5)
    for j, ln in enumerate(['Cilt yaşlanmasının görünen izlerinin', 'çoğu güneşten gelir. Her sabah,', 'kışın da: SPF 30+.']):
        text_a(c, (76, 1320 + j * 58), ln, F(MED, 40), CREAM, a)
    cta(c, t, (390, 1560), "Kaydet, 30'larında teşekkür edersin", CREAM, BERRY, 2.3, 32)
    logo(c, 'A', True); return c

# ---------- Perşembe 12
def t1(t):  # 10:30 Reels yönlendirme
    return photo_story(t, 'kombin/IMG_4187.jpg', (0.5, 0.3), 'YENİ REELS', (RED, CREAM),
                       [('Giymek', F(BOLD, 130), 1040, CREAM), ('vs. stil', F(ACC, 130), 1175, PINK), ('vermek.', F(BOLD, 130), 1320, CREAM)],
                       ('Aynı tişört, aynı jean. Fark detayda.', 1495), 'Profilde izle ›', gtop=560)

def t2(t):  # 13:00 Çanta düellosu
    return duel(t, PINK, BERRY, 'ÇANTA DÜELLOSU', 'Sonbaharda hangisi?', 'canta/IMG_4241.jpg', 'canta/IMG_4239.jpg', 'Bordo klasik', 'Pastel sürpriz')

def clock(d, cx, cy, R, t, face, hand):
    k = back(t / 0.6); r = R * max(k, 0)
    if r <= 2: return
    d.ellipse([cx - r - 14, cy - r - 14, cx + r + 14, cy + r + 14], fill=hand)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=face)
    for i in range(12):
        a = i * math.pi / 6; d.ellipse([cx + 0.82 * r * math.cos(a) - 6, cy + 0.82 * r * math.sin(a) - 6, cx + 0.82 * r * math.cos(a) + 6, cy + 0.82 * r * math.sin(a) + 6], fill=hand)
    p = ease((t - 0.4) / 1.6)
    m = 45 * p; hh = 7 + 45 / 60 * p  # 7:00 → 7:45
    am = math.radians(m * 6 - 90); ah = math.radians((hh % 12) * 30 - 90)
    d.line([(cx, cy), (cx + 0.5 * r * math.cos(ah), cy + 0.5 * r * math.sin(ah))], fill=hand, width=16)
    d.line([(cx, cy), (cx + 0.72 * r * math.cos(am), cy + 0.72 * r * math.sin(am))], fill=RED, width=10)
    d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=hand)

def t3(t):  # 19:00 30'lara not — sabah 7:45 formu
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blob(d, W + 40, 1700, 420, t, BERRY)
    clock(d, 810, 560, 170, t, CREAM, PLUM)
    sticker(c, (230, 790), "30'LARA NOT", F(BOLD, 32), PINK, PLUM, -6, back((t - 0.3) / 0.4))
    stack(c, t, [('Sabah 7:45', F(BOLD, 112), 850, CREAM), ('formu.', F(ACC, 120), 985, PINK)])
    steps = ['Yüzü yıka, nemlendir', 'SPF 30+ (bulut olsa da)', 'Maskara + krem allık']
    for j, s in enumerate(steps):
        k = back((t - 1.4 - j * 0.3) / 0.4); a = ease((t - 1.4 - j * 0.3) / 0.4)
        y = 1180 + j * 100
        if k > 0:
            rr = int(36 * k); d.ellipse([110 - rr, y + 30 - rr, 110 + rr, y + 30 + rr], fill=PINK)
            text_a(c, (110, y + 30), str(j + 1), F(BOLD, 40), PLUM, 1, anchor='mm')
        text_a(c, (172, y + 30), s, F(MED, 46), CREAM, a, anchor='lm')
    text_a(c, (76, 1500), 'Toplam 5 dakika. Gün boyu derli toplu.', F(MED, 36), PINK, ease((t - 2.5) / 0.5))
    cta(c, t, (300, 1595), 'Kaydet, yarın dene ›', CREAM, BERRY, 2.8, 34)
    logo(c, 'B', True); return c

# ---------- Cuma 13
def f1(t):  # 10:30 Sokak carousel'ine yönlendirme
    return photo_story(t, 'ayakkabi/IMG_4226.jpg', (0.5, 0.35), 'YENİ GÖNDERİ', (PINK, PLUM),
                       [('Sokağın', F(BOLD, 130), 1040, CREAM), ('yazılı olmayan', F(ACC, 105), 1180, PINK), ('5 kuralı.', F(BOLD, 130), 1300, CREAM)],
                       ("20'sinde de, 50'sinde de işe yarar.", 1495), 'Kaydır, kuralını seç ›', gtop=560)

def f2(t):  # 13:00 Doğru/yanlış — gözenek
    return truefalse(t, PLUM, BERRY, BERRY, PLUM, 'CİLT BAKIMI TESTİ', ['"Sıcak su gözeneği', 'açar, soğuk su', 'kapatır."'], 'YANLIŞ!',
                     ['Gözeneklerin kası yok;', 'açılıp kapanamazlar.', 'Ilık suyla yıka, düzenli temizle:', 'tıkanmayan gözenek az görünür.'])

def f3(t):  # 19:00 40'lara not — boyun ve eller
    c = Image.new('RGB', (W, H), PINK); d = ImageDraw.Draw(c)
    blob(d, W + 30, 330, 400, t, BERRY)
    dots(d, 90, 1650, 6, 3, 46, 7, BERRY)
    sticker(c, (230, 560), "40'LARA NOT", F(BOLD, 32), PLUM, CREAM, -6, back((t - 0.2) / 0.4))
    stack(c, t, [('Boyun ve', F(BOLD, 112), 620, PLUM), ('eller de', F(BOLD, 112), 750, PLUM), ('yüzün devamı.', F(ACC, 110), 885, BERRY)], t0=0.5)
    # üç bölge: yüz → boyun → el sırtı, dalga çizgisiyle bağlı
    xs = [200, 540, 880]; y = 1180
    p = ease((t - 1.5) / 1.0)
    if p > 0: wave_line(d, xs[0], xs[0] + (xs[2] - xs[0]) * p, y, 18, 170, BERRY, 8, t * 2)
    for j, lab in enumerate(['Yüz', 'Boyun', 'El sırtı']):
        k = back((t - 1.5 - j * 0.35) / 0.4)
        if k > 0:
            rr = int(70 * k * (1 + 0.05 * math.sin(t * 4 + j)))
            d.ellipse([xs[j] - rr, y - rr, xs[j] + rr, y + rr], fill=PLUM if j == 0 else RED)
            sparkle(d, xs[j], y, 30 * k, CREAM)
            text_a(c, (xs[j], y + 130), lab, F(BOLD, 40), PLUM, ease((t - 1.7 - j * 0.35) / 0.4), anchor='ms')
    a = ease((t - 2.6) / 0.5)
    for j, ln in enumerate(['Nemlendirici ve SPF çenede bitmesin:', 'boyna, dekolteye, el sırtına da.']):
        text_a(c, (W // 2, 1420 + j * 58), ln, F(MED, 40), PLUM, a, anchor='ms')
    cta(c, t, (W // 2, 1600), 'Kaydet, akşam rutinine ekle ›', BERRY, CREAM, 3.0, 34)
    logo(c, 'B', True); return c

# ---------- Cumartesi 14
def s1(t):  # 10:30 Reels teaser (11:00)
    return photo_story(t, 'ayakkabi/IMG_4228.jpg', (0.5, 0.4), "SAAT 11:00'DE", (RED, CREAM),
                       [('Topuklar', F(BOLD, 150), 1060, CREAM), ('bizde.', F(ACC, 160), 1220, PINK)],
                       ('Yeni Reels bugün profilde.', 1470), 'Takip et, kaçırma ›', gtop=600)

def heart(d, cx, cy, s, col):
    pts = []
    for i in range(60):
        a = 2 * math.pi * i / 60
        x = 16 * math.sin(a) ** 3; y = 13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)
        pts.append((cx + x * s / 16, cy - y * s / 16))
    d.polygon(pts, fill=col)

def s2(t):  # 13:00 Günün sorusu — ilişki
    c = Image.new('RGB', (W, H), BERRY); d = ImageDraw.Draw(c)
    blob(d, W - 40, 1620, 430, t, RED)
    k = back((t - 0.2) / 0.5)
    if k > 0: heart(d, 860, 470, 120 * k * (1 + 0.08 * abs(math.sin(t * 4))), PINK)
    sticker(c, (260, 560), 'GÜNÜN SORUSU', F(BOLD, 32), PINK, PLUM, -6, back((t - 0.2) / 0.4))
    stack(c, t, [('Seni en çok', F(BOLD, 100), 630, CREAM), ('ne etkiler?', F(ACC, 120), 760, PINK)], t0=0.4)
    opts = ['Gün ortası "nasılsın" mesajı', 'Habersiz küçük bir sürpriz', 'Telefonu bırakıp dinlemesi']
    for j, o in enumerate(opts):
        a = ease((t - 1.2 - j * 0.3) / 0.5);
        if a <= 0: continue
        y = 1000 + j * 150; x = 80 + int((1 - a) * -400)
        d.rounded_rectangle([x, y, x + 920, y + 116], radius=58, fill=CREAM)
        d.ellipse([x + 16, y + 16, x + 100, y + 100], fill=RED if j != 1 else PLUM)
        text_a(c, (x + 58, y + 58), 'ABC'[j], F(BOLD, 44), CREAM, 1, anchor='mm')
        text_a(c, (x + 128, y + 58), o, F(BOLD, 38), PLUM, 1, anchor='lm')
    cta(c, t, (W // 2, 1540), 'Harfini yanıtla, anonim paylaşalım', CREAM, BERRY, 2.4, 32)
    logo(c, 'A', True); return c

# ---------- Pazar 15
def u1(t):  # 10:30 Hafta sonu manifestosu — 50+
    return photo_story(t, 'kombin/IMG_4183.jpg', (0.5, 0.25), 'HAFTA SONU MANİFESTOSU', (PINK, PLUM),
                       [('Kural yok,', F(BOLD, 140), 1060, CREAM), ('Pudra var.', F(ACC, 150), 1220, PINK)],
                       ("50'sinde deri ceket mi? Neden olmasın.", 1470), 'Annene, teyzene gönder ›', gtop=560)

def u2(t):  # 13:00 Manikür düellosu
    return duel(t, CREAM, RED, 'MANİKÜR DÜELLOSU', 'Bu haftanın rengi?', 'tirnak/IMG_4161.jpg', 'tirnak/IMG_4159.jpg', 'Krom kahve', 'Adaçayı yeşili',
                cen=((0.5, 0.45), (0.45, 0.5)))

def u3(t):  # 19:00 Editörün stili (Eliz'in fotoğrafı)
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blob(d, -120, 560, 400, t, BERRY)
    a = ease((t - 0.2) / 0.6)
    if a > 0:
        im = rounded(kb('kisisel/IMG_2991.jpg', (640, 860), t, 0.06, (0.5, 0.55)), 40)
        c.paste(im, (W - 700 + int((1 - a) * 300), 330), im)
    sticker(c, (250, 1250), 'EDİTÖRÜN STİLİ', F(BOLD, 30), PINK, PLUM, -6, back((t - 0.5) / 0.4))
    stack(c, t, [('Çizgili', F(BOLD, 100), 1300, CREAM), ('geniş paça', F(ACC, 100), 1415, PINK), ('+ sivri bot.', F(BOLD, 100), 1530, CREAM)], t0=0.9)
    sparks(d, t, [(960, 1290, 44, 2.0)], PINK)
    cta(c, t, (W - 330, 1250 - 60), 'Yarın ne giyiyorsun?', CREAM, BERRY, 2.3, 34, 4)
    logo(c, 'B', True); return c

fns = dict(w1=w1, w2=w2, w3=w3, t1=t1, t2=t2, t3=t3, f1=f1, f2=f2, f3=f3, s1=s1, s2=s2, u1=u1, u2=u2, u3=u3)
DATES = dict(w='1111', t='1112', f='1113', s='1114', u='1115')
SLOT = {'1': '1030', '2': '1300', '3': '1900'}
if __name__ == '__main__':
    arg = sys.argv[1]
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '2026-11')
    if arg == 'preview':
        tt = float(sys.argv[2]) if len(sys.argv) > 2 else 4.8
        sh = Image.new('RGB', (7 * 275 + 5, 2 * 490 + 5), 'white')
        for k, (n, fn) in enumerate(fns.items()):
            sh.paste(fn(tt).resize((270, 480)), (5 + (k % 7) * 275, 5 + (k // 7) * 490))
        sh.save(sys.argv[3] if len(sys.argv) > 3 else 'rev.jpg', quality=85)
    elif arg == 'frame':
        fns[sys.argv[2]](float(sys.argv[3])).save(sys.argv[4], quality=88)
    else:
        for n in arg.split(','):
            render(fns[n], f'{out}/{DATES[n[0]]}_story_{SLOT[n[1]]}.mp4', 6, (W, H))
            print('ok', n, flush=True)
