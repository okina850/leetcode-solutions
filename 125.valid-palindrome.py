#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        left = 0
        right = N - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True



# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         N = len(s)
#         left = 0
#         right = N - 1 

#         if N == 1:
#             return True

#         while left < right:
#             while left < right and not s[left].isalnum():
#                 left += 1
#             while left < right and not s[right].isalnum():
#                 right -= 1
                        
#             if s[left].lower() != s[right].lower():
#                 return False
            
#             left += 1
#             right -= 1

            
#         return True


                

#====== best solution========
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1

#         while left < right:
#             while left < right and not s[left].isalnum():
#                 left += 1
#             while left < right and not s[right].isalnum():
#                 right -= 1

#             if left >= right: 
#                 break

#             if s[left].lower() != s[right].lower():
#                 return False
#             left += 1
#             right -= 1
#         #print(f"last left:({left},{s[left]}),right:({right},{s[right]})")
#         #if s[left].lower() != s[right].lower():
#         #    return False
        
#         return True




# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left, right = 0, len(s) -1

#         while left < right:
#             # 左ポインタを英数字に到達するまで進める
#             while left < right and not s[left].isalnum():
#                 left += 1
            
#             # 右ポインタを英数字に到達するまで戻す
#             while left < right and not s[right].isalnum():
#                 right -= 1

#             if left < right:
#                 if s[left].lower() != s[right].lower():
#                     return False
                
#                 left += 1
#                 right -= 1
            
#         return True


            
# @lc code=end

if __name__ == "main":
    solver = Solution()

    s = "A man, a plan, a canal: Panama"
    result = solver.isPalindrome(s)

    print(result)
     