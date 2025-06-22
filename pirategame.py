import pygame
import random
pygame.init()
WIDTH=600
HEIGHT=600
score=0
screen=pygame.display.set_mode((WIDTH,HEIGHT))
font=pygame.font.SysFont("Times New Roman",25)
pirate_ship=pygame.image.load("images\pirate_ship.png")
Treasure=pygame.image.load("images\Treasure.png")
pirate_ship=pygame.transform.scale(pirate_ship,(600,600))
pirate=pygame.image.load("images\pirate.png")
Bomb=pygame.image.load("images\Bomb.png")
text=font.render("score"+str(score),True,"red")
class treasure(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load("images\Treasure.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.center=self.x,self.y

chest=pygame.sprite.Group()
for i in range(10):
    x=random.randint(50,650)
    y=random.randint(50,650)
    p2=treasure(x,y)
    chest.add(p2) 
run=True

while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        
     
    screen.fill("red")
    screen.blit(pirate_ship,(0,0))
    chest.draw(screen)  
    pygame.display.update()
