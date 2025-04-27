import pygame
pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
galaxy=pygame.image.load("images\galaxy.png")
Redship=pygame.image.load("images\Redship.png")
Redship=pygame.transform.scale(Redship,(50,70))
Redship=pygame.transform.rotate(Redship,90)
yellowship=pygame.image.load("images\yellowship.png")
yellowship=pygame.transform.scale(yellowship,(50,70))
yellowship=pygame.transform.rotate(yellowship,270)
run=True
redx=100
redy=100
yellowx=500
yellowy=100
Border=pygame.Rect(300,0,10,1000)
Redbullets=[]
yellowbullets=[]

while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                redy-=30
            if event.key==pygame.K_s:
                redy+=30
            if event.key==pygame.K_a:
                redx-=30 
            if event.key==pygame.K_d and redx<250:
                redx+=30
            if event.key==pygame.K_UP:
                yellowy-=30
            if event.key==pygame.K_DOWN:
                yellowy+=30
            if event.key==pygame.K_LEFT and yellowx>325:
                yellowx-=30
            if event.key==pygame.K_RIGHT:
                yellowx+=30
            if event.key==pygame.K_q:
                bullet=pygame.Rect(redx,redy+35,5,5)
                Redbullets.append(bullet)
            if event.key==pygame.K_e:
                bullet=pygame.Rect(yellowx,yellowy+35,5,5)
                yellowbullets.append(bullet)
    screen.fill("red")
    screen.blit(galaxy,(0,0))
    pygame.draw.rect(screen,"red",Border)
    screen.blit(Redship,(redx,redy))
    screen.blit(yellowship,(yellowx,yellowy))
    for bullet in Redbullets:
        pygame.draw.rect(screen,"red",bullet)
        bullet.x+=3
    for bullet in yellowbullets:
        pygame.draw.rect(screen,"yellow",bullet)
        bullet.x-=3
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
    pygame.display.update()
