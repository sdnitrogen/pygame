import pygame, sys
from pygame.locals import *
pygame.init()

window_height = 600
window_width = 600

Canvas = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('MINI PROJECT')

pygame.display.update()

ballimage = pygame.image.load('Ball.png')
ballrect = ballimage.get_rect()
pygame.mixer.music.load('ballmusic.ogg')

black = (0,0,0)
white = (255,255,255)
font = pygame.font.SysFont(None, 20, False, True)
fps = 60
mainClock = pygame.time.Clock()


while True:

    moveup = movedown = moveright = moveleft = False
    ballrect.centerx = ballrect.centery = 300
    pygame.mixer.music.play(-1)
    
    while True:     
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_UP:
                    moveup = True               
                if event.key == K_DOWN:
                    movedown = True
                if event.key == K_LEFT:
                    moveleft = True
                if event.key == K_RIGHT:
                    moveright = True
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    

            if event.type == KEYUP:

                if event.key == K_UP:
                    moveup = False
                if event.key == K_DOWN:
                    movedown = False
                if event.key == K_LEFT:
                    moveleft = False
                if event.key == K_RIGHT:
                    moveright = False

        if (moveup and (ballrect.top > 0)):
            ballrect.top-= 5
        if (movedown and (ballrect.bottom < 600)):
            ballrect.bottom += 5
        if (moveleft and (ballrect.left > 0)):
            ballrect.left -= 5
        if (moveright and (ballrect.right < 600)):
            ballrect.right += 5

        x = str(ballrect.centerx)
        y = str(ballrect.centery)

        obj_x = font.render(x, 1, white)
        obj_y = font.render(y, 1, white)

        obj_xrect = obj_x.get_rect()
        obj_yrect = obj_y.get_rect()

        obj_xrect.topleft = (10, 10)
        obj_yrect.topleft = (50, 10)
        
                
        Canvas.fill(black)
        Canvas.blit(obj_x, obj_xrect)
        Canvas.blit(obj_y, obj_yrect)
    
        
        Canvas.blit(ballimage, ballrect)
        pygame.display.update()

        mainClock.tick(fps)
    pygame.mixer.music.stop()
