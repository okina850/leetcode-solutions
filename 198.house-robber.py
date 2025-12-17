#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        # N = 1のとき
        if N == 1:
            return nums[0]
        # N = 2のとき
        if N == 2:
            return max(nums[0], nums[1])
        
        # N = 3以上
        prevTwo = nums[0]
        prevOne = max(nums[0], nums[1])
        for i in range(2, N):
            currMaxProfit = max(prevTwo + nums[i], prevOne)
            prevTwo = prevOne
            prevOne = currMaxProfit



        return prevOne





# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         N = len(nums)
#         if N == 1:
#             return nums[0]
#         if N == 2:
#             return max(nums[0],nums[1])
        
#         prev_two = nums[0]
#         prev_one = max(nums[0],nums[1])
#         #curr_max = max(prev_two + nums[2], prev_one)

#         for i in range(2, N):
#             curr_max = max(prev_two + nums[i],prev_one)
#             prev_two = prev_one
#             prev_one = curr_max

#         return prev_one


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         N = len(nums)
#         prevTwo = nums[0]
#         prevOne = max(nums[0],nums[1])
#         curr = max(prevTwo + nums[2],prevOne)

#         for i in range(3,N+1):
#             curr = max(prevTwo + nums[i],prevOne)
#             prevTwo = prevOne
#             prevOne = curr


#     return curr
        














        





# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) == 2:
#             return max(nums[0],nums[1])
        
#         prev_two = nums[0]
#         prev_one = max(nums[0],nums[1])
#         curr_max = max(prev_two + nums[2] ,prev_one)

#         for i in range(2,len(nums)):
#             curr_max = max(prev_two + nums[i] ,prev_one)
#             prev_two = prev_one
#             prev_one = curr_max

#         return curr_max
# class Solution:
#     def rob(self, nums: List[int]) -> int:
        
#         # エッジケース: 家がない場合は利益0
#         if not nums:
#             return 0
        
#         # エッジケース: 家が1軒の場合
#         if len(nums) == 1:
#             return nums[0]

#         # 1. DPの状態変数を定義 (O(1) 空間最適化)
        
#         # DP[i-2] に相当: 2軒前の家までの最大利益
#         prev_two = nums[0] # 最初の家までの利益
        
#         # DP[i-1] に相当: 1軒前の家までの最大利益
#         prev_one = max(nums[0], nums[1]) # 1軒目と2軒目のうち高い方
        
#         # 2. 3軒目 (i=2) から最後の家までを計算
#         for i in range(2, len(nums)):
#             # 漸化式: 
#             # 1. i番目を盗まない (prev_one) 
#             # 2. i番目を盗む (prev_two + nums[i])
#             current_max = max(prev_one, prev_two + nums[i])
            
#             # 3. 状態の更新 (次のループのためにポインタをずらす)
#             # prev_two は prev_one の値に更新
#             prev_two = prev_one
#             # prev_one は current_max の値に更新
#             prev_one = current_max
            
#         return prev_one       
# @lc code=end

