# ��������� �������

WIN_WIDTH        = 600 #������ ������������ ����
WIN_HEIGHT       = 500 # ������
WINDOW           = (WIN_WIDTH, WIN_HEIGHT) # ���������� ������ � ������ � ���� ����������
MAP_WIDTH        = 500 #������ ������������ ����
MAP_HEIGHT       = 500 # ������
GAME_SCREEN      = (MAP_WIDTH, MAP_HEIGHT)
MENU_WIDTH       = 100
MENU_HEIGHT      = 500
GAME_MENU        = (MENU_WIDTH, MENU_HEIGHT)
CELL_SIZE        = 5
COUNT_CELLS_X    = int(WIN_WIDTH / CELL_SIZE)
COUNT_CELLS_Y    = int(WIN_HEIGHT / CELL_SIZE)
#MAP_WIDTH_CELLS  = 100 #������ ������������ ����
#MAP_HEIGHT_CELLS = 100 # ������
BACKGROUND_COLOR = (255,255,255)
ALIVE_COLOR      = (0,0,0)
NEIGHBOR_SET = ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, -1), (1, 1))