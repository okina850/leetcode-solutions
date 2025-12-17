#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        char_latestIndex = {}
        max_length = 0
        left = 0
        right = 0

        for right in range(len(s)):
            char = s[right]

            if char in char_latestIndex and char_latestIndex[char] >= left:
                left = char_latestIndex[char] + 1
            char_latestIndex[char] = right
            
            max_length = max(max_length,right - left + 1)

        return max_length
# @lc code=end

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s:
#             return 0
            
#         # ハッシュマップ: {文字: その文字が出現した最新のインデックス}
#         char_map = {}
#         max_length = 0
#         left = 0 # 左ポインタ

#         # right を進めることでウィンドウを右に拡張
#         for right in range(len(s)):
#             char = s[right]
            
#             # 1. 重複チェックと左ポインタの移動 (leftの収縮)
#             #   - char がマップにあり、かつ
#             #   - その文字の最新のインデックスが left より右側にある (ウィンドウ内にある)
#             if char in char_map and char_map[char] >= left:
#                 # 左ポインタを、重複した文字の次のインデックスへ移動
#                 # これがこの解法の O(N) を実現する鍵
#                 left = char_map[char] + 1
            
#             # 2. ハッシュマップの更新 (最新インデックスを記録)
#             char_map[char] = right
            
#             # 3. 最大長さの更新
#             # 現在のウィンドウの長さは (right - left + 1)
#             current_length = right - left + 1
#             max_length = max(max_length, current_length)
            
#         return max_length