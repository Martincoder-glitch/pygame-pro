import pygame
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
class Rocket(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load("images\Rocket.png")
        self.rect=self.image.get_rect()
        self.rect.center=self.x,self.y
r1=Rocket(10,50)
rocket_group=pygame.sprite.Group()
rocket_group.add(r1)
run=True
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                r1.rect.y-=30
            if event.key==pygame.K_DOWN:
                r1.rect.y+=30
            if event.key==pygame.K_LEFT:
                    r1.rect.x-=30
            if event.key==pygame.K_RIGHT:
                r1.rect.x+=30      
    screen.fill("red")
    rocket_group.draw(screen)
    pygame.display.update()
