from anim import *
import sys
W,H=1080,1350
def cover(t):
    c=Image.new('RGB',(W,H),BERRY); d=ImageDraw.Draw(c)
    p=math.sin(t*1.5)*18; s=ease(t/0.8)
    r=int(460*s); d.ellipse([1020-r-p,1150-r-p,1020+r+p,1150+r+p],fill=PINK)
    r2=int(260*s); d.ellipse([30-r2,30-r2,30+r2,30+r2],fill=(168,30,90))
    dots(d,820,150,5,4,46,7,PINK)
    sticker(c,(270,330),"PUDRA'YA HOŞ GELDİN",F(BOLD,32),PINK,PLUM,-5,back((t-0.1)/0.4))
    for txt,font,y,st,col in [('Her kadının',F(BOLD,120),400,0.35,CREAM),('dergisi.',F(ACC,170),540,0.7,PINK)]:
        a=ease((t-st)/0.5); text_a(c,(70,y),txt,font,col,a,int(40*(1-a)))
    for j,ln in enumerate(['Filtresiz güzellik.','Akıllı stil.','Gerçek ilişkiler.']):
        a=ease((t-1.2-j*0.25)/0.45); text_a(c,(76,780+j*62),ln,F(MED,46),CREAM,a,int(20*(1-a)))
    for (x,y,r,st) in [(880,420,48,1.6),(980,620,28,1.9),(640,330,30,2.1)]:
        k=back((t-st)/0.4)
        if k>0: sparkle(d,x,y,r*k*(1+0.1*math.sin(t*4+x)),CREAM)
    a=ease((t-2.3)/0.4)
    if a>0: text_a(c,(W-80+int(10*math.sin(t*6)),1250),'yaşını bul  ›',F(BOLD,40),PLUM,a,anchor='ra')
    logo(c,'A'); return c

ages=[("20'lerdeysen",['Aylık 500 TL\'ye güzellik','Flörtün kırmızı bayrakları','İlk cilt rutinin'],PINK,BERRY,PLUM,RED,'B'),
      ("30'lardaysan",['5 dakikalık makyaj','Ofisten akşama kombin','İlişkide denge'],PLUM,RED,CREAM,PINK,'B'),
      ("40'lardaysan",['Akıllı cilt bakımı','Zamansız stil','Kimsenin söylemediği gerçekler'],RED,PLUM,CREAM,PINK,'A'),
      ("50'sindeysen",['Kural yok, cesaret var','Sana yakışan renkler','Cilt gerçekleri'],CREAM,PINK,PLUM,BERRY,'B')]
def age(i):
    title,items,bg,blob,tc,nc,lv=ages[i]
    def fn(t):
        c=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(c)
        s=ease(t/0.7); p=math.sin(t*1.4)*14; r=int(400*s)
        d.ellipse([W-40-r-p,1330-r-p,W-40+r+p,1330+r+p],fill=blob)
        big={0:'20+',1:'30+',2:'40+',3:'50+'}[i]
        a=ease((t-0.4)/0.8); text_a(c,(60,1250),big,F(ACC,330),blob,a*0.9 if a>0 else 0,int(60*(1-a)),anchor='ls')
        sticker(c,(240,280),'SENİN İÇİN',F(BOLD,30),nc,CREAM if nc!=PINK else PLUM,-6,back((t-0.1)/0.4))
        a=ease((t-0.3)/0.5); text_a(c,(70,340),title,F(BOLD,120),tc,a,int(40*(1-a)))
        text_a(c,(76,500),"Pudra'da seni bekleyenler:",F(REG,40),tc,ease((t-0.7)/0.4))
        for j,it in enumerate(items):
            k=back((t-1.0-j*0.35)/0.4)
            if k<=0: continue
            y=620+j*130
            d.ellipse([76,y,76+int(64*k),y+int(64*k)],fill=nc)
            text_a(c,(108,y+32),'✓' if False else str(j+1),F(BOLD,int(36*k)+1),CREAM if nc!=PINK else PLUM,1,anchor='mm')
            a=ease((t-1.0-j*0.35)/0.4); text_a(c,(170,y+6),it,F(BOLD,48),tc,a,int(16*(1-a)))
        for (x,y,rr,st) in [(990,250,40,2.0),(900,170,22,2.3)]:
            k=back((t-st)/0.4)
            if k>0: sparkle(d,x,y,rr*k*(1+0.12*math.sin(t*5+x)),nc)
        text_a(c,(80,1280),'PUDRA DERGİ',F(BOLD,22),tc,1); text_a(c,(W-80,1278),f'{i+2}/6',F(MED,24),tc,1,anchor='ra')
        logo(c,lv); return c
    return fn

def last(t):
    c=Image.new('RGB',(W,H),PLUM); d=ImageDraw.Draw(c)
    p=math.sin(t*1.5)*20; r=int(420*ease(t/0.7))
    d.ellipse([W-60-r-p,260-r-p,W-60+r+p,260+r+p],fill=BERRY); r2=int(300*ease(t/0.7)); d.ellipse([-80-r2,1250-r2,-80+r2,1250+r2],fill=RED)
    sticker(c,(W//2,380),'SÖZ VERİYORUZ',F(BOLD,32),PINK,PLUM,-4,back((t-0.1)/0.4))
    for txt,font,y,st,col in [('Burada',F(BOLD,140),540,0.3,CREAM),('filtre yok.',F(ACC,150),710,0.65,PINK)]:
        a=ease((t-st)/0.5); text_a(c,(W//2,y),txt,font,col,a,int(40*(1-a)),anchor='ms')
    a=ease((t-1.3)/0.5); text_a(c,(W//2,820),'Her gün, senden bir parça.',F(MED,44),CREAM,a,anchor='ms')
    k=back((t-1.8)/0.45)*(1+0.03*math.sin(t*6))
    sticker(c,(W//2,980),'Takip et ›',F(BOLD,56),CREAM,BERRY,-2,k,56,26)
    a=ease((t-2.4)/0.5); text_a(c,(W//2,1140),'Hangi sayfa sendin? Yorumlara yaz.',F(BOLD,40),PINK,a,anchor='ms')
    logo(c,'B'); return c

# Story (9:16) — Pudra öne çıkanı için
SW,SH=1080,1920
def st1(t):
    c=Image.new('RGB',(SW,SH),BERRY); d=ImageDraw.Draw(c)
    p=math.sin(t*1.5)*20; r=int(420*ease(t/0.8)); d.ellipse([SW+40-r-p,1700-r-p,SW+40+r+p,1700+r+p],fill=PINK)
    sticker(c,(300,520),'BİZ KİMİZ?',F(BOLD,34),PINK,PLUM,-6,back((t-0.1)/0.4))
    for j,(txt,font,col) in enumerate([('Pudra,',F(BOLD,130),CREAM),('her yaştan',F(BOLD,110),CREAM),('kadının',F(BOLD,110),CREAM),('dergisi.',F(ACC,140),PINK)]):
        a=ease((t-0.4-j*0.25)/0.5); text_a(c,(70,620+j*150),txt,font,col,a,int(40*(1-a)))
    a=ease((t-1.8)/0.5); text_a(c,(76,1260),'Kusursuzluk değil, gerçeklik.',F(MED,44),CREAM,a)
    logo(c,'A',True); return c
def st2(t):
    c=Image.new('RGB',(SW,SH),PLUM); d=ImageDraw.Draw(c)
    p=math.sin(t*1.5)*20; r=int(420*ease(t/0.8)); d.ellipse([-100-r-p,500-r-p,-100+r+p,500+r+p],fill=BERRY)
    sticker(c,(SW//2,480),'BURADA NE BULURSUN?',F(BOLD,34),PINK,PLUM,-4,back((t-0.1)/0.4))
    for j,(lab,col) in enumerate([('Moda',RED),('Güzellik',PINK),('Cilt bakımı',CREAM),('İlişkiler',RED)]):
        k=back((t-0.5-j*0.3)/0.4)
        sticker(c,(SW//2+(-1)**j*120,680+j*190),lab,F(BOLD,72),col,PLUM if col!=RED else CREAM,(-1)**j*5,k,50,24)
    a=ease((t-2.0)/0.5); text_a(c,(SW//2,1500),'Samimi, dürüst, her gün.',F(MED,46),CREAM,a,anchor='ms')
    logo(c,'B',True); return c
def st3(t):
    c=Image.new('RGB',(SW,SH),PINK); d=ImageDraw.Draw(c)
    p=math.sin(t*1.5)*20; r=int(460*ease(t/0.8)); d.ellipse([SW-60-r-p,420-r-p,SW-60+r+p,420+r+p],fill=BERRY)
    for j,(txt,font,col) in enumerate([('Bizi takip et,',F(BOLD,110),PLUM),('bildirimleri',F(BOLD,110),PLUM),('aç.',F(ACC,150),BERRY)]):
        a=ease((t-0.3-j*0.25)/0.5); text_a(c,(70,760+j*150),txt,font,col,a,int(40*(1-a)))
    k=back((t-1.5)/0.4)
    if k>0:
        bx,by=820,1300; d.ellipse([bx-int(110*k),by-int(110*k),bx+int(110*k),by+int(110*k)],fill=BERRY)
        sw=math.sin(t*12)*8 if t>1.9 else 0
        d.pieslice([bx-50+sw,by-60,bx+50+sw,by+40],180,360,fill=CREAM); d.rectangle([bx-50+sw,by-12,bx+50+sw,by+30],fill=CREAM)
        d.ellipse([bx-12+sw,by+30,bx+12+sw,by+52],fill=CREAM)
    logo(c,'B',True); return c

fns={'i1':(cover,(W,H)),'i2':(age(0),(W,H)),'i3':(age(1),(W,H)),'i4':(age(2),(W,H)),'i5':(age(3),(W,H)),'i6':(last,(W,H)),'h1':(st1,(SW,SH)),'h2':(st2,(SW,SH)),'h3':(st3,(SW,SH))}
n=sys.argv[1]
if n=='preview':
    from PIL import Image as I
    sh=I.new('RGB',(6*270+35,338*1+500),'white')
    for k,key in enumerate(['i1','i2','i3','i4','i5','i6']): sh.paste(fns[key][0](4.5).resize((270,338)),(5+k*275,5))
    for k,key in enumerate(['h1','h2','h3']): sh.paste(fns[key][0](4.5).resize((270,480)),(5+k*275,350))
    sh.save('/home/claude/pudra/rev_intro.jpg',quality=85)
else:
    fn,sz=fns[n]; render(fn,f'/home/claude/pudra/out6/{n}.mp4',6,sz)
