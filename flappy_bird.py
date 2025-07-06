import pygame
import random
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
flying=False
score=0
clock=pygame.time.Clock()
pipe_gap=150
pipe_frequency=1500
last_pipe=pygame.time.get_ticks()-pipe_frequency
class Pole(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        super().__init__()
        self.x=x
        self.y=y
        self.pos=pos
        self.image=pole
        self.rect=self.image.get_rect()
        self.rect.center=self.x,self.y
        if pos==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-int(pipe_gap /2)]
        if pos==-1:
            self.rect.topleft=[x,y+int(pipe_gap/2)]
    def update(self):
        self.rect.x-=5
        if self.rect.right< 0:
            self.kill()

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.images=images
        self.index=0
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=self.x,self.y
        self.counter=0
        self.vel=0
        self.clicked=False
    def update(self):  
        if flying==True:
            self.vel+=0.5
            if self.rect.bottom<500:
                self.rect.y+=self.vel
        if game==True:
            #jump
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                self.vel=-5
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False

            self.counter+=1  
            if self.counter>5:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
            self.image=self.images[self.index]
bird_group=pygame.sprite.Group()
flappy=Bird(50,300)
bird_group.add(flappy)
pole_group=pygame.sprite.Group()
run=True
while run==True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and game==True:
            flying=True
    screen.fill("red")
    screen.blit(background,(0,0))
    screen.blit(platform,(platform_x,500))
    if pygame.sprite.groupcollide(bird_group,pole_group,False,False):
        game=False
    if flappy.rect.bottom>500:
        game=False
        flying=False
    if  game==True:
        timenow=pygame.time.get_ticks()
        if timenow-last_pipe>pipe_frequency:
            random.randint
            h=random.randint(-100,100)
            bottompole=Pole(WIDTH,HEIGHT/2+h,-1)
            toppole=Pole(WIDTH,HEIGHT/2+h,+1)
            pole_group.add(bottompole)
            pole_group.add(toppole)
            last_pipe=timenow
        platform_x-=5
        if abs(platform_x)>=35:
            platform_x=0
        bird_group.update()   
        pole_group.update ()
    bird_group.draw(screen)
    pole_group.draw(screen)
    pygame.display.update()
