import pygame
import sys
from settings import *
from menu import show_main_menu
from game import SnakeGame
from leaderboard import add_score, load_leaderboard

def get_player_name(screen):
    """
    獲取玩家名字
    """
    name = ""
    input_active = True
    font = pygame.font.SysFont('arial', 32)
    
    while input_active:
        screen.fill(BLACK)
        # 顯示提示文字
        prompt_text = font.render("Enter your name:", True, WHITE)
        name_text = font.render(name, True, WHITE)
        screen.blit(prompt_text, (FRAME_SIZE_X//2 - prompt_text.get_width()//2, FRAME_SIZE_Y//2 - 50))
        screen.blit(name_text, (FRAME_SIZE_X//2 - name_text.get_width()//2, FRAME_SIZE_Y//2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.strip():
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 10:  # 限制名字長度
                    if event.unicode.isalnum():  # 只允許字母和數字
                        name += event.unicode

def show_leaderboard_and_continue(screen, difficulty, game_speed):
    """
    顯示排行榜和繼續選項
    """
    screen.fill(BLACK)
    font = pygame.font.SysFont("arial", 36)
    small_font = pygame.font.SysFont("arial", 24)
    
    # 獲取該難度的排行榜
    leaderboard = load_leaderboard(game_speed)  # 使用 game_speed 作為難度參數
    
    # 顯示排行榜標題
    title_text = font.render(f"{difficulty.capitalize()} Mode Leaderboard", True, WHITE)
    title_rect = title_text.get_rect(center=(FRAME_SIZE_X // 2, 50))
    screen.blit(title_text, title_rect)
    
    # 顯示排行榜內容
    start_y = 120
    for i, entry in enumerate(leaderboard):
        score_text = small_font.render(f"{i+1}. {entry['name']}: {entry['score']}", True, WHITE)
        score_rect = score_text.get_rect(center=(FRAME_SIZE_X // 2, start_y + i * 40))
        screen.blit(score_text, score_rect)
    
    # 顯示繼續提示
    continue_text = font.render("Press SPACE to continue or ESC to quit", True, WHITE)
    continue_rect = continue_text.get_rect(center=(FRAME_SIZE_X // 2, FRAME_SIZE_Y - 100))
    screen.blit(continue_text, continue_rect)
    
    pygame.display.flip()
    
    # 等待玩家選擇是否繼續
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

def main():
    pygame.init()
    clock = pygame.time.Clock()

    # 定義難度對應的速度
    DIFFICULTY_SPEEDS = {
        "easy": 10,
        "normal": 18,
        "hard": 25
    }

    while True:
        # 顯示主選單並獲取難度設定
        difficulty = show_main_menu()
        if difficulty is None:  # 如果用戶關閉視窗
            break
            
        # 創建遊戲視窗
        screen = pygame.display.set_mode((FRAME_SIZE_X, FRAME_SIZE_Y))
        
        # 將難度字串轉換為對應的速度數值
        game_speed = DIFFICULTY_SPEEDS[difficulty.lower()]
        
        # 創建並開始遊戲
        game = SnakeGame(game_speed)
        score = game.run()
        
        # 獲取玩家名字並更新分數
        name = get_player_name(screen)
        add_score(game_speed, name, score)  # 使用 game_speed 作為難度參數
        
        # 顯示排行榜和繼續選項
        if not show_leaderboard_and_continue(screen, difficulty, game_speed):
            break
            
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
