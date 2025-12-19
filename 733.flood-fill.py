#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        initialColor = image[sr][sc]
        
        if initialColor == newColor:
            return image

        def dfs(r, c):
            if not (0 <= r < R and 0 <= c < C):
                return
            if not image[r][c] == initialColor:
                return
            
            image[r][c] = newColor
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc)

        dfs(sr, sc)

        return image























# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         R, C = len(image), len(image[0])
#         initialColor = image[sr][sc]
#         visited = [[False] * C for _ in range(R)]
#         #if initialColor == newColor:
#         #    return image
#         def dfs(r, c):
            
#             # 終了条件1: キャンバスの外
#             if not (0 <= r < R and 0 <= c < C):
#                 return                        
#             # 終了条件2: 色が違う領域
#             if image[r][c] != initialColor:
#                 return            
#             # 終了条件3: 訪問済み
#             if visited[r][c]:
#                 return 
            
#             visited[r][c] = True
#             image[r][c] = newColor

#             for dr, dc in [(-1,0), (1, 0), (0, -1), (0, 1)]:
#                 dfs(r + dr, c + dc)

#         dfs(sr, sc)

#         return image














# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         R, C = len(image), len(image[0])
#         initialColor = image[sr][sc]
        

#         if initialColor == newColor:
#             return image

#         def dfs(r,c):
#             if not (0 <= r < R and 0 <= c < C and image[r][c] == initialColor):
#                 return
            
#             image[r][c] = newColor
            
#             for dr, dc in [(0,-1),(0, 1),(-1, 0),(1, 0)]:
#                 dfs(r + dr, c + dc)

#         dfs(sr, sc)

#         return image




# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         self.R = len(image)
#         self.C = len(image[0])
#         self.image = image
#         self.initialColor = image[sr][sc]
#         self.newColor = newColor
#         if self.initialColor == self.newColor:
#             return self.image

#         self.dfs(sr,sc)

#         return self.image

#     def dfs(self, r, c):
#         # ここでミスった、 !=でなく==
#         if not (0 <= r < self.R and 0 <= c < self.C and self.image[r][c] == self.initialColor):
#             return
        
#         self.image[r][c] = self.newColor
        
#         for dr, dc in [(0,-1),(0,1),(-1,0),(1,0)]:
#             self.dfs(r + dr, c + dc)





# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         self.R = len(image)
#         self.C = len(image[0])
#         self.image = image
#         self.prevColor = image[sr][sc]
#         self.newColor = newColor

#         if self.prevColor == self.newColor:
#             return image
        
#         self.dfs(sr,sc)

#         return self.image
        



#     def dfs(self,r,c):
#         # 停止条件1: 画面外
#         if not (0 <= r < self.R and 0 <= c < self.C):
#             return
#         # 停止条件2: 境界外
#         if self.image[r][c] != self.prevColor:
#             return
        
#         self.image[r][c] = self.newColor

#         for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
#             self.dfs(r + dr, c + dc)

# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         R = len(image)
#         C = len(image[0])
#         originalColor = image[sr][sc]
        
#         # 1. 事前チェック: 元の色と新しい色が同じなら、処理を回避
#         #    （無限再帰を防ぐための重要なガードレール）
#         if originalColor == newColor:
#             return image

#         def dfs(r: int, c: int):
#             # 停止条件 (1): 境界外に出た場合
#             if not (0 <= r < R and 0 <= c < C):
#                 return
            
#             # 停止条件 (2): 現在のセルの色が、元の色と異なる場合（連結が途切れた）
#             if image[r][c] != originalColor:
#                 return

#             # 2. 処理: 現在のセルを新しい色に塗り替える（訪問済みマーク）
#             image[r][c] = newColor

#             # 3. 再帰: 上下左右の4方向を探索
#             # 移動方向: 右, 左, 下, 上
#             for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 dfs(r + dr, c + dc)

#         # DFSの開始
#         dfs(sr, sc)
        
#         return image  
# @lc code=end

if __name__ == "__main__":
    # --- デバッグしたいテストケースをここに記述する ---
    
    # 1. Solutionクラスのインスタンスを作成
    solver = Solution()
    
    # 2. テストケースの入力値を定義
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr, sc, newColor = (1,1,2)
    
    # 3. 実行結果を取得
    #result = solver.twoSum(nums, target)
    result = solver.floodFill(image, sr, sc, newColor)
    
    # 4. 結果を表示 (確認用)
    print(f"Input: image={image}, sr={sr}, sc={sc}, newColor={newColor}")
    print(f"Output: {result}")
    
    # --- 必要に応じて別のテストケースを追加 ---
