import json
import os

# 設定排行榜資料夾
SCORES_DIR = "scores"

# 確保資料夾存在
if not os.path.exists(SCORES_DIR):
  os.makedirs(SCORES_DIR)

# 難度對應表
DIFFICULTY_MAP = {
  10: "easy",
  18: "normal",
  25: "hard"
}

# 預設排行榜資料
DEFAULT_SCORES = [{"name": "Player1", "score": 0}, {"name": "Player2", "score": 0}, {"name": "Player3", "score": 0}]

def get_difficulty_filename(difficulty):
  """
  將數字難度轉換為對應的檔案名稱
  """
  difficulty_name = DIFFICULTY_MAP.get(difficulty, "normal")  # 如果找不到對應，預設使用 normal
  return f"{difficulty_name}.json"

def load_leaderboard(difficulty):
  """
  讀取指定難易度的排行榜
  """
  filename = get_difficulty_filename(difficulty)
  file_path = os.path.join(SCORES_DIR, filename)
  
  if not os.path.exists(file_path):
      # 如果檔案不存在，初始化為預設資料
      with open(file_path, "w") as file:
          json.dump(DEFAULT_SCORES, file)
  try:
      with open(file_path, "r") as file:
          return json.load(file)
  except Exception as e:
      print(f"Error loading leaderboard for {difficulty} ({filename}): {e}")
      return DEFAULT_SCORES

def save_leaderboard(difficulty, leaderboard):
  """
  儲存排行榜到檔案
  """
  filename = get_difficulty_filename(difficulty)
  file_path = os.path.join(SCORES_DIR, filename)
  with open(file_path, "w") as file:
      json.dump(leaderboard, file)

def add_score(difficulty, name, score):
    """
    新增一個分數到排行榜，並保持排序
    每次都新增為新紀錄，不更新舊有紀錄
    """
    leaderboard = load_leaderboard(difficulty)
    
    # 直接新增一筆新紀錄
    leaderboard.append({"name": name, "score": score})
    
    # 根據分數排序（由高到低）
    leaderboard.sort(key=lambda x: (-x["score"], x["name"]))
    
    # 只保留前三名
    leaderboard = leaderboard[:3]
    
    # 儲存更新後的排行榜
    save_leaderboard(difficulty, leaderboard)
    
    return leaderboard
