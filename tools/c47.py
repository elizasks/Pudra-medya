"""47. hafta (16–22 Kasım 2026) carousel'leri: Kırmızı Bayrak (16), Kandırılmamak İçin (18), Yaş Köşesi (20)."""
from anim import *
from illus import bubble
import sys, os
W, H = 1080, 1350
DENIM = (52, 72, 120); DENIM2 = (84, 108, 160)
TAN = (150, 92, 58); TAN2 = (110, 62, 36)
GREYC = (225, 214, 220)


def blobs(c, t, col, pos=(W - 110, 1120), R=380):
    d = ImageDraw.Draw(c); s = ease(t / 0.7); p = math.sin(t * 1.4) * 14
    r = int(R * s); d.ellipse([pos[0] - r - p, pos[1] - r - p, pos[0] + r + p, pos[1] + r + p], fill=col)


def footer(c, i, n, col):
    text_a(c, (70, 1290), 'PUDRA DERGİ', F(BOLD, 22), col, 1)
    text_a(c, (W - 70, 1288), f'{i}/{n}', F(MED, 24), col, 1, anchor='ra')


def item_page(t, i, n, bg, blobcol, fg, acc, stk, stkcol, num, title, body, ill, lg, cta=None):
    c = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(c)
    blobs(c, t, blobcol, (W - 70, 1150), 360)
    sticker(c, (W - 60 - F(BOLD, 28).getlength(stk) / 2 - 30, 110), stk, F(BOLD, 28), stkcol[0], stkcol[1], 5, back((t - 0.1) / 0.4))
    a = ease((t - 0.15) / 0.5)
    text_a(c, (66 - int(40 * (1 - a)), 180), num, F(BOLD, 110), acc, a)
    for j, ln in enumerate(title):
        a = ease((t - 0.35 - j * 0.2) / 0.5)
        text_a(c, (70, 320 + j * 96), ln, F(ACC if j == len(title) - 1 else BOLD, 84 if j == len(title) - 1 else 78), acc if j == len(title) - 1 else fg, a, int(30 * (1 - a)))
    a = ease((t - 0.9) / 0.5); y = 320 + len(title) * 96 + 30
    for ln in wrap(F(REG, 36), body, W - 150):
        text_a(c, (72, y), ln, F(REG, 36), fg, a); y += 50
    ill(c, max(0.0, t - 0.6), y)
    if cta:
        s = back((t - 2.4) / 0.45)
        if s > 0: sticker(c, (W // 2 + int(6 * math.sin(t * 6)), 1215), cta, F(BOLD, 38), fg, bg, -2, s, 34, 16)
    footer(c, i, n, fg)
    logo(c, lg); return c


# ================== ILLÜSTRASYONLAR
def ill_phone(c, t, cx, cy, body=PLUM, scr=PINK):
    d = ImageDraw.Draw(c)
    sh = math.sin(t * 40) * 8 if (t % 1.6) < 0.6 else 0
    x = cx + sh
    for k in range(3):
        r = 120 + k * 40 + (t * 60 % 40)
        d.arc([cx - r, cy - r, cx + r, cy + r], 200, 250, fill=body, width=8)
        d.arc([cx - r, cy - r, cx + r, cy + r], 290, 340, fill=body, width=8)
    d.rounded_rectangle([x - 80, cy - 150, x + 80, cy + 150], radius=30, fill=body)
    d.rounded_rectangle([x - 64, cy - 120, x + 64, cy + 120], radius=16, fill=scr)
    d.ellipse([x - 40, cy - 60, x + 40, cy + 20], fill=body)
    d.ellipse([x - 22, cy - 92, x + 22, cy - 52], fill=CREAM)
    d.rounded_rectangle([x - 30, cy + 50, x + 30, cy + 90], radius=20, fill=(60, 170, 90))
    bubble(c, cx + 250, cy - 150, 'Bir ricam var...', F(BOLD, 34), CREAM, PLUM, back((t - 0.6) / 0.4), -4)


def ill_party(c, t, cx, cy, col=CREAM):
    d = ImageDraw.Draw(c)
    # konfeti
    for j in range(16):
        x = cx - 330 + (j * 53) % 520; y = cy - 160 + ((t * (80 + j * 7) + j * 40) % 320)
        cc = [PINK, RED, CREAM, (255, 196, 92)][j % 4]
        d.rectangle([x, y, x + 14, y + 22], fill=cc)
    k = back(t / 0.5)
    if k > 0:  # kupa
        s = k
        d.polygon([(cx - 210 - 70 * s, cy - 110 * s), (cx - 210 + 70 * s, cy - 110 * s), (cx - 210 + 40 * s, cy + 10 * s), (cx - 210 - 40 * s, cy + 10 * s)], fill=(255, 196, 92))
        d.rectangle([cx - 222, cy + 10 * s, cx - 198, cy + 60 * s], fill=(255, 196, 92))
        d.rounded_rectangle([cx - 270 * 1, cy + 60 * s, cx - 150, cy + 90 * s], radius=8, fill=(255, 196, 92))
        sparkle(d, cx - 210, cy - 60 * s, 26 * s, CREAM)
    bubble(c, cx - 200, cy - 230, 'Terfi aldım!', F(BOLD, 34), RED, CREAM, back((t - 0.4) / 0.4), 3)
    bubble(c, cx + 200, cy - 40, 'Hıı. İyi bari.', F(BOLD, 34), GREYC, PLUM, back((t - 1.2) / 0.4), -3, 'right')


def ill_secret(c, t, cx, cy, fg=CREAM, acc=RED):
    d = ImageDraw.Draw(c)
    open_ = ease((t - 0.9) / 0.4)
    x = cx - 200
    d.arc([x - 55, cy - 150 - 50 * open_, x + 55, cy - 40 - 50 * open_], 180, 360, fill=fg, width=22)
    d.line([(x + 55 - 11, cy - 95 - 50 * open_), (x + 55 - 11, cy - 40)], fill=fg, width=22) if open_ < 0.5 else None
    d.line([(x - 55 + 11, cy - 95 - 50 * open_), (x - 55 + 11, cy - 40 - 50 * open_ + 10)], fill=fg, width=22)
    d.rounded_rectangle([x - 90, cy - 50, x + 90, cy + 110], radius=24, fill=acc)
    d.ellipse([x - 18, cy + 5, x + 18, cy + 41], fill=fg); d.rectangle([x - 7, cy + 30, x + 7, cy + 75], fill=fg)
    for j in range(3):
        p = ease((t - 1.2 - j * 0.3) / 0.7)
        if p > 0:
            bx = x + 120 + p * (190 + j * 40); by = cy - 140 + j * 120
            bubble(c, bx, by, '...', F(BOLD, 40), fg, acc, min(1, p * 1.5))
            r = 34; hx = cx + 330; hy = cy - 140 + j * 120
            d.ellipse([hx - r, hy - r, hx + r, hy + r], fill=PINK)


def ill_talk(c, t, cx, cy, fg=PLUM, acc=BERRY, bg=CREAM):
    msgs = ['Benim patron yine...', 'Bir de annem...', 'Sonra ne oldu biliyor musun?']
    for j, m in enumerate(msgs):
        k = back((t - 0.2 - j * 0.45) / 0.4)
        bubble(c, cx - 140 + j * 30, cy - 170 + j * 95, m, F(BOLD, 32), acc, CREAM, k, (-1) ** j * 2)
    k = back((t - 1.9) / 0.4)
    bubble(c, cx + 270, cy + 140, 'Peki ben?', F(MED, 24), bg, fg, k * 0.9, 0, 'right')


def ill_rain(c, t, cx, cy, fg=CREAM, acc=PINK):
    d = ImageDraw.Draw(c)
    bubble(c, cx - 230, cy - 150, 'Hayır, bu sefer olmaz.', F(BOLD, 32), fg, RED, back((t - 0.2) / 0.4), -3)
    k = ease((t - 0.9) / 0.5)
    if k > 0:
        x = cx + 210; y = cy - 10
        for (dx, dy, r) in [(-70, 10, 60), (0, -25, 78), (75, 10, 58), (0, 30, 60)]:
            rr = r * k; d.ellipse([x + dx - rr, y + dy - rr, x + dx + rr, y + dy + rr], fill=(120, 110, 125))
        for j in range(9):
            rx = x - 90 + j * 22; ry = y + 70 + ((t * 300 + j * 37) % 130)
            d.line([(rx, ry), (rx - 6, ry + 22)], fill=acc, width=5)
        # surat asık kafa
        hx, hy = x, y + 230
        d.ellipse([hx - 60, hy - 60, hx + 60, hy + 60], fill=acc)
        d.arc([hx - 25, hy + 10, hx + 25, hy + 40], 200, 340, fill=PLUM, width=6)
        d.line([(hx - 30, hy - 15), (hx - 10, hy - 8)], fill=PLUM, width=6); d.line([(hx + 30, hy - 15), (hx + 10, hy - 8)], fill=PLUM, width=6)


def bottle(c, t, cx, cy, s, body, cap, label, txt, tcol=PLUM):
    d = ImageDraw.Draw(c)
    bw, bh = 200 * s, 330 * s
    d.rounded_rectangle([cx - 46 * s, cy - bh / 2 - 80 * s, cx + 46 * s, cy - bh / 2 + 6 * s], radius=int(12 * s), fill=cap)
    d.rounded_rectangle([cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2], radius=int(40 * s), fill=body)
    d.rounded_rectangle([cx - bw / 2 + 18 * s, cy - 60 * s, cx + bw / 2 - 18 * s, cy + 80 * s], radius=int(14 * s), fill=label)
    fs = int(30 * s)
    while F(BOLD, fs).getlength(txt) > bw - 50 * s and fs > 10: fs -= 1
    d.text((cx, cy + 10 * s), txt, font=F(BOLD, fs), fill=tcol, anchor='mm')


def stamp(c, t, cx, cy, txt, col, ang=-12):
    k = back(t / 0.35)
    if k <= 0: return
    sticker(c, (cx, cy), txt, F(BOLD, 34), col, CREAM, ang, k * (1 + max(0, 0.3 - t) * 2), 30, 14)


def ill_hypo(c, t, cx, cy):
    bottle(c, t, cx - 120 + 6 * math.sin(t * 2), cy, 1.0, CREAM, BERRY, PINK, 'HİPOALERJENİK')
    stamp(c, t - 1.1, cx + 170, cy - 40, 'GARANTİ DEĞİL', RED)


def ill_clip(c, t, cx, cy, fg=PLUM, acc=BERRY):
    d = ImageDraw.Draw(c)
    x0, y0 = cx - 330, cy - 190
    d.rounded_rectangle([x0, y0, x0 + 300, y0 + 380], radius=24, fill=CREAM)
    d.rounded_rectangle([x0 + 100, y0 - 24, x0 + 200, y0 + 22], radius=12, fill=fg)
    for j in range(3):
        y = y0 + 80 + j * 95
        d.rounded_rectangle([x0 + 34, y, x0 + 84, y + 50], radius=10, outline=fg, width=5)
        d.rounded_rectangle([x0 + 110, y + 18, x0 + 260, y + 32], radius=7, fill=GREYC)
        k = ease((t - 0.3 - j * 0.3) / 0.3)
        if k > 0:
            d.line([(x0 + 42, y + 26), (x0 + 42 + 14 * k, y + 26 + 14 * k)], fill=acc, width=8)
            if k > 0.5: d.line([(x0 + 56, y + 40), (x0 + 56 + 30 * (k - 0.5) * 2, y + 40 - 36 * (k - 0.5) * 2)], fill=acc, width=8)
    bubble(c, cx + 200, cy - 120, 'Kaç kişide?', F(BOLD, 34), acc, CREAM, back((t - 1.3) / 0.4), 3)
    bubble(c, cx + 220, cy + 30, 'Sonuç ne?', F(BOLD, 34), RED, CREAM, back((t - 1.7) / 0.4), -3)


def leaf(d, cx, cy, s, ang, col, vein):
    pts = []
    for i in range(40):
        u = i / 39 * math.pi
        x = math.cos(u) * 120 * s; y = math.sin(u) * 50 * s
        pts.append((x, y))
    pts += [(x, -y) for (x, y) in reversed(pts)]
    ca, sa = math.cos(ang), math.sin(ang)
    d.polygon([(cx + x * ca - y * sa, cy + x * sa + y * ca) for x, y in pts], fill=col)
    d.line([(cx - 110 * s * ca, cy - 110 * s * sa), (cx + 110 * s * ca, cy + 110 * s * sa)], fill=vein, width=int(5 * s))


def ill_natural(c, t, cx, cy):
    d = ImageDraw.Draw(c)
    leaf(d, cx - 220, cy - 20, 1.3, -0.6 + 0.08 * math.sin(t * 2), (96, 150, 92), (70, 118, 70))
    leaf(d, cx - 120, cy + 70, 0.9, 0.5 + 0.08 * math.sin(t * 2 + 1), (124, 176, 110), (96, 150, 92))
    # damlalık
    x = cx + 120; y = cy - 210
    d.rounded_rectangle([x - 26, y, x + 26, y + 60], radius=20, fill=BERRY)
    d.polygon([(x - 14, y + 60), (x + 14, y + 60), (x + 4, y + 190), (x - 4, y + 190)], fill=CREAM)
    p = (t % 1.4) / 1.4; dy = y + 200 + p * 160
    d.ellipse([x - 12, dy, x + 12, dy + 26], fill=(255, 196, 92)); d.polygon([(x - 11, dy + 10), (x, dy - 14), (x + 11, dy + 10)], fill=(255, 196, 92))
    k = back((t - 1.2) / 0.4)
    if k > 0:
        tx, ty, r = cx + 300, cy + 40, 110 * k
        d.polygon([(tx, ty - r), (tx + r * 0.95, ty + r * 0.7), (tx - r * 0.95, ty + r * 0.7)], fill=RED)
        d.text((tx, ty + r * 0.45), '!', font=F(BOLD, max(8, int(120 * k))), fill=CREAM, anchor='ms')


def ill_spf(c, t, cx, cy, fg=PLUM, acc=BERRY):
    d = ImageDraw.Draw(c)
    for j, (lab, pct, col) in enumerate([('SPF 30', 97, acc), ('SPF 50', 98, RED)]):
        y = cy - 130 + j * 170
        q = ease((t - 0.3 - j * 0.4) / 1.0)
        d.text((cx - 400, y), lab, font=F(BOLD, 46), fill=fg, anchor='lm')
        d.rounded_rectangle([cx - 210, y - 34, cx + 300, y + 34], radius=34, fill=GREYC)
        if q > 0.03: d.rounded_rectangle([cx - 210, y - 34, cx - 210 + 510 * pct / 100 * q, y + 34], radius=34, fill=col)
        d.text((cx + 330, y), f'%{int(pct * q)}', font=F(BOLD, 50), fill=col, anchor='lm')
    k = back((t - 1.8) / 0.4)
    if k > 0: sticker(c, (cx - 40, cy + 200), 'Fark sadece %1', F(BOLD, 34), fg, CREAM, -3, k, 30, 14)


def ill_jar(c, t, cx, cy, fg=PLUM, acc=BERRY):
    d = ImageDraw.Draw(c)
    x = cx - 180
    d.rounded_rectangle([x - 150, cy - 40, x + 150, cy + 170], radius=30, fill=CREAM)
    d.rounded_rectangle([x - 130, cy - 20, x + 130, cy + 150], radius=22, outline=acc, width=6)
    d.text((x, cy + 72), '12M', font=F(BOLD, 80), fill=acc, anchor='mm')
    ang = -35 * ease((t - 0.4) / 0.6)
    lid = Image.new('RGBA', (340, 80), (0, 0, 0, 0)); ImageDraw.Draw(lid).rounded_rectangle([10, 10, 330, 70], radius=22, fill=acc)
    lid = lid.rotate(-ang, expand=True, resample=Image.BICUBIC)
    c.paste(lid, (int(x - lid.width / 2 + 30 * ease((t - 0.4) / 0.6)), int(cy - 70 - lid.height / 2 - 40 * ease((t - 0.4) / 0.6))), lid)
    # takvim
    k = back((t - 1.1) / 0.4)
    if k > 0:
        tx, ty = cx + 230, cy + 40; w = 200 * k; h = 210 * k
        d.rounded_rectangle([tx - w / 2, ty - h / 2, tx + w / 2, ty + h / 2], radius=int(20 * k), fill=CREAM)
        d.rounded_rectangle([tx - w / 2, ty - h / 2, tx + w / 2, ty - h / 2 + 56 * k], radius=int(20 * k), fill=RED)
        for j in range(3):
            for i in range(3):
                d.ellipse([tx - 60 * k + i * 60 * k - 9 * k, ty + j * 45 * k - 9 * k, tx - 60 * k + i * 60 * k + 9 * k, ty + j * 45 * k + 9 * k], fill=fg)
        p = ease((t - 1.6) / 0.5)
        if p > 0: d.ellipse([tx + 60 * k - 26, ty + 90 * k - 26, tx + 60 * k + 26, ty + 90 * k + 26], outline=RED, width=int(6 * p) + 1)


def ill_jeans(c, t, cx, cy):
    lay = Image.new('RGBA', (360, 560), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.polygon([(50, 30), (310, 30), (322, 550), (205, 550), (180, 190), (155, 550), (38, 550)], fill=DENIM)
    d.rectangle([40, 20, 320, 66], fill=DENIM2)
    d.line([(180, 66), (180, 160)], fill=DENIM2, width=5)
    for x in (70, 290): d.arc([x - 50, 50, x + 50, 140], 0, 180, fill=DENIM2, width=5)
    d.ellipse([170, 30, 190, 50], fill=(220, 180, 90))
    lay = lay.rotate(math.sin(t * 2) * 4, expand=True, resample=Image.BICUBIC)
    c.paste(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)), lay)


def ill_blazer(c, t, cx, cy, col=PLUM, lap=BERRY):
    lay = Image.new('RGBA', (440, 480), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.polygon([(120, 20), (40, 70), (0, 440), (70, 450), (110, 200)], fill=col)
    d.polygon([(320, 20), (400, 70), (440, 440), (370, 450), (330, 200)], fill=col)
    d.rounded_rectangle([90, 20, 350, 470], radius=26, fill=col)
    d.polygon([(170, 20), (220, 260), (270, 20)], fill=CREAM)
    d.polygon([(150, 20), (220, 280), (190, 140), (130, 120)], fill=lap)
    d.polygon([(290, 20), (220, 280), (250, 140), (310, 120)], fill=lap)
    for y in (320, 390): d.ellipse([210, y, 230, y + 20], fill=CREAM)
    lay = lay.rotate(math.sin(t * 2) * 3, expand=True, resample=Image.BICUBIC)
    c.paste(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)), lay)


def ill_boot(c, t, cx, cy):
    b = abs(math.sin(t * 3)) * 26
    lay = Image.new('RGBA', (440, 460), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.polygon([(110, 10), (250, 10), (260, 290), (420, 340), (430, 410), (130, 410), (100, 300)], fill=TAN)
    d.rectangle([110, 10, 250, 46], fill=TAN2)
    d.rectangle([100, 400, 430, 430], fill=TAN2)
    d.polygon([(100, 410), (160, 410), (150, 455), (110, 455)], fill=TAN2)
    d.line([(240, 60), (240, 280)], fill=TAN2, width=5)
    c.paste(lay, (int(cx - 220), int(cy - 230 - b)), lay)
    d2 = ImageDraw.Draw(c); w = 170 - b * 2
    d2.ellipse([cx - w, cy + 225, cx + w, cy + 245], fill=(0, 0, 0) if False else (200, 170, 180))


def ill_scarf(c, t, cx, cy, col=RED, col2=(255, 196, 92)):
    d = ImageDraw.Draw(c)
    pts_top = []; pts_bot = []
    for i in range(41):
        u = i / 40; x = cx - 330 + u * 660
        y = cy - 40 + math.sin(u * 6 + t * 3) * 40 * u
        pts_top.append((x, y - 55)); pts_bot.append((x, y + 55))
    d.polygon(pts_top + list(reversed(pts_bot)), fill=col)
    for k in range(1, 4):
        i = k * 10; d.line([pts_top[i], pts_bot[i]], fill=col2, width=10)
    ex, ey = pts_top[-1]; ex2, ey2 = pts_bot[-1]
    for j in range(7):
        fx = ex + 4; fy = ey + 8 + j * (ey2 - ey - 16) / 6
        d.line([(fx, fy), (fx + 40 + 6 * math.sin(t * 5 + j), fy + 6)], fill=col, width=7)


# ================== A · KIRMIZI BAYRAK (16 Kasım)
def a_cover(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blobs(c, t, PLUM, (W - 60, 1180), 420)
    r2 = int(220 * ease(t / 0.8)); d.ellipse([-120 - r2, 260 - r2, -120 + r2, 260 + r2], fill=(232, 80, 96))
    waving_flag(d, 640, 700, 480, t, CREAM, PLUM)
    sticker(c, (W - 260, 110), 'KIRMIZI BAYRAK', F(BOLD, 30), CREAM, RED, 5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Arkadaşlıkta', F(BOLD, 98), 220, 0.2, CREAM), ('5 kırmızı', F(ACC, 124), 335, 0.4, PLUM), ('bayrak.', F(BOLD, 98), 480, 0.6, CREAM)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(30 * (1 - a)))
    a = ease((t - 1.2) / 0.5)
    text_a(c, (70, 650), 'Biri bile tanıdıksa,', F(MED, 40), CREAM, a)
    text_a(c, (70, 702), 'sonuna kadar kaydır.', F(MED, 40), CREAM, a)
    s = back((t - 1.8) / 0.4)
    if s > 0: sticker(c, (210, 900), 'Kaydet', F(BOLD, 42), PLUM, CREAM, -6, s, 34, 14)
    text_a(c, (70 + int(8 * math.sin(t * 6)), 1230), 'kaydır  ›', F(BOLD, 38), CREAM, ease((t - 2.0) / 0.4))
    logo(c, 'A'); return c

def a_cover0(t): return a_cover(t + 3.5)

STK_A = 'KIRMIZI BAYRAK'
def a1(t): return item_page(t, 2, 6, PINK, (236, 170, 192), PLUM, RED, STK_A, (RED, CREAM), '01', ['Sadece işi', 'düşünce arar.'],
                            'Senin günün nasıl geçti, hiç sormaz. Telefon çaldıysa bir ricası vardır.',
                            lambda c, t, y: ill_phone(c, t, 420, 1010), 'B')
def a2(t): return item_page(t, 3, 6, PLUM, BERRY, CREAM, PINK, STK_A, (RED, CREAM), '02', ['Sevincine', 'sevinemez.'],
                            'Terfi aldın, "iyi bari" der, konuyu değiştirir. Gerçek dost seninle birlikte zıplar.',
                            lambda c, t, y: ill_party(c, t, 560, 1040), 'B')
def a3(t): return item_page(t, 4, 6, BERRY, (120, 12, 60), CREAM, PINK, STK_A, (CREAM, BERRY), '03', ['Sırrını', 'taşır.'],
                            'Sana başkalarının sırlarını anlatıyorsa, seninkileri de başkalarına anlatıyordur.',
                            lambda c, t, y: ill_secret(c, t, 520, 1030), 'A')
def a4(t): return item_page(t, 5, 6, CREAM, PINK, PLUM, BERRY, STK_A, (RED, CREAM), '04', ['Sohbet hep', 'onun derdi.'],
                            'İki saat dinlersin; sıra sana gelince saatine bakar.',
                            lambda c, t, y: ill_talk(c, t, 500, 1000), 'B')
def a5(t): return item_page(t, 6, 6, RED, BERRY, CREAM, PLUM, STK_A, (CREAM, RED), '05', ['Hayır deyince', 'küser.'],
                            'Sınır koyunca seni suçlu hissettiriyorsa, sorun senin "hayır"ında değil.',
                            lambda c, t, y: ill_rain(c, t, 470, 840), 'A', 'Kaçı tanıdık? Sayıyı yaz ›')

# ================== B · KANDIRILMAMAK İÇİN (18 Kasım)
def b_cover(t):
    c = Image.new('RGB', (W, H), PLUM); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 80, 1120), 420)
    dots(d, 800, 470, 5, 3, 44, 6, (90, 50, 70))
    sticker(c, (W - 300, 110), 'KANDIRILMAMAK İÇİN', F(BOLD, 28), PINK, PLUM, 5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Kozmetik', F(BOLD, 100), 210, 0.2, CREAM), ('etiketinde', F(BOLD, 100), 322, 0.35, CREAM), ('5 tuzak.', F(ACC, 130), 440, 0.55, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(30 * (1 - a)))
    a = ease((t - 1.2) / 0.5)
    text_a(c, (70, 640), 'Rafta okumadan alma.', F(MED, 40), CREAM, a)
    text_a(c, (70, 692), 'Kaydet, alışverişte aç.', F(MED, 40), CREAM, a)
    bottle(c, t, 720, 1000, 1.05, CREAM, RED, PINK, '%100 MUCİZE')
    # büyüteç
    mx = 760 + 90 * math.sin(t * 1.6); my = 980 + 30 * math.cos(t * 1.6)
    d.line([(mx + 70, my + 70), (mx + 150, my + 150)], fill=PINK, width=26)
    d.ellipse([mx - 95, my - 95, mx + 95, my + 95], outline=PINK, width=18)
    d.rounded_rectangle([720 - 105 * 1.05 + 18, 1000 - 60, 720 + 105 * 1.05 - 18, 1000 + 82], radius=14, fill=PINK)
    d.text((720, 1010), '%100 MUCİZE', font=F(BOLD, 26), fill=PLUM, anchor='mm')
    s = back((t - 1.8) / 0.4)
    if s > 0: sticker(c, (230, 880), 'Kaydet', F(BOLD, 42), RED, CREAM, -6, s, 34, 14)
    text_a(c, (70 + int(8 * math.sin(t * 6)), 1230), 'kaydır  ›', F(BOLD, 38), CREAM, ease((t - 2.0) / 0.4))
    logo(c, 'B'); return c

def b_cover0(t): return b_cover(t + 3.5)

STK_B = 'KANDIRILMAMAK İÇİN'
def b1(t): return item_page(t, 2, 6, PINK, (236, 170, 192), PLUM, BERRY, STK_B, (PLUM, CREAM), '01', ['"Hipoalerjenik"', 'garanti değil.'],
                            'Alerji yapmaz demek değil, yalnızca daha düşük risk iddiası. Alerjin varsa içerik listesine bak.',
                            lambda c, t, y: ill_hypo(c, t, 520, 1010), 'B')
def b2(t): return item_page(t, 3, 6, CREAM, PINK, PLUM, RED, STK_B, (PLUM, CREAM), '02', ['"Dermatolojik', 'test edildi"'],
                            'Testin yapıldığını söyler; kaç kişide, hangi ciltte, sonucun ne çıktığını söylemez.',
                            lambda c, t, y: ill_clip(c, t, 540, 1010), 'B')
def b3(t): return item_page(t, 4, 6, PLUM, BERRY, CREAM, PINK, STK_B, (PINK, PLUM), '03', ['"Doğal" demek', 'güvenli değil.'],
                            'Esansiyel yağlar ve bitki özleri de tahriş ya da alerji yapabilir. Önce kolunun içinde dene.',
                            lambda c, t, y: ill_natural(c, t, 520, 1010), 'B')
def b4(t): return item_page(t, 5, 6, CREAM, PINK, PLUM, BERRY, STK_B, (PLUM, CREAM), '04', ['SPF 50, iki kat', 'koruma değil.'],
                            "SPF 30 UVB'nin yaklaşık %97'sini, SPF 50 %98'ini süzer. Asıl fark: bol sürmek, 2 saatte bir yenilemek.",
                            lambda c, t, y: ill_spf(c, t, 480, 1010), 'B')
def b5(t): return item_page(t, 6, 6, BERRY, (120, 12, 60), CREAM, PINK, STK_B, (PINK, PLUM), '05', ['Açık kavanoz', 'simgesine bak.'],
                            '"12M" yazıyorsa açtıktan sonra 12 ay içinde bitir. Açtığın tarihi kapağa yaz.',
                            lambda c, t, y: ill_jar(c, t, 500, 920, PLUM, BERRY), 'A', 'Hangisine kandın? Numarasını yaz ›')

# ================== C · YAŞ KÖŞESİ (20 Kasım)
def c_cover(t):
    c = Image.new('RGB', (W, H), BERRY); d = ImageDraw.Draw(c)
    blobs(c, t, (120, 12, 60), (W - 60, 1150), 420)
    sticker(c, (W - 230, 110), 'YAŞ KÖŞESİ', F(BOLD, 30), PINK, PLUM, 5, back((t - 0.1) / 0.4))
    for txt, font, y, st, col in [('Her yaşın', F(BOLD, 100), 210, 0.2, CREAM), ('bir yatırım', F(ACC, 120), 325, 0.4, PINK), ('parçası.', F(BOLD, 100), 470, 0.6, CREAM)]:
        a = ease((t - st) / 0.5); text_a(c, (66, y), txt, font, col, a, int(30 * (1 - a)))
    a = ease((t - 1.2) / 0.5)
    text_a(c, (70, 640), "20'lerden 50+'ya: yıllarca", F(MED, 40), CREAM, a)
    text_a(c, (70, 692), 'giyeceğin 4 parça.', F(MED, 40), CREAM, a)
    cols = [PINK, RED, CREAM, (255, 196, 92)]
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
def c1(t): return item_page(t, 2, 6, PINK, (236, 170, 192), PLUM, BERRY, STK_C, (BERRY, CREAM), "20'LER", ['İyi kesim', 'koyu jean.'],
                            'Trendi değil, kalçana oturanı seç. Koyu yıkama hem ofiste hem akşam yemeğinde çalışır.',
                            lambda c, t, y: ill_jeans(c, t, 540, 1010), 'B')
def c2(t): return item_page(t, 3, 6, CREAM, PINK, PLUM, RED, STK_C, (BERRY, CREAM), "30'LAR", ['Omzu oturan', 'bir blazer.'],
                            "Omuz dikişi tam omzunda bitsin. Jean'le de, takımla da giyilir; terziye götürmeye değer.",
                            lambda c, t, y: ill_blazer(c, t, 540, 1010), 'B')
def c3(t): return item_page(t, 4, 6, PLUM, BERRY, CREAM, PINK, STK_C, (PINK, PLUM), "40'LAR", ['Kaliteli', 'deri bot.'],
                            'Gerçek deri, sağlam taban, rahat topuk. İyi bakılan deri bot yıllarca seninle yürür.',
                            lambda c, t, y: ill_boot(c, t, 560, 990), 'B')
def c4(t): return item_page(t, 5, 6, CREAM, PINK, PLUM, RED, STK_C, (BERRY, CREAM), '50+', ['Canlı renkli', 'bir yün atkı.'],
                            'Yüzüne yakın canlı bir renk teni aydınlatır. Siyah paltoya bile hayat verir.',
                            lambda c, t, y: ill_scarf(c, t, 520, 1010), 'B')

def c5(t):
    c = Image.new('RGB', (W, H), RED); d = ImageDraw.Draw(c)
    blobs(c, t, BERRY, (W - 60, 1220), 380)
    sparkle(d, 930, 300, 30 + 6 * math.sin(t * 4), PINK)
    for txt, font, y, st, col in [('Senin parçan', F(BOLD, 92), 200, 0.2, CREAM), ('hangisi?', F(ACC, 120), 305, 0.4, PINK)]:
        a = ease((t - st) / 0.5); text_a(c, (70, y), txt, font, col, a, int(30 * (1 - a)))
    opts = [('A', 'Koyu jean'), ('B', 'Blazer'), ('C', 'Deri bot'), ('D', 'Renkli atkı')]
    y = 500
    for k, (l, txt) in enumerate(opts):
        s = ease((t - 0.8 - k * 0.25) / 0.45)
        if s > 0:
            x = 70 - int(60 * (1 - s))
            d.rounded_rectangle([x, y, x + 600, y + 96], radius=48, fill=CREAM)
            d.ellipse([x + 10, y + 8, x + 90, y + 88], fill=PLUM)
            d.text((x + 50, y + 66), l, font=F(BOLD, 46), fill=CREAM, anchor='ms')
            d.text((x + 116, y + 66), txt, font=F(BOLD, 40), fill=PLUM, anchor='ls')
        y += 112
    sticker(c, (360, 1010), 'Harfini yorumlara yaz ›', F(BOLD, 42), PLUM, CREAM, -3, back((t - 2.0) / 0.45) * (1 + 0.03 * math.sin(t * 6)), 36, 18)
    a = ease((t - 2.5) / 0.4)
    text_a(c, (72, 1105), 'Annene, kızına,', F(BOLD, 40), CREAM, a)
    text_a(c, (72, 1157), 'ablana gönder.', F(ACC, 52), PINK, a)
    ill_scarf(c, max(0, t - 1.0), 0, 0) if False else None
    ill_boot(c, max(0, t - 1.0), 860, 640) if False else None
    footer(c, 6, 6, CREAM)
    logo(c, 'A'); return c

def c_q(t): return c5(t)

SETS = {
    'a': ('1116_kirmizibayrak', [a_cover0, a1, a2, a3, a4, a5]),
    'b': ('1118_etikettuzak', [b_cover0, b1, b2, b3, b4, b5]),
    'c': ('1120_yaskosesi', [c_cover0, c1, c2, c3, c4, c5]),
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
