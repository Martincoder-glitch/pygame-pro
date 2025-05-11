import pygame
import random
from random import randint
pygame.init()
WIDTH=500
HEIGHT=500
TITLE="bumblebee game"
Bee=pygame.Rect(300,0,64,64)
Flower=pygame.Rect(1,70,64,64)
# Actor=("Actor")
# one=Actor("one") 
# one.x = 200
# one.y=100
# flower=Actor("flower")
# flower.x = 250
# flower.y = 3

screen=pygame.display.set_mode((WIDTH,HEIGHT))
one=pygame.image.load("images\one.png")
flower=pygame.image.load("images\Flower.png")
galaxy=pygame.image.load("images\galaxy.png")
font=pygame.font.SysFont("Times New Roman",25)
score=0
gameover=False
Flower.x=randint(70,(WIDTH-70))   
Flower.y=randint(70,(HEIGHT-70))
# def place_flower():
#     flower.x=randint(70,(WIDTH-70))
#     flower.y=randint(70,(HEIGHT-70))qq

# def update():
#     global score
   
#     if one.colliderect(flower):
#         place_flower()
#         score +=1
# def timeup():
#     global gameover
#     gameover=True
text=font.render("score"+str(score),True,"red")
def place_flower():
        Flower.x=randint(70,(WIDTH-70))
        Flower.y=randint(70,(HEIGHT-70))
run=True
while run==True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                Bee.y-=30
            if event.key==pygame.K_DOWN:
                Bee.y+=30
            if event.key==pygame.K_LEFT:
                    Bee.x-=30
            if event.key==pygame.K_RIGHT:
                Bee.x+=30      
        if event.type ==pygame.QUIT:
            pygame.quit()
           
    screen.blit(galaxy,(0,0)) 
    screen.blit(one,(Bee.x,Bee.y))
    screen.blit(flower,(Flower.x,Flower.y))  
    screen. blit(text,(100,50)) 
    if Bee.colliderect(Flower):
        place_flower()
        score +=1
        text=font.render("score"+str( score),True,"yellow") 
    pygame.display.update()



pygame.display.update()
