import pygame
from settings import *
from leaderboard import load_leaderboard, DIFFICULTY_MAP

def draw_menu_option(screen, text, y_position, selected, font):
    """繪製選單選項"""
    color = GREEN if selected else WHITE
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(FRAME_SIZE_X // 2, y_position))
    screen.blit(text_surface, text_rect)

def show_main_menu():
    """顯示主選單"""
    screen = pygame.display.set_mode((FRAME_SIZE_X, FRAME_SIZE_Y))
    font = pygame.font.SysFont("arial", 36)
    title_font = pygame.font.SysFont("arial", 48)

    options = ["Easy", "Normal", "Hard", "Leaderboard", "Exit"]
    selected = 0

    while True:
        screen.fill(BLACK)
        
        # 繪製標題
        title = title_font.render("Pi Snake Game", True, WHITE)
        title_rect = title.get_rect(center=(FRAME_SIZE_X // 2, 100))
        screen.blit(title, title_rect)

        # 繪製選項
        for i, option in enumerate(options):
            draw_menu_option(screen, option, 200 + i * 60, selected == i, font)

        pygame.display.flip()

        # 處理輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[selected] == "Exit":
                        return None
                    elif options[selected] == "Leaderboard":
                        show_leaderboard(screen)
                    else:
                        return options[selected].lower()

def show_leaderboard(screen):
    """顯示排行榜"""
    font = pygame.font.SysFont("arial", 30)
    title_font = pygame.font.SysFont("arial", 36)
    
    # 使用與主遊戲相同的難度設定
    difficulties = [10, 18, 25]  # 對應 easy, normal, hard
    current_diff = 0

    while True:
        screen.fill(BLACK)
        
        # 顯示標題
        title = title_font.render("Leaderboard", True, WHITE)
        title_rect = title.get_rect(center=(FRAME_SIZE_X // 2, 50))
        screen.blit(title, title_rect)
        
        # 顯示當前難度
        diff_name = DIFFICULTY_MAP[difficulties[current_diff]].upper()
        diff_text = font.render(f"Difficulty: {diff_name}", True, GREEN)
        diff_rect = diff_text.get_rect(center=(FRAME_SIZE_X // 2, 100))
        screen.blit(diff_text, diff_rect)

        # 顯示排行榜數據
        scores = load_leaderboard(difficulties[current_diff])
        for i, score in enumerate(scores):
            text = f"{i+1}. {score['name']}: {score['score']}"
            score_text = font.render(text, True, WHITE)
            score_rect = score_text.get_rect(center=(FRAME_SIZE_X // 2, 160 + i * 40))
            screen.blit(score_text, score_rect)

        # 顯示操作提示
        help_text = font.render("← → Change Difficulty | ESC Back", True, WHITE)
        help_rect = help_text.get_rect(center=(FRAME_SIZE_X // 2, FRAME_SIZE_Y - 50))
        screen.blit(help_text, help_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_LEFT:
                    current_diff = (current_diff - 1) % len(difficulties)
                elif event.key == pygame.K_RIGHT:
                    current_diff = (current_diff + 1) % len(difficulties)
