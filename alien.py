import pygame
import random
alien=pygame.Rect(1,70,64,64)
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
Alien=pygame.image.load("images\Alien.png")
run=True
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type ==pygame.MOUSEMOTION:
            Pos=pygame.mouse.get_pos()
            if alien.collidepoint(Pos):
                alien.x=random.randint(50,550)
                alien.y=random.randint(50,550)
    screen.fill("blue")
    screen.blit(Alien,(alien.x,alien.y))
    pygame.display.update()