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
    def draw (self):
        pygame.draw.rect(screen,self.clr,(self.x,self.y,self.w,self.h))
    def grow(self):
        self.w+=50
        self.h+=50   
        self.draw()
r1=Rectangle(200,250,250,200,"yellow")      
run=True
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill("red")
            r1.draw()
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            screen.fill("green")
            r1.grow()
            pygame.display.update()
        if event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            r2=Rectangle(pos[0],pos[1],10,5,"blue")
            r2.draw()
            pygame.display.update()

            