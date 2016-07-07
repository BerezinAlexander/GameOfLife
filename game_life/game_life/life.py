from draw import *
import itertools
from log import *
from time import clock

class Life(object):
    """description of class"""
    
    alive_cons = []

    def __init__(self, scr):
        logger.info("Life.init")
        self.draw = Draw(scr)

    def initPopul(self, alive = [(4,6), (5,6), (6,6),(6,5), (5,4), (30,10), (30,11), (30,12)]):
        #logger.info("Life.initPopul")
        self.alive_cons = alive
        self.draw.setBlackCells(self.alive_cons)
        self.draw.drawAll()

    def addCell(self, cell):
        #logger.info("Life.addCell")
        self.alive_cons.append(cell)
    
    def drawAlive(self, flagDraw):
        #logger.info("Life.drawAlive start")
        #start2 = clock()
        if(flagDraw):
            self.newStep()
        self.draw.setBlackCells(self.alive_cons)
        #logger.info("Life.draw.drawAll start")
        start = clock()
        self.draw.drawAll()
        #end = clock()
        #logger.info("Life.draw.drawAll finish [%s]", end-start)
        #logger.info("Life.drawAlive finish [%s]", end-start2)

    def newStep(self):
        logger.info("Life.newStep start")
        start = clock()
        # получение живых клеток и их соседей
        neightbors = []
        for al in self.alive_cons:
            neightbors += self.get_neightbors(al)
        board = neightbors + self.alive_cons
        board = list(set(board))
        logger.info("Life.newStep fill board [%s], board.count: [%s]", clock() - start, len(board))
        start = clock()
        alive_cons_new = []
        for con in board:
            neib = self.get_neightbors(con)
            count_neib = self.count_alive_neib(neib)
            if ((count_neib == 3) or (count_neib == 2 and self.is_alive(con))):
                alive_cons_new.append(con)
        self.alive_cons = alive_cons_new
        end = clock()
        logger.info("Life.newStep finish [%s]", end-start)

    # подсчет кол-ва живых соседей
    def count_alive_neib(self, neib):
        #logger.info("Life.count_alive_neib")
        count = 0
        for ne in neib:
            if (self.is_alive(ne)):
                count += 1
        return count

    # проверка на живучесть
    def is_alive(self, con):
        #logger.info("Life.is_alive")
        for al in self.alive_cons: 
            if con == al: 
                return True
        return False 
            
    # функция получения соседей    
    def get_neightbors(self, con):
        #logger.info("Life.get_neightbors")
        x, y = con
        neighbors = [(x + i, y + j)
                    for i in range(-1, 2)
                    for j in range(-1, 2)
                    if not i == j == 0]
        return neighbors