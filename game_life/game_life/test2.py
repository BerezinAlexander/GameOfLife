from itertools import chain
import cProfile
from settings import *

NEIGHBOR_SET = ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, -1), (1, 1))
           
# Получение всех соседей
def get_neightbors(con):
    x, y = con
    return  set((x + dx, y + dy) for dx, dy in NEIGHBOR_SET)

def next_step(alives, board):
    new_alives = set()
    for con in board:
        count_neib = len(alives & get_neightbors(con))
        if ((count_neib == 3) or (count_neib == 2 and con in alives)):
            new_alives.add(con)
    return new_alives

def usl(al):
    if(al[0] < -2 or al[0] > COUNT_CELLS_X + 2):
        return 0
    elif(al[1] < -2 or al[1] > COUNT_CELLS_Y + 2):
        return 0
    return 1

def dead_sort(alives):
    
    alives = list(sorted(alives,key=lambda x: x[0]))
    for al in alives:
        if al[0] < 0:
            alives.remove(al)
        else:
            break
    for al in reversed(alives):
        if al[0] > COUNT_CELLS_X:
            alives.remove(al)
        else:
            break 

    alives = list(sorted(alives,key=lambda x: x[1]))
    for al in alives:
        if al[1] < 0:
            alives.remove(al)
        else:
            break
    for al in reversed(alives):
        if al[1] > COUNT_CELLS_Y:
            alives.remove(al)
        else:
            break 
        
def dead_contour(alives):
    for i in range(-1, COUNT_CELLS_X + 1):
        if (i, -1) in alives:
            alives.remove((i, -1))
        if (i, COUNT_CELLS_Y + 1) in alives:
            alives.remove((i, COUNT_CELLS_Y + 1))
        if (-1, i) in alives:
            alives.remove((-1, i))
        if (COUNT_CELLS_X + 1, i) in alives:
            alives.remove((COUNT_CELLS_X + 1, i))

# фигура L
def shapeL(point):
    crd = set()
    crd.add( (point) )
    crd.add( (point[0]  , point[1]+1) )
    crd.add( (point[0]  , point[1]+2) )
    crd.add( (point[0]+1, point[1]+2) )
    crd.add( (point[0]+2, point[1]+2) )
    crd.add( (point[0]+2, point[1]+1) )
    return crd

def test(alives, count):
    for i in range(count):        
        # получение живых клеток и их соседей
        board = alives | set(chain(*(get_neightbors(point) for point in alives)))
        alives = next_step(alives, board)
        
        if i%16 == 0:
            #dead_contour(alives)  
            #dead_sort(alives)  
            alives = set(filter(usl, alives))
    
        #if i%16 == 0:
        #    alives = set(filter(usl, alives))

als = shapeL( (50,50) )

cProfile.run('test(als,1000)')