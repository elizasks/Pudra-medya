"""47. hafta (16–22 Kasım 2026) story'leri."""
import os, sys, math
from w46 import *  # W,H=1080x1920, photo/kb/rounded/blob/stack/cta/sparks/photo_story/duel/truefalse/heart/sun
import c47


def opts_story(t, bg, circ, label, q1, q2, opts, cta_txt, lg='A', icon=None):
    c = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(c)
    blob(d, W - 40, 1640, 430, t, circ)
    if icon: icon(c, d, t)
    sticker(c, (60 + F(BOLD, 32).getlength(label) / 2 + 30, 560), label, F(BOLD, 32), PINK, PLUM, -6, back((t - 0.2) / 0.4))
    stack(c, t, [(q1, F(BOLD, 96), 630, CREAM), (q2, F(ACC, 112), 755, PINK)], t0=0.4)
    for j, o in enumerate(opts):
        a = ease((t - 1.2 - j * 0.3) / 0.5)
        if a <= 0: continue
        y = 990 + j * 150; x = 80 + int((1 - a) * -400)
        d.rounded_rectangle([x, y, x + 920, y + 116], radius=58, fill=CREAM)
        d.ellipse([x + 16, y + 16, x + 100, y + 100], fill=RED if j != 1 else PLUM)
        text_a(c, (x + 58, y + 58), 'ABCD'[j], F(BOLD, 44), CREAM, 1, anchor='mm')
        text_a(c, (x + 128, y + 58), o, F(BOLD, 38), PLUM, 1, anchor='lm')
    cta(c, t, (W // 2, 990 + len(opts) * 150 + 60), cta_txt, CREAM, bg, 2.4, 32)
    logo(c, lg, True); return c


def promo(t, bg, circ, stk, stkcol, lines, sub, cta_txt, ill, lg='A', ctacol=(CREAM, None)):
    c = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(c)
    blob(d, W - 20, 1600, 440, t, circ)
    ill(c, d, t)
    sticker(c, (60 + F(BOLD, 32).getlength(stk) / 2 + 30, 860), stk, F(BOLD, 32), stkcol[0], stkcol[1], -6, back((t - 0.2) / 0.4))
    y = 930; items = []
    for txt, font, col in lines:
        items.append((txt, font, y, col)); y += int(font.size * 1.18)
    stack(c, t, items, t0=0.4)
    if sub:
        a = ease((t - 1.5) / 0.5)
        for j, ln in enumerate(sub):
            text_a(c, (76, y + 30 + j * 56), ln, F(MED, 42), CREAM, a)
        y += 30 + len(sub) * 56
    cta(c, t, (70 + F(BOLD, 38).getlength(cta_txt) / 2 + 38, min(y + 110, 1600)), cta_txt, ctacol[0], ctacol[1] or bg, 2.0)
    logo(c, lg, True); return c


# ---------- Pazartesi 16
def a1(t):  # 10:30 → Kırmızı bayrak carousel
    def ill(c, d, t):
        r2 = int(230 * ease(t / 0.8)); d.ellipse([-80 - r2, 420 - r2, -80 + r2, 420 + r2], fill=(232, 80, 96))
        fy = int(1960 - 1500 * ease((t - 0.3) / 0.9)); waving_flag(d, 640, fy, 400, t, CREAM, PLUM)
    return promo(t, RED, PLUM, 'KIRMIZI BAYRAK', (CREAM, RED),
                 [('Arkadaşlıkta', F(BOLD, 104), CREAM), ('5 kırmızı', F(ACC, 124), PLUM), ('bayrak.', F(BOLD, 104), CREAM)],
                 ['Biri bile tanıdıksa oku.'], 'Yeni gönderi profilde ›', ill, 'A', (CREAM, RED))

def a2(t):  # 13:00 D/Y yağlı cilt
    return truefalse(t, PINK, BERRY, BERRY, PLUM, 'CİLT TESTİ', ['"Yağlı cilt', 'nemlendirici', 'kullanmaz."'], 'YANLIŞ!',
                     ['Yağlı cildin de neme ihtiyacı var.', 'Kurutursan bariyer zayıflar.', 'Çözüm: hafif, jel kıvamlı,', 'gözenek tıkamayan formül.'], fg1=PLUM)

def a3(t):  # 19:00 Editörün stili — c685bd54
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blob(d, -120, 600, 420, t, BERRY)
    a = ease((t - 0.2) / 0.6)
    if a > 0:
        im = rounded(kb('kisisel/c685bd54.jpg', (640, 880), t, 0.06, (0.5, 0.5)), 40)
        c.paste(im, (W - 700 + int((1 - a) * 300), 330), im)
    sticker(c, (250, 1270), 'EDİTÖRÜN STİLİ', F(BOLD, 30), PINK, PLUM, -6, back((t - 0.5) / 0.4))
    stack(c, t, [('Haki kargo', F(BOLD, 100), 1320, CREAM), ('+ siyah triko.', F(ACC, 96), 1440, PINK)], t0=0.9)
    text_a(c, (76, 1590), 'Pazartesi formülü: rahat ama derli toplu.', F(MED, 36), CREAM, ease((t - 1.8) / 0.5))
    sparks(d, t, [(960, 1300, 44, 2.0)], PINK)
    cta(c, t, (W - 330, 1210), 'Sen bugün ne giydin?', CREAM, BERRY, 2.3, 34, 4)
    logo(c, 'B', True); return c

# ---------- Salı 17
def b1(t):  # 10:30 → 18:00 Reels teaser
    def ill(c, d, t):
        p = ease((t - 0.3) / 1.6)
        cx, cy = 800, 500
        col = tuple(int((255, 196, 92)[i] * (1 - p) + CREAM[i] * p) for i in range(3))
        sun(d, cx, cy, 150, t, col, PINK) if p < 0.5 else None
        if p >= 0.5:
            d.ellipse([cx - 150, cy - 150, cx + 150, cy + 150], fill=CREAM)
            off = 110 * (p - 0.5) * 2
            d.ellipse([cx - 150 + off, cy - 170, cx + 150 + off, cy + 130], fill=BERRY)
            sparks(d, t, [(620, 380, 26, 1.3), (960, 720, 20, 1.5), (700, 700, 16, 1.7)], PINK)
    return promo(t, BERRY, (120, 12, 60), "BU AKŞAM 18:00", (RED, CREAM),
                 [('Gündüz mü,', F(BOLD, 116), CREAM), ('gece mi?', F(ACC, 130), PINK)],
                 ['İki adımda dönüşüm: kedi eyeliner', '+ bordo ruj. Yeni Reels geliyor.'], 'Takip et, kaçırma ›', ill, 'A', (CREAM, BERRY))

def b2(t):  # 13:00 çizme düellosu
    return duel(t, PINK, BERRY, 'ÇİZME DÜELLOSU', 'Kışın hangisi?', 'ayakkabi/IMG_4217.jpg', 'ayakkabi/IMG_4219.jpg', 'Kırmızı yarışçı', 'Siyah yarışçı',
                cen=((0.5, 0.5), (0.5, 0.5)))

def b3(t):  # 19:00 50'lere not — krem allık
    c = Image.new('RGB', (W, H), PINK); d = ImageDraw.Draw(c)
    blob(d, W + 30, 330, 400, t, BERRY)
    dots(d, 90, 1660, 6, 3, 46, 7, BERRY)
    # yüz + allık
    k = back((t - 0.2) / 0.5)
    if k > 0:
        cx, cy, r = 780, 520, 170 * k
        d.rounded_rectangle([cx - r * 1.3, cy - r * 1.4, cx + r * 1.3, cy + r * 0.9], radius=int(r * 1.1) + 1, fill=(206, 204, 212))
        d.ellipse([cx - r, cy - r * 1.15, cx + r, cy + r * 1.15], fill=(236, 196, 166))
        d.chord([cx - r * 1.05, cy - r * 1.3, cx + r * 1.05, cy - r * 0.05], 180, 360, fill=(206, 204, 212))
        for ex in (-0.38, 0.38): d.arc([cx + ex * r - 26, cy - 10, cx + ex * r + 26, cy + 20], 200, 340, fill=PLUM, width=6)
        d.arc([cx - 40, cy + 60, cx + 40, cy + 100], 20, 160, fill=RED, width=8)
        p = ease((t - 1.0) / 0.8)
        if p > 0:
            lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
            for sx in (-1, 1):
                bx = cx + sx * r * 0.55; by = cy + 30
                ld.ellipse([bx - 50, by - 30 - 30 * p, bx + 50, by + 20], fill=(226, 90, 120, int(150 * p)))
            c.paste(lay, (0, 0), lay)
            d.line([(cx + r * 0.55, cy + 40), (cx + r * 0.95, cy - 40 * p)], fill=BERRY, width=6)
    sticker(c, (230, 840), "50'LERE NOT", F(BOLD, 32), PLUM, CREAM, -6, back((t - 0.2) / 0.4))
    stack(c, t, [('Allığı biraz', F(BOLD, 104), 900, PLUM), ('yukarı sür.', F(ACC, 112), 1030, BERRY)], t0=0.5)
    a = ease((t - 1.8) / 0.5)
    for j, ln in enumerate(['Elmacık kemiğinin üstünden şakağa', 'doğru dağıt: yüz kalkık görünür.', 'Krem allık tende daha doğal durur.']):
        text_a(c, (76, 1200 + j * 58), ln, F(MED, 40), PLUM, a)
    cta(c, t, (300, 1490), 'Kaydet, yarın dene ›', BERRY, CREAM, 2.6, 34)
    logo(c, 'B', True); return c

# ---------- Çarşamba 18
def c1(t):  # 10:30 → etiket carousel
    def ill(c, d, t):
        c47.bottle(c, t, 790, 520, 1.2, CREAM, RED, PINK, 'HİPOALERJENİK')
        c47.stamp(c, t - 1.0, 760, 700, 'GERÇEKTEN Mİ?', BERRY, 8)
    return promo(t, PLUM, BERRY, 'KANDIRILMAMAK İÇİN', (PINK, PLUM),
                 [('Kozmetik', F(BOLD, 110), CREAM), ('etiketinde', F(BOLD, 110), CREAM), ('5 tuzak.', F(ACC, 124), PINK)],
                 ['Rafta okumadan alma.'], 'Yeni gönderi profilde ›', ill, 'B', (CREAM, PLUM))

def c2(t):  # 13:00 günün sorusu — ilişki
    def icon(c, d, t):
        k = back((t - 0.2) / 0.5)
        if k > 0: heart(d, 860, 440, 110 * k * (1 + 0.08 * abs(math.sin(t * 4))), PINK)
    return opts_story(t, BERRY, RED, 'GÜNÜN SORUSU', 'Kavgadan sonra', 'ilk kim yazar?',
                      ['Ben, uzatmam', 'O; ben beklerim', 'İkimiz de inatçıyız'], 'Harfini yanıtla, anonim paylaşalım', 'A', icon)

def c3(t):  # 19:00 manikür ilhamı — IMG_4158
    return photo_story(t, 'tirnak/IMG_4158.jpg', (0.5, 0.4), 'KAZAK MEVSİMİ MANİKÜRÜ', (PINK, PLUM),
                       [('Nude', F(BOLD, 140), 1040, CREAM), ('+ ince çizgi.', F(ACC, 120), 1190, PINK)],
                       ('Kısa tırnakta da şık, uzamasına da göz yumar.', 1390), 'Kaydet, manikürcüne göster ›')

# ---------- Perşembe 19
def d1(t):  # 10:30 → Filtre vs Gerçek Reels (10:00)
    def ill(c, d, t):
        cx, cy = 790, 520
        p = ease((t - 0.4) / 1.4)
        d.ellipse([cx - 230, cy - 230, cx + 230, cy + 230], fill=CREAM)
        d.ellipse([cx - 200, cy - 200, cx + 200, cy + 200], fill=(236, 196, 166))
        lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        for j in range(26):  # gözenek/doku noktaları
            a = j * 2.4; rr = 40 + (j * 37) % 150
            x = cx + rr * math.cos(a); y = cy + rr * math.sin(a)
            ld.ellipse([x - 5, y - 5, x + 5, y + 5], fill=(196, 140, 108, int(255 * p)))
        c.paste(lay, (0, 0), lay)
        sticker(c, (cx - 130, cy + 270), 'FİLTRE', F(BOLD, 30), PINK, PLUM, -8, 1 - p if p < 1 else 0.01)
        sticker(c, (cx + 120, cy + 270), 'SEN', F(BOLD, 36), RED, CREAM, 6, back((t - 1.6) / 0.4))
    return promo(t, BERRY, (120, 12, 60), 'YENİ REELS', (RED, CREAM),
                 [('Biri filtre,', F(BOLD, 116), CREAM), ('biri sen.', F(ACC, 130), PINK)],
                 ['Gözenek, leke, doku: kusur değil.'], 'Profilde izle ›', ill, 'A', (CREAM, BERRY))

def d2(t):  # 13:00 D/Y saç yıkama
    return truefalse(t, PLUM, BERRY, BERRY, PLUM, 'SAÇ TESTİ', ['"Saçı her gün', 'yıkamak', 'döker."'], 'YANLIŞ!',
                     ['Yıkarken gördüğün teller', 'zaten dökülmeye hazırdı.', 'Şampuan dökülme yapmaz;', 'sıklığı saç tipine göre seç.'])

def d3(t):  # 19:00 20'lere not — çanta IMG_4240
    return photo_story(t, 'canta/IMG_4240.jpg', (0.5, 0.5), "20'LERE NOT", (PINK, PLUM),
                       [('Beş trend çanta', F(BOLD, 96), 1040, CREAM), ('yerine bir iyi', F(ACC, 104), 1160, PINK), ('çanta.', F(BOLD, 96), 1290, CREAM)],
                       ('Nötr renk, sağlam sap, her şeye gider.', 1440), 'Kaydet, maaş gününde aç ›')

# ---------- Cuma 20
def e1(t):  # 10:30 → Yaş köşesi carousel
    def ill(c, d, t):
        cols = [PINK, RED, CREAM, (255, 196, 92)]
        for j, lab in enumerate(["20'ler", "30'lar", "40'lar", '50+']):
            k = back((t - 0.3 - j * 0.25) / 0.4)
            if k <= 0: continue
            x = 560 + (j % 2) * 270; y = 360 + (j // 2) * 270 + int(14 * math.sin(t * 3 + j)); r = 120 * k
            d.ellipse([x - r, y - r, x + r, y + r], fill=cols[j])
            text_a(c, (x, y + 20 * k), lab, F(BOLD, max(6, int(54 * k))), PLUM, 1, anchor='ms')
    return promo(t, BERRY, (120, 12, 60), 'YAŞ KÖŞESİ', (PINK, PLUM),
                 [('Her yaşın', F(BOLD, 110), CREAM), ('bir yatırım', F(ACC, 120), PINK), ('parçası.', F(BOLD, 110), CREAM)],
                 ['Seninki hangisi?'], 'Yeni gönderi profilde ›', ill, 'A', (CREAM, BERRY))

def e2(t):  # 13:00 manikür düellosu
    return duel(t, CREAM, BERRY, 'MANİKÜR DÜELLOSU', 'Hafta sonu rengi?', 'tirnak/IMG_4160.jpg', 'tirnak/IMG_4197.jpg', 'Bulut mavisi', 'Lila kıvrım',
                cen=((0.5, 0.5), (0.5, 0.5)))

def e3(t):  # 19:00 ilişki ilham — kendinle randevu
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blob(d, W + 30, 1650, 420, t, BERRY)
    # mum
    k = back((t - 0.2) / 0.5)
    if k > 0:
        cx, cy = 800, 640
        d.rounded_rectangle([cx - 60, cy - 120 * k, cx + 60, cy + 180], radius=20, fill=CREAM)
        fl = 1 + 0.12 * math.sin(t * 14); k = max(k, 0.25)
        d.ellipse([cx - 30 * k, cy - 120 * k - 110 * fl * k, cx + 30 * k, cy - 120 * k - 10], fill=(255, 196, 92))
        d.ellipse([cx - 14 * k, cy - 120 * k - 60 * fl * k, cx + 14 * k, cy - 120 * k - 14], fill=CREAM)
        d.line([(cx, cy - 120 * k), (cx, cy - 120 * k - 16)], fill=PLUM, width=5)
    sparks(d, t, [(620, 420, 26, 0.9), (970, 380, 20, 1.1), (980, 760, 16, 1.3)], PINK)
    sticker(c, (260, 940), 'CUMA AKŞAMI NOTU', F(BOLD, 30), PINK, PLUM, -6, back((t - 0.3) / 0.4))
    stack(c, t, [('Bu akşam', F(BOLD, 104), 1000, CREAM), ('kendinle', F(ACC, 120), 1125, PINK), ('randevun var.', F(BOLD, 104), 1270, CREAM)], t0=0.5)
    a = ease((t - 1.8) / 0.5)
    text_a(c, (76, 1430), 'Telefon sessizde, sevdiğin yemek, iyi bir film.', F(MED, 36), CREAM, a)
    cta(c, t, (360, 1560), 'Buna ihtiyacı olana gönder ›', CREAM, PLUM, 2.4, 34)
    logo(c, 'B', True); return c

# ---------- Cumartesi 21
def f1(t):  # 10:30 → 11:00 Reels teaser — IMG_4227
    return photo_story(t, 'ayakkabi/IMG_4227.jpg', (0.5, 0.4), "SAAT 11:00'DE", (RED, CREAM),
                       [('Hafta sonu', F(BOLD, 130), 1040, CREAM), ('ilhamı.', F(ACC, 150), 1180, PINK)],
                       ('Yeni Reels bugün profilde.', 1400), 'Takip et, kaçırma ›')

def f2(t):  # 13:00 günün sorusu — güzellik
    def icon(c, d, t):
        k = back((t - 0.2) / 0.5)
        if k > 0:  # ruj
            cx, cy = 840, 420; s = k
            d.rounded_rectangle([cx - 55 * s, cy + 20 * s, cx + 55 * s, cy + 170 * s], radius=int(10 * s) + 1, fill=CREAM)
            d.rectangle([cx - 40 * s, cy - 40 * s, cx + 40 * s, cy + 20 * s], fill=(214, 190, 120))
            d.polygon([(cx - 32 * s, cy - 40 * s), (cx + 32 * s, cy - 40 * s), (cx + 32 * s, cy - 120 * s), (cx - 32 * s, cy - 80 * s)], fill=RED)
    return opts_story(t, PLUM, BERRY, 'GÜNÜN SORUSU', 'Tek ürün hakkın', 'olsa hangisi?',
                      ['Maskara', 'Ruj', 'Nemlendirici', 'Kapatıcı'], 'Harfini yanıtla ›', 'B', icon)

def f3(t):  # 19:00 Hafta sonu manifestosu
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blob(d, -60, 520, 380, t, (232, 80, 96))
    blob(d, W + 20, 1650, 430, t, PLUM, 0.3)
    sparks(d, t, [(860, 420, 54, 0.5), (960, 560, 28, 0.8)], CREAM)
    sticker(c, (330, 760), 'HAFTA SONU MANİFESTOSU', F(BOLD, 30), CREAM, RED, -5, back((t - 0.2) / 0.4))
    stack(c, t, [('Bu hafta sonu', F(BOLD, 96), 830, CREAM), ('kimseye', F(BOLD, 96), 945, CREAM), ('"yakışır mı?"', F(ACC, 116), 1070, PLUM), ('diye sorma.', F(BOLD, 96), 1215, CREAM)], t0=0.4)
    text_a(c, (76, 1380), 'Sevdiysen giy. Gerisi detay.', F(MED, 44), CREAM, ease((t - 1.9) / 0.5))
    cta(c, t, (W // 2, 1540), 'Annene, teyzene, kızına gönder ›', CREAM, RED, 2.4, 34)
    logo(c, 'A', True); return c

# ---------- Pazar 22
def g1(t):  # 10:30 Filtresiz pazar
    def ill(c, d, t):
        cx, cy = 790, 500
        k = back((t - 0.2) / 0.5)
        if k > 0:
            for j, (dx, dy, col) in enumerate([(-120, 40, CREAM), (60, -40, PINK), (150, 110, (255, 196, 92))]):
                kk = back((t - 0.3 - j * 0.25) / 0.4)
                if kk <= 0: continue
                x = cx + dx; y = cy + dy + 10 * math.sin(t * 2 + j)
                d.rounded_rectangle([x - 60 * kk, y - 110 * kk, x + 60 * kk, y + 110 * kk], radius=int(28 * kk) + 1, fill=col)
                d.rounded_rectangle([x - 40 * kk, y - 150 * kk, x + 40 * kk, y - 105 * kk], radius=int(10 * kk) + 1, fill=PLUM)
            text_a(c, (cx + 60, cy - 50), 'SPF', F(BOLD, 40), PLUM, ease((t - 1.0) / 0.4), anchor='mm')
    return promo(t, BERRY, (120, 12, 60), 'FİLTRESİZ', (CREAM, BERRY),
                 [('Pazar yüzü:', F(BOLD, 110), CREAM), ('makyajsız,', F(ACC, 120), PINK), ('dinlenmiş.', F(BOLD, 110), CREAM)],
                 ['Bugün sadece temizle, nemlendir,', 'güneş kremi sür. Cildin de tatilde.'], 'Bugün makyajsız mısın?', ill, 'A', (CREAM, BERRY))

def g2(t):  # 13:00 D/Y pahalı krem
    return truefalse(t, CREAM, BERRY, PINK, PLUM, 'CİLT BAKIMI TESTİ', ['"Pahalı krem', 'her zaman daha', 'iyi çalışır."'], 'YANLIŞ!',
                     ['Etkiyi fiyat değil; içerik,', 'formül ve düzenli kullanım', 'belirler. Etiketi oku,', 'markaya değil içeriğe bak.'], fg1=PLUM)

def g3(t):  # 19:00 30'lara not — IMG_4218
    return photo_story(t, 'ayakkabi/IMG_4218.jpg', (0.5, 0.5), "30'LARA NOT", (PINK, PLUM),
                       [('Siyah sivri bot', F(BOLD, 96), 1040, CREAM), ('= kışın yarısı.', F(ACC, 104), 1160, PINK)],
                       ('Jean, etek, takım: hepsini tamamlar.', 1320), 'Kaydet, dolabına bak ›')

fns = dict(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3, d1=d1, d2=d2, d3=d3,
           e1=e1, e2=e2, e3=e3, f1=f1, f2=f2, f3=f3, g1=g1, g2=g2, g3=g3)
DATES = dict(a='1116', b='1117', c='1118', d='1119', e='1120', f='1121', g='1122')
SLOT = {'1': '1030', '2': '1300', '3': '1900'}
if __name__ == '__main__':
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
