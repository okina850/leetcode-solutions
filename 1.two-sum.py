#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        numToIndex = {}

        for i in range(N):
            curr = nums[i]
            complement = target - curr
            
            if complement in numToIndex:
                return [numToIndex[complement],i]
            
            numToIndex[curr] = i

























# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         itemToIndex_map = {}
#         N = len(nums)
#         for i in range(N):
#             curr =  nums[i]
#             complement = target - curr
#             if complement in itemToIndex_map:
#                 return [itemToIndex_map[complement],i]
#             itemToIndex_map[curr] = i


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         N = len(nums)
#         index_map = {}
#         for i in range(N):
#             curr = nums[i]
#             complement = target - curr
#             if complement in index_map:
#                 return [index_map[complement],i]
#             index_map[curr] = i



# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         ahaha = {}
#         N = len(nums)
#         for i in range(N):
#             complement = target - nums[i]
#             if complement in ahaha:
#                 return [ahaha[complement],i]
#             ahaha[nums[i]] = i
# @lc code=end

if __name__ == "__main__":
    # --- デバッグしたいテストケースをここに記述する ---
    
    # 1. Solutionクラスのインスタンスを作成
    solver = Solution()
    
    # 2. テストケースの入力値を定義
    # 例: Two Sum問題のサンプルケース
    nums = [2, 7, 11, 15]
    target = 9
    
    # 3. 実行結果を取得
    result = solver.twoSum(nums, target)
    
    # 4. 結果を表示 (確認用)
    print(f"Input: nums={nums}, target={target}")
    print(f"Output: {result}")
    
    # --- 必要に応じて別のテストケースを追加 ---