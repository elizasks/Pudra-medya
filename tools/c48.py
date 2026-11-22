"""48. hafta carousel'leri: KANDIRILMAMAK İÇİN cilt mitleri (25 Kasım), YAŞ KÖŞESİ Black Friday (27 Kasım)."""
from c47 import *
import sys, os
BLACK = (22, 14, 18); GOLD = (255, 196, 92); ORANGE = (255, 150, 60)


# ================== ILLÜSTRASYONLAR — mitler
def ill_foam(c, t, cx, cy):
    d = ImageDraw.Draw(c)
    # tüp
    x = cx - 200
    lay = Image.new('RGBA', (220, 420), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.polygon([(20, 0), (200, 0), (170, 330), (50, 330)], fill=CREAM)
    ld.rounded_rectangle([60, 330, 160, 410], radius=14, fill=BERRY)
    ld.rectangle([60, 120, 160, 200], fill=PINK)
    lay = lay.rotate(180 + 10 * math.sin(t * 2), expand=True, resample=Image.BICUBIC)
    c.paste(lay, (int(x - lay.width / 2), int(cy - 120 - lay.height / 2)), lay)
    for j in range(14):
        p = ((t * 0.45 + j * 0.071) % 1.0)
        bx = x + 60 + (j * 61) % 260 + 20 * math.sin(t * 2 + j); by = cy + 160 - p * 420; r = 18 + (j % 4) * 10
        d.ellipse([bx - r, by - r, bx + r, by + r], outline=BERRY, width=5)
    stamp(c, t - 1.2, cx + 200, cy - 40, 'TEMİZLİK ÖLÇÜSÜ DEĞİL', RED)


def ill_pimple(c, t, cx, cy):
    d = ImageDraw.Draw(c)
    x = cx - 150
    d.ellipse([x - 190, cy - 190, x + 190, cy + 190], fill=(236, 196, 166))
    pul = 1 + 0.1 * math.sin(t * 6)
    d.ellipse([x - 40 * pul, cy - 40 * pul, x + 40 * pul, cy + 40 * pul], fill=(222, 120, 120))
    d.ellipse([x - 14, cy - 14, x + 14, cy + 14], fill=CREAM)
    k = back((t - 0.6) / 0.4)
    if k > 0:
        r = 120 * k
        d.ellipse([x - r, cy - r, x + r, cy + r], outline=RED, width=int(22 * k) + 1)
        d.line([(x - r * 0.7, cy + r * 0.7), (x + r * 0.7, cy - r * 0.7)], fill=RED, width=int(22 * k) + 1)
    bubble(c, cx + 220, cy - 80, 'Dokunma!', F(BOLD, 40), RED, CREAM, back((t - 1.1) / 0.4), -4)
    bubble(c, cx + 230, cy + 70, 'İz bırakır.', F(BOLD, 34), CREAM, PLUM, back((t - 1.5) / 0.4), 3, 'right')


def jar(d, x, cy, lab, col, s=1.0):
    d.rounded_rectangle([x - 110 * s, cy - 20 * s, x + 110 * s, cy + 140 * s], radius=int(26 * s), fill=CREAM)
    d.rounded_rectangle([x - 120 * s, cy - 70 * s, x + 120 * s, cy - 10 * s], radius=int(18 * s), fill=col)
    d.text((x, cy + 62 * s), lab, font=F(BOLD, int(44 * s)), fill=col, anchor='mm')


def ill_eyecream(c, t, cx, cy):
    d = ImageDraw.Draw(c)
    a = ease((t - 0.2) / 0.6); b = ease((t - 0.5) / 0.6)
    jar(d, cx - 260 - int(200 * (1 - a)), cy, 'YÜZ', BERRY)
    jar(d, cx + 40 + int(200 * (1 - b)), cy + 30, 'GÖZ', RED, 0.75)
    k = back((t - 1.1) / 0.4)
    if k > 0: text_a(c, (cx - 100, cy + 60), '=', F(BOLD, int(90 * k) + 1), CREAM, 1, anchor='mm')
    # göz
    e = back((t - 1.4) / 0.4)
    if e > 0:
        ex, ey = cx + 300, cy - 120
        d.chord([ex - 90 * e, ey - 50 * e, ex + 90 * e, ey + 50 * e], 0, 360, fill=CREAM)
        d.ellipse([ex - 32 * e, ey - 32 * e, ex + 32 * e, ey + 32 * e], fill=PLUM)
        sparkle(d, ex + 100, ey - 50, 22 * e, PINK)


def ill_loop(c, t, cx, cy, fg=PLUM):
    d = ImageDraw.Draw(c)
    bottle(c, t, cx - 200, cy, 0.95, CREAM, BERRY, PINK, 'SERUM')
    # dönen ok
    x, y, r = cx + 220, cy - 30, 120
    st = (t * 120) % 360
    d.arc([x - r, y - r, x + r, y + r], st, st + 280, fill=RED, width=20)
    a = math.radians(st + 280)
    hx, hy = x + r * math.cos(a), y + r * math.sin(a)
    d.polygon([(hx + 30 * math.cos(a), hy + 30 * math.sin(a)), (hx - 30 * math.cos(a), hy - 30 * math.sin(a)),
               (hx + 36 * math.cos(a + math.pi / 2), hy + 36 * math.sin(a + math.pi / 2))], fill=RED)
    k = back((t - 1.0) / 0.4)
    if k > 0: heart(d, x, y + 6, 54 * k * (1 + 0.08 * math.sin(t * 5)), BERRY)
    sticker(c, (cx + 220, cy + 170), 'Hâlâ iş görüyor', F(BOLD, 32), fg, CREAM, -3, back((t - 1.4) / 0.4), 28, 14)


def heart(d, cx, cy, s, col):
    from illus import heart_pts
    d.polygon(heart_pts(cx, cy, s), fill=col)


def ill_pores(c, t, cx, cy):
    d = ImageDraw.Draw(c)
    x = cx - 180
    d.ellipse([x - 180, cy - 180, x + 180, cy + 180], fill=(236, 196, 166))
    for j in range(18):
        a = j * 2.4; rr = 30 + (j * 37) % 140
        px, py = x + rr * math.cos(a), cy + rr * math.sin(a)
        d.ellipse([px - 6, py - 6, px + 6, py + 6], fill=(196, 140, 108))
    # buhar + buz
    for j in range(3):
        p = (t * 0.6 + j * 0.33) % 1
        pts = [(cx + 100 + j * 50 + 12 * math.sin(u / 6 + t * 4), cy - 20 - u - p * 100) for u in range(0, 110, 6)]
        d.line(pts, fill=(255, 220, 200), width=7)
    k = back((t - 0.7) / 0.4)
    if k > 0:
        ix, iy = cx + 330, cy + 30; s = 70 * k
        d.rounded_rectangle([ix - s, iy - s, ix + s, iy + s], radius=int(18 * k) + 1, fill=(196, 226, 240))
        d.line([(ix - s * 0.5, iy - s * 0.4), (ix - s * 0.1, iy - s * 0.6)], fill=CREAM, width=8)
    k2 = back((t - 1.3) / 0.4)
    if k2 > 0:
        for (ax, ay) in [(cx + 150, cy - 110), (cx + 330, cy + 30)]:
            r = 95 * k2
            d.line([(ax - r * 0.7, ay - r * 0.7), (ax + r * 0.7, ay + r * 0.7)], fill=RED, width=16)
            d.line([(ax - r * 0.7, ay + r * 0.7), (ax + r * 0.7, ay - r * 0.7)], fill=RED, width=16)


# ================== B · KANDIRILMAMAK İÇİN — cilt mitleri (25 Kasım)
def b_cover(t):
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 80, 1120), 420)
    dots(d, 800, 470, 5, 3, 44, 6, (90, 50, 70))
    sticker(c, (W - 300, 110), 'KANDIRILMAMAK İÇİN', F(BOLD, 28), PINK, PLUM, 5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Cilt bakımında', F(BOLD, 96), 210, 0.2, CREAM), ('hâlâ inanılan', F(BOLD, 96), 318, 0.35, CREAM), ('5 mit.', F(ACC, 140), 430, 0.55, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(30 * (1 - a)))
    a = ease((t - 1.2) / 0.5)
    text_a(c, (70, 640), 'Paranı da cildini de korur.', F(MED, 40), CREAM, a)
    text_a(c, (70, 692), 'Kaydet, rafta aç.', F(MED, 40), CREAM, a)
    bottle(c, t, 720, 1010, 1.05, CREAM, RED, PINK, 'MUCİZE KREM')
    for j in range(10):
        p = ((t * 0.5 + j * 0.13) % 1.0)
        x = 600 + (j * 47) % 260; y = 850 - p * 200; r = 14 + (j % 3) * 8
        d.ellipse([x - r, y - r, x + r, y + r], outline=PINK, width=4)
    stamp(c, 1.0, 900, 900, 'MİT!', RED, 10)
    s = back((t - 1.8) / 0.4)
    if s > 0: sticker(c, (230, 880), 'Kaydet', F(BOLD, 42), RED, CREAM, -6, s, 34, 14)
    text_a(c, (70 + int(8 * math.sin(t * 6)), 1230), 'kaydır  ›', F(BOLD, 38), CREAM, ease((t - 2.0) / 0.4))
    logo(c, 'B'); return c

def b_cover0(t): return b_cover(t + 3.5)

STK = 'KANDIRILMAMAK İÇİN'
def b1(t): return item_page(t, 2, 6, PINK, (236, 170, 192), PLUM, BERRY, STK, (PLUM, CREAM), '01', ['Bol köpük =', 'temiz cilt.'],
                            'Köpük, temizlik gücünün ölçüsü değil. Sert, çok köpüren temizleyiciler cildi kurutup gerebilir. Yüzün "gıcır gıcır" olmamalı.',
                            lambda c, t, y: ill_foam(c, t, 540, 1030), 'B')
def b2(t): return item_page(t, 3, 6, CREAM, PINK, PLUM, RED, STK, (PLUM, CREAM), '02', ['Sivilceyi sıkmak', 'çabuk geçirir.'],
                            'Sıkmak iltihabı derine itebilir; kızarıklık uzar, iz ve leke riski artar. Bırak geçsin ya da dermatoloğa git.',
                            lambda c, t, y: ill_pimple(c, t, 540, 1030), 'B')
def b3(t): return item_page(t, 4, 6, PLUM, BERRY, CREAM, PINK, STK, (PINK, PLUM), '03', ['Göz kremi', 'şart.'],
                            'Şart değil. Yüz kremin gözünü yakmıyor, tahriş etmiyorsa göz çevresine de nazikçe sürebilirsin.',
                            lambda c, t, y: ill_eyecream(c, t, 540, 1010), 'B')
def b4(t): return item_page(t, 5, 6, CREAM, PINK, PLUM, BERRY, STK, (PLUM, CREAM), '04', ['Cilt ürüne alışır,', 'değiştir.'],
                            'Cilt ürüne "bağışıklık" kazanmaz. İşe yarıyorsa devam. Mevsim ya da ihtiyacın değişince rutini güncelle.',
                            lambda c, t, y: ill_loop(c, t, 540, 1020), 'B')
def b5(t): return item_page(t, 6, 6, BERRY, (120, 12, 60), CREAM, PINK, STK, (PINK, PLUM), '05', ['Sıcak su açar,', 'soğuk kapatır.'],
                            'Gözeneklerin kası yok; açılıp kapanmazlar. Sıcak su ise cildi kurutur. Ilık suyla yıka, gözeneği temiz tut.',
                            lambda c, t, y: ill_pores(c, t, 520, 900), 'A', 'Hangisine inanıyordun? Numarasını yaz ›')


# ================== ILLÜSTRASYONLAR — yaş köşesi
def ill_sunscreen(c, t, cx, cy):
    d = ImageDraw.Draw(c)
    sx, sy = cx + 220, cy - 80; k = ease(t / 0.8); r = 100 * k
    for i in range(12):
        a = t * 0.6 + i * math.pi / 6
        d.line([(sx + r * 1.25 * math.cos(a), sy + r * 1.25 * math.sin(a)), (sx + r * 1.6 * math.cos(a), sy + r * 1.6 * math.sin(a))], fill=GOLD, width=12)
    d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=GOLD)
    lay = Image.new('RGBA', (200, 420), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.polygon([(10, 60), (190, 60), (160, 400), (40, 400)], fill=CREAM)
    ld.rounded_rectangle([40, 0, 160, 70], radius=16, fill=RED)
    ld.text((100, 220), 'SPF', font=F(BOLD, 50), fill=BERRY, anchor='mm'); ld.text((100, 280), '30+', font=F(BOLD, 50), fill=BERRY, anchor='mm')
    lay = lay.rotate(-8 + 5 * math.sin(t * 2), expand=True, resample=Image.BICUBIC)
    c.paste(lay, (int(cx - 200 - lay.width / 2), int(cy - lay.height / 2)), lay)


def ill_vitc(c, t, cx, cy):
    d = ImageDraw.Draw(c)
    x = cx - 180
    d.rounded_rectangle([x - 80, cy - 90, x + 80, cy + 180], radius=30, fill=ORANGE)
    d.rounded_rectangle([x - 60, cy - 10, x + 60, cy + 100], radius=12, fill=CREAM)
    d.text((x, cy + 45), 'C', font=F(BOLD, 80), fill=ORANGE, anchor='mm')
    d.rectangle([x - 30, cy - 150, x + 30, cy - 90], fill=PLUM)
    d.ellipse([x - 40, cy - 220, x + 40, cy - 140], fill=PLUM)
    p = (t % 1.3) / 1.3
    dy = cy - 40 + p * 0
    # dilim
    k = back((t - 0.6) / 0.4)
    if k > 0:
        ox, oy, r = cx + 230, cy, 130 * k
        d.ellipse([ox - r, oy - r, ox + r, oy + r], fill=ORANGE)
        d.ellipse([ox - r * 0.85, oy - r * 0.85, ox + r * 0.85, oy + r * 0.85], fill=(255, 210, 140))
        for i in range(8):
            a = t * 0.5 + i * math.pi / 4
            d.line([(ox, oy), (ox + r * 0.85 * math.cos(a), oy + r * 0.85 * math.sin(a))], fill=ORANGE, width=6)
    sticker(c, (cx + 20, cy + 250), 'Sabah, SPF altına', F(BOLD, 30), PLUM, CREAM, -3, back((t - 1.3) / 0.4), 26, 12)


def ill_night(c, t, cx, cy, bg):
    d = ImageDraw.Draw(c)
    mx, my = cx + 220, cy - 60; k = back(t / 0.5); r = 120 * k
    if r > 1:
        d.ellipse([mx - r, my - r, mx + r, my + r], fill=GOLD)
        d.ellipse([mx - r + 60 * k, my - r - 20 * k, mx + r + 60 * k, my + r - 20 * k], fill=bg)
    for j, (sx, sy) in enumerate([(cx - 60, cy - 180), (cx + 60, cy + 120), (cx + 380, cy + 60)]):
        sparkle(d, sx, sy, 22 * (1 + 0.3 * math.sin(t * 4 + j)), CREAM)
    jar(d, cx - 220, cy + 10, 'RETİNOL', BERRY, 0.9 + 0.03 * math.sin(t * 3))


def ill_barrier(c, t, cx, cy, fg):
    d = ImageDraw.Draw(c)
    bw, bh = 120, 56
    for row in range(4):
        for col in range(5):
            k = back((t - 0.2 - (row * 5 + col) * 0.05) / 0.35)
            if k <= 0: continue
            x = cx - 330 + col * (bw + 8) + (row % 2) * 60; y = cy + 120 - row * (bh + 8)
            d.rounded_rectangle([x, y + (1 - k) * 60, x + bw, y + bh + (1 - k) * 60], radius=10, fill=[BERRY, RED, (236, 120, 150)][(row + col) % 3])
    for j in range(5):
        p = (t * 0.5 + j * 0.2) % 1
        x = cx - 250 + j * 120; y = cy + 210 + p * 60
        d.ellipse([x - 14, y - 14, x + 14, y + 18], fill=(150, 200, 230)); d.polygon([(x - 13, y), (x, y - 30), (x + 13, y)], fill=(150, 200, 230))
    sticker(c, (cx + 240, cy - 170), 'Nem içeride kalır', F(BOLD, 30), RED, CREAM, 4, back((t - 1.4) / 0.4), 26, 12)


# ================== C · YAŞ KÖŞESİ Black Friday (27 Kasım)
def c_cover(t):
    c = Image.new('RGB', (W, H), BLACK); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1150), 420)
    sticker(c, (W - 230, 110), 'YAŞ KÖŞESİ', F(BOLD, 30), RED, CREAM, 5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [("Black Friday'de", F(BOLD, 92), 210, 0.2, CREAM), ('yaşına göre', F(ACC, 116), 315, 0.4, PINK), ('sepete değer', F(BOLD, 92), 460, 0.6, CREAM), ('tek ürün.', F(BOLD, 92), 565, 0.6, CREAM)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(30 * (1 - a)))
    a = ease((t - 1.2) / 0.5)
    text_a(c, (70, 715), 'Gerisi beklesin. Dürüst liste.', F(MED, 40), CREAM, a)
    cols = [PINK, RED, CREAM, GOLD]
    for j, lab in enumerate(["20'ler", "30'lar", "40'lar", '50+']):
        k = back((t - 0.6 - j * 0.25) / 0.4)
        if k <= 0: continue
        x = 180 + j * 240; y = 960 + int(14 * math.sin(t * 3 + j)); r = 105 * k
        d.ellipse([x - r, y - r, x + r, y + r], fill=cols[j])
        text_a(c, (x, y + 18 * k), lab, F(BOLD, max(6, int(48 * k))), PLUM, 1, anchor='ms')
    s = back((t - 1.8) / 0.4)
    if s > 0: sticker(c, (210, 1130), 'Kaydet', F(BOLD, 42), RED, CREAM, -6, s, 34, 14)
    text_a(c, (70 + int(8 * math.sin(t * 6)), 1235), 'kaydır  ›', F(BOLD, 38), CREAM, ease((t - 2.0) / 0.4))
    logo(c, 'A'); return c

def c_cover0(t): return c_cover(t + 3.5)

STK_C = 'YAŞ KÖŞESİ'
def c1(t): return item_page(t, 2, 6, PINK, (236, 170, 192), PLUM, BERRY, STK_C, (BERRY, CREAM), "20'LER", ['Güneş kremi.', 'Her gün.'],
                            'Geniş spektrumlu SPF 30+. Görünen yaşlanmanın büyük kısmı güneşten gelir; en ucuz yaşlanma karşıtı yatırım bu.',
                            lambda c, t, y: ill_sunscreen(c, t, 540, 1010), 'B')
def c2(t): return item_page(t, 3, 6, CREAM, PINK, PLUM, RED, STK_C, (BERRY, CREAM), "30'LAR", ['C vitamini', 'serumu.'],
                            'Sabah, güneş kreminin altına. Tonu aydınlatır, antioksidan kalkan olur. Havayla bozulur: indirim var diye üç tane alma.',
                            lambda c, t, y: ill_vitc(c, t, 540, 1000), 'B')
def c3(t): return item_page(t, 4, 6, PLUM, BERRY, CREAM, PINK, STK_C, (PINK, PLUM), "40'LAR", ['Retinol', '(gece).'],
                            'İnce çizgi ve doku için en çok araştırılan içerik. Haftada 2-3 gece başla, sabah mutlaka SPF. Hamilelikte kullanılmaz.',
                            lambda c, t, y: ill_night(c, t, 540, 1010, PLUM), 'B')
def c4(t): return item_page(t, 5, 6, CREAM, PINK, PLUM, RED, STK_C, (BERRY, CREAM), '50+', ['Seramidli', 'zengin krem.'],
                            'Menopozla cilt incelir, kurur. Seramid bariyeri destekler, nemi içeride tutar. Boynunu ve ellerini unutma.',
                            lambda c, t, y: ill_barrier(c, t, 540, 1010, PLUM), 'B')

def c5(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blobs(c, t, BLACK, (W - 60, 1220), 380)
    sparkle(d, 930, 300, 30 + 6 * math.sin(t * 4), PINK)
    for txt, font, y, st, col in [('Senin sepetinde', F(BOLD, 88), 200, 0.2, CREAM), ('hangisi?', F(ACC, 120), 305, 0.4, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    opts = [('A', 'Güneş kremi'), ('B', 'C vitamini'), ('C', 'Retinol'), ('D', 'Seramidli krem')]
    y = 500
    for k, (l, txt) in enumerate(opts):
        s = ease((t - 0.8 - k * 0.25) / 0.45)
        if s > 0:
            x = 70 - int(60 * (1 - s))
            d.rounded_rectangle([x, y, x + 620, y + 96], radius=48, fill=CREAM)
            d.ellipse([x + 10, y + 8, x + 90, y + 88], fill=PLUM)
            d.text((x + 50, y + 66), l, font=F(BOLD, 46), fill=CREAM, anchor='ms')
            d.text((x + 116, y + 66), txt, font=F(BOLD, 40), fill=PLUM, anchor='ls')
        y += 112
    sticker(c, (360, 1010), 'Harfini yorumlara yaz ›', F(BOLD, 42), PLUM, CREAM, -3, back((t - 2.0) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 36, 18)
    a = ease((t - 2.5) / 0.4)
    text_a(c, (72, 1105), 'Sepeti dolu arkadaşına', F(BOLD, 40), CREAM, a)
    text_a(c, (72, 1157), 'gönder.', F(ACC, 52), PINK, a)
    footer(c, 6, 6, CREAM)
    logo(c, 'A'); return c


SETS = {
    'b': ('1125_ciltmitleri', [b_cover0, b1, b2, b3, b4, b5]),
    'c': ('1127_yaskosesi_bf', [c_cover0, c1, c2, c3, c4, c5]),
}
if __name__ == '__main__':
    arg = sys.argv[1]
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '2026-11')
    if arg == 'preview':
        tt = float(sys.argv[2]); key = sys.argv[3]
        pages = SETS[key][1]
        s = Image.new('RGB', (3 * 550 + 10, 2 * 685 + 10), (230, 230, 230))
        for k, f in enumerate(pages): s.paste(f(tt).resize((540, 675)), ((k % 3) * 550 + 10, (k // 3) * 685 + 10))
        s.save(sys.argv[4], quality=85)
    else:
        key, i = arg[0], int(arg[1:])
        name, pages = SETS[key]
        render(pages[i - 1], f'{out}/{name}_{i}.mp4', 6, (W, H))
        print('ok', arg, flush=True)
