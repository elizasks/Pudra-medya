"""48. hafta (23–29 Kasım 2026) story'leri."""
import os, sys, math
from w47 import *  # w46 yardımcıları + opts_story, promo
import c47
from PIL import ImageFilter

BLACK = (22, 14, 18)
GOLD = (255, 196, 92)


def edstil(t, name, cen, bg, circ, l1, l2, sub, q, lg='B'):
    c = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(c)
    blob(d, -120, 600, 420, t, circ)
    a = ease((t - 0.2) / 0.6)
    if a > 0:
        im = rounded(kb(name, (640, 880), t, 0.06, cen), 40)
        c.paste(im, (W - 700 + int((1 - a) * 300), 330), im)
    sticker(c, (250, 1270), 'EDİTÖRÜN STİLİ', F(BOLD, 30), PINK, PLUM, -6, back((t - 0.5) / 0.4))
    stack(c, t, [(l1, F(BOLD, 100), 1320, CREAM), (l2, F(ACC, 96), 1440, PINK)], t0=0.9)
    text_a(c, (76, 1590), sub, F(MED, 36), CREAM, ease((t - 1.8) / 0.5))
    sparks(d, t, [(960, 1300, 44, 2.0)], PINK)
    cta(c, t, (W - 330, 1210), q, CREAM, circ, 2.3, 34, 4)
    logo(c, lg, True); return c


def note_story(t, bg, circ, stk, stkcol, lines, body, cta_txt, ill, fg=CREAM, acc=PINK, lg='A', y0=900):
    c = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(c)
    blob(d, W + 30, 330, 400, t, circ)
    ill(c, d, t)
    sticker(c, (60 + F(BOLD, 32).getlength(stk) / 2 + 30, y0 - 60), stk, F(BOLD, 32), stkcol[0], stkcol[1], -6, back((t - 0.2) / 0.4))
    items = []; y = y0
    for j, (txt, f) in enumerate(lines):
        items.append((txt, f, y, acc if f.path == ACC else fg)); y += int(f.size * 1.2)
    stack(c, t, items, t0=0.5)
    a = ease((t - 1.8) / 0.5); y += 40
    for ln in body:
        text_a(c, (76, y), ln, F(MED, 40), fg, a); y += 58
    cta(c, t, (70 + F(BOLD, 34).getlength(cta_txt) / 2 + 38, min(y + 90, 1600)), cta_txt, acc if bg != PINK else BERRY, bg if bg != PINK else CREAM, 2.6, 34)
    logo(c, lg, True); return c


# ---------- Pazartesi 23
def a1(t):  # 10:30 → Black Friday carousel
    def ill(c, d, t):
        sw = math.sin(t * 2.2) * 10
        tag = Image.new('RGBA', (420, 300), (0, 0, 0, 0)); td = ImageDraw.Draw(tag)
        td.polygon([(0, 150), (90, 20), (410, 20), (410, 280), (90, 280)], fill=CREAM)
        td.ellipse([60, 130, 100, 170], fill=BLACK)
        td.text((250, 150), '%70?', font=F(BOLD, 110), fill=RED, anchor='mm')
        k = back((t - 0.2) / 0.5)
        if k > 0:
            tg = tag.resize((max(1, int(420 * k)), max(1, int(300 * k)))).rotate(-12 + sw, expand=True, resample=Image.BICUBIC)
            c.paste(tg, (int(780 - tg.width / 2), int(520 - tg.height / 2)), tg)
            d.line([(560, 300), (640 + 3 * sw, 500)], fill=GOLD, width=6)
        c47.stamp(c, t - 1.1, 800, 700, 'GERÇEKTEN Mİ?', RED, 8)
    return promo(t, BLACK, BERRY, 'KANDIRILMAMAK İÇİN', (RED, CREAM),
                 [("Black Friday'de", F(BOLD, 100), CREAM), ('kandırılmamak', F(ACC, 112), PINK), ('için 5 kural.', F(BOLD, 100), CREAM)],
                 ['27 Kasım geliyor. Sepete atmadan oku.'], 'Yeni gönderi profilde ›', ill, 'A', (CREAM, BLACK))

def a2(t):  # 13:00 D/Y dudak
    return truefalse(t, PINK, BERRY, BERRY, PLUM, 'DUDAK TESTİ', ['"Dudak kuruyunca', 'yalamak', 'nem verir."'], 'YANLIŞ!',
                     ['Tükürük buharlaşırken dudağı', 'daha da kurutur. Çözüm: kokusuz,', 'vazelin ya da balmumu içeren', 'bir dudak balmı.'], fg1=PLUM)

def a3(t):  # 19:00 Editörün stili — IMG_2001
    return edstil(t, 'kisisel/IMG_2001.jpg', (0.5, 0.45), PLUM, BERRY, 'Total siyah', '+ pliseli mini.',
                  'Tek renk giyince dokuyla oyna: pli, deri, örgü.', 'Total siyah sever misin?')

# ---------- Salı 24
def b1(t):  # 10:30 → 18:00 gündem teaser (cam cilt)
    def ill(c, d, t):
        cx, cy, r = 790, 500, 210
        k = back((t - 0.1) / 0.5)
        if k <= 0: return
        rr = r * k
        d.ellipse([cx - rr - 18, cy - rr - 18, cx + rr + 18, cy + rr + 18], fill=GOLD)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(214, 228, 236))
        p = (t * 0.6) % 1.4 - 0.2
        lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        sx = cx - rr + p * 2 * rr
        ld.polygon([(sx - 40, cy - rr), (sx + 30, cy - rr), (sx - 60, cy + rr), (sx - 130, cy + rr)], fill=(255, 255, 255, 150))
        m = Image.new('L', c.size, 0); ImageDraw.Draw(m).ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=255)
        c.paste(lay, (0, 0), Image.composite(lay.split()[3], Image.new('L', c.size, 0), m))
        sparks(d, t, [(cx + 150, cy - 160, 34, 0.6), (cx - 170, cy + 120, 22, 0.9)], CREAM)
        sticker(c, (cx, cy + rr + 50), '36 / 38 YANILTICI', F(BOLD, 34), RED, CREAM, -4, back((t - 1.0) / 0.4))
    return promo(t, BERRY, (120, 12, 60), "BU AKŞAM 18:00", (RED, CREAM),
                 [('Cam cilt', F(BOLD, 116), CREAM), ('videoları', F(ACC, 124), PINK), ('ne kadar dürüst?', F(BOLD, 84), CREAM)],
                 ['Dermatologlar en popüler 38 videoyu', 'inceledi. Sonuç akşam profilde.'], 'Takip et, kaçırma ›', ill, 'A', (CREAM, BERRY))

def b2(t):  # 13:00 çanta düellosu
    return duel(t, PINK, BERRY, 'ÇANTA DÜELLOSU', 'Kışın hangisi?', 'canta/IMG_4238.jpg', 'canta/IMG_4242.jpg', 'Yeşil kroko', 'Bordo baget',
                cen=((0.5, 0.5), (0.5, 0.5)))

def b3(t):  # 19:00 50'lere not — kaş
    def ill(c, d, t):
        cx, cy = 780, 470
        for side in (-1, 1):
            bx = cx + side * 150
            pts = [(bx - 120 * side * -1 if False else bx - 120, cy + 30), (bx, cy - 30), (bx + 120, cy + 10)]
            d.line(pts, fill=(200, 150, 130), width=8, joint='curve')
            for j in range(18):
                p = ease((t - 0.4 - j * 0.07) / 0.3)
                if p <= 0: continue
                u = j / 17; x = bx - 120 + 240 * u
                y = cy + 30 - 60 * math.sin(u * math.pi * 0.85) + (10 if u > 0.7 else 0)
                ang = -1.1 if u < 0.6 else -0.5
                L = 46 * p
                d.line([(x, y), (x + L * math.cos(ang) * 0.6, y + L * math.sin(ang))], fill=PLUM, width=7)
            d.ellipse([bx - 70, cy + 70, bx + 70, cy + 130], fill=CREAM)
            d.ellipse([bx - 26, cy + 74, bx + 26, cy + 126], fill=PLUM)
        # kalem
        k = ease((t - 0.3) / 2.0); px = cx - 270 + 540 * k
        d.line([(px, cy - 70), (px + 90, cy - 220)], fill=BERRY, width=26)
        d.polygon([(px - 12, cy - 64), (px + 10, cy - 76), (px - 4, cy - 50)], fill=PLUM)
    return note_story(t, PINK, BERRY, "50'LERE NOT", (PLUM, CREAM),
                      [('Kaşını incecik', F(BOLD, 100)), ('alma.', F(ACC, 112))],
                      ['Yıllarla kaş seyrelir. Kaş kalemiyle', 'kısa, tüy tüy çizgilerle doldur:', 'yüz anında canlanır.'],
                      'Kaydet, yarın dene ›', ill, PLUM, BERRY, 'B', 880)

# ---------- Çarşamba 25
def c1(t):  # 10:30 → cilt mitleri carousel
    def ill(c, d, t):
        c47.bottle(c, t, 790, 520, 1.2, CREAM, BERRY, PINK, 'MUCİZE KREM')
        for j in range(10):
            p = ((t * 0.5 + j * 0.13) % 1.0)
            x = 640 + (j * 47) % 320; y = 420 - p * 260; r = 14 + (j % 3) * 8
            d.ellipse([x - r, y - r, x + r, y + r], outline=PINK, width=4)
        c47.stamp(c, t - 1.0, 780, 760, 'MİT!', RED, 8)
    return promo(t, PLUM, BERRY, 'KANDIRILMAMAK İÇİN', (PINK, PLUM),
                 [('Cilt bakımında', F(BOLD, 104), CREAM), ('hâlâ inanılan', F(BOLD, 104), CREAM), ('5 mit.', F(ACC, 124), PINK)],
                 ['Kaçına inanıyordun?'], 'Yeni gönderi profilde ›', ill, 'B', (CREAM, PLUM))

def c2(t):  # 13:00 günün sorusu — ilişki
    def icon(c, d, t):
        k = back((t - 0.2) / 0.5)
        if k > 0:
            from illus import bubble
            bubble(c, 780, 380, '!!!', F(BOLD, int(70 * k) + 1), CREAM, RED, 1, -6)
            bubble(c, 900, 520, '...', F(BOLD, int(70 * k) + 1), PINK, PLUM, 1, 5, 'right')
    return opts_story(t, BERRY, RED, 'GÜNÜN SORUSU', 'Tartışmada seni', 'en çok ne kızdırır?',
                      ['"Sakin ol" denmesi', 'Sessiz kalınması', 'Eski konuların açılması'], 'Harfini yanıtla, anonim paylaşalım', 'A', icon)

def c3(t):  # 19:00 manikür — IMG_4195
    return photo_story(t, 'tirnak/IMG_4195.jpg', (0.5, 0.4), 'KIŞ MANİKÜRÜ', (PINK, PLUM),
                       [('Nude zemin', F(BOLD, 130), 1040, CREAM), ('+ siyah kıvrım.', F(ACC, 110), 1180, PINK)],
                       ('Grafik ama sade: her kombine uyar.', 1380), 'Kaydet, manikürcüne göster ›')

# ---------- Perşembe 26
def d1(t):  # 10:30 → 18:00 gündem teaser (smoky)
    def ill(c, d, t):
        cx, cy = 790, 520
        k = back((t - 0.1) / 0.5)
        if k <= 0: return
        p = ease((t - 0.6) / 1.6)
        lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        for j in range(6):
            rr = 90 + j * 26 * p
            ld.ellipse([cx - 230 - rr * 0.2, cy - 90 - rr * 0.5, cx + 230 + rr * 0.9, cy + 30 + rr * 0.2], fill=(120, 72, 52, int(46 * p)))
        c.paste(lay.filter(ImageFilter.GaussianBlur(18)), (0, 0), lay.filter(ImageFilter.GaussianBlur(18)))
        s = k
        d.chord([cx - 210 * s, cy - 110 * s, cx + 210 * s, cy + 110 * s], 0, 360, fill=CREAM)
        d.ellipse([cx - 80 * s, cy - 80 * s, cx + 80 * s, cy + 80 * s], fill=(122, 72, 40))
        d.ellipse([cx - 40 * s, cy - 40 * s, cx + 40 * s, cy + 40 * s], fill=BLACK)
        d.ellipse([cx + 14 * s, cy - 30 * s, cx + 34 * s, cy - 10 * s], fill=CREAM)
        d.arc([cx - 220 * s, cy - 130 * s, cx + 220 * s, cy + 90 * s], 195, 345, fill=BLACK, width=10)
        for j in range(7):
            a = math.radians(200 + j * 22); x = cx + 220 * s * math.cos(a); y = cy - 20 + 110 * s * math.sin(a)
            d.line([(x, y), (x + 30 * math.cos(a), y + 40 * math.sin(a))], fill=BLACK, width=6)
    return promo(t, BERRY, (120, 12, 60), "BU AKŞAM 18:00", (RED, CREAM),
                 [('Smoky göz', F(BOLD, 116), CREAM), ('geri döndü.', F(ACC, 124), PINK)],
                 ['Bu kez dağınık. Kusursuz çizgi', 'çekmek zorunda değilsin.'], 'Takip et, kaçırma ›', ill, 'A', (CREAM, BERRY))

def d2(t):  # 13:00 D/Y parfüm
    return truefalse(t, PLUM, BERRY, BERRY, PLUM, 'PARFÜM TESTİ', ['"Parfümü bileğine', 'sürüp ovuşturmak', 'kalıcı yapar."'], 'YANLIŞ!',
                     ['Ovuşturmak üst notaları hızla', 'dağıtır, koku çabuk değişir.', 'Sık, bekle, kendi kurusun.', 'Nemli ten kokuyu daha iyi tutar.'])

def d3(t):  # 19:00 40'lara not — IMG_4224
    return photo_story(t, 'ayakkabi/IMG_4224.jpg', (0.5, 0.5), "40'LARA NOT", (PINK, PLUM),
                       [('Alçak topuk,', F(BOLD, 110), 1040, CREAM), ('yüksek etki.', F(ACC, 112), 1170, PINK)],
                       ('Kırmızı kısa topuk: jean de, elbise de kurtarır.', 1370), 'Kaydet, dolabına bak ›')

# ---------- Cuma 27 (Black Friday)
def e1(t):  # 10:30 → Yaş köşesi BF carousel
    def ill(c, d, t):
        cols = [PINK, RED, CREAM, GOLD]
        for j, lab in enumerate(["20'ler", "30'lar", "40'lar", '50+']):
            k = back((t - 0.3 - j * 0.25) / 0.4)
            if k <= 0: continue
            x = 560 + (j % 2) * 270; y = 360 + (j // 2) * 270 + int(14 * math.sin(t * 3 + j)); r = 120 * k
            d.ellipse([x - r, y - r, x + r, y + r], fill=cols[j])
            text_a(c, (x, y + 20 * k), lab, F(BOLD, max(6, int(54 * k))), PLUM, 1, anchor='ms')
    return promo(t, BLACK, BERRY, 'YAŞ KÖŞESİ', (RED, CREAM),
                 [('Bugün sepete', F(BOLD, 106), CREAM), ('yaşına göre', F(ACC, 116), PINK), ('tek ürün.', F(BOLD, 106), CREAM)],
                 ['Black Friday için dürüst liste.'], 'Yeni gönderi profilde ›', ill, 'A', (CREAM, BLACK))

def e2(t):  # 13:00 ayakkabı düellosu
    return duel(t, CREAM, BERRY, 'AYAKKABI DÜELLOSU', 'Cuma akşamı hangisi?', 'ayakkabi/IMG_4230.jpg', 'ayakkabi/IMG_4225.jpg', 'Renkli sivri', 'Sneaker topuk',
                cen=((0.5, 0.5), (0.5, 0.5)))

def e3(t):  # 19:00 cayma hakkı
    def ill(c, d, t):
        cx, cy = 790, 500
        k = back((t - 0.2) / 0.5)
        if k <= 0: return
        w, h = 300 * k, 320 * k
        d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=int(30 * k) + 1, fill=CREAM)
        d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy - h / 2 + 80 * k], radius=int(30 * k) + 1, fill=RED)
        for x in (-70, 70): d.rounded_rectangle([cx + x * k - 10, cy - h / 2 - 30 * k, cx + x * k + 10, cy - h / 2 + 30 * k], radius=8, fill=PLUM)
        n = min(14, int(1 + 13 * ease((t - 0.6) / 1.4)))
        text_a(c, (cx, cy + 90 * k), str(n), F(BOLD, max(8, int(150 * k))), PLUM, 1, anchor='ms')
        text_a(c, (cx, cy + 135 * k), 'GÜN', F(BOLD, max(8, int(36 * k))), BERRY, 1, anchor='ms')
        sparks(d, t, [(cx + 190, cy - 170, 30, 1.8), (cx - 190, cy + 150, 22, 2.0)], PINK)
    return note_story(t, PLUM, BERRY, 'CUMA AKŞAMI NOTU', (PINK, PLUM),
                      [('Pişman olduğun', F(BOLD, 96)), ('sepete', F(ACC, 110)), ('14 gün var.', F(BOLD, 96))],
                      ['Online alışverişte çoğu üründe', '14 gün cayma hakkın var. Açılmış', 'kozmetik gibi istisnalar hariç.'],
                      'Sepet delisi arkadaşına gönder ›', ill, CREAM, PINK, 'B', 900)

# ---------- Cumartesi 28
def f1(t):  # 10:30 Editörün stili — IMG_3030
    return edstil(t, 'kisisel/IMG_3030.jpg', (0.5, 0.5), BERRY, (120, 12, 60), 'Geniş paça', '+ yeşil body.',
                  'Hafta sonu formülü: rahat paça, canlı üst.', 'Bugün ne giyiyorsun?', 'A')

def f2(t):  # 13:00 günün sorusu — kış derdi
    def icon(c, d, t):
        k = back((t - 0.2) / 0.5)
        if k > 0:
            cx, cy = 850, 430; r = 110 * k; rot = t * 0.4
            for i in range(6):
                a = rot + i * math.pi / 3
                x2, y2 = cx + r * math.cos(a), cy + r * math.sin(a)
                d.line([(cx, cy), (x2, y2)], fill=CREAM, width=12)
                for s in (0.55, 0.8):
                    bx, by = cx + r * s * math.cos(a), cy + r * s * math.sin(a)
                    for da in (0.6, -0.6):
                        d.line([(bx, by), (bx + 30 * k * math.cos(a + da), by + 30 * k * math.sin(a + da))], fill=CREAM, width=8)
    return opts_story(t, PLUM, BERRY, 'GÜNÜN SORUSU', 'Kışın en çok', 'neyden bıktın?',
                      ['Çatlayan dudak', 'Elektriklenen saç', 'Kuruyan eller', 'Donuk ten'], 'Harfini yanıtla, çözümü yazalım ›', 'B', icon)

def f3(t):  # 19:00 Hafta sonu manifestosu
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blob(d, -60, 520, 380, t, (232, 80, 96))
    blob(d, W + 20, 1650, 430, t, PLUM, 0.3)
    sparks(d, t, [(860, 420, 54, 0.5), (960, 560, 28, 0.8)], CREAM)
    sticker(c, (330, 760), 'HAFTA SONU MANİFESTOSU', F(BOLD, 30), CREAM, RED, -5, back((t - 0.2) / 0.4))
    stack(c, t, [('İndirim', F(BOLD, 110), 830, CREAM), ('sana değil,', F(ACC, 116), 960, PLUM), ('sepete', F(BOLD, 110), 1100, CREAM), ('yakışır.', F(ACC, 116), 1230, PLUM)], t0=0.4)
    text_a(c, (76, 1400), 'Sen zaten tam fiyatına değersin.', F(MED, 44), CREAM, ease((t - 1.9) / 0.5))
    cta(c, t, (W // 2, 1540), 'Bunu duymak isteyene gönder ›', CREAM, RED, 2.4, 34)
    logo(c, 'A', True); return c

# ---------- Pazar 29
def g1(t):  # 10:30 Filtresiz — ılık su
    def ill(c, d, t):
        cx, cy = 760, 420
        k = back((t - 0.2) / 0.5)
        if k <= 0: return
        d.rounded_rectangle([cx - 180 * k, cy - 50 * k, cx + 60 * k, cy + 20 * k], radius=int(30 * k) + 1, fill=CREAM)
        d.rounded_rectangle([cx + 20 * k, cy - 50 * k, cx + 80 * k, cy + 110 * k], radius=int(26 * k) + 1, fill=CREAM)
        d.rounded_rectangle([cx - 120 * k, cy - 100 * k, cx - 40 * k, cy - 50 * k], radius=10, fill=PINK)
        for j in range(5):
            p = ((t * 0.9 + j * 0.2) % 1.0)
            y = cy + 130 + p * 330; x = cx + 50
            d.ellipse([x - 16, y - 16, x + 16, y + 20], fill=(150, 200, 230)); d.polygon([(x - 15, y), (x, y - 34), (x + 15, y)], fill=(150, 200, 230))
        # termometre
        tx, ty = cx + 250, cy + 120
        d.rounded_rectangle([tx - 28, ty - 170, tx + 28, ty + 100], radius=28, fill=CREAM)
        d.ellipse([tx - 52, ty + 60, tx + 52, ty + 164], fill=CREAM)
        lv = ease((t - 0.8) / 1.0)
        d.ellipse([tx - 38, ty + 74, tx + 38, ty + 150], fill=(255, 160, 92))
        d.rounded_rectangle([tx - 14, ty + 90 - 140 * lv, tx + 14, ty + 100], radius=14, fill=(255, 160, 92))
        sticker(c, (tx - 20, ty - 220), 'ILIK', F(BOLD, 36), GOLD, PLUM, 6, back((t - 1.6) / 0.4))
    return promo(t, BERRY, (120, 12, 60), 'FİLTRESİZ', (CREAM, BERRY),
                 [('Yüzünü', F(BOLD, 110), CREAM), ('sıcak suyla', F(ACC, 120), PINK), ('yıkama.', F(BOLD, 110), CREAM)],
                 ['Sıcak su cildin yağını söküp kurutur.', 'Ilık su yeter; havluyla bastırarak kurula.'], 'Pazar rutinine ekle ›', ill, 'A', (CREAM, BERRY))

def g2(t):  # 13:00 D/Y kışın SPF
    return truefalse(t, CREAM, BERRY, PINK, PLUM, 'CİLT BAKIMI TESTİ', ['"Kışın, bulutlu', 'havada güneş', 'kremi gerekmez."'], 'YANLIŞ!',
                     ['UVA ışınları bulutun ve camın', 'içinden geçer, kışın da vardır.', 'Yüzüne her sabah SPF 30+;', 'karda yansıma daha da artar.'], fg1=PLUM)

def g3(t):  # 19:00 20'lere not — IMG_4234
    return photo_story(t, 'canta/IMG_4234.jpg', (0.5, 0.5), "20'LERE NOT", (PINK, PLUM),
                       [('Siyah kombin', F(BOLD, 110), 1040, CREAM), ('+ renkli çanta.', F(ACC, 104), 1170, PINK)],
                       ('Tek renkli parça bütün görünümü taşır.', 1360), 'Kaydet, dolabına bak ›')

fns = dict(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3, d1=d1, d2=d2, d3=d3,
           e1=e1, e2=e2, e3=e3, f1=f1, f2=f2, f3=f3, g1=g1, g2=g2, g3=g3)
DATES = dict(a='1123', b='1124', c='1125', d='1126', e='1127', f='1128', g='1129')
SLOT = {'1': '1030', '2': '1300', '3': '1900'}
if __name__ == '__main__':
    from PIL import ImageFilter
    arg = sys.argv[1]
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '2026-11')
    if arg == 'preview':
        tt = float(sys.argv[2]); keys = sys.argv[3].split(',')
        sh = Image.new('RGB', (len(keys) * 365 + 5, 655), 'white')
        for k, n in enumerate(keys):
            sh.paste(fns[n](tt).resize((360, 640)), (5 + k * 365, 5))
        sh.save(sys.argv[4], quality=85)
    else:
        for n in arg.split(','):
            render(fns[n], f'{out}/{DATES[n[0]]}_story_{SLOT[n[1]]}.mp4', 6, (W, H))
            print('ok', n, flush=True)
