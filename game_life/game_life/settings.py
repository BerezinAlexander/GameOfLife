# ��������� �������

WIN_WIDTH        = 800 #������ ������������ ����
WIN_HEIGHT       = 640 # ������
WINDOW           = (WIN_WIDTH, WIN_HEIGHT) # ���������� ������ � ������ � ���� ����������
GAME_SCREEN      = (700, 640)
GAME_MENU        = (100, 640)
BACKGROUND_COLOR = (255,255,255)
ALIVE_COLOR      = (0,0,0)
CELL_SIZE        = 10
COUNT_CELLS_X    = int(WIN_WIDTH / CELL_SIZE)
COUNT_CELLS_Y    = int(WIN_HEIGHT / CELL_SIZE)
NEIGHBOR_SET = ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, -1), (1, 1))