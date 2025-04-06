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
r1=circle(200,200,"green",50)
r2=circle(150,200,"blue",40)
r3=circle(250,150,"orange",60)
r4=circle(100,300,"yellow",55)
while run==True:
    t=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
    screen.fill("red")
    r1.draw()
    r2.draw()
    r3.draw()
    r4.draw()
    r1.update(t)
    r2.update(t)
    r3.update(t)
    r4.update(t)
    pygame.display.update()             