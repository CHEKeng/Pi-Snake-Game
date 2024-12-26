import pygame
from settings import *

def draw_text(surface, text, size, x, y, color=WHITE, font_name='consolas'):
    """繪製文字"""
    font = pygame.font.SysFont(font_name, size)
    text_surface = font.render(str(text), True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

def draw_number(surface, number, x, y, size=14):
    """繪製遊戲中的數字方塊"""
    pygame.draw.rect(surface, WHITE, pygame.Rect(x, y, 10, 10))
    font = pygame.font.SysFont('consolas', size)
    text_surface = font.render(str(number), True, BLACK)
    text_rect = text_surface.get_rect(center=(x + 5, y + 5))
    surface.blit(text_surface, text_rect)

def draw_progress_bar(surface, score, current_digit):
    """繪製置中的進度條，已收集的數字保持綠色"""
    # 繪製進度條背景
    bar_rect = pygame.Rect(
        PROGRESS_BAR_START_X - PROGRESS_CELL_MARGIN,
        PROGRESS_BAR_Y,
        PROGRESS_BAR_TOTAL_WIDTH + PROGRESS_CELL_MARGIN * 2,
        PROGRESS_BAR_HEIGHT
    )
    pygame.draw.rect(surface, WHITE, bar_rect, 2)

    # 計算要顯示的圓周率數字範圍
    start_index = max(0, score - PROGRESS_BAR_CELLS // 2)
    
    # 繪製進度格子
    for i in range(PROGRESS_BAR_CELLS):
        index = start_index + i
        if index >= len(PI_SEQUENCE):
            break
        
        # 計算每個格子的位置
        x = PROGRESS_BAR_START_X + i * (PROGRESS_CELL_WIDTH + PROGRESS_CELL_MARGIN)
        cell_rect = pygame.Rect(
            x,
            PROGRESS_BAR_Y + 5,
            PROGRESS_CELL_WIDTH,
            PROGRESS_BAR_HEIGHT - 10
        )
        
        # 決定顏色：
        # - 已收集的數字（index < score）顯示為綠色
        # - 當前要收集的數字（index == score）閃爍綠色
        # - 未收集的數字（index > score）顯示為白色
        if index < score:
            color = GREEN  # 已收集的數字
        elif index == score:
            # 當前數字使用閃爍效果
            if pygame.time.get_ticks() % 1000 < 500:
                color = GREEN
            else:
                color = WHITE
        else:
            color = WHITE  # 未收集的數字

        # 繪製格子
        pygame.draw.rect(surface, color, cell_rect, 1)
        
        # 繪製數字
        font = pygame.font.SysFont('consolas', 20)
        num_text = font.render(PI_SEQUENCE[index], True, color)
        num_rect = num_text.get_rect(center=cell_rect.center)
        surface.blit(num_text, num_rect)

    # 在進度條上方顯示當前需要收集的數字
    next_text = f"Next: {current_digit}"
    font = pygame.font.SysFont('consolas', 24)
    text_surface = font.render(next_text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = FRAME_SIZE_X // 2
    text_rect.bottom = PROGRESS_BAR_Y - 5
    surface.blit(text_surface, text_rect)