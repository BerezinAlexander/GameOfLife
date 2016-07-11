from draw import *
import itertools
from log import *
from time import clock
from itertools import chain
import cProfile

# функция получения соседей    
def get_neightbors(con):
    x, y = con
    return  set((x + dx, y + dy) for dx, dy in NEIGHBOR_SET)

class Life(object):
    """description of class"""

    def __init__(self, scr):
        logger.info("Life.init")
        self.alive_cons = set()
        self.countGeneration = 0
        self.draw = Draw(scr)

    def initPopul(self, alive = set( [(4,6), (5,6), (6,6),(6,5), (5,4), (30,10), (30,11), (30,12)] )):
        self.alive_cons = alive
        self.draw.setBlackCells(self.alive_cons)
        self.draw.drawAll()

    def addCell(self, cell):
        self.alive_cons.add(cell)
    
    def drawAlive(self, flagDraw):
        if(flagDraw):
            self.newStep()
        self.draw.setBlackCells(self.alive_cons)
        self.draw.drawAll()

    def newStep(self):
        self.countGeneration += 1
        # получение живых клеток и их соседей
        board = self.alive_cons | set(chain(*(get_neightbors(point) for point in self.alive_cons)))

        start = clock()
        
        alive_cons_new = set()
        for con in board:
            count_neib = len(self.alive_cons & get_neightbors(con))
            if ((count_neib == 3) or (count_neib == 2 and con in self.alive_cons)):
                alive_cons_new.add(con)
        
        end = clock()
        logger.info("Life.newStep fill board [%s], board.count: [%s], alives: [%s]", clock() - start, len(board), len(self.alive_cons))
        if self.countGeneration%16 == 0:
            alive_cons_new = set(filter(usl, alive_cons_new))

        self.alive_cons = alive_cons_new
    
    # фигура L
    def shapeL(self, point):
        crd = set()
        crd.add( (point) )
        crd.add( (point[0], point[1]+1) )
        crd.add( (point[0], point[1]+2) )
        crd.add( (point[0]+1, point[1]+2) )
        crd.add( (point[0]+2, point[1]+2) )
        crd.add( (point[0]+2, point[1]+1) )
        return crd
    # фигура квадрат 2х2
    def shapeSquare(self, point):
        crd = set()
        crd.add( (point) )
        crd.add( (point[0], point[1]+1) )
        crd.add( (point[0]+1, point[1]) )
        crd.add( (point[0]+1, point[1]+1) )
        return crd

def usl(al):
    if(al[0] < -2 or al[0] > COUNT_CELLS_X + 2):
        return 0
    elif(al[1] < -2 or al[1] >COUNT_CELLS_X + 2):
        return 0
    return 1