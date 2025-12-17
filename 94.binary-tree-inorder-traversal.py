#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

# TreeNode は LeetCode で定義されているノード構造
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        def traverse(node):
            
            if not node:
                return

            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
            return

        traverse(root)

        return result







# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []
        
#         def traverse(node: Optional[TreeNode]):
#             # ベースケース: ノードが None なら、何もしないで戻る
#             if not node:
#                 return
            
#             # 1. 左部分木を再帰的に走査
#             traverse(node.left)
            
#             # 2. 根の値を記録
#             result.append(node.val)
            
#             # 3. 右部分木を再帰的に走査
#             traverse(node.right)

#         traverse(root)
#         return result      
        
# @lc code=end

