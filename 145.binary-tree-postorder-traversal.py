#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node):
            if not node:
                return 
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)

            return
        
        traverse(root)
        
        return


# class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node: Optional[TreeNode]):
            # ベースケース: ノードが None なら終了
            if not node:
                return
            
            # 1. 左部分木を再帰的に走査
            traverse(node.left)
            
            # 2. 右部分木を再帰的に走査
            traverse(node.right)
            
            # 3. 根の値を記録 (最後に訪問)
            result.append(node.val)

        traverse(root)
        return result
# @lc code=end

