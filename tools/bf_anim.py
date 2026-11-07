from anim import *
from illus import bubble
import sys
W,H=1080,1350
BLACK=(22,14,18)

# ---------- illüstrasyonlar (yerel tuvale, cx,cy merkez)
def il_screenshot(c,t,cx,cy):
    d=ImageDraw.Draw(c)
    x0,y0=cx-130,cy-230
    d.rounded_rectangle([x0,y0,x0+260,y0+460],radius=40,fill=CREAM,outline=PLUM,width=10)
    d.rounded_rectangle([x0+100,y0+18,x0+160,y0+32],radius=7,fill=PLUM)
    d.rounded_rectangle([x0+30,y0+60,x0+230,y0+250],radius=20,fill=PINK)
    # çanta silueti
    d.rounded_rectangle([x0+75,y0+130,x0+185,y0+220],radius=18,fill=BERRY)
    d.arc([x0+95,y0+90,x0+165,y0+170],180,360,fill=BERRY,width=10)
    d.text((x0+130,y0+300),'1.299 TL',font=F(BOLD,46),fill=PLUM,anchor='ms')
    d.text((x0+130,y0+350),'7 Kasım',font=F(MED,28),fill=BERRY,anchor='ms')
    for k in range(3):
        f=(t-0.8-k*1.2)
        if 0<f<0.3:
            a=int(255*(1-f/0.3))
            lay=Image.new('RGBA',c.size,(0,0,0,0)); ImageDraw.Draw(lay).rounded_rectangle([x0,y0,x0+260,y0+460],radius=40,fill=(255,255,255,a))
            c.alpha_composite(lay) if c.mode=='RGBA' else c.paste(lay,(0,0),lay)
    s=back((t-1.0)/0.35)
    bubble(c,cx+230,cy-170,'Kaydedildi!',F(BOLD,32),RED,CREAM,s,-6,'left')
    k=back((t-1.3)/0.4)
    if k>0: sparkle(d,cx-210,cy-120,34*k,PINK)

def il_checklist(c,t,cx,cy):
    d=ImageDraw.Draw(c)
    x0,y0=cx-210,cy-230
    d.rounded_rectangle([x0,y0,x0+420,y0+470],radius=28,fill=CREAM)
    d.rounded_rectangle([x0+150,y0-24,x0+270,y0+20],radius=14,fill=BERRY)
    items=['Kaban','Bot','Nemlendirici','Ruj']
    for i,it in enumerate(items):
        y=y0+80+i*95
        d.rounded_rectangle([x0+40,y,x0+90,y+50],radius=10,outline=PLUM,width=5)
        d.text((x0+115,y+3),it,font=F(BOLD,40),fill=PLUM)
        k=ease((t-0.7-i*0.45)/0.3)
        if k>0:
            p1=(x0+50,y+25); p2=(x0+63,y+40); p3=(x0+84,y+8)
            if k<0.5: e=(p1[0]+(p2[0]-p1[0])*k*2,p1[1]+(p2[1]-p1[1])*k*2); d.line([p1,e],fill=RED,width=8)
            else:
                e=(p2[0]+(p3[0]-p2[0])*(k-0.5)*2,p2[1]+(p3[1]-p2[1])*(k-0.5)*2); d.line([p1,p2,e],fill=RED,width=8,joint='curve')
    s=back((t-2.6)/0.4)
    bubble(c,cx+160,cy+230,'Liste dışı = hayır',F(BOLD,30),PLUM,CREAM,s,5,'left')

def il_timer(c,t,cx,cy):
    d=ImageDraw.Draw(c)
    d.rounded_rectangle([cx-260,cy-120,cx+260,cy+120],radius=36,fill=BLACK,outline=RED,width=8)
    sec=max(0,59-int(t*7))
    blink=int(t*4)%2==0
    d.text((cx,cy+45),f'00:{sec:02d}',font=F(BOLD,150),fill=RED if blink else CREAM,anchor='ms')
    s=back((t-0.6)/0.35)*(1+0.06*math.sin(t*14))
    sticker(c,(cx+170,cy-170),'SON 2 ÜRÜN!',F(BOLD,40),RED,CREAM,8,s,30,16)
    s=back((t-1.8)/0.35)
    bubble(c,cx-180,cy+220,'Acele ettiriyorlar',F(BOLD,30),CREAM,PLUM,s,-4,'right')
    for k,(x,y) in enumerate([(cx-300,cy-150),(cx+300,cy+150)]):
        f=back((t-1.0-k*0.3)/0.4)
        if f>0: sparkle(d,x,y,30*f,PINK)

def il_box(c,t,cx,cy):
    d=ImageDraw.Draw(c)
    bob=math.sin(t*3)*6
    d.polygon([(cx-170,cy-60+bob),(cx+170,cy-60+bob),(cx+170,cy+170+bob),(cx-170,cy+170+bob)],fill=(196,140,96))
    d.polygon([(cx-170,cy-60+bob),(cx-120,cy-130+bob),(cx+220,cy-130+bob),(cx+170,cy-60+bob)],fill=(222,170,120))
    d.polygon([(cx+170,cy-60+bob),(cx+220,cy-130+bob),(cx+220,cy+100+bob),(cx+170,cy+170+bob)],fill=(160,110,72))
    d.rectangle([cx-30,cy-60+bob,cx+30,cy+170+bob],fill=(235,215,180))
    d.text((cx,cy+90+bob),'İADE',font=F(BOLD,44),fill=PLUM,anchor='ms')
    # dönen iade oku
    ang=t*120; R=250
    a0=ang; a1=ang+250
    d.arc([cx-R,cy-R+20,cx+R,cy+R+20],a0,a1,fill=RED,width=14)
    ex=cx+R*math.cos(math.radians(a1)); ey=cy+20+R*math.sin(math.radians(a1))
    tx=-math.sin(math.radians(a1)); ty=math.cos(math.radians(a1))
    nx,ny=math.cos(math.radians(a1)),math.sin(math.radians(a1))
    d.polygon([(ex+tx*34,ey+ty*34),(ex+nx*24,ey+ny*24),(ex-nx*24,ey-ny*24)],fill=RED)
    s=back((t-1.2)/0.4)
    bubble(c,cx-230,cy-190,'Kargo kaç TL?',F(BOLD,32),CREAM,PLUM,s,-5,'right')

def il_tag(c,t,cx,cy):
    d=ImageDraw.Draw(c)
    sw=math.sin(t*2.6)*7
    tag=Image.new('RGBA',(460,300),(0,0,0,0)); td=ImageDraw.Draw(tag)
    td.polygon([(60,20),(440,20),(440,280),(60,280),(10,150)],fill=CREAM)
    td.ellipse([42,135,72,165],fill=PLUM)
    td.text((250,110),'1.000 TL',font=F(BOLD,58),fill=(150,130,140),anchor='ms')
    k=ease((t-0.6)/0.4)
    if k>0: td.line([(150,90),(150+200*k,90)],fill=RED,width=9)
    a=ease((t-1.0)/0.4)
    if a>0: td.text((250,205),'800 TL',font=F(BOLD,80),fill=RED+(int(255*a),),anchor='ms')
    tag=tag.rotate(sw,expand=True,resample=Image.BICUBIC)
    c.paste(tag,(int(cx-tag.width/2),int(cy-tag.height/2-20)),tag)
    d.line([(cx-200,cy-230),(cx-185,cy-20)],fill=PINK,width=4)
    # damga
    s=(t-1.6)
    if s>0:
        sc=max(1.0,2.2-s*4)
        st=Image.new('RGBA',(300,300),(0,0,0,0)); sd=ImageDraw.Draw(st)
        sd.ellipse([10,10,290,290],outline=RED,width=12)
        sd.text((150,135),'SON',font=F(BOLD,48),fill=RED,anchor='ms')
        sd.text((150,200),'30 GÜN',font=F(BOLD,52),fill=RED,anchor='ms')
        st=st.resize((int(220*sc),int(220*sc)),Image.LANCZOS).rotate(-14,expand=True,resample=Image.BICUBIC)
        c.paste(st,(int(cx+240-st.width/2),int(cy+30-st.height/2)),st)

# ---------- sayfalar
def cover(t):
    c=Image.new('RGB',(W,H),BLACK); d=ImageDraw.Draw(c)
    p=math.sin(t*1.5)*18; s=ease(t/0.8)
    r=int(500*s); d.ellipse([1040-r-p,1120-r-p,1040+r+p,1120+r+p],fill=RED)
    r2=int(260*s); d.ellipse([20-r2,20-r2,20+r2,20+r2],fill=BERRY)
    dots(d,820,150,5,4,46,7,(90,40,60))
    sticker(c,(300,320),'BLACK FRIDAY · 27 KASIM',F(BOLD,32),RED,CREAM,-5,back((t-0.1)/0.4))
    for txt,font,y,st,col in [('Kandırılmamak',F(BOLD,104),400,0.35,CREAM),('için',F(ACC,120),520,0.65,PINK),('5 kural.',F(BOLD,170),650,0.95,CREAM)]:
        a=ease((t-st)/0.5); text_a(c,(70,y),txt,font,col,a,int(40*(1-a)))
    # % rozet
    k=back((t-1.3)/0.45)
    if k>0:
        R=int(150*k); bx,by=800+int(6*math.sin(t*3)),1000
        d.ellipse([bx-R,by-R,bx+R,by+R],fill=PINK)
        text_a(c,(bx,by+int(55*k)),'%',F(BOLD,max(1,int(170*k))),BERRY,1,anchor='ms')
    sticker(c,(310,1100),'Sepete atmadan önce oku.',F(BOLD,32),CREAM,BLACK,3,back((t-1.7)/0.4))
    a=ease((t-2.1)/0.4)
    if a>0: text_a(c,(W-80+int(10*math.sin(t*6)),1250),'kaydır  ›',F(BOLD,40),CREAM,a,anchor='ra')
    logo(c,'B'); return c

items=[('Fiyatı bugünden kaydet.','Beğendiğin ürünün ekran görüntüsünü şimdi al. 27 Kasım\'da karşılaştır.',il_screenshot),
       ('Önce liste, sonra sepet.','İhtiyacını şimdiden yaz. Listede yoksa, indirimde de yok.',il_checklist),
       ("'Son 2 ürün!' bir taktik.",'Geri sayım ve stok uyarıları seni acele ettirmek için.',il_timer),
       ('Kargo ve iadeyi oku.','Ucuz ürün, pahalı kargoyla ucuz değildir.',il_box),
       ('Yasa senin tarafında.','İndirim, son 30 günün en düşük fiyatı üzerinden hesaplanmak zorunda.',il_tag)]
themes=[(PINK,BERRY,BLACK,PLUM,RED,BLACK,CREAM,'B'),
        (BLACK,RED,CREAM,PINK,RED,PINK,BLACK,'B'),
        (RED,BLACK,CREAM,CREAM,PINK,CREAM,RED,'A'),
        (CREAM,PINK,BLACK,PLUM,BERRY,BLACK,CREAM,'B'),
        (BLACK,BERRY,CREAM,PINK,PINK,RED,CREAM,'B')]
def item(i):
    (tt,sub,ill),(bg,blob,tc,sc,nc,stb,stf,lv)=items[i-1],themes[i-1]
    TL=wrap(F(BOLD,80),tt,W-160); SL=wrap(F(REG,38),sub,W-160)
    def fn(t):
        c=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(c)
        s=ease(t/0.7); p=math.sin(t*1.4)*14
        r=int(390*s); d.ellipse([W-110-r-p,1060-r-p,W-110+r+p,1060+r+p],fill=blob)
        a=ease((t-0.1)/0.5); text_a(c,(70+int(-60*(1-a)),150),f'0{i}',F(BOLD,200),nc,a)
        sticker(c,(470,250),'BLACK FRIDAY',F(BOLD,28),stb,stf,-7,back((t-0.5)/0.4))
        y=420
        for j,ln in enumerate(TL):
            a=ease((t-0.6-j*0.15)/0.45); text_a(c,(80,y),ln,F(BOLD,80),tc,a,int(30*(1-a))); y+=94
        y+=14; a=ease((t-1.0)/0.5)
        for ln in SL: text_a(c,(80,y),ln,F(REG,38),sc,a); y+=50
        wave_line(d,0,W*ease((t-1.1)/0.8),y+40,14,180,nc,5,-t*2)
        lay=Image.new('RGBA',(900,560),(0,0,0,0)); ill(lay,max(0,t-0.4),450,300)
        zf=1035/900; lay=lay.resize((1035,int(560*zf)),Image.LANCZOS)
        top=max(y+70,700); avail=1250-top
        if lay.height>avail: lay=lay.resize((int(lay.width*avail/lay.height),avail),Image.LANCZOS)
        ia=ease((t-0.3)/0.4)
        if ia<1: lay.putalpha(lay.split()[3].point(lambda v:int(v*ia)))
        c.paste(lay,((W-lay.width)//2,top),lay)
        if i==5:
            sticker(c,(W//2,1270),'Kaydet, 27 Kasım\'da lazım olacak ›',F(BOLD,40),RED,CREAM,-3,back((t-2.4)/0.45)*(1+0.03*math.sin(t*6)),38,18)
        else:
            text_a(c,(80,1280),'PUDRA DERGİ',F(BOLD,22),sc,1)
            text_a(c,(W-80,1278),f'{i+1}/6',F(MED,24),sc,1,anchor='ra')
        logo(c,lv); return c
    return fn

if sys.argv[1]=='preview':
    fr=[cover(3.5)]+[item(i)(4.5) for i in range(1,6)]
    s=Image.new('RGB',(3*405+40,2*506+30),(235,230,232))
    for k,im in enumerate(fr): s.paste(im.resize((405,506)),((k%3)*415+10,(k//3)*516+10))
    s.save('rev_bf.jpg',quality=85)
elif sys.argv[1]=='1': render(cover,'out5/bf_1.mp4',6,(W,H),'out5/bf_1.jpg')
else:
    i=int(sys.argv[1])-1; render(item(i),f'out5/bf_{i+1}.mp4',6,(W,H),f'out5/bf_{i+1}.jpg')
