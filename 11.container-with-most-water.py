#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        left = 0
        right = N - 1
        maxArea = 0
        
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            currentArea = h * w

            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea


















# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         N = len(height)
#         left = 0
#         right = N-1
#         maxArea = 0
#         while left < right:
#             h = min(height[left],height[right])
#             w = right - left
#             currArea = h*w

#             maxArea = max(maxArea, currArea)

#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
        
#         return maxArea






# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#        left = 0
#        right = len(height) - 1
#        max_area = 0
#        while left < right:
#            h = min(height[left],height[right])
#            w = right - left
#            curr_area = h*w

#            max_area = max(max_area,curr_area)

#            if height[left] < height[right]:
#                left += 1
#            else:
#                right -= 1

#        return max_area 


# @lc code=end

