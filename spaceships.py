import pygame
import time 
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
font=pygame.font.SysFont("Times New Roman",25)
run=True
redx=100
redy=100
yellowx=500
yellowy=100
Border=pygame.Rect(300,0,10,1000)
Redbullets=[]
yellowbullets=[]
Red_health=100
Yellow_health=100
text=font.render("Redhealth"+str(Red_health),True,"red")
text2=font.render("Yellowhealth"+str(Yellow_health),True,"yellow")
red=pygame.Rect(redx,redy,50,70)
yellow=pygame.Rect(yellowx,yellowy,50,70)
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                red.y-=30
            if event.key==pygame.K_s:
                red.y+=30
            if event.key==pygame.K_a:
                red.x-=30 
            if event.key==pygame.K_d and red.x<250:
                red.x+=30
            if event.key==pygame.K_UP:
                yellow.y-=30
            if event.key==pygame.K_DOWN:
                yellow.y+=30
            if event.key==pygame.K_LEFT and yellow.x>325:
                yellow.x-=30
            if event.key==pygame.K_RIGHT:
                yellow.x+=30
            if event.key==pygame.K_q:
                bullet=pygame.Rect(red.x,red.y+35,5,5)
                Redbullets.append(bullet)
            if event.key==pygame.K_e:
                bullet=pygame.Rect(yellow.x,yellow.y+35,5,5)
                yellowbullets.append(bullet)
    screen.fill("red")
    screen.blit(galaxy,(0,0))
    screen. blit(text,(100,50))
    screen. blit(text2,(400,50))
    pygame.draw.rect(screen,"red",Border)
    screen.blit(Redship,(red.x,red.y))
    screen.blit(yellowship,(yellow.x,yellow.y))
    if Red_health==0:
        run=False
        text=font.render("Gameover",True,"red")
        screen.blit(text,(300,300))
        pygame.display.update()
        time.sleep(2)
    if Yellow_health==0:
        run=False
        text=font.render("Gameover",True,"Yellow")
        screen.blit(text,(300,300))
        pygame.display.update()
        time.sleep(2)
    for bullet in Redbullets:
        pygame.draw.rect(screen,"red",bullet)
        bullet.x+=3
        if yellow.colliderect(bullet):
            Redbullets.remove(bullet)
            Yellow_health-=1
            text2=font.render("Yellowhealth"+str(Yellow_health),True,"yellow")
    for bullet in yellowbullets:
        pygame.draw.rect(screen,"yellow",bullet)
        bullet.x-=3
        if red.colliderect(bullet):
            yellowbullets.remove(bullet)
            Red_health-=1
            text=font.render("Redhealth"+str(Red_health),True,"red")
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
    pygame.display.update()
