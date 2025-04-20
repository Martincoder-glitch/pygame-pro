import pygame
pygame.init()
WIDTH=900
HEIGHT=900
run=True 
screen=pygame.display.set_mode((WIDTH,HEIGHT))
yellowbulb=pygame.image.load("images\yellowbulb.png")
whitebulb=pygame.image.load("images\whitebulb.png")
font=pygame.font.SysFont("Times New Roman",50)
run=True
while run==True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill("red")
            screen.fill("red")
            screen.blit(yellowbulb,(0,0))
            text=font.render("ON",True,"green")
            screen.blit(text,(450,450))
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            screen.fill("green")
            screen.fill("red")
            screen.blit(whitebulb,(0,0))
            text=font.render("OFF",True,"green")
            screen.blit(text,(20,20))
            pygame.display.update()
        