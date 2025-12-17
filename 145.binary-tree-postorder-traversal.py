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

######
## 再帰法
#####

# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
        
#         def dfs(node):
#             if not node:
#                 return
#             dfs(node.left)    # 左
#             dfs(node.right)   # 右
#             res.append(node.val) # 根
            
#         dfs(root)
#         return res

#######
### 非再帰
#######

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        res = []
        
        # ステップ1: 「根 -> 右 -> 左」の順で取り出す
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            # Preorderとは逆に、左を先に積んで右を後に積む 
            # -> 取り出すときは「右 -> 左」の順になる
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        # ステップ2: 最後にひっくり返す (根右左 -> 左右根)
        return res[::-1]


# @lc code=end

