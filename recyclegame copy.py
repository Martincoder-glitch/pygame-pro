import pygame
import random
pygame.init()
WIDTH=700
HEIGHT=700
score=0
screen=pygame.display.set_mode((WIDTH,HEIGHT))
Renewable=pygame.image.load("images\Renewable.png")
font=pygame.font.SysFont("Times New Roman",25)
bag=pygame.image.load("images\Bag.png")
pencil=pygame.image.load("images\pencil.png")
box=pygame.image.load("images\Box.png")
images=[bag,pencil,box]
Renewable=pygame.transform.scale(Renewable,(700,700))
text=font.render("score"+str(score),True,"red")
class Recycling_bin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load("images\Recycling_bin.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.center=self.x,self.y
class plastic_bag(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load("images\plastic_bag.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.center=self.x,self.y
class Bag(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.image=random.choice(images)
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.center=self.x,self.y

recycle_group=pygame.sprite.Group()
Plastic_group=pygame.sprite.Group()
bag_group=pygame.sprite.Group()
r1=Recycling_bin(50,50)
recycle_group.add(r1)
for i in range(5):
    x=random.randint(50,650)
    y=random.randint(50,650)
    p1=plastic_bag(x,y)
    Plastic_group.add(p1)
for i in range(10):
    x=random.randint(50,650)
    y=random.randint(50,650)
    p2=Bag(x,y)
    bag_group.add(p2)
run=True
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type ==pygame.MOUSEMOTION:
                Pos=pygame.mouse.get_pos()
                r1.rect.center=Pos
    screen.fill("red")
    screen.blit(Renewable,(0,0))
    recycle_group.draw(screen)
    Plastic_group.draw(screen)
    bag_group.draw(screen)
    itemlist= pygame.sprite.spritecollide(r1,bag_group,True)
    for item in itemlist:
        score+=1
        text=font.render("score"+str(score),True,"red")
    itemlist2= pygame.sprite.spritecollide(r1,Plastic_group,True)
    for item in itemlist2:
        score-=1
        text=font.render("score"+str(score),True,"red")
    screen. blit(text,(100,50))
    pygame.display.update()
