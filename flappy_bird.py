import pygame
pygame.init()
WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pole=pygame.image.load("images\pole.png")
bird_1=pygame.image.load("images\Bird_1.png")
bird_2=pygame.image.load("images\Bird_2.png")
bird_3=pygame.image.load("images\Bird_3.png")
background=pygame.image.load("images\Background.png")
platform=pygame.image.load("images\platform.png")
platform_x=0
images=[bird_1,bird_2,bird_3]
game=True

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.images=images
        self.index=0
        self.image=self.image[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=self.x,self.y
        self.counter=0
    def update(self):  
        self.counter+=1  
        if self.counter>5:
            self.counter=0
            self.index+=1
            if self.index>=len(self.images):
                self.index=0
        self.image=self.image[self.index]
run=True
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
    screen.fill("red")
    screen.blit(background,(0,0))
    screen.blit(platform,(platform_x,500))
    if  game==True:
        platform_x-=5
        if abs(platform_x)>=35:
            platform_x=0
    pygame.display.update()
