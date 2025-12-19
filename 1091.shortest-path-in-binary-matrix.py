#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[str]]) -> int:
        N = len(grid)
        
        # スタートかゴールが壁なら、即終了（境界条件）
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        
        # キータップ：(行, 列, ここまでの歩数)
        # 最初の地点ですでに「1歩目」とカウントするルール
        queue = deque([(0, 0, 1)])
        
        # 訪問済み管理：gridを直接2に書き換えることでメモリ節約（だましだましテク）
        grid[0][0] = 2 
        
        while queue:
            r, c, dist = queue.popleft()
            
            # ゴールに到達した瞬間の dist が最短
            if r == N - 1 and c == N - 1:
                return dist
            
            # 8方向（上下左右 + 斜め）
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0: continue # 自分自身はスキップ
                    
                    nr, nc = r + dr, c + dc
                    
                    # 1. 範囲内 2. 道(0)である 
                    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                        # 予約するタイミングで「訪問済み(2)」にする（二度手間防止）
                        grid[nr][nc] = 2
                        queue.append((nr, nc, dist + 1))
                        
        return -1
# @lc code=end

