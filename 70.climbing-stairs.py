#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start

class Solution:
    def climbStairs(self, n: int):

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # 1段目
        prevTwo = 1
        # 2段目
        prevOne = 2
        # 3段目からn段目 ただしn は3以上
        for _ in range(3, n + 1):
            currCombination = prevTwo + prevOne
            prevTwo = prevOne
            prevOne = currCombination
        
        return prevOne



        










# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         # after 3 
#         ways_prev_two = 1
#         ways_prev_one = 2
#         curr = 3

#         for i in range(2,n):
#             curr = ways_prev_two + ways_prev_one
            
#             ways_prev_two = ways_prev_one
#             ways_prev_one = curr
#         return curr
    
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
        
#         prev_two = 1
#         prev_one = 2
#         curr = 3

#         for _ in range(3,n + 1):
#             curr = prev_two + prev_one
#             prev_two = prev_one
#             prev_one = curr
        
#         return curr

        
# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         # エッジケース (n=1, n=2 以外の小さな値もカバー)
#         if n <= 0:
#             return 0
#         if n == 1:
#             return 1
        
#         # DPの状態変数を定義
#         # ways[n-2] に相当
#         prev_two = 1 # n=1段目までの方法の数
#         # ways[n-1] に相当
#         prev_one = 2 # n=2段目までの方法の数

#         # 3段目 (i=3) から n 段目までを計算
#         for i in range(3, n + 1):
#             # ways[n] = ways[n-1] + ways[n-2]
#             current_ways = prev_one + prev_two
            
#             # 状態の更新 (次のループのためにポインタをずらす)
#             # prev_two は prev_one の値に更新される
#             prev_two = prev_one
#             # prev_one は current_ways の値に更新される
#             prev_one = current_ways
            
#         # n=2のときはループに入らず prev_one を返すため、
#         # n > 2の場合はループ後の prev_one が答えとなる
#         return prev_one
        
# @lc code=end

