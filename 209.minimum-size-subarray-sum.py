#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List




# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
#         N = len(nums)
#         left = 0
#         current_sum = 0
#         # 最小長を格納。N+1 はありえない大きな値。
#         min_length = N + 1 

#         # right (r) ポインタでウィンドウを拡張
#         for right in range(N):
#             current_sum += nums[right]
            
#             # current_sum が target 以上である限り、left (l) ポインタでウィンドウを縮小し、最小長をチェック
#             while current_sum >= target:
#                 # 1. 最小長を更新
#                 min_length = min(min_length, right - left + 1)
                
#                 # 2. ウィンドウを縮小
#                 current_sum -= nums[left]
#                 left += 1

#         # min_length が初期値のままなら 0 を返し、そうでなければ最小長を返す
#         return min_length if min_length <= N else 0
# @lc code=end

