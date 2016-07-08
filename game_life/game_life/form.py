import sys
from time import sleep
# Импортируем библиотеку pygame
import pygame
from pygame import *
from settings import *
from life import *

class Form(object):
    """description of class"""

    def __init__(self):
        pygame.init() # Инициация PyGame, обязательная строчка         
        window = pygame.display.set_mode(WINDOW) # Создаем окошко
        screen = pygame.Surface(GAME_SCREEN)
        menu   = pygame.Surface(GAME_MENU)
        pygame.display.set_caption("Life") # Пишем в шапку
        mainLoop = True # флаг главного цикла

        clock = pygame.time.Clock()

        life = Life(screen)
        life.initPopul()

        flDraw = True
    
        #initial data here
        while mainLoop:
            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    mainLoop = False
                if event.type == MOUSEBUTTONDOWN: 
                    if event.button == 1: 
                        crd = event.pos
                        life.addCell((int( crd[0]//10.0), int( crd[1]//10.0)))
                if event.type == KEYDOWN: 
                    if event.key == K_SPACE:
                        flDraw = not flDraw
                         
                   
            screen.fill(BACKGROUND_COLOR)
            menu.fill((100,100,100))
            
            #create frame here 
            life.drawAlive(flDraw) 


            window.blit(screen, [0,0])
            window.blit(menu, [700,0])
            pygame.display.flip()

            clock.tick(50)
            pygame.display.set_caption("fps: " + str(clock.get_fps()))
            
                                               
               
            #pygame.display.update()
    
        pygame.quit() 




