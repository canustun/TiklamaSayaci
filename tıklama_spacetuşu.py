#space tuşuna hızlı basma sayım aracı
import pygame as p
from datetime import datetime

p.init()

font=p.font.SysFont('Bold',40)
zaman=datetime.now()
skor,süre,ortalama=0,20,[]
ortalama_skoru=0

p.display.set_caption("Tıklama Sayacı")
ekran=p.display.set_mode((400,250))
calis=True
while calis:
    tiklama=p.key.get_pressed()
    ekran.fill("Blue")
    for i in p.event.get():
        if i.type==p.QUIT:
            calis=False
        if i.type==p.KEYUP:
            if tiklama[p.K_SPACE]:
                skor+=1
    
    a=datetime.now()-zaman
    if a.seconds>=1:
        süre-=1
        ortalama.append(skor-ortalama_skoru)
        ortalama_skoru=skor
        zaman=datetime.now()

    if tiklama[p.K_y]:
            skor,süre,zaman=0,20,datetime.now()
            ekran.fill("Blue")
            ortalama_skoru=0
            
    if süre<1:
        topla=0
        for i in ortalama:
            topla+=i    
        
        ekran.fill("Cyan")
        ekran.blit(font.render("Süre Bitti !",True,("Black")),(150,50))
        ekran.blit(p.font.SysFont('Bold',21).render(f" {skor} Adet Tıkladınız :)",True,("black")),(130,150))
        ekran.blit(p.font.SysFont('Bold',21).render(f"Saniyede Tıklama Ortalamanız : {str(topla/len(ortalama))[:4]}",True,("black")),(90,170))

        skor,süre,zaman=0,20,datetime.now()
        ortalama,ortalama_skoru=[],0

        p.display.update()
        p.time.wait(10000)

    ekran.blit(p.font.SysFont('Bold',25).render("Baştan Başlamak için Y tuşuna bas",True,("Orange")),(50,160))
    ekran.blit(font.render("Kalan Saniye : "+str(süre),True,("White")),(55,50))
    ekran.blit(font.render("Tıklama Sayısı : "+str(skor),True,("White")),(55,100))

    p.display.update()
