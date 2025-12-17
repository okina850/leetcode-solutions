#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
#from collections import Counter
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}

        for char in s:
            map_s[char] = map_s.get(char, 0) + 1
        
        for char in t:
            if not char in map_s.keys():
                return False
            map_s[char] -= 1
        
        for cnt in map_s.values():
            if cnt != 0:
                return False
        
        return True

















# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         map_s = {}

#         # register s
#         for char in s:
#             map_s[char] = map_s.get(char, 0) + 1

#         for char in t:
#             if not char in map_s.keys():
#                 return False
            
#             map_s[char] -= 1
        
#         for num in map_s.values():
#             if num != 0:
#                 return False
        
#         return True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         counts = {} 
#         if len(s) != len(t):
#             return False
#         for char in s:
#             counts[char] = counts.get(char,0) + 1
        
#         for char in t:
#             if not char in counts.keys():
#                 return False
#             counts[char] -= 1
        
#         for count in counts.values():
#             if count != 0:
#                 return False
        
#         return True
            
        
# @lc code=end
if __name__ == "__main__":
    # Solutionクラスのインスタンスを作成
    solver = Solution()
    
    # --- テストケース ---
    
    # 1. 正常系 (True)
    s1, t1 = "anagram", "nagaram"
    print(f"Test 1: s='{s1}', t='{t1}' -> Result: {solver.isAnagram(s1, t1)} (Expected: True)")
    
    # 2. 正常系 (False - 文字が異なる)
    s2, t2 = "rat", "car"
    print(f"Test 2: s='{s2}', t='{t2}' -> Result: {solver.isAnagram(s2, t2)} (Expected: False)")
    
    # 3. 正常系 (False - 長さが異なる)
    s3, t3 = "a", "ab"
    print(f"Test 3: s='{s3}', t='{t3}' -> Result: {solver.isAnagram(s3, t3)} (Expected: False)")
    
    # 4. エッジケース (False - 頻度が異なる: 'a'の数が違う)
    s4, t4 = "aacc", "ccac"
    print(f"Test 4: s='{s4}', t='{t4}' -> Result: {solver.isAnagram(s4, t4)} (Expected: False)")

    # 5. エッジケース (False - tにsにない文字が含まれる)
    s5, t5 = "abc", "abx"
    print(f"Test 5: s='{s5}', t='{t5}' -> Result: {solver.isAnagram(s5, t5)} (Expected: False)")
