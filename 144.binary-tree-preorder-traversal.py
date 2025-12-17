#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

# TreeNode は既に定義されていると仮定

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
            return

        traverse(root)

        return result





# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []
        
#         def traverse(node: Optional[TreeNode]):
#             # ベースケース: ノードが None なら終了
#             if not node:
#                 return
            
#             # 1. 根の値を記録
#             result.append(node.val)
            
#             # 2. 左部分木を再帰的に走査
#             traverse(node.left)
            
#             # 3. 右部分木を再帰的に走査
#             traverse(node.right)

#         traverse(root)
#         return result
# @lc code=end

