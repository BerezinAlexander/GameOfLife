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
        screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
        pygame.display.set_caption("Life") # Пишем в шапку
        mainLoop = True # флаг главного цикла

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
        
            #sleep(1)
            
            #create frame here 
            life.drawAlive(flDraw)
                                       
            pygame.display.update()
    
        pygame.quit() 




