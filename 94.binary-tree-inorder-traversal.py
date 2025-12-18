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
    # inorderは左ルート右
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left
            # 最後の左を入れる
            curr = stack.pop()
            res.append(curr.val)
            
            curr = curr.right

        return res  
                        




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

