"""PUDRA GÜNDEM — Buz gibi sarı bitti, bu kış saçlar ısınıyor (25 Kasım 2026; yayın 1 Aralık 18:00).
Kaynaklar: Who What Wear (18 Kasım 2026, Kaitlyn McLintock; Jerome Lordet, Erin Bowers),
Who What Wear UK (18 Kasım 2026, Eleanor Vousden; Hershesons, Nicola Clarke),
HOLA! USA (5 Kasım 2026, Shirley Gomez)."""
from anim import *
from PIL import ImageFilter
import sys, os
W, H = 1080, 1350
OUT = 'out_1125'; os.makedirs(OUT, exist_ok=True)

SKIN = (242, 204, 182)
SKIN_D = (226, 180, 156)
ICE = (222, 226, 236)
ESP = (66, 38, 28); ESP_L = (112, 70, 46)
HONEY = (220, 166, 86); HONEY_L = (244, 206, 140)
WINE = (112, 20, 48); WINE_L = (164, 46, 80)
CUP = (250, 244, 240)
SHADES = {'ice': (ICE, (246, 248, 252)), 'esp': (ESP, ESP_L), 'honey': (HONEY, HONEY_L), 'wine': (WINE, WINE_L)}


def lerp(a, b, u):
    return tuple(int(a[i] + (b[i] - a[i]) * u) for i in range(3))


def cycle_col(t, seq=('ice', 'esp', 'honey', 'wine'), hold=1.1, fade=0.4, light=False):
    per = hold + fade; n = len(seq)
    k = int(t // per) % n; u = (t % per - hold) / fade
    a = SHADES[seq[k]][1 if light else 0]; b = SHADES[seq[(k + 1) % n]][1 if light else 0]
    return a if u <= 0 else lerp(a, b, min(1, u))


def lock(c, t, cx, top, L, w, shade, k=1.0, seed=0):
    """Dalgalı saç tutamı + üstte tel toka."""
    if k <= 0.02: return
    L = L * k; w = w * k
    base, light = SHADES[shade] if isinstance(shade, str) else shade
    lay = Image.new('RGBA', (int(w * 3), int(L + 60)), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    ox = w * 1.5
    n = 9
    for j in range(n):
        u = j / (n - 1) - 0.5
        col = lerp(base, light, 0.5 + 0.5 * math.sin(j * 1.9 + seed))
        pts = []
        for y in range(0, int(L), 6):
            v = y / L
            amp = w * 0.16 * (0.3 + v)
            x = ox + u * w * (1 - 0.55 * v) + amp * math.sin(v * 7.5 + t * 2.4 + seed + j * 0.15)
            pts.append((x, y + 30))
        d.line(pts, fill=col, width=max(2, int(w / n * 1.7)), joint='curve')
    # parlak tel
    pts = [(ox - w * 0.12 + w * 0.12 * math.sin(y / L * 7.5 + t * 2.4 + seed), y + 30) for y in range(0, int(L * 0.7), 6)]
    if len(pts) > 1: d.line(pts, fill=lerp(light, (255, 255, 255), 0.45), width=max(2, int(w * 0.06)), joint='curve')
    d.rounded_rectangle([ox - w * 0.62, 14, ox + w * 0.62, 50], radius=16, fill=(212, 180, 120))
    d.rounded_rectangle([ox - w * 0.5, 22, ox + w * 0.5, 30], radius=4, fill=(246, 226, 180))
    c.paste(lay, (int(cx - ox), int(top)), lay)


def head(c, t, cx, cy, s, hair, hair_l, k=1.0):
    """Stilize kadın portresi: uzun dalgalı saç, yüz, omuz."""
    if k <= 0.02: return
    s = s * k
    d = ImageDraw.Draw(c)
    sway = math.sin(t * 1.8) * 10 * s
    # arka saç
    d.ellipse([cx - 230 * s, cy - 300 * s, cx + 230 * s, cy + 150 * s], fill=hair)
    for side in (-1, 1):
        pts = [(cx + side * 120 * s, cy - 120 * s)]
        for y in range(0, 470, 20):
            v = y / 470
            pts.append((cx + side * (210 * s + 26 * s * math.sin(v * 9 + t * 2.2)) + sway * v, cy - 100 * s + y * s))
        pts += [(cx + side * 60 * s + sway, cy + 380 * s), (cx + side * 60 * s, cy - 120 * s)]
        d.polygon(pts, fill=hair)
    # boyun + omuz
    d.rounded_rectangle([cx - 52 * s, cy + 40 * s, cx + 52 * s, cy + 200 * s], radius=int(30 * s), fill=SKIN_D)
    d.ellipse([cx - 290 * s, cy + 170 * s, cx + 290 * s, cy + 560 * s], fill=CREAM if hair != CREAM else PINK)
    d.rounded_rectangle([cx - 52 * s, cy + 120 * s, cx + 52 * s, cy + 190 * s], radius=int(24 * s), fill=SKIN_D)
    # ön saç tutamları omuz üstünde
    for side in (-1, 1):
        pts = []
        for y in range(0, 300, 15):
            v = y / 300
            pts.append((cx + side * (150 * s + 18 * s * math.sin(v * 8 + t * 2.4 + side)) + sway * v, cy + y * s))
        d.line(pts, fill=hair, width=int(70 * s), joint='curve')
    # yüz
    d.ellipse([cx - 120 * s, cy - 170 * s, cx + 120 * s, cy + 110 * s], fill=SKIN)
    # perçem
    d.chord([cx - 140 * s, cy - 230 * s, cx + 150 * s, cy - 10 * s], 180, 360, fill=hair)
    d.ellipse([cx - 10 * s, cy - 200 * s, cx + 150 * s, cy - 60 * s], fill=hair)
    # parlama
    d.arc([cx - 190 * s, cy - 270 * s, cx + 80 * s, cy + 20 * s], 200, 250, fill=hair_l, width=int(14 * s))
    # yüz detay
    blink = 1 if (t % 3.2) > 0.12 else 0.15
    for ex in (-48, 48):
        d.ellipse([cx + ex * s - 9 * s, cy - 20 * s - 9 * s * blink, cx + ex * s + 9 * s, cy - 20 * s + 9 * s * blink], fill=PLUM)
    d.ellipse([cx - 86 * s, cy + 14 * s, cx - 50 * s, cy + 36 * s], fill=(240, 168, 170))
    d.ellipse([cx + 50 * s, cy + 14 * s, cx + 86 * s, cy + 36 * s], fill=(240, 168, 170))
    d.arc([cx - 26 * s, cy + 26 * s, cx + 26 * s, cy + 62 * s], 20, 160, fill=RED, width=int(7 * s))


def coffee(c, t, cx, cy, s, k=1.0):
    if k <= 0.02: return
    s = s * k; d = ImageDraw.Draw(c)
    d.ellipse([cx - 150 * s, cy + 60 * s, cx + 150 * s, cy + 110 * s], fill=(226, 214, 210))
    d.rounded_rectangle([cx - 100 * s, cy - 60 * s, cx + 100 * s, cy + 90 * s], radius=int(46 * s), fill=CUP)
    d.ellipse([cx + 70 * s, cy - 30 * s, cx + 150 * s, cy + 50 * s], outline=CUP, width=int(18 * s))
    d.ellipse([cx - 92 * s, cy - 76 * s, cx + 92 * s, cy - 44 * s], fill=ESP)
    for j in range(3):
        x0 = cx + (j - 1) * 44 * s
        pts = [(x0 + 12 * s * math.sin(y / 30 + t * 3 + j), cy - 90 * s - y * s) for y in range(0, 150, 6)]
        ph = (t * 0.8 + j * 0.3) % 1
        d.line(pts[:max(2, int(len(pts) * (0.4 + 0.6 * ph)))], fill=(255, 255, 255), width=int(8 * s), joint='curve')


def honey(c, t, cx, cy, s, k=1.0):
    if k <= 0.02: return
    s = s * k; d = ImageDraw.Draw(c)
    # kavanoz
    d.rounded_rectangle([cx - 110 * s, cy - 70 * s, cx + 110 * s, cy + 140 * s], radius=int(40 * s), fill=HONEY)
    d.rounded_rectangle([cx - 120 * s, cy - 100 * s, cx + 120 * s, cy - 60 * s], radius=int(14 * s), fill=(160, 100, 60))
    d.rounded_rectangle([cx - 84 * s, cy - 40 * s, cx - 60 * s, cy + 100 * s], radius=int(10 * s), fill=HONEY_L)
    # kepçe + damla
    d.line([(cx + 30 * s, cy - 260 * s), (cx + 30 * s, cy - 150 * s)], fill=(160, 100, 60), width=int(14 * s))
    for j in range(3):
        d.ellipse([cx - 10 * s, cy - 160 * s + j * 24 * s, cx + 70 * s, cy - 136 * s + j * 24 * s], fill=(190, 126, 70))
    ph = (t * 0.7) % 1
    dy = ph * 160 * s
    r = 14 * s * (0.6 + 0.4 * ph)
    d.line([(cx + 30 * s, cy - 90 * s), (cx + 30 * s, cy - 90 * s + dy * 0.6)], fill=HONEY, width=int(10 * s))
    d.ellipse([cx + 30 * s - r, cy - 90 * s + dy - r, cx + 30 * s + r, cy - 90 * s + dy + r * 1.3], fill=HONEY)


def berries(c, t, cx, cy, s, k=1.0):
    if k <= 0.02: return
    s = s * k; d = ImageDraw.Draw(c)
    for j, (dx, dy, R) in enumerate([(-70, 30, 70), (60, 50, 62), (-5, -40, 56)]):
        b = math.sin(t * 2.6 + j * 1.4) * 8 * s
        x, y = cx + dx * s, cy + dy * s + b
        d.line([(x, y - R * s), (x + 30 * s, y - R * s - 90 * s)], fill=(70, 110, 70), width=int(9 * s))
        d.ellipse([x - R * s, y - R * s, x + R * s, y + R * s], fill=WINE)
        d.ellipse([x - R * 0.55 * s, y - R * 0.6 * s, x - R * 0.15 * s, y - R * 0.2 * s], fill=WINE_L)
    d.ellipse([cx + 10 * s, cy - 200 * s, cx + 120 * s, cy - 150 * s], fill=(90, 150, 90))


def blobs(c, t, col, pos=(W - 110, 1120), R=380):
    d = ImageDraw.Draw(c); s = ease(t / 0.7); p = math.sin(t * 1.4) * 14
    r = int(R * s); d.ellipse([pos[0] - r - p, pos[1] - r - p, pos[0] + r + p, pos[1] + r + p], fill=col)


def footer(c, i, col):
    text_a(c, (70, 1290), 'PUDRA DERGİ', F(BOLD, 22), col, 1)
    text_a(c, (W - 70, 1288), f'{i}/5', F(MED, 24), col, 1, anchor='ra')


# ---------- 1 · KAPAK
def p1(t):
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1140), 450)
    dots(d, 860, 230, 4, 3, 44, 6, (90, 50, 72))
    sticker(c, (370, 250), 'PUDRA GÜNDEM · SAÇ', F(BOLD, 30), PINK, PLUM, -4, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Buz gibi sarı', F(BOLD, 108), 316, 0.3, CREAM),
                                  ('bitti.', F(BOLD, 108), 436, 0.5, CREAM),
                                  ('Bu kış saçlar ısınıyor.', F(ACC, 80), 566, 0.75, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(36 * (1 - a)))
    a = ease((t - 1.3) / 0.5)
    text_a(c, (70, 700), 'Londra ve New York kuaförleri', F(MED, 36), CREAM, a)
    text_a(c, (70, 750), 'aynı şeyi söylüyor: 3 sıcak ton.', F(MED, 36), CREAM, a)
    head(c, t, 770, 1050, 0.62, cycle_col(t), cycle_col(t, light=True))
    a = ease((t - 2.0) / 0.4)
    if a > 0:
        sticker(c, (190, 930), 'Kaydet', F(BOLD, 42), RED, CREAM, -6, back((t - 2.0) / 0.4), 34, 14)
        text_a(c, (70 + int(8 * math.sin(t * 6)), 1230), 'kaydır  ›', F(BOLD, 38), CREAM, a)
    sparkle(d, 330, 1080, 24 + 6 * math.sin(t * 4), PINK)
    sparkle(d, 1000, 640, 18 + 5 * math.sin(t * 5 + 1), CREAM)
    logo(c, 'A'); return c


def trend_page(t, i, bg, blob, ink, accent, tag, tagbg, tagfg, t1, t2, body, tip, shade, illus, logo_v):
    c = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(c)
    blobs(c, t, blob, (W - 80, 1210), 320)
    sticker(c, (W - 290, 110), tag, F(BOLD, 30), tagbg, tagfg, 5, back((t - 0.2) / 0.4))
    a = ease((t - 0.25) / 0.5); text_a(c, (70, 200), t1, F(BOLD, 90), ink, a, int(28 * (1 - a)))
    a = ease((t - 0.45) / 0.5); text_a(c, (70, 300), t2, F(ACC, 96), accent, a, int(28 * (1 - a)))
    a = ease((t - 0.9) / 0.5); y = 450
    for ln in wrap(F(REG, 34), body, 600):
        text_a(c, (72, y), ln, F(REG, 34), ink, a); y += 48
    # Pudra kutusu
    k = back((t - 1.5) / 0.5)
    if k > 0.02:
        lines = wrap(F(MED, 33), tip, 560)
        bh = 90 + len(lines) * 46
        box = Image.new('RGBA', (640, bh + 10), (0, 0, 0, 0)); bd = ImageDraw.Draw(box)
        bd.rounded_rectangle([0, 0, 630, bh], radius=34, fill=tagbg)
        bd.text((34, 28), 'PUDRA DİYOR Kİ', font=F(BOLD, 26), fill=accent if tagbg != accent else tagfg)
        yy = 70
        for ln in lines: bd.text((34, yy), ln, font=F(MED, 33), fill=tagfg); yy += 46
        if k != 1: box = box.resize((max(1, int(640 * k)), max(1, int((bh + 10) * k))))
        c.paste(box, (66, y + 30), box)
    lock(c, t, 870, 400, 700, 180, shade, back((t - 0.6) / 0.6), seed=i)
    illus(c, t, 330, 1170, 0.85, back((t - 1.9) / 0.5))
    footer(c, i, ink)
    logo(c, logo_v); return c


def p2(t):
    return trend_page(t, 2, PINK, (236, 170, 192), PLUM, BERRY, 'TREND 1 · ESMER', PLUM, CREAM,
                      'Espresso', 'esmer.',
                      'Koyu kahveyle çikolata arası, parlak ve sıcak bir esmer. Kuaförlere göre soğuk, küllü kahveler yerini bu derinliğe bırakıyor.',
                      'Zaten esmersen boyaya gerek yok. Şeffaf bir parlatıcı (gloss) bu etkiyi verir.',
                      'esp', coffee, 'B')


def p3(t):
    return trend_page(t, 3, PLUM, BERRY, CREAM, HONEY_L, 'TREND 2 · SARI', HONEY, PLUM,
                      'Tereyağı', 'sarısı.',
                      'Buz gibi platin geri çekiliyor. Yerine bal, tereyağı ve sıcak bej tonlarında daha yumuşak, daha doğal bir sarı geliyor.',
                      'Kökleri biraz koyu bırak. Uzadıkça kaçmış değil, bilerek yapılmış gibi durur.',
                      'honey', honey, 'A')


def p4(t):
    return trend_page(t, 4, CREAM, PINK, PLUM, WINE, 'TREND 3 · KIZIL', WINE, CREAM,
                      'Şarap', 'kızılı.',
                      'Bakırın yerini şarap, mürdüm ve erik alıyor. Işıkta kırmızı-mor parlayan koyu, sıcak bir kızıl.',
                      'İlk kez deneyeceksen yarı kalıcı boyayla başla. Beğenmezsen yıkandıkça açılır.',
                      'wine', berries, 'B')


# ---------- 5 · SORU
def p5(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1220), 380)
    sparkle(d, 950, 300, 30 + 6 * math.sin(t * 4), PINK)
    for txt, font, y, st, col in [('Bu kış', F(BOLD, 96), 200, 0.2, CREAM),
                                  ('saçında', F(BOLD, 96), 306, 0.35, CREAM),
                                  ('hangisi?', F(ACC, 120), 410, 0.5, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    opts = [('A', 'Espresso esmer', 'esp'), ('B', 'Tereyağı sarısı', 'honey'),
            ('C', 'Şarap kızılı', 'wine'), ('D', 'Buz sarıdan vazgeçmem', 'ice')]
    y = 590
    for k, (l, txt, sh) in enumerate(opts):
        s = ease((t - 0.9 - k * 0.25) / 0.45)
        if s > 0:
            x = 70 - int(60 * (1 - s))
            d.rounded_rectangle([x, y, x + 640, y + 88], radius=44, fill=CREAM)
            d.ellipse([x + 10, y + 8, x + 86, y + 84], fill=PLUM)
            d.text((x + 48, y + 64), l, font=F(BOLD, 44), fill=CREAM, anchor='ms')
            d.text((x + 108, y + 61), txt, font=F(BOLD, 34), fill=PLUM, anchor='ls')
            d.ellipse([x + 578, y + 20, x + 626, y + 68], fill=SHADES[sh][0], outline=PLUM if sh == 'ice' else None, width=2)
        y += 100
    sticker(c, (330, 1050), 'Harfini yorumlara yaz ›', F(BOLD, 40), PLUM, CREAM, -3,
            back((t - 2.0) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 34, 18)
    a = ease((t - 2.5) / 0.4)
    text_a(c, (72, 1122), 'Kuaför arkadaşına', F(BOLD, 40), CREAM, a)
    text_a(c, (72, 1172), 'gönder.', F(ACC, 52), PINK, a)
    if t > 0.8:
        head(c, t - 0.8, 900, 1010, 0.4, cycle_col(t, ('esp', 'honey', 'wine')), cycle_col(t, ('esp', 'honey', 'wine'), light=True),
             k=back((t - 0.8) / 0.5))
    footer(c, 5, CREAM)
    logo(c, 'A'); return c


# ---------- STORY
def story(t):
    SW, SH = 1080, 1920
    c = Image.new('RGB', (SW, SH), BERRY); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 22; r = int(440 * ease(t / 0.8))
    d.ellipse([1080 - r - p, 1400 - r - p, 1080 + r + p, 1400 + r + p], fill=(120, 12, 60))
    dots(d, 820, 430, 5, 3, 44, 6, (180, 60, 110))
    sticker(c, (300, 420), 'PUDRA GÜNDEM', F(BOLD, 34), CREAM, BERRY, -5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Buz gibi sarı', F(BOLD, 108), 500, 0.3, CREAM),
                                  ('bitti.', F(BOLD, 108), 620, 0.5, CREAM),
                                  ('Bu kış saçlar ısınıyor.', F(ACC, 76), 752, 0.75, PINK),
                                  ('+ kuaförlerin 3 sıcak tonu', F(MED, 46), 880, 1.1, CREAM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    head(c, t, SW // 2 + 60, 1250, 0.7, cycle_col(t, ('ice', 'esp', 'honey', 'wine')), cycle_col(t, light=True))
    for j, sh in enumerate(['esp', 'honey', 'wine']):
        k = back((t - 1.2 - j * 0.2) / 0.4)
        if k > 0.02:
            R = 34 * k; x = 100 + j * 90; y = 1010
            d.ellipse([x - R, y - R, x + R, y + R], fill=SHADES[sh][0], outline=CREAM, width=4)
    s2 = back((t - 2.2) / 0.45)
    if s2 > 0: sticker(c, (SW // 2 + int(8 * math.sin(t * 6)), 1600), 'Yeni gönderide ›', F(BOLD, 46), PLUM, CREAM, -2, s2, 42, 22)
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
