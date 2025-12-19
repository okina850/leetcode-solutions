#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    """ツリーノードのクラス定義（通常は提供される）"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)

        return max(leftHeight, rightHeight) + 1








# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
        
#         leftDepth = self.maxDepth(root.left)
#         rightDepth = self.maxDepth(root.right)

#         return max(leftDepth, rightDepth) + 1











# # class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root == None:
#             return 0
        
#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right) 

#         return max(left_depth,right_depth) + 1

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
        
#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right)

#         return max(left_depth, right_depth) + 1


# class TreeNode:
#     """ツリーノードのクラス定義（通常は提供される）"""
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
        
#         # a. ベースケース: ノードがNone（空）であれば、深さは0
#         if root is None:
#             return 0
        
#         # b. 再帰ステップ:
#         # 左部分木の最大深さを求める
#         left_depth = self.maxDepth(root.left)
        
#         # 右部分木の最大深さを求める
#         right_depth = self.maxDepth(root.right)
        
#         # c. 結果の結合:
#         # 左右の深さを比較し、深い方に現在のノードの深さ (1) を加える
#         return max(left_depth, right_depth) + 1
# @lc code=end

if __name__ == "__main__":
    
    # 1. 💡 TreeNode クラスの定義（通常、LeetCodeでは提供されますが、デバッグ用に必要）
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        # 💡 このメソッドを追加する
        def __repr__(self):
            # ノードの値だけを表示する
            return f"Node({self.val})" 
            # または、接続先も表示するなら：
            # return f"Node(val={self.val}, left={self.left.val if self.left else 'None'}, right={self.right.val if self.right else 'None'})"
    def print_tree(root, level=0, prefix="Root: "):
        """ツリー全体をインデント付きで表示するヘルパー関数 (DFS)"""
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.val))
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")

# --- 実行 ---
# print_tree(root)    
    # 2. テストケースのツリーを作成 (例: [3, 9, 20, None, None, 15, 7] -> 深さ 3)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node20 = TreeNode(20, left=node15, right=node7)
    node9 = TreeNode(9)
    root = TreeNode(3, left=node9, right=node20)
    
    # 3. 実行
    solver = Solution()
    
    # 正しい解答コード（+1を含む）を使う
    # 注意: ファイル内のコードを修正してからデバッグしてください
    result = solver.maxDepth(root)
    
    print(root)
    # 4. 結果の表示
    print(f"Tree Depth: {result} (Expected: 3)") 
    
    # 💡 エッジケースのテスト
    result_empty = solver.maxDepth(None)
    print(f"Empty Tree Depth: {result_empty} (Expected: 0)")
    print_tree(root)