import pygame
import time 
pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
rocket=pygame.image.load("images\Rocket.png")
space=pygame.image.load("images\space.png")
font=pygame.font.SysFont("Times New Roman",50)
rocketx=300
rockety=300
run=True
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                rockety-=30
            if event.key==pygame.K_s:
                rockety+=30
            if event.key==pygame.K_a:
                rocketx-=30
            if event.key==pygame.K_d:
                rocketx+=30
    screen.fill("red")
    screen.blit(space,(0,0))
    screen.blit(rocket,(rocketx,rockety))
   
    rockety+=0.5
    if rockety>=600:
        run=False
        text=font.render("Gameover",True,"green")
        screen.blit(text,(300,300))
        pygame.display.update()
        time.sleep(2)
    pygame.display.update()
    

