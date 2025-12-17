#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k は次に val と等しくない要素を挿入する位置を示すポインタ。
        # また、結果として残る新しい配列の長さを示す。
        k = 0
        
        # i は配列全体を反復処理するためのポインタ。
        for i in range(len(nums)):
            # 現在の要素が削除対象の値 val と等しくない場合
            if nums[i] != val:
                # この要素は残すべきなので、k の位置にコピーする
                nums[k] = nums[i]
                # 次の挿入位置へポインタ k を進める
                k += 1
                
        # k は、新しい配列の長さ（残った要素の数）を示す
        return k
# @lc code=end

