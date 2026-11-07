"""Kırmızı bayrak sayfaları için hareketli illüstrasyonlar."""
import math
from PIL import Image, ImageDraw, ImageFilter
from anim import F, BOLD, MED, ease, back
from pudra import BERRY, CREAM, PLUM, PINK, RED

SKIN = (236, 196, 166)
SKIN2 = (196, 140, 108)
GREY = (205, 200, 206)
HAIRS = [PLUM, (122, 62, 34), (226, 184, 86)]


def bubble(c, x, y, txt, font, bg, fg, scale=1.0, angle=0, tail='left', pad=(26, 14)):
    if scale <= 0.02: return
    d0 = ImageDraw.Draw(Image.new('RGB', (1, 1)))
    tw = d0.textlength(txt, font=font); bb = font.getbbox(txt); th = bb[3] - bb[1]
    w, h = int(tw + 2 * pad[0]), int(th + 2 * pad[1])
    s = Image.new('RGBA', (w + 40, h + 40), (0, 0, 0, 0)); sd = ImageDraw.Draw(s)
    sd.rounded_rectangle([20, 10, 20 + w, 10 + h], radius=min(28, h // 2), fill=bg)
    if tail == 'left':
        sd.polygon([(34, 6 + h), (30, 36 + h), (60, 6 + h)], fill=bg)
    else:
        sd.polygon([(w - 10, 6 + h), (w + 8, 36 + h), (w - 40, 6 + h)], fill=bg)
    sd.text((20 + pad[0], 10 + pad[1] - bb[1]), txt, font=font, fill=fg)
    if scale != 1: s = s.resize((max(1, int(s.width * scale)), max(1, int(s.height * scale))), Image.LANCZOS)
    if angle: s = s.rotate(angle, expand=True, resample=Image.BICUBIC)
    c.paste(s, (int(x - s.width / 2), int(y - s.height / 2)), s)


def heart_pts(cx, cy, s, n=60):
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        x = 16 * math.sin(a) ** 3
        y = 13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)
        pts.append((cx + x * s / 16, cy - y * s / 16))
    return pts


# 1) Garsona kaba davranıyor -------------------------------------------------
def waiter(c, t, cx=800, cy=360, dark=PLUM):
    d = ImageDraw.Draw(c)
    shake = math.sin(t * 45) * 7 if 0.95 < t < 1.6 else 0
    x = cx + shake
    # gövde
    d.rounded_rectangle([x - 40, cy - 60, x + 110, cy + 170], radius=40, fill=dark)
    d.polygon([(x + 5, cy - 60), (x + 65, cy - 60), (x + 35, cy + 20)], fill=CREAM)
    d.polygon([(x + 35, cy - 48), (x + 15, cy - 60), (x + 15, cy - 36)], fill=RED)
    d.polygon([(x + 35, cy - 48), (x + 55, cy - 60), (x + 55, cy - 36)], fill=RED)
    # kol + tepsi
    wob = math.sin(t * 9) * (6 if t > 0.95 else 1.5)
    d.line([(x + 95, cy - 25), (x + 160, cy - 115)], fill=dark, width=30)
    d.ellipse([x + 145, cy - 140, x + 180, cy - 105], fill=SKIN)
    tray = Image.new('RGBA', (200, 120), (0, 0, 0, 0)); td = ImageDraw.Draw(tray)
    td.ellipse([10, 80, 190, 104], fill=GREY)
    td.polygon([(80, 20), (120, 20), (112, 82), (88, 82)], fill=CREAM)
    td.polygon([(84, 46), (116, 46), (112, 82), (88, 82)], fill=PINK)
    tray = tray.rotate(wob, resample=Image.BICUBIC)
    c.paste(tray, (int(x + 65), int(cy - 210)), tray)
    # kafa
    d.ellipse([x - 12, cy - 175, x + 92, cy - 70], fill=SKIN)
    d.pieslice([x - 14, cy - 182, x + 94, cy - 100], 180, 360, fill=dark)
    big = t > 0.95
    er = 9 if big else 5
    for ex in (x + 22, x + 58):
        d.ellipse([ex - er, cy - 125 - er, ex + er, cy - 125 + er], fill=CREAM if big else dark)
        if big: d.ellipse([ex - 4, cy - 129, ex + 4, cy - 121], fill=dark)
    if big: d.ellipse([x + 32, cy - 98, x + 48, cy - 82], fill=dark)
    else: d.line([(x + 30, cy - 92), (x + 50, cy - 92)], fill=dark, width=4)
    # ter damlası
    if t > 1.2:
        k = ((t - 1.2) % 1.4) / 1.4
        sy = cy - 150 + k * 90; a = int(255 * (1 - k))
        lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ld.ellipse([x + 92, sy, x + 110, sy + 22], fill=(150, 200, 255, a))
        ld.polygon([(x + 92, sy + 9), (x + 101, sy - 12), (x + 110, sy + 9)], fill=(150, 200, 255, a))
        c.paste(lay, (0, 0), lay)
    # müşterinin şıklatan eli
    hx = cx - 330 + 160 * ease((t - 0.3) / 0.45)
    hy = cy + 10
    d.rectangle([cx - 430, hy - 18, hx - 20, hy + 18], fill=SKIN2)
    d.ellipse([hx - 40, hy - 34, hx + 24, hy + 34], fill=SKIN2)
    d.rounded_rectangle([hx + 4, hy - 46, hx + 26, hy - 8], radius=10, fill=SKIN2)
    d.rounded_rectangle([hx - 30, hy - 52, hx - 8, hy - 14], radius=10, fill=SKIN2)
    for k in range(3):
        snap = (t - 0.75 - k * 0.55)
        if 0 < snap < 0.35:
            a = 1 - snap / 0.35; L = 24 + 30 * (1 - a)
            for ang in (-60, -20, 20):
                r = math.radians(ang)
                x0 = hx + 30 + 20 * math.cos(r); y0 = hy - 60 + 20 * math.sin(r)
                d.line([(x0, y0), (x0 + L * math.cos(r), y0 + L * math.sin(r))], fill=RED, width=6)
    # konuşma balonu
    s = back((t - 0.8) / 0.35)
    jit = math.sin(t * 30) * 3 if t > 0.8 else 0
    bubble(c, cx - 200 + jit, cy - 170, 'Hey, garson!', F(BOLD, 34), RED, CREAM, s, 4, 'right')


# 2) Bütün eski sevgilileri deli --------------------------------------------
def runner(c, x, y, t, k, face, scale, outline):
    d = ImageDraw.Draw(c)
    sw = math.sin(t * 16 + k * 2)
    # bacaklar
    for sgn in (1, -1):
        a = sgn * sw * 0.7
        d.line([(x, y - 30 * scale), (x + face * math.sin(a) * 55 * scale, y + 30 * scale)],
               fill=outline, width=int(9 * scale))
    # elbise
    d.polygon([(x - 32 * scale, y - 20 * scale), (x + 32 * scale, y - 20 * scale), (x, y - 100 * scale)],
              fill=[BERRY, PINK, CREAM][k])
    # kollar
    for sgn in (1, -1):
        a = -sgn * sw * 0.9
        d.line([(x, y - 80 * scale), (x + face * math.sin(a) * 45 * scale, y - 55 * scale)],
               fill=SKIN, width=int(8 * scale))
    # saç arkası + kafa
    hy = y - 125 * scale; hr = 26 * scale
    flow = -face * (12 + 6 * math.sin(t * 12 + k)) * scale
    d.ellipse([x - hr + flow - 6, hy - hr, x + hr + flow + 6, hy + hr + 30 * scale], fill=HAIRS[k])
    d.ellipse([x - hr, hy - hr, x + hr, hy + hr], fill=SKIN)
    d.chord([x - hr - 2, hy - hr - 4, x + hr + 2, hy + hr * 0.5], 180, 360, fill=HAIRS[k])
    d.ellipse([x + face * 8 * scale - 3, hy - 3, x + face * 8 * scale + 3, hy + 3], fill=outline)
    d.ellipse([x + face * 8 * scale - 6, hy + 10 * scale - 5, x + face * 8 * scale + 6, hy + 10 * scale + 5], fill=outline)
    # başında dönen spiral
    sp = []
    for i in range(30):
        a = i / 29 * 4 * math.pi + t * 8
        r = 2 + i * 0.55 * scale
        sp.append((x + r * math.cos(a), hy - 55 * scale + r * 0.6 * math.sin(a)))
    d.line(sp, fill=outline, width=3)


def exes(c, t, cx=800, cy=380, outline=CREAM):
    figs = []
    for k in range(3):
        ph = t * 2.4 + k * 2.094
        x = cx + 200 * math.cos(ph); y = cy + 60 * math.sin(ph)
        face = 1 if -math.sin(ph) > 0 else -1
        sc = 0.85 + 0.15 * (math.sin(ph) + 1) / 2
        figs.append((y, x, k, face, sc))
    d = ImageDraw.Draw(c)
    for k in range(3):  # toz bulutları
        ph = t * 2.4 + k * 2.094 - 0.35
        x = cx + 200 * math.cos(ph); y = cy + 60 * math.sin(ph) + 30
        r = 10 + 4 * math.sin(t * 10 + k)
        d.ellipse([x - r, y - r * 0.6, x + r, y + r * 0.6], fill=outline)
    for y, x, k, face, sc in sorted(figs):
        runner(c, x, y, t, k, face, sc, outline)
    s = back((t - 0.6) / 0.4)
    bubble(c, cx - 190, cy - 175, 'Hepsi deli!', F(BOLD, 34), CREAM, PLUM, s, -4, 'right')


# 3) Telefon masada ters ------------------------------------------------------
def phone(c, t, cx=800, cy=380, table=PLUM, body=PLUM, line=CREAM):
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([cx - 260, cy + 70, cx + 260, cy + 110], radius=20, fill=table)
    buzz = (t % 1.3) < 0.55 and t > 0.6
    jx = math.sin(t * 70) * 5 if buzz else 0
    jy = math.cos(t * 55) * 2 if buzz else 0
    # alttan sızan bildirim ışığı
    if buzz:
        glow = Image.new('RGBA', c.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
        a = int(170 * (0.6 + 0.4 * math.sin(t * 20)))
        gd.rounded_rectangle([cx - 175, cy - 40, cx + 175, cy + 85], radius=40, fill=PINK + (a,))
        glow = glow.filter(ImageFilter.GaussianBlur(22))
        c.paste(glow, (0, 0), glow)
    x0, y0 = cx - 150 + jx, cy - 20 + jy
    d.rounded_rectangle([x0, y0, x0 + 300, y0 + 85], radius=26, fill=body, outline=line, width=4)
    d.rounded_rectangle([x0 + 18, y0 + 12, x0 + 92, y0 + 72], radius=16, fill=(70, 40, 55))
    for (ex, ey, r) in [(x0 + 40, y0 + 30, 11), (x0 + 70, y0 + 30, 11), (x0 + 40, y0 + 56, 11)]:
        d.ellipse([ex - r, ey - r, ex + r, ey + r], fill=(30, 15, 22), outline=line, width=2)
    d.ellipse([x0 + 64, y0 + 50, x0 + 76, y0 + 62], fill=CREAM)
    if buzz:
        for side, ang in ((-1, 8), (1, -8)):
            bx = cx + side * 220; by = cy - 60 + math.sin(t * 25) * 4
            bubble(c, bx, by, 'bzzz', F(BOLD, 30), CREAM, BERRY, 1.0, ang, 'left' if side < 0 else 'right', (18, 8))
    s = back((t - 1.6) / 0.4)
    bubble(c, cx - 60, cy - 190, 'Yok bir şey, iş.', F(BOLD, 32), CREAM, PLUM, s, -3, 'right')


# 4) Sadece kendini anlatıyor -------------------------------------------------
def talker(c, t, cx=800, cy=380, fg=PLUM, bg=CREAM):
    d = ImageDraw.Draw(c)
    # saat: ibreler hızla dönüyor
    ccx, ccy, r = cx + 150, cy + 60, 78
    d.ellipse([ccx - r, ccy - r, ccx + r, ccy + r], fill=bg, outline=fg, width=7)
    for i in range(12):
        a = i / 12 * 2 * math.pi
        d.line([(ccx + (r - 16) * math.cos(a), ccy + (r - 16) * math.sin(a)),
                (ccx + (r - 6) * math.cos(a), ccy + (r - 6) * math.sin(a))], fill=fg, width=3)
    am = t * 6; ah = t * 0.5
    d.line([(ccx, ccy), (ccx + 58 * math.sin(am), ccy - 58 * math.cos(am))], fill=RED, width=5)
    d.line([(ccx, ccy), (ccx + 38 * math.sin(ah), ccy - 38 * math.cos(ah))], fill=fg, width=7)
    d.ellipse([ccx - 7, ccy - 7, ccx + 7, ccy + 7], fill=fg)
    msgs = ['Ben...', 'Benim işim...', 'Ben bir keresinde...', 'Bende de...']
    for i, m in enumerate(msgs):
        st = 0.3 + i * 0.55
        s = back((t - st) / 0.35)
        if s <= 0: continue
        up = 70 * sum(1 for j in range(i + 1, len(msgs)) if t > 0.3 + j * 0.55)
        y = cy + 40 - up - 0 * i
        if y < cy - 250: continue
        bubble(c, cx - 110, y, m, F(BOLD, 32), fg, bg, s, 0, 'left')
    if t > 2.6:
        a = ease((t - 2.6) / 0.4)
        bubble(c, ccx + 10, ccy - 130, 'zzz', F(BOLD, 30), RED, CREAM, a, 6, 'right', (16, 8))


# 5) Kıskanıyorum çünkü seviyorum ---------------------------------------------
def lockheart(c, t, cx=800, cy=330, fg=CREAM, accent=RED):
    d = ImageDraw.Draw(c)
    sh = math.sin(t * 40) * 6 if 1.05 < t < 1.45 else 0
    beat = 1 + 0.05 * math.sin(t * 7)
    d.polygon(heart_pts(cx + sh, cy, 150 * beat), fill=accent)
    # zincir halkaları kalbin önünden geçiyor
    n = int(9 * ease((t - 0.2) / 0.7))
    for i in range(n):
        x = cx - 210 + i * 52; y = cy + 10 + (i - 4) * 10
        if i % 2 == 0: d.ellipse([x - 26, y - 15, x + 26, y + 15], outline=fg, width=9)
        else: d.ellipse([x - 15, y - 24, x + 15, y + 24], outline=fg, width=9)
    # asma kilit: kilit kolu aşağı iner ve "klik"
    drop = 50 * (1 - ease((t - 0.6) / 0.45))
    lx, ly = cx + 10 + sh, cy + 110
    d.arc([lx - 46, ly - 100 - drop, lx + 46, ly - 10 - drop], 180, 360, fill=fg, width=14)
    d.line([(lx - 39, ly - 55 - drop), (lx - 39, ly - 20)], fill=fg, width=14)
    d.line([(lx + 39, ly - 55 - drop), (lx + 39, ly - 20)], fill=fg, width=14)
    d.rounded_rectangle([lx - 62, ly - 30, lx + 62, ly + 70], radius=18, fill=fg)
    d.ellipse([lx - 12, ly + 2, lx + 12, ly + 26], fill=PLUM)
    d.polygon([(lx - 7, ly + 20), (lx + 7, ly + 20), (lx, ly + 48)], fill=PLUM)
    k = (t - 1.05)
    if 0 < k < 0.5:
        bubble(c, lx + 150, ly - 70, 'klik!', F(BOLD, 34), accent, CREAM, back(k / 0.25), -8, 'left', (18, 10))
