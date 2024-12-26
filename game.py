import pygame
import random
import sys
from settings import *
from utils import *
from leaderboard import add_score


class SnakeGame:
    def __init__(self, difficulty):
        """
        初始化遊戲。
        """
        self.screen = pygame.display.set_mode((FRAME_SIZE_X, FRAME_SIZE_Y))
        pygame.display.set_caption('Pi Snake Game')
        self.clock = pygame.time.Clock()
        self.difficulty = difficulty
        self.reset_game()

    def reset_game(self):
        """
        重置遊戲狀態。
        """
        self.snake_pos = list(INITIAL_SNAKE_POS)  # 使用設定檔中的初始位置
        self.snake_body = [pos[:] for pos in INITIAL_SNAKE_BODY]  # 深度複製初始身體
        self.direction = INITIAL_DIRECTION
        self.change_to = self.direction
        self.score = 0
        self.current_pi_index = 0
        self.numbers_on_screen = []
        self.numbers_positions = []
        self.expected_digit = PI_SEQUENCE[0]
        self.generate_numbers()

    def generate_numbers(self):
        """
        生成遊戲畫面上的數字，確保數字數量穩定為 PROGRESS_BAR_CELLS 個，且不與蛇的身體重疊。
        """
        while len(self.numbers_positions) < PROGRESS_BAR_CELLS:
            x = random.randrange(0, FRAME_SIZE_X - 10, 10)  # 確保對齊網格
            y = random.randrange(0, FRAME_SIZE_Y - PROGRESS_BAR_HEIGHT - 20, 10)  # 避開進度條區域
            pos = [x, y]
            
            # 確保新生成的數字位置不會與蛇身重疊
            if pos not in self.snake_body and pos not in self.numbers_positions:
                self.numbers_positions.append(pos)
                # 從 PI_SEQUENCE 中獲取下一個數字
                next_number = PI_SEQUENCE[self.current_pi_index % len(PI_SEQUENCE)]
                self.numbers_on_screen.append(next_number)
                self.current_pi_index += 1

    def handle_input(self):
        """
        處理玩家輸入，更新蛇的方向。
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != 'DOWN':
                    self.change_to = 'UP'
                elif event.key == pygame.K_DOWN and self.direction != 'UP':
                    self.change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                    self.change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                    self.change_to = 'RIGHT'

    def update(self):
        """
        更新遊戲狀態，包括蛇的移動、碰撞檢查和分數更新。
        """
        # 更新方向
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        # 移動蛇
        if self.direction == 'UP':
            self.snake_pos[1] -= 10
        if self.direction == 'DOWN':
            self.snake_pos[1] += 10
        if self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_pos[0] += 10

        # 更新蛇身
        self.snake_body.insert(0, list(self.snake_pos))

        # 檢查是否吃到數字
        if self.snake_pos in self.numbers_positions:
            index = self.numbers_positions.index(self.snake_pos)
            collected_number = self.numbers_on_screen[index]

            if collected_number == self.expected_digit:
                self.score += 1
                self.expected_digit = PI_SEQUENCE[self.score % len(PI_SEQUENCE)]
                self.numbers_positions.pop(index)
                self.numbers_on_screen.pop(index)
                self.generate_numbers()
            else:
                return False
        else:
            self.snake_body.pop()

        # 檢查碰撞
        if (
            self.snake_pos[0] < 0 or 
            self.snake_pos[0] >= FRAME_SIZE_X or
            self.snake_pos[1] < 0 or 
            self.snake_pos[1] >= FRAME_SIZE_Y - PROGRESS_BAR_HEIGHT - PROGRESS_BAR_MARGIN or
            self.snake_pos in self.snake_body[1:]
        ):
            return False

        return True

    def draw(self):
        """
        繪製遊戲畫面。
        """
        self.screen.fill(BLACK)

        # 繪製蛇
        for block in self.snake_body:
            pygame.draw.rect(self.screen, GREEN, pygame.Rect(block[0], block[1], 10, 10))

        # 繪製數字
        for i, pos in enumerate(self.numbers_positions):
            draw_number(self.screen, str(self.numbers_on_screen[i]), pos[0], pos[1])

        # 繪製分數（左上角）
        draw_text(self.screen, f"Score: {self.score}", 20, 10, 10)

        # 繪製進度條（置中）
        draw_progress_bar(self.screen, self.score, self.expected_digit)

        pygame.display.flip()

    def show_game_over(self):
        """
        顯示遊戲結束畫面
        """
        self.screen.fill(BLACK)
        
        # 設置字體
        font = pygame.font.SysFont('arial', 48)
        
        # 建立遊戲結束文字
        game_over_text = font.render('Game Over', True, RED)
        score_text = font.render(f'Final Score {self.score}', True, WHITE)
        
        # 獲取文字區域並置中
        game_over_rect = game_over_text.get_rect(center=(FRAME_SIZE_X // 2, FRAME_SIZE_Y // 2 - 50))
        score_rect = score_text.get_rect(center=(FRAME_SIZE_X // 2, FRAME_SIZE_Y // 2 + 50))
        
        # 繪製文字
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        
        # 更新顯示
        pygame.display.flip()
        
        # 等待一段時間
        pygame.time.wait(2000)

    def run(self):
        """
        運行遊戲主迴圈。
        """
        running = True
        while running:
            self.handle_input()
            if not self.update():
                self.show_game_over()
                running = False
                break
            self.draw()
            self.clock.tick(self.difficulty)
        
        return self.score
