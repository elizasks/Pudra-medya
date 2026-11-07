import os
from anim import *
from pudra import fit
import sys
W,H=1080,1920; P=os.environ.get('PUDRA_PHOTOS','photos/')
_ph={}
def photo(name):
    if name not in _ph: _ph[name]=load(P+name)
    return _ph[name]
def kb(name,box,t,zoom=0.06,cen=(0.5,0.5)):
    w,h=box; z=1+zoom*min(t,6)/6
    im=fit(photo(name),(int(w*z),int(h*z)),cen)
    ox=(im.width-w)//2; oy=(im.height-h)//2
    return im.crop((ox,oy,ox+w,oy+h))
def rounded(im,r):
    m=Image.new('L',im.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,im.width-1,im.height-1],radius=r,fill=255)
    out=Image.new('RGBA',im.size); out.paste(im,(0,0),m); return out
def grad(c,top,h,col,amax):
    g=Image.new('L',(1,h))
    for i in range(h): g.putpixel((0,i),int(amax*(i/h)**1.5))
    g=g.resize((W,h)); solid=Image.new('RGB',(W,h),col)
    reg=c.crop((0,top,W,top+h)); c.paste(Image.composite(solid,reg,g),(0,top))

# Pzt 10:30 — Reels duyurusu
def s2_1(t):
    c=kb('IMG_4185.jpeg',(W,H),t,0.08,(0.5,0.45)); grad(c,700,1220,PLUM,240); d=ImageDraw.Draw(c)
    sticker(c,(240,1040),'YENİ REELS',F(BOLD,32),RED,CREAM,-6,back((t-0.3)/0.4))
    for txt,font,y,st,col in [('Sonbahar',F(BOLD,150),1100,0.6,CREAM),('formülü',F(ACC,150),1260,0.95,PINK)]:
        a=ease((t-st)/0.5); text_a(c,(70,y),txt,font,col,a,int(50*(1-a)))
    text_a(c,(76,1460),'7 parça, sıfır düşünme.',F(MED,40),CREAM,ease((t-1.5)/0.5))
    a=ease((t-2.0)/0.4)
    if a>0: sticker(c,(W//2+int(8*math.sin(t*6)),1580),'Profilde izle ›',F(BOLD,40),CREAM,BERRY,0,a,40,20)
    for (x,y,r,st) in [(920,1150,40,1.3),(1000,1300,24,1.6)]:
        k=back((t-st)/0.4)
        if k>0: sparkle(d,x,y,r*k*(1+0.12*math.sin(t*5+x)),PINK)
    logo(c,'B',True); return c

# Pzt 13:00 — A mı B mi?
def s2_2(t):
    c=Image.new('RGB',(W,H),PINK); d=ImageDraw.Draw(c)
    p=math.sin(t*1.5)*20; r=int(420*ease(t/0.7))
    d.ellipse([W-80-r-p,1700-r-p,W-80+r+p,1700+r+p],fill=BERRY)
    text_a(c,(W//2,400),'SONBAHAR DÜELLOSU',F(BOLD,32),BERRY,ease((t-0.1)/0.4),anchor='ms')
    text_a(c,(W//2,500),'Hangisi senin?',F(BOLD,84),PLUM,ease((t-0.3)/0.5),int(30*(1-ease((t-0.3)/0.5))),anchor='ms')
    bw,bh=470,800
    for k,(name,lab,x0,dir) in enumerate([('IMG_4186.jpeg','A',50,-1),('IMG_4189.jpeg','B',W-50-bw,1)]):
        a=ease((t-0.6-k*0.25)/0.6); 
        if a<=0: continue
        im=rounded(kb(name,(bw,bh),t,0.05),36)
        x=int(x0+dir*(1-a)*500); y=600+int(20*math.sin(t*2+k))
        c.paste(im,(x,y),im)
        s=back((t-1.3-k*0.2)/0.4)
        if s>0:
            cx=x+bw//2; cy=y+bh-10; rr=int(70*s)
            d.ellipse([cx-rr,cy-rr,cx+rr,cy+rr],fill=RED if k==0 else PLUM)
            text_a(c,(cx,cy+30*s),lab,F(BOLD,int(90*s)+1),CREAM,1,anchor='ms')
    a=ease((t-2.0)/0.5)
    text_a(c,(W//2,1560),'A mı, B mi? Harfini yanıtla.',F(MED,42),PLUM,a,anchor='ms')
    logo(c,'B',True); return c

# Pzt 19:00 — Editörün ipucu (kullanıcının fotoğrafı)
def s2_3(t):
    c=Image.new('RGB',(W,H),PLUM); d=ImageDraw.Draw(c)
    r=int(380*ease(t/0.7)); p=math.sin(t*1.4)*16
    d.ellipse([-120-r-p,520-r-p,-120+r+p,520+r+p],fill=BERRY)
    a=ease((t-0.2)/0.6)
    im=rounded(kb('IMG_4039.jpeg',(640,860),t,0.06,(0.5,0.42)),40)
    c.paste(im,(W-640-60+int((1-a)*300),330),im) if a>0 else None
    sticker(c,(250,1250),'EDİTÖRÜN İPUCU',F(BOLD,30),PINK,PLUM,-6,back((t-0.5)/0.4))
    for txt,font,y,st,col in [('Haki + siyah',F(BOLD,100),1310,0.9,CREAM),('= en kolay',F(ACC,100),1430,1.25,PINK),('şıklık.',F(BOLD,100),1545,1.55,CREAM)]:
        a=ease((t-st)/0.5); text_a(c,(70,y),txt,font,col,a,int(40*(1-a)))
    k=back((t-2.1)/0.4)
    if k>0: sparkle(d,960,1290,44*k*(1+0.1*math.sin(t*5)),PINK)
    logo(c,'B',True); return c

# Sal 10:30 — Tırnak ilhamı
def s3_1(t):
    c=kb('IMG_4162.jpeg',(W,H),t,0.07,(0.5,0.4)); grad(c,800,1120,PLUM,235); d=ImageDraw.Draw(c)
    sticker(c,(280,1080),'SEZONUN RENGİ',F(BOLD,32),CREAM,PLUM,-5,back((t-0.3)/0.4))
    for txt,font,y,st,col in [('Çikolata',F(ACC,170),1130,0.6,PINK),('kahve.',F(BOLD,150),1330,0.95,CREAM)]:
        a=ease((t-st)/0.5); text_a(c,(70,y),txt,font,col,a,int(50*(1-a)))
    a=ease((t-1.6)/0.4)
    if a>0: sticker(c,(330+int(6*math.sin(t*6)),1600),'Kaydet, manikürde göster ›',F(BOLD,34),CREAM,BERRY,0,a,34,18)
    for k,(x,y) in enumerate([(880,1230),(980,1400)]):
        s=back((t-1.2-k*0.3)/0.4)
        if s>0: sparkle(d,x,y,(36-k*10)*s,PINK)
    logo(c,'A',True); return c

# Sal 13:00 — Doğru mu yanlış mı?
def s3_2(t):
    flip=t>3.0
    bg=PLUM if not flip else RED
    c=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(c)
    p=math.sin(t*1.6)*20; r=int(380*ease(t/0.7))
    d.ellipse([W-60-r-p,360-r-p,W-60+r+p,360+r+p],fill=BERRY if not flip else PLUM)
    dots(d,90,1620,6,3,46,7,BERRY if not flip else PINK)
    sticker(c,(W//2,560),'CİLT BAKIMI TESTİ',F(BOLD,32),PINK,PLUM,-4,back((t-0.1)/0.4))
    if not flip:
        for j,ln in enumerate(['"Kışın güneş','kremine gerek','yok."']):
            a=ease((t-0.4-j*0.2)/0.5); text_a(c,(W//2,820+j*130),ln,F(BOLD,110),CREAM,a,int(40*(1-a)),anchor='ms')
        a=ease((t-1.3)/0.4)
        text_a(c,(W//2,1280),'Doğru mu, yanlış mı?',F(ACC,80),PINK,a,anchor='ms')
        k=(t-1.8)
        if k>0:
            cnt=3-int(k/0.4)
            if cnt>0: text_a(c,(W//2,1520),str(cnt),F(BOLD,160),PINK,1,anchor='ms')
    else:
        k=back((t-3.0)/0.4)
        text_a(c,(W//2,860),'YANLIŞ!',F(BOLD,int(180*max(k,0.01))),CREAM,1,anchor='ms')
        a=ease((t-3.4)/0.5)
        for j,ln in enumerate(['UVA ışınları bulutların ve','camın arasından geçer.','Kışın da SPF sür.']):
            text_a(c,(W//2,1040+j*70),ln,F(MED,48),CREAM,a,int(20*(1-a)),anchor='ms')
        a=ease((t-4.2)/0.4)
        if a>0: sticker(c,(W//2,1400),'Bilmeyen arkadaşına gönder ›',F(BOLD,38),CREAM,RED,-3,a,38,20)
    logo(c,'B',True); return c

# Sal 19:00 — İlişki sorusu (yarınki carousel'e ısınma)
def s3_3(t):
    c=Image.new('RGB',(W,H),BERRY); d=ImageDraw.Draw(c)
    p=math.sin(t*1.5)*18; r=int(430*ease(t/0.8))
    d.ellipse([W-40-r-p,1560-r-p,W-40+r+p,1560+r+p],fill=RED)
    r2=int(240*ease(t/0.8)); d.ellipse([-60-r2,380-r2,-60+r2,380+r2],fill=(168,30,90))
    fy=int(1900-560*ease((t-0.4)/0.8)); waving_flag(d,720,fy,340,t,CREAM,PLUM)
    sticker(c,(300,560),'GÜNÜN SORUSU',F(BOLD,32),PINK,PLUM,-6,back((t-0.2)/0.4))
    for j,(ln,font,col) in enumerate([('İlk buluşmada',F(BOLD,92),CREAM),('en büyük',F(BOLD,92),CREAM),('kırmızı bayrak',F(ACC,110),PINK),('sence ne?',F(BOLD,92),CREAM)]):
        a=ease((t-0.5-j*0.25)/0.5); text_a(c,(70,720+j*120),ln,font,col,a,int(40*(1-a)))
    a=ease((t-1.8)/0.4)
    if a>0: sticker(c,(330+int(6*math.sin(t*6)),1300),'Yanıtla, anonim paylaşacağız',F(BOLD,32),CREAM,BERRY,3,a,34,18)
    logo(c,'A',True); return c

fns={'s2_1':s2_1,'s2_2':s2_2,'s2_3':s2_3,'s3_1':s3_1,'s3_2':s3_2,'s3_3':s3_3}
name=sys.argv[1]
if name=='preview':
    from PIL import Image as I
    sh=I.new('RGB',(6*270+35,480+10),'white')
    for k,(n,fn) in enumerate(fns.items()):
        tt=4.8 if n!='s3_2' else 2.6
        sh.paste(fn(tt).resize((270,480)),(5+k*275,5))
    sh.save('rev_st.jpg',quality=85)
    fn=fns['s3_2']; fn(4.8).resize((270,480)).save('rev_st2.jpg')
else:
    render(fns[name],f'out4/{name}.mp4',6,(W,H))
