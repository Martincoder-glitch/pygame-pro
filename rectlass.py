import pygame
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
class Rectangle():
    def __init__(self,x,y,w,h,clr):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.clr=clr
    def draw(self):
       pygame.draw.rect(screen,self.clr,(self.x,self.y,self.w,self.h))
r1=Rectangle(200,200,250,300,"blue")
r2=Rectangle(100,250,250,300,"yellow")
run=True
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
    screen.fill("red")
    r1.draw()
    r2.draw()
    pygame.display.update()