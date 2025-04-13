import pygame
import time
pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#adding images
cake=pygame.image.load("images\cake.jpg")
decor=pygame.image.load("images\decor.jpg")
confetti=pygame.image.load("images\confetti.jpg")
#adding fonts
font=pygame.font.SysFont("Times New Roman",50)
run=True
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
    screen.fill("red")
    screen.blit(cake,(0,0))
    text=font.render("happy birthday",True,"green")
    screen.blit(text,(20,20))
    pygame.display.update()
    time.sleep(2)
    screen.blit(decor,(0,0))
    text=font.render("the party venue",True,"green")
    screen.blit(text,(200,250))
    pygame.display.update()
    time.sleep(2)
    screen.blit(confetti,(0,0))
    text=font.render("Confetti",True,"green")
    screen.blit(text,(20,20))
    pygame.display.update()
    time.sleep(2)