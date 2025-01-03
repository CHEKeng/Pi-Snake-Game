# 遊戲視窗設定
FRAME_SIZE_X = 720
FRAME_SIZE_Y = 480

# 難度選項（蛇的速度）
DIFFICULTY_OPTIONS = {
    "easy": 10,
    "normal": 18,
    "hard": 25
}

# 顏色設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 圓周率數字序列
PI_SEQUENCE = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

# 蛇的初始設定
INITIAL_SNAKE_POS = [100, 50]
INITIAL_SNAKE_BODY = [[100, 50], [90, 50], [80, 50]]
INITIAL_DIRECTION = 'RIGHT'

# 進度條設定
PROGRESS_BAR_HEIGHT = 30
PROGRESS_BAR_MARGIN = 10
PROGRESS_BAR_Y = FRAME_SIZE_Y - PROGRESS_BAR_HEIGHT - PROGRESS_BAR_MARGIN
PROGRESS_CELL_WIDTH = 30
PROGRESS_CELL_MARGIN = 2
PROGRESS_BAR_CELLS = 10  # 一次顯示多少個數字

# 計算進度條總寬度
PROGRESS_BAR_TOTAL_WIDTH = (PROGRESS_CELL_WIDTH + PROGRESS_CELL_MARGIN) * PROGRESS_BAR_CELLS
# 計算進度條起始 X 座標（置中）
PROGRESS_BAR_START_X = (FRAME_SIZE_X - PROGRESS_BAR_TOTAL_WIDTH) // 2