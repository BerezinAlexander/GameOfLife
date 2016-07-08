from time import clock
import random

import cProfile
import re
#cProfile.run('re.compile("foo|bar")')

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

als = set()
for i in range(0, 800):
    als.add((random.randrange(0,50,1), random.randrange(0,50,1)))

board = set()
for i in range(0, 3000):
    board.add((random.randrange(0,50,1), random.randrange(0,50,1)))


cProfile.run('next_step(als,board)')

start = clock()

als = next_step(als, board)

end = clock()
print(end-start)

start = clock()

