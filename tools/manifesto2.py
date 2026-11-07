from anim import *
def make(W,H,story):
    oy=0 if not story else 285
    def fn(t):
        c=Image.new('RGB',(W,H),PLUM); d=ImageDraw.Draw(c)
        p=math.sin(t*1.6)*26; s=ease(t/0.8)
        r=int(470*s); d.ellipse([1030-r-p,-170+oy-r-p,1030+r+p,-170+oy+r+p],fill=BERRY)
        r=int(400*s); d.ellipse([20-r+p,1330+oy-r+p,20+r-p,1330+oy+r-p],fill=RED)
        dots(d,90,170+oy,5,3,46,7,BERRY)
        sticker(c,(W//2,330+oy),'PUDRA · MANİFESTO',F(BOLD,30),PINK,PLUM,-5,back((t-0.1)/0.45))
        for txt,font,y,st,col in [('Topuklar',F(BOLD,170),560,0.4,CREAM),('bizde,',F(BOLD,170),740,0.8,CREAM),('söz de bizde.',F(ACC,130),920,1.3,PINK)]:
            a=ease((t-st)/0.55); text_a(c,(W//2,y+oy),txt,font,col,a,int(70*(1-a)),anchor='ms')
        a=ease((t-2.0)/0.5)
        if a>0:
            w=int(220*a); d.line([(W//2-w//2,1010+oy),(W//2+w//2,1010+oy)],fill=PINK,width=5)
            text_a(c,(W//2,1090+oy),'Kadının dünyası. Herkes misafir.',F(MED,40),CREAM,a,anchor='ms')
        for (x,y,r,st,col) in [(960,300,44,2.5,PINK),(120,300,30,2.8,CREAM),(930,1220,40,3.1,RED),(150,1100,26,3.4,PINK)]:
            k=back((t-st)/0.4)
            if k>0: sparkle(d,x,y+oy,r*k*(1+0.12*math.sin(t*5+x)),col)
        logo(c,'B',story); return c
    return fn
render(make(1080,1920,True),'out3/p3_story.mp4',7,(1080,1920))
render(make(1080,1350,False),'out3/p3_1.mp4',7,(1080,1350),'out3/p3_1.jpg')
