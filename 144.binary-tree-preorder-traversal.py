#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    # preorderは根左右
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []


        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return res


        


        


# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
        
#         # 1. 根をスタックに入れる
#         stack = [root]
#         res = []
        
#         # 2. スタックが空になるまで回す
#         while stack:
#             # 取り出した瞬間に「根」として記録（これがPreorderの核）
#             node = stack.pop()
#             res.append(node.val)
            
#             # 3. 右、左の順でスタックに積む
#             # （スタックから出すときは逆の「左、右」の順になる）
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
                
#         return res
#####
### saiki
####
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def traverse(node):
#             if not node:
#                 return
#             res.append(node.val)
#             traverse(node.left)
#             traverse(node.right)
            
#         traverse(root)

#         return res
# @lc code=end

