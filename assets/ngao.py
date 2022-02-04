import pygame, sys

from pyparsing import java_style_comment
pygame.init()
screen= pygame.display.set_mode((432,768))
clock = pygame.time.Clock() 
bg = pygame.image.load('assets/background-night.png') 
bg = pygame.transform.scale2x(bg)
floor = pygame.image.load('assets/floor.png')
floor = pygame.transform.scale2x(floor) 
while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
    screen.blit(bg, (0,0))
    screen.blit(bg, (0,0))
    pygame.display.update()
    clock.tick(120)