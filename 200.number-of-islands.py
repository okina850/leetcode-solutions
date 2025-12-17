#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#import sys
#sys.setrecursionlimit(2000)
#from typing import List
# @lc code=start
#from typing import List
import sys
# 再帰制限の引き上げはそのまま残しておきましょう
sys.setrecursionlimit(2000) 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        cnt = 0
        visited = [[False] * C for _ in range(R)]

        def dfs(r, c):
            if not (0 <= r < R and 0 <= c < C):
                return
            if grid[r][c] == "0":
                return 
            if visited[r][c]:
                return
            
            visited[r][c] = True

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc)


        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and not visited[r][c]:
                    cnt += 1
                    dfs(r, c)

        return cnt
            










# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         R, C = len(grid), len(grid[0])
#         numOfIslands = 0

#         def dfs(r,c):
#             if not (0 <= r < R and 0 <= c < C and grid[r][c] == "1"):
#                 return
#             grid[r][c] = "0"
#             for dr, dc in [(0, -1),(0, 1),(-1, 0),(1,0)]:
#                 dfs(r + dr, c + dc)

#         for r in range(R):
#             for c in range(C):
#                 if grid[r][c] == "1":
#                     numOfIslands += 1
#                     dfs(r,c)

#         return numOfIslands            



    


        
        




# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         self.rows = len(grid)
#         self.cols = len(grid[0])
#         self.grid = grid
#         self.numOfIslands = 0
#         for r in range(self.rows):
#             for c in range(self.cols):
#                 if self.grid[r][c] == "1":
#                     self.numOfIslands += 1
#                     self.dfs(r,c)
        
#         return self.numOfIslands
#     def dfs(self,r,c):            
#         if r < 0 or r >= self.rows or c < 0 or c >= self.cols or self.grid[r][c] == "0":
#             return
#         self.grid[r][c] = "0"

#         self.dfs(r+1,c)
#         self.dfs(r-1,c)
#         self.dfs(r,c+1)
#         self.dfs(r,c-1)
            

        



        






















# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         self.rows = len(grid)
#         self.cols = len(grid[0])
#         self.grid = grid

#         self.num_of_islands = 0

#         for r in range(self.rows):
#             for c in range(self.cols):
#                 if self.grid[r][c] == "1":
#                     self.num_of_islands += 1
#                     self.paint(r,c)
        
#         return self.num_of_islands
#
#
#
#        
#
#     def paint(self, r,c):
#         if r < 0 or r >= self.rows or c < 0 or c >= self.cols or self.grid[r][c] == "0":
#             return
#         self.grid[r][c] = "0"
#         self.paint(r,c + 1)
#         self.paint(r,c - 1)
#         self.paint(r + 1, c)
#         self.paint(r - 1, c)

#         #self.grid[r][c] == "0"

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]:
#             return 0
        
#         self.rows = len(grid)
#         self.cols = len(grid[0])
#         self.grid = grid
#         num_islands = 0

#         for r in range(self.rows):
#             for c in range(self.cols):
#                 if self.grid[r][c] =='1':
#                     num_islands += 1
#                     self.dfs(r,c)

#         return num_islands
    
#     def dfs(self,r,c):
#         if r < 0 or r >= self.rows or c < 0 or c >= self.cols or self.grid[r][c] == '0':
#             return
        
#         self.grid[r][c] = '0'

#         self.dfs(r+1,c)
#         self.dfs(r-1,c)
#         self.dfs(r,c+1)
#         self.dfs(r,c-1)
        
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]:
#             return 0

#         self.rows = len(grid)  # インスタンス変数として保存
#         self.cols = len(grid[0]) # インスタンス変数として保存
#         self.grid = grid       # インスタンス変数として保存
#         num_islands = 0

#         # 1. 全マス走査
#         for r in range(self.rows):
#             for c in range(self.cols):
#                 # 2. 未訪問の陸地（'1'）を発見
#                 if self.grid[r][c] == '1':
#                     num_islands += 1
#                     # メソッドとして呼び出す
#                     self.dfs(r, c)  

#         return num_islands

#     # -----------------------------------------------------
#     # DFS関数をクラスの独立したメソッドとして定義
#     # -----------------------------------------------------
#     def dfs(self, r, c):
#         # ベースケース: 範囲外、または水域の場合は探索を終了
#         # self.rowsとself.colsを参照
#         if r < 0 or r >= self.rows or c < 0 or c >= self.cols or self.grid[r][c] == '0':
#             return
        
#         # 訪問済みとしてマーク（self.gridを参照）
#         self.grid[r][c] = '0' 
        
#         # 上下左右に探索
#         self.dfs(r + 1, c)
#         self.dfs(r - 1, c)
#         self.dfs(r, c + 1)
#         self.dfs(r, c - 1) 
# @lc code=end

