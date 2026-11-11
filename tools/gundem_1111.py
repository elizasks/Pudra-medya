"""PUDRA GÜNDEM — 11.11 Bekarlar Günü: güzellik sepetini ödemeden önce 4 soru (11 Kasım 2026)."""
from anim import *
from illus import bubble
import sys, os
W, H = 1080, 1350
OUT = 'out_1111'; os.makedirs(OUT, exist_ok=True)
GOLD = (226, 184, 86)

# ---------- illüstrasyonlar
def lipstick(d, x, y, s, col=RED):
    d.rounded_rectangle([x - 22 * s, y - 10 * s, x + 22 * s, y + 70 * s], radius=6 * s, fill=GOLD)
    d.rectangle([x - 16 * s, y - 50 * s, x + 16 * s, y - 10 * s], fill=col)
    d.polygon([(x - 16 * s, y - 50 * s), (x + 16 * s, y - 72 * s), (x + 16 * s, y - 50 * s)], fill=col)

def jar(d, x, y, s, body=PINK, lid=PLUM):
    d.rounded_rectangle([x - 50 * s, y - 20 * s, x + 50 * s, y + 55 * s], radius=14 * s, fill=body)
    d.rounded_rectangle([x - 56 * s, y - 46 * s, x + 56 * s, y - 18 * s], radius=8 * s, fill=lid)

def bottle(d, x, y, s, body=CREAM, cap=BERRY):
    d.rounded_rectangle([x - 34 * s, y - 40 * s, x + 34 * s, y + 70 * s], radius=16 * s, fill=body)
    d.rectangle([x - 12 * s, y - 70 * s, x + 12 * s, y - 40 * s], fill=cap)
    d.rounded_rectangle([x - 20 * s, y - 92 * s, x + 20 * s, y - 68 * s], radius=6 * s, fill=cap)

def basket(c, t, cx, cy, col=CREAM, stroke=PLUM, sc=1.0, items=True):
    """Alışveriş sepeti; ürünler sırayla zıplayarak içine düşer."""
    d = ImageDraw.Draw(c)
    s = sc
    # ürünler (sepetin arkasında)
    if items:
        prods = [(lambda x, y: lipstick(d, x, y, 1.15 * s), -95, 0.3),
                 (lambda x, y: bottle(d, x, y, 1.1 * s), 10, 0.6),
                 (lambda x, y: jar(d, x, y, 1.0 * s), 105, 0.9)]
        for fn, dx, st in prods:
            k = ease((t - st) / 0.45)
            if k <= 0: continue
            bob = math.sin(t * 3 + dx) * 4 * s
            y = cy - 60 * s - (1 - k) * 300 * s + bob
            if k >= 1: y -= abs(math.sin((t - st - 0.45) * 7)) * 10 * s * max(0, 1 - (t - st - 0.45))
            fn(cx + dx * s, y)
    # sepet gövdesi
    top = cy - 20 * s
    d.polygon([(cx - 210 * s, top), (cx + 210 * s, top), (cx + 165 * s, cy + 170 * s), (cx - 165 * s, cy + 170 * s)], fill=col)
    for k in range(1, 5):
        x = cx - 210 * s + k * 84 * s; xb = cx - 165 * s + k * 66 * s
        d.line([(x, top + 18 * s), (xb, cy + 160 * s)], fill=stroke, width=max(3, int(7 * s)))
    d.line([(cx - 195 * s, cy + 75 * s), (cx + 195 * s, cy + 75 * s)], fill=stroke, width=max(3, int(7 * s)))
    d.rounded_rectangle([cx - 225 * s, top - 22 * s, cx + 225 * s, top + 8 * s], radius=10 * s, fill=stroke)
    d.arc([cx - 170 * s, top - 200 * s, cx + 170 * s, top + 120 * s], 200, 340, fill=stroke, width=max(4, int(12 * s)))

def il_cover(c, t, cx, cy):
    basket(c, t, cx, cy, CREAM, PLUM, 0.85)
    d = ImageDraw.Draw(c)
    s = back((t - 1.4) / 0.4) * (1 + 0.05 * math.sin(t * 7))
    sticker(c, (cx + 150, cy - 160), '%40', F(BOLD, 52), RED, CREAM, 12, s, 26, 12)
    s = back((t - 1.7) / 0.4)
    sticker(c, (cx + 10, cy - 300), '%25', F(BOLD, 40), PINK, PLUM, -10, s, 22, 10)
    for k, (x, y) in enumerate([(cx + 250, cy - 60), (cx - 260, cy + 40)]):
        f = back((t - 1.0 - k * 0.3) / 0.4)
        if f > 0: sparkle(d, x, y, (26 + 5 * math.sin(t * 5 + k)) * f, PINK)

def il_clock(c, t, cx, cy):
    """23:59'a geri sayan saat + takvim yaprağı."""
    d = ImageDraw.Draw(c)
    # takvim
    k = back((t - 0.3) / 0.4)
    if k > 0:
        cal = Image.new('RGBA', (240, 250), (0, 0, 0, 0)); cd = ImageDraw.Draw(cal)
        cd.rounded_rectangle([0, 0, 239, 249], radius=26, fill=CREAM)
        cd.rounded_rectangle([0, 0, 239, 70], radius=26, fill=RED); cd.rectangle([0, 40, 239, 70], fill=RED)
        cd.text((120, 50), 'KASIM', font=F(BOLD, 34), fill=CREAM, anchor='ms')
        cd.text((120, 200), '11', font=F(BOLD, 120), fill=PLUM, anchor='ms')
        cal = cal.resize((max(1, int(240 * k)), max(1, int(250 * k))), Image.LANCZOS).rotate(-8 + 3 * math.sin(t * 2), expand=True, resample=Image.BICUBIC)
        c.paste(cal, (int(cx - 250 - cal.width / 2), int(cy - cal.height / 2)), cal)
    # dijital saat
    a = ease((t - 0.6) / 0.4)
    if a > 0:
        x0, y0 = cx - 40, cy - 95
        d.rounded_rectangle([x0, y0, x0 + 420, y0 + 190], radius=34, fill=PLUM, outline=RED, width=8)
        sec = max(0, 50 + int(t * 1.6)) % 60
        colon = ':' if int(t * 2) % 2 == 0 else ' '
        d.text((x0 + 210, y0 + 120), f'23{colon}59', font=F(BOLD, 110), fill=CREAM, anchor='ms')
        d.text((x0 + 210, y0 + 170), 'bu gece', font=F(MED, 26), fill=PINK, anchor='ms')
    s = back((t - 1.6) / 0.4)
    bubble(c, cx + 200, cy - 170, 'Bu gece bitiyor', F(BOLD, 32), RED, CREAM, s, -5, 'left')

def il_pao(c, t, cx, cy, fg=CREAM, bg=PLUM):
    """Açık kavanoz simgesi: kapak açılır, 12M yazar."""
    d = ImageDraw.Draw(c)
    k = ease((t - 0.4) / 0.6)
    # kavanoz gövdesi
    d.rounded_rectangle([cx - 110, cy - 40, cx + 110, cy + 130], radius=22, outline=fg, width=10)
    d.text((cx, cy + 82), '12M', font=F(BOLD, 64), fill=fg, anchor='ms')
    # kapak (açılıyor)
    ang = -30 * k
    lid = Image.new('RGBA', (280, 60), (0, 0, 0, 0)); ld = ImageDraw.Draw(lid)
    ld.rounded_rectangle([20, 10, 260, 50], radius=10, outline=fg + (255,), width=10)
    lid = lid.rotate(-ang, expand=True, resample=Image.BICUBIC)
    c.paste(lid, (int(cx - 135), int(cy - 30 - lid.height + 22 - 12 * k)), lid)
    s = back((t - 1.2) / 0.4)
    bubble(c, cx + 270, cy - 30, 'Açınca 12 ay', F(BOLD, 32), RED, CREAM, s, 4, 'left')

def il_threshold(c, t, cx, cy, fg=PLUM):
    """Sepet tutarı alt limite doğru dolan çubuk."""
    d = ImageDraw.Draw(c)
    x0, x1, y = cx - 380, cx + 380, cy
    d.rounded_rectangle([x0, y - 34, x1, y + 34], radius=34, fill=PINK)
    k = min(0.82, ease((t - 0.4) / 1.4) * 0.82)
    if k > 0.05: d.rounded_rectangle([x0, y - 34, x0 + (x1 - x0) * k, y + 34], radius=34, fill=BERRY)
    d.text((x0 + 20, y + 82), 'Sepet: 410 TL', font=F(BOLD, 32), fill=fg)
    d.text((x1, y + 82), 'İndirim için: 500 TL', font=F(BOLD, 32), fill=RED, anchor='ra')
    # bayrak çizgisi
    d.line([(x1 - 6, y - 70), (x1 - 6, y + 40)], fill=RED, width=6)
    s = back((t - 1.9) / 0.4) * (1 + 0.04 * math.sin(t * 6))
    bubble(c, cx - 120, cy - 110, '+1 ürün daha mı?', F(BOLD, 34), PLUM, CREAM, s, -4, 'right')
    s = back((t - 2.5) / 0.4)
    sticker(c, (cx + 240, cy - 110), 'GEREK YOK', F(BOLD, 34), RED, CREAM, 8, s, 24, 12)

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
    blobs(c, t, RED, (W - 60, 1180), 360)
    r2 = int(220 * ease(t / 0.8)); d.ellipse([-r2 + 40, 380 - r2, 40 + r2, 380 + r2], fill=(120, 12, 60))
    dots(d, 830, 230, 5, 3, 44, 6, (180, 60, 110))
    sticker(c, (360, 245), 'PUDRA GÜNDEM · 11.11', F(BOLD, 32), CREAM, BERRY, -4, back((t - 0.1) / 0.4))
    a = ease((t - 0.3) / 0.6); text_a(c, (60, 300), '11.11', F(BOLD, 250), PINK, a, int(50 * (1 - a)))
    for txt, font, y, st, col in [('Sepetin dolu,', F(BOLD, 88), 610, 0.7, CREAM),
                                  ('kafan net mi?', F(ACC, 104), 715, 0.95, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (68, y), txt, font, col, a, int(36 * (1 - a)))
    a = ease((t - 1.4) / 0.5)
    text_a(c, (70, 880), 'Güzellikte 11.11 indirimleri', F(MED, 38), CREAM, a)
    text_a(c, (70, 932), 'birçok markada bu gece bitiyor.', F(MED, 38), CREAM, a)
    il_cover(c, max(0, t - 0.6), 810, 1185)
    a = ease((t - 2.2) / 0.4)
    text_a(c, (70, 1080), 'Ödemeden önce', F(BOLD, 46), CREAM, a)
    text_a(c, (70, 1138), '4 soru.', F(ACC, 60), PINK, a)
    if a > 0: text_a(c, (70 + int(8 * math.sin(t * 6)), 1240), 'kaydır  ›', F(BOLD, 38), CREAM, a)
    logo(c, 'A'); return c

# ---------- 2 · NE OLUYOR
def p2(t):
    c = Image.new('RGB', (W, H), PINK); d = ImageDraw.Draw(c)
    blobs(c, t, (236, 170, 192), (W - 80, 260), 300)
    sticker(c, (W - 300, 110), 'NE OLUYOR?', F(BOLD, 30), BERRY, CREAM, 5, back((t - 0.2) / 0.4))
    for txt, font, y, st, col in [('11.11 =', F(BOLD, 110), 230, 0.3, BERRY),
                                  ('Bekarlar Günü', F(ACC, 104), 360, 0.55, PLUM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    body = ["Tarihteki dört tane 1, Çin'de üniversite öğrencilerinin",
            "bekarlık şakasıydı. 2009'da dev bir online",
            "alışveriş festivaline dönüştü."]
    a = ease((t - 1.0) / 0.5)
    y = 520
    for ln in body: text_a(c, (72, y), ln, F(REG, 36), PLUM, a); y += 50
    a = ease((t - 1.4) / 0.5)
    y += 20
    for ln in ['Bu yıl güzellik markalarında %25 ile %45', "arası sepet indirimleri var. Birçoğu", 'bu gece 23:59\'da bitiyor.']:
        text_a(c, (72, y), ln, F(BOLD, 38), BERRY, a); y += 52
    wave_line(d, 0, W * ease((t - 1.2) / 0.8), y + 30, 12, 170, BERRY, 5, -t * 2)
    il_clock(c, max(0, t - 0.8), 560, 1090)
    footer(c, 2, PLUM)
    logo(c, 'B'); return c

# ---------- 3–4 · SORULAR
def qpage(i, qs, bg, blob, tc, sc, nc, lv, ill):
    def fn(t):
        c = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(c)
        blobs(c, t, blob, (W - 100, 1150), 330)
        sticker(c, (W - 290, 110), 'SANA NE DEMEK?', F(BOLD, 30), RED, CREAM, -5, back((t - 0.2) / 0.4))
        y = 220
        for j, (num, title, body) in enumerate(qs):
            st = 0.3 + j * 0.9
            a = ease((t - st) / 0.5)
            text_a(c, (70 - int(40 * (1 - a)), y), num, F(BOLD, 90), nc, a)
            TL = wrap(F(BOLD, 56), title, W - 330)
            yy = y + 8
            for ln in TL:
                aa = ease((t - st - 0.15) / 0.45); text_a(c, (250, yy), ln, F(BOLD, 56), tc, aa, int(24 * (1 - aa))); yy += 66
            yy += 8
            aa = ease((t - st - 0.4) / 0.5)
            for ln in wrap(F(REG, 34), body, W - 330): text_a(c, (252, yy), ln, F(REG, 34), sc, aa); yy += 46
            y = max(yy, y + 200) + 50
        ill(c, max(0, t - 1.6), y)
        footer(c, i, sc)
        logo(c, lv); return c
    return fn

def ill3(c, t, y):
    il_pao(c, t, 420, max(y + 200, 940))

def ill4(c, t, y):
    il_threshold(c, t, W // 2, max(y + 230, 920))

p3 = qpage(3, [('01', 'Bunu zaten kullanıyor muyum?',
                'Bildiğin favoriyi stokla. Hiç denemediğin bir ürünü indirim var diye dev boy alma.'),
               ('02', 'Açınca kaç ay dayanır?',
                "Ambalajdaki açık kavanoz simgesi (6M, 12M) açıldıktan sonraki süreyi söyler. 3 serum stoklamadan önce bak.")],
           PLUM, BERRY, CREAM, PINK, RED, 'B', ill3)
p4 = qpage(4, [('03', 'İndirimin şartı ne?',
                "Çoğu sepet indirimi alt limit ya da '2 al' ister. Limiti tutturmak için ihtiyacın olmayanı ekleme."),
               ('04', 'Set gerçekten ucuz mu?',
                'Setteki ürünlerin tek tek fiyatını topla. Kullanmayacağın mini boylar indirim değil.')],
           CREAM, PINK, PLUM, BERRY, RED, 'A', ill4)

# ---------- 5 · SORU
def p5(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1220), 380)
    sparkle(d, 930, 300, 30 + 6 * math.sin(t * 4), PINK)
    for txt, font, y, st, col in [('Senin sepetinde', F(BOLD, 86), 220, 0.2, CREAM),
                                  ('ne var?', F(ACC, 120), 320, 0.5, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    opts = [('A', 'Yıllardır kullandığım favori'), ('B', 'İlk kez deneyeceğim yenilik'), ('C', 'Sepeti boşalttım, cüzdan mutlu')]
    y = 540
    for k, (l, txt) in enumerate(opts):
        s = ease((t - 0.9 - k * 0.3) / 0.45)
        if s > 0:
            x = 70 - int(60 * (1 - s))
            d.rounded_rectangle([x, y, x + 860, y + 104], radius=52, fill=CREAM)
            d.ellipse([x + 14, y + 12, x + 94, y + 92], fill=PLUM)
            d.text((x + 54, y + 70), l, font=F(BOLD, 48), fill=CREAM, anchor='ms')
            d.text((x + 120, y + 70), txt, font=F(BOLD, 40), fill=PLUM, anchor='ls')
        y += 130
    basket(c, max(0, t - 1.6), 830, 1150, CREAM, PLUM, 0.55)
    sticker(c, (380, 1010), 'Harfini yorumlara yaz ›', F(BOLD, 42), PLUM, CREAM, -3,
            back((t - 2.2) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 36, 18)
    a = ease((t - 2.7) / 0.4)
    text_a(c, (72, 1120), 'Sepeti taşan arkadaşına', F(BOLD, 40), CREAM, a)
    text_a(c, (72, 1172), 'gönder.', F(ACC, 52), PINK, a)
    footer(c, 5, CREAM)
    logo(c, 'A'); return c

# ---------- STORY
def story(t):
    SW, SH = 1080, 1920
    c = Image.new('RGB', (SW, SH), BERRY); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 22; r = int(330 * ease(t / 0.8))
    d.ellipse([1100 - r - p, 1700 - r - p, 1100 + r + p, 1700 + r + p], fill=RED)
    dots(d, 800, 420, 5, 3, 44, 6, (180, 60, 110))
    sticker(c, (320, 420), 'PUDRA GÜNDEM · 11.11', F(BOLD, 34), CREAM, BERRY, -5, back((t - 0.1) / 0.4))
    a = ease((t - 0.3) / 0.6); text_a(c, (60, 480), '11.11', F(BOLD, 240), PINK, a, int(40 * (1 - a)))
    for txt, font, y, st, col in [('bu gece bitiyor.', F(ACC, 92), 780, 0.6, CREAM),
                                  ('Ödemeden önce', F(BOLD, 72), 920, 0.9, CREAM),
                                  ('4 soruya bak.', F(BOLD, 72), 1005, 1.1, CREAM)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    basket(c, max(0, t - 1.0), 700, 1330, CREAM, PLUM, 0.85)
    s2 = back((t - 2.2) / 0.45)
    if s2 > 0: sticker(c, (SW // 2 + int(8 * math.sin(t * 6)), 1570), 'Yeni gönderide ›', F(BOLD, 46), PLUM, CREAM, -2, s2, 42, 22)
    logo(c, 'B', True); return c

PAGES = [p1, p2, p3, p4, p5]
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
