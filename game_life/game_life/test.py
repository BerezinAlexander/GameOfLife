from time import clock
import random

# проверка на живучесть
def is_alive(con, alive_cons):
    #logger.info("Life.is_alive")
    for al in alive_cons: 
        if con == al: 
            return True
    return False 

# подсчет кол-ва живых соседей
def count_alive_neib(neib, als):
    #logger.info("Life.count_alive_neib")
    count = 0
    for ne in neib:
        if (is_alive(ne, als)):
            count += 1
    return count
            
# функция получения соседей    
def get_neightbors(con):
    #logger.info("Life.get_neightbors")
    x, y = con
    neighbors = [(x + i, y + j)
                for i in range(-1, 2)
                for j in range(-1, 2)
                if not i == j == 0]
    return neighbors

als = []
for i in range(0, 101):
    als.append((random.randrange(0,50,1), random.randrange(0,50,1)))
#con = (2,7)

board = []
for i in range(0, 701):
    board.append((random.randrange(0,50,1), random.randrange(0,50,1)))

start = clock()

for con in board:
    neib = get_neightbors(con)
    count_neib = count_alive_neib(neib, als)
    if ((count_neib == 3) or (count_neib == 2 and is_alive(con, als))):
        sdf = 4

end = clock()
print(end-start)