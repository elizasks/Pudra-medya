"""PUDRA GÜNDEM v2 — Met Gala 2027: Pudra'nın hayal ettiği gündelik gala elbiseleri (oylama)."""
from anim import *
from pudra import fit
import sys, os
W, H = 1080, 1350
PH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'photos', 'gundem') + '/'
OUT = 'out_gm2'; os.makedirs(OUT, exist_ok=True)
_c = {}
def img(name, size):
    k = (name, size)
    if k not in _c: _c[k] = fit(load(PH + name), size)
    return _c[k]

def kb(name, t, box=(W, H), zoom=0.07, pan=(0, 0)):
    """Yavaş yakınlaşma (Ken Burns)."""
    z = 1 + zoom * min(t, 6) / 6
    big = img(name, (int(box[0] * 1.07), int(box[1] * 1.07)))
    cw, ch = int(box[0] * 1.07 / z), int(box[1] * 1.07 / z)
    ox = (big.width - cw) // 2 + int(pan[0] * (z - 1) * 400); oy = (big.height - ch) // 2 + int(pan[1] * (z - 1) * 400)
    return big.crop((ox, oy, ox + cw, oy + ch)).resize(box, Image.LANCZOS)

def grad(c, top, h, col, amax):
    g = Image.new('L', (1, h))
    for i in range(h): g.putpixel((0, i), int(amax * (i / h) ** 1.4))
    g = g.resize((c.width, h)); solid = Image.new('RGB', (c.width, h), col)
    reg = c.crop((0, top, c.width, top + h)); c.paste(Image.composite(solid, reg, g), (0, top))

def ai_tag(c, x, y, a=1):
    text_a(c, (x, y), 'Pudra hayal etti · yapay zekâ görseli', F(MED, 22), PINK, a, anchor='ra')

# ---------- 1 · KAPAK (müze salonu)
def cover(t):
    c = kb('metgala_salon.png', t, zoom=0.08)
    grad(c, 620, 730, PLUM, 245)
    sticker(c, (300, 735), 'PUDRA GÜNDEM · MET GALA 2027', F(BOLD, 30), RED, CREAM, -4, back((t - 0.2) / 0.4))
    for txt, font, y, st, col in [('Kotun, tişörtün,', F(BOLD, 86), 800, 0.5, CREAM),
                                  ('trençkotun…', F(BOLD, 86), 900, 0.75, CREAM),
                                  ('artık müzelik.', F(ACC, 110), 1010, 1.05, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(40 * (1 - a)))
    a = ease((t - 1.6) / 0.5)
    text_a(c, (72, 1170), "2027 Met Gala teması: gündelik kıyafet.", F(MED, 36), CREAM, a)
    a = ease((t - 2.2) / 0.4)
    if a > 0: text_a(c, (72, 1260), 'Biz 5 gala elbisesi hayal ettik.  kaydır ›', F(BOLD, 32), PINK, a)
    ai_tag(c, W - 40, 1310, ease((t - 0.5) / 0.5))
    logo(c, 'A'); return c

# ---------- 2–6 · ELBİSELER
LOOKS = [('metgala_kot.png', 'Kot', 'Denim, kırmızı halıda.', (0, -0.3)),
         ('metgala_kapusonlu.png', 'Kapüşonlu', 'Konfor da şık olabilir.', (0, -0.4)),
         ('metgala_tisort.png', 'Beyaz tişört', 'En sade parça, en büyük etek.', (0, -0.4)),
         ('metgala_sisme.png', 'Şişme mont', 'Kışın en sıcak gala elbisesi.', (0, -0.4)),
         ('metgala_trenc.png', 'Trençkot', 'Klasik ama dramalı.', (0, -0.4))]
def look(i):
    name, title, note, pan = LOOKS[i]
    last = i == len(LOOKS) - 1
    def fn(t):
        c = kb(name, t, zoom=0.06, pan=pan)
        grad(c, 760 if not last else 560, 590 if not last else 790, PLUM, 240)
        d = ImageDraw.Draw(c)
        # numara rozeti
        s = back((t - 0.2) / 0.45)
        if s > 0:
            R = int(78 * s); cx, cy = W - 130, 140
            d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=RED)
            if s > 0.5: text_a(c, (cx, cy + int(30 * s)), f'0{i+1}', F(BOLD, max(8, int(80 * s))), CREAM, 1, anchor='ms')
        if not last:
            a = ease((t - 0.5) / 0.5); text_a(c, (70, 1040), title, F(BOLD, 96), CREAM, a, int(30 * (1 - a)))
            a = ease((t - 0.8) / 0.5); text_a(c, (72, 1150), 'gala elbisesi', F(ACC, 64), PINK, a, int(20 * (1 - a)))
            a = ease((t - 1.3) / 0.5); text_a(c, (72, 1240), note, F(MED, 38), CREAM, a)
        else:
            a = ease((t - 0.4) / 0.5); text_a(c, (70, 830), f'{title} gala elbisesi', F(BOLD, 50), PINK, a)
            for txt, font, y, st, col in [('Hangisini', F(BOLD, 104), 900, 0.8, CREAM), ('giyerdin?', F(ACC, 112), 1015, 1.05, PINK)]:
                a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
            a = ease((t - 1.6) / 0.5)
            text_a(c, (72, 1170), '01 Kot · 02 Kapüşonlu · 03 Tişört · 04 Şişme mont · 05 Trenç', F(MED, 28), CREAM, a)
            sticker(c, (330, 1262), 'Numarasını yorumlara yaz ›', F(BOLD, 36), RED, CREAM, -3,
                    back((t - 2.1) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 34, 16)
        ai_tag(c, W - 40, 1318 if not last else 1325, 1)
        logo(c, 'A'); return c
    return fn

# ---------- STORY
def story(t):
    SW, SH = 1080, 1920
    c = Image.new('RGB', (SW, SH), BERRY); d = ImageDraw.Draw(c)
    p = math.sin(t * 1.5) * 22; r = int(300 * ease(t / 0.8))
    d.ellipse([1100 - r - p, 1900 - r - p, 1100 + r + p, 1900 + r + p], fill=RED)
    sticker(c, (300, 370), 'PUDRA GÜNDEM', F(BOLD, 34), CREAM, BERRY, -5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Met Gala 2027', F(BOLD, 92), 450, 0.3, CREAM), ('teması: gündelik kıyafet.', F(ACC, 72), 560, 0.6, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    a = ease((t - 0.8) / 0.6)
    if a > 0:
        ph = kb('metgala_kot.png', t, box=(820, 820), zoom=0.07, pan=(0, -0.3))
        m = Image.new('L', ph.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, 819, 819], radius=40, fill=int(255 * a))
        c.paste(ph, (130, 700 + int(40 * (1 - a))), m)
    text_a(c, (SW - 130, 1540), 'Pudra hayal etti · yapay zekâ görseli', F(MED, 22), PINK, a, anchor='ra')
    s2 = back((t - 2.2) / 0.45)
    if s2 > 0: sticker(c, (SW // 2 + int(8 * math.sin(t * 6)), 1610), 'Hangisini giyerdin? Postta ›', F(BOLD, 42), PLUM, CREAM, 0, s2, 40, 22)
    logo(c, 'B', True); return c

PAGES = [cover] + [look(i) for i in range(5)]
if __name__ == '__main__':
    arg = sys.argv[1]
    if arg == 'preview':
        tt = float(sys.argv[2]) if len(sys.argv) > 2 else 5
        fr = [f(tt) for f in PAGES]
        s = Image.new('RGB', (3 * 550 + 10, 2 * 685 + 10), (230, 230, 230))
        for k, im in enumerate(fr): s.paste(im.resize((540, 675)), ((k % 3) * 550 + 10, (k // 3) * 685 + 10))
        s.save(f'{OUT}/sheet.jpg', quality=85)
        story(tt).resize((540, 960)).save(f'{OUT}/st.jpg', quality=85)
    elif arg == 'story':
        render(story, f'{OUT}/story.mp4', 6, (1080, 1920), f'{OUT}/story.jpg')
    else:
        i = int(arg); render(PAGES[i - 1], f'{OUT}/p{i}.mp4', 6, (W, H), f'{OUT}/p{i}.jpg')
