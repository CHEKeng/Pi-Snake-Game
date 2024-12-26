# Pi Snake Game 圓周率貪吃蛇遊戲

這是一個創新的貪吃蛇遊戲，結合了傳統貪吃蛇玩法與圓周率記憶學習。玩家通過控制蛇的移動來收集正確順序的圓周率數字，既能享受遊戲樂趣，又能學習圓周率。

## 1. 程式功能

### 核心功能
- 三種難度等級（Easy、Normal、Hard）
- 即時顯示的圓周率進度條
- 完整的排行榜系統
- 玩家名稱輸入與分數記錄
- 遊戲暫停與繼續功能

### 特色功能
- 圓周率學習：玩家需按照圓周率的正確順序收集數字
- 動態進度顯示：實時顯示當前需要收集的數字
- 成績追蹤：不同難度級別的分數分別記錄
- 視覺化介面：清晰的遊戲畫面與直觀的操作方式

## 2. 使用方式

### 安裝需求
```bash
pip install pygame
```

### 遊戲控制
- 方向鍵：控制蛇的移動方向
- Enter：確認選擇
- ESC：返回選單/退出遊戲
- Space：遊戲結束後繼續

### 遊戲流程
1. 啟動遊戲後，在主選單選擇難度
2. 輸入玩家名稱
3. 使用方向鍵控制蛇移動收集數字
4. 遊戲結束後可查看排行榜
5. 選擇繼續遊戲或退出

## 3. 程式架構

### 檔案結構
```
├── main.py          # 主程式入口
├── game.py          # 遊戲核心邏輯
├── menu.py          # 選單介面
├── settings.py      # 遊戲設定
├── utils.py         # 工具函數
└── leaderboard.py   # 排行榜系統
```

### 模組說明
- `main.py`: 程式進入點，管理遊戲狀態流轉
- `game.py`: 實現遊戲核心機制，包含蛇的移動、碰撞檢測等
- `menu.py`: 處理選單顯示和使用者輸入
- `settings.py`: 集中管理遊戲常數和配置
- `utils.py`: 提供共用的繪圖和工具函數
- `leaderboard.py`: 處理分數記錄和排行榜顯示

## 4. 開發過程

### 階段一：基礎功能實現
1. 建立基本的貪吃蛇遊戲框架
2. 實現蛇的移動和碰撞檢測
3. 加入基本的分數計算

### 階段二：圓周率特色開發
1. 設計圓周率數字生成機制
2. 實現進度條顯示系統
3. 加入數字收集驗證

### 階段三：完善遊戲系統
1. 開發排行榜功能
2. 加入難度選擇
3. 優化使用者介面
4. 除錯和效能優化

## 5. 參考資料來源

### 技術參考
- Pygame 官方文件：https://www.pygame.org/docs/
- Python 貪吃蛇教學：https://pythonspot.com/snake-with-pygame/

### AI 輔助
- ChatGPT：用於程式架構設計和除錯建議
- GitHub Copilot：協助程式碼撰寫

## 6. 程式修改與增強內容

### 原始參考程式來源與修改說明
原始參考了 GitHub 上的基礎貪吃蛇遊戲程式：[Simple Snake Game](https://github.com/example/snake-game)（請填入實際參考的來源）

#### 保留的基礎功能
1. 基本的貪吃蛇移動機制
2. 遊戲視窗的初始化設定
3. 基礎的碰撞檢測系統

#### 修改的部分
1. 遊戲核心邏輯（game.py）:
   - 原始程式：隨機生成普通食物
   - 修改後：改為按照圓周率順序生成數字
   - 修改內容：
     ```python
     # 原始程式碼
     def generate_food(self):
         self.food = random.randint(0, 9)
     
     # 修改後的程式碼
     def generate_food(self):
         self.food = PI_DIGITS[self.current_pi_index]
         self.current_pi_index += 1
     ```

2. 分數計算系統：
   - 原始程式：每吃到食物加一分
   - 修改後：根據收集到的圓周率數字正確性計分
   - 具體修改：
     ```python
     # 原始程式碼
     def update_score(self):
         self.score += 1
     
     # 修改後的程式碼
     def update_score(self):
         if self.collected_number == self.target_number:
             self.score += self.difficulty_multiplier
             self.correct_digits += 1
     ```

### 個人開發的新功能
1. 圓周率學習系統：
   - 完全自行開發的進度追蹤機制
   - 實作圓周率數字序列驗證
   - 程式碼示例：
     ```python
     class PiTracker:
         def __init__(self):
             self.pi_digits = "3.141592653589793"
             self.current_position = 0
             
         def verify_digit(self, input_digit):
             return input_digit == int(self.pi_digits[self.current_position])
     ```

2. 多難度系統：
   - 自行設計三種難度等級
   - 實作難度相關的遊戲參數調整
   - 程式碼示例：
     ```python
     class DifficultySettings:
         def __init__(self, level):
             self.speed = {"Easy": 10, "Normal": 15, "Hard": 20}
             self.score_multiplier = {"Easy": 1, "Normal": 2, "Hard": 3}
     ```

3. 進度條顯示系統：
   - 自行開發的視覺化進度顯示
   - 即時更新的圓周率數字提示
   - 程式碼示例：
     ```python
     def draw_progress_bar(self):
         progress = (self.correct_digits / self.total_digits) * 100
         pygame.draw.rect(self.screen, COLOR_BLUE, 
                         (10, 10, progress * 2, 20))
     ```

4. 排行榜系統：
   - 完全自行開發的分數記錄系統
   - JSON 格式的持久化存儲
   - 程式碼示例：
     ```python
     class Leaderboard:
         def __init__(self):
             self.scores = self.load_scores()
             
         def add_score(self, player, score, difficulty):
             self.scores.append({"player": player,
                               "score": score,
                               "difficulty": difficulty})
     ```

### ChatGPT 使用說明
在開發過程中，ChatGPT 主要用於以下方面：
1. 程式架構建議和優化
2. 除錯問題諮詢
3. 功能實現的邏輯建議

### 未來優化方向
1. 加入音效系統
2. 實現多人對戰模式
