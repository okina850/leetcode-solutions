#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m-1
        p2 = n-1
        p_write = m + n - 1

        while p2 >= 0:
            
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p_write] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_write] = nums2[p2]
                p2 -= 1

            p_write -= 1



# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         nums1 をインプレイスで修正し、nums1 と nums2 をマージしてソート済み配列とする。
        
#         nums1: マージ結果を格納する配列 (m+nのサイズがある)
#         m: nums1の有効な要素数
#         nums2: マージ対象の配列
#         n: nums2の要素数
        
#         時間計算量: O(m + n)
#         空間計算量: O(1)
#         """
        
#         # 1. 3つのポインタを設定
#         # p1: nums1の有効な要素の末尾 (インデックス m-1)
#         p1 = m - 1
        
#         # p2: nums2の末尾 (インデックス n-1)
#         p2 = n - 1
        
#         # p_write: 書き込み位置 (マージ後の配列の末尾、インデックス m+n-1)
#         p_write = m + n - 1
        
#         # 2. メインループ: nums2の要素がなくなるまで繰り返す (p2 >= 0)
#         # p_write はインデックス 0 に向かって進む
#         while p2 >= 0:
            
#             # 比較: nums1[p1] と nums2[p2] を比較する
#             #
#             # 条件: p1 >= 0 （nums1にまだ比較すべき有効な要素が残っている）
#             #     AND nums1[p1] > nums2[p2] （nums1の要素の方が大きい）
            
#             if p1 >= 0 and nums1[p1] > nums2[p2]:
#                 # ケース1: nums1の要素が大きい
#                 # nums1の大きい要素をp_writeの位置に移動 (後ろに移動)
#                 nums1[p_write] = nums1[p1]
#                 p1 -= 1 # nums1ポインタを前に移動
#             else:
#                 # ケース2: nums2の要素の方が大きいか、p1が既に先頭に達している
#                 # nums2の要素をp_writeの位置に格納
#                 nums1[p_write] = nums2[p2]
#                 p2 -= 1 # nums2ポインタを前に移動
            
#             # どちらのケースでも、書き込みポインタを前に移動
#             p_write -= 1

        
# @lc code=end

