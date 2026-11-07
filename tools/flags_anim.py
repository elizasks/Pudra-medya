from anim import *
from illus import waiter, exes, phone, talker, lockheart
import sys
W,H=1080,1350

def cover(t):
    c=Image.new('RGB',(W,H),BERRY); d=ImageDraw.Draw(c)
    p=math.sin(t*1.5)*18; s=ease(t/0.8)
    r=int(470*s); d.ellipse([1030-r-p,1090-r-p,1030+r+p,1090+r+p],fill=RED)
    r2=int(290*s); d.ellipse([20-r2,20-r2,20+r2,20+r2],fill=(168,30,90))
    dots(d,820,150,5,4,46,7,PINK)
    text_a(c,(80,290),'PUDRA · İLİŞKİLER',F(BOLD,30),PINK,ease((t-0.1)/0.4))
    text_a(c,(76,350),'İlk buluşmada',F(BOLD,92),CREAM,ease((t-0.25)/0.5),int(40*(1-ease((t-0.25)/0.5))))
    text_a(c,(72,470),'5 kırmızı',F(ACC,170),PINK,ease((t-0.55)/0.5),int(40*(1-ease((t-0.55)/0.5))))
    text_a(c,(76,660),'bayrak.',F(BOLD,150),CREAM,ease((t-0.85)/0.5),int(40*(1-ease((t-0.85)/0.5))))
    fy=int(1300-420*ease((t-0.6)/0.8)); waving_flag(d,780,fy,300,t,CREAM,PLUM)
    for (x,y,r,st,col) in [(700,330,46,1.2,PINK),(990,620,30,1.4,CREAM)]:
        k=back((t-st)/0.4)
        if k>0: sparkle(d,x,y,r*k*(1+0.1*math.sin(t*4+x)),col)
    sticker(c,(320,1080),'Görürsen kahveni bitirme, kalk.',F(BOLD,30),CREAM,BERRY,4,back((t-1.5)/0.45))
    a=ease((t-2.0)/0.4)
    if a>0:
        off=int(10*math.sin(t*6))
        text_a(c,(W-80+off,1240),'kaydır  ›',F(BOLD,40),CREAM,a,anchor='ra')
    logo(c,'A'); return c

items=[('Garsona kaba davranıyor.','Sana nasıl davranacağının fragmanı bu.'),
 ("Bütün eski sevgilileri 'deli'.",'Ortak nokta kim, bir düşün.'),
 ('Telefonu masada, ekranı hep ters.','Saklanan bir şey varsa erken belli olur.'),
 ('İki saattir sadece kendini anlatıyor.','Senin mesleğini hâlâ sormadı.'),
 ("'Kıskanıyorum, çünkü seviyorum.'",'Hayır. Bunun adı kontrol.')]
themes=[(PINK,BERRY,PLUM,PLUM,RED,RED,CREAM,'B'),
        (PLUM,RED,CREAM,PINK,RED,PINK,PLUM,'B'),
        (RED,PLUM,CREAM,CREAM,PINK,CREAM,RED,'A'),
        (CREAM,PINK,PLUM,PLUM,BERRY,BERRY,CREAM,'B'),
        (BERRY,PLUM,CREAM,PINK,PINK,RED,CREAM,'A')]
def item(i):
    (tt,sub),(bg,blob,tc,sc,nc,stb,stf,lv)=items[i-1],themes[i-1]
    TL=wrap(F(BOLD,80),tt,W-160); SL=wrap(F(REG,38),sub,W-160)
    def fn(t):
        c=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(c)
        s=ease(t/0.7); p=math.sin(t*1.4)*14
        r=int(390*s); d.ellipse([W-110-r-p,1060-r-p,W-110+r+p,1060+r+p],fill=blob)
        for (sx,sy,sr,st) in [(90,1120,30,1.6),(170,1010,18,1.9)]:
            k=back((t-st)/0.4)
            if k>0: sparkle(d,sx,sy,sr*k*(1+0.12*math.sin(t*5+sx)),nc)
        a=ease((t-0.1)/0.5); text_a(c,(70+int(-60*(1-a)),150),f'0{i}',F(BOLD,200),nc,a)
        fa=ease((t-0.3)/0.5)
        if fa>0: waving_flag(d,W-200,int(170+60*(1-fa)),130,t,RED if bg!=RED else CREAM,CREAM if bg in (PLUM,BERRY,RED) else PLUM)
        sticker(c,(480,250),'KIRMIZI BAYRAK',F(BOLD,28),stb,stf,-7,back((t-0.5)/0.4))
        y=420
        for j,ln in enumerate(TL):
            a=ease((t-0.6-j*0.15)/0.45); text_a(c,(80,y),ln,F(BOLD,80),tc,a,int(30*(1-a))); y+=94
        y+=14; a=ease((t-1.0)/0.5)
        for ln in SL: text_a(c,(80,y),ln,F(REG,38),sc,a); y+=50
        wave_line(d,0,W*ease((t-1.1)/0.8),y+40,14,180,nc,5,-t*2)
        tl=max(0,t-0.4)
        cfg={1:(900,520,520,330),2:(700,400,350,300),3:(760,420,380,300),4:(820,470,380,340),5:(900,520,450,250)}[i]
        lay=Image.new('RGBA',cfg[:2],(0,0,0,0))
        if i==1: waiter(lay,tl,cx=cfg[2],cy=cfg[3])
        elif i==2: exes(lay,tl,cx=cfg[2],cy=cfg[3])
        elif i==3: phone(lay,tl,cx=cfg[2],cy=cfg[3],table=PINK,body=PLUM,line=CREAM)
        elif i==4: talker(lay,tl,cx=cfg[2],cy=cfg[3],fg=PLUM,bg=CREAM)
        else: lockheart(lay,tl,cx=cfg[2],cy=cfg[3])
        zf=1035/cfg[0]; lay=lay.resize((1035,int(cfg[1]*zf)),Image.LANCZOS)
        if lay.height>600: lay=lay.crop((0,lay.height-600,1035,lay.height))
        ia=ease((t-0.3)/0.4)
        if ia<1:
            al=lay.split()[3].point(lambda v:int(v*ia)); lay.putalpha(al)
        c.paste(lay,(22,y+60 if y+60<680 else 680),lay)
        d=ImageDraw.Draw(c)
        if i==5:
            sticker(c,(W//2,1255),'Bunu o arkadaşına gönder ›',F(BOLD,44),CREAM,BERRY,-3,back((t-2.2)/0.45)*(1+0.03*math.sin(t*6)),42,20)
        else:
            text_a(c,(80,1280),'PUDRA DERGİ',F(BOLD,22),sc,1)
            text_a(c,(W-80,1278),f'{i+1}/6',F(MED,24),sc,1,anchor='ra')
        logo(c,lv); return c
    return fn

which=sys.argv[1]
if which=='1': render(cover,'out3/p2_1.mp4',5,(W,H),'out3/p2_1.jpg')
else:
    i=int(which)-1; render(item(i),f'out3/p2_{i+1}.mp4',6,(W,H),f'out3/p2_{i+1}.jpg')
