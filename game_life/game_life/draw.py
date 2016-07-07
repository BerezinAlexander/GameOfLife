import math, sys, pygame
from pygame.locals import * 
from settings import *

class Draw(object):

    blackCells = []

    def __init__(self,scr):
        self.screen = scr

    def drawAll(self):
        for i in range(0, COUNT_CELLS_Y):
            for j in range(0, COUNT_CELLS_X):
                self.drawCell((j,i), 0)
        for pos in self.blackCells:
            self.drawCell(pos,1)
        #self.drawCell((1,1), 1)

    def drawCell(self, crd, type):
        if type == 1: 
            rect_1_color = ALIVE_COLOR
            rect_1_width = 0
        else:
            rect_1_color = BACKGROUND_COLOR
            rect_1_width = 1

        rect_1_rect = Rect((crd[0] * CELL_SIZE,crd[1] * CELL_SIZE), (CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, rect_1_color, rect_1_rect, rect_1_width)

    def setBlackCells(self, cells):
        self.blackCells = cells