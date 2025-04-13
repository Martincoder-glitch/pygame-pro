import pygame
pygame.init()
WIDTH=500
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()
run=True  
class circle():
    def __init__(self,x,y,clr,radius):
        self.x=x
        self.y=y
        self.clr=clr
        self.radius=radius
        self.vx=200
        self.vy=0
        self.gravity=2000
    def update(self,t):
        uy=self.vy
        self.vy+=self.gravity*t
        self.y+=(self.vy+uy)*0.5*t
        self.x+=self.vx*t
        if self.y>=HEIGHT-self.radius:
            self.y=HEIGHT-self.radius
            self.vy=-self.vy*0.9
        if self.x>=WIDTH-self.radius or self.x<=self.radius:
            self.vx=-self.vx    
    def draw(self):
        pygame.draw.circle(screen,self.clr,(self.x,self.y),self.radius)
    def grow(self):
        self.radius+=50   
        self.draw()
    def shrink(self):
        self.radius-=50  
        self.draw()
r1=circle(200,200,"green",50)
r2=circle(150,200,"blue",40)
run=True
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill("red")
            r1.draw()
            r2.shrink()
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            screen.fill("green")
            r1.grow()
            r2.grow()
            pygame.display.update()
        if event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            r3=circle(pos[0],pos[1],"blue",50)
            r3.draw()
            pygame.display.update()

    
    pygame.display.update()             