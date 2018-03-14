import pygame, sys
from pygame.locals import *
pygame.init()

canvas = pygame.display.set_mode((300,300))
pygame.display.set_caption('Draw')

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0,255, 0)
canvas.fill(black)

pygame.draw.polygon(canvas, white, ((100,100), (200,200), (100,200), (200, 100)), 2)
pygame.draw.circle(canvas, red, (150, 150), 50, 2)
pygame.draw.rect(canvas, green, (90 , 90, 120, 120), 2)
pygame.display.update()
