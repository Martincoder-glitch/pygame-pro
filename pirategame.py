import pygame
pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pirate_ship=pygame.image.load("images\pirate_ship.png")
Treasure=pygame.image.load("images\Treasure.png")
pirate=pygame.image.load("images\pirate.png")
Bomb=pygame.image.load("images\Bomb.png")
run=True
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
    screen.fill("red")
    screen.blit(pirate_ship)
    pygame.display.update()
