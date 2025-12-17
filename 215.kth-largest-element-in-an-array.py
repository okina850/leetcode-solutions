#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for n in nums:
            heapq.heappush(min_heap, n)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


# class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. 最小ヒープを初期化
        min_heap = []
        
        for n in nums:
            # 2. ヒープに要素を追加 (push)
            heapq.heappush(min_heap, n)
            
            # 3. サイズkを超えた場合の処理
            if len(min_heap) > k:
                # 最小ヒープの最小値（根）を削除 (pop)
                # これにより、ヒープは常に上位k個を保持する
                heapq.heappop(min_heap)
                
        # 4. 結果の返却
        # ループ終了後、ヒープの根（最も小さい要素）がk番目に大きな要素
        return min_heap[0]
# @lc code=end

