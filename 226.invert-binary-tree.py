#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        tmp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tmp

        return root



# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:

#         if root == None:
#             return None
        

#         self.invertTree(root.left)
#         self.invertTree(root.right)

#         tmp = root.left
#         root.left = root.right
#         root.right = tmp

#         return root


# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if root is None:
#             return None
        
#         tmp = self.invertTree(root.right)
#         root.right = self.invertTree(root.left)
#         root.left = tmp
        
#         return root
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
        
#         # a. ベースケース: ノードがNoneであれば、処理終了
#         if root is None:
#             return None
        
#         # b. 再帰ステップ: 左右の子ノードに対して再帰的に反転を呼び出す
#         #    （この時点で、子ノードの反転は完了していると「信じる」）
#         self.invertTree(root.left)
#         self.invertTree(root.right)
        
#         # c. 処理（入れ替え）：現在のノードの左右の子を交換する
#         #    一時変数を使って安全にポインタを付け替える
#         temp = root.left
#         root.left = root.right
#         root.right = temp
        
#         # 反転後の現在の根ノードを返す
#         return root      
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

# 2. テストケースのツリーを作成 (例: [3, 9, 20, None, None, 15, 7])
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node20 = TreeNode(20, left=node15, right=node7)
    node9 = TreeNode(9)
    root = TreeNode(3, left=node9, right=node20)

    print("--- 処理前のツリー ---")
    print_tree(root) # L:9, R:20

    # 3. 実行: invertTree メソッドを呼び出す
    solver = Solution()
    # 反転された新しい根ノードを受け取る
    inverted_root = solver.invertTree(root) 
    
    print("\n--- 処理後のツリー ---")
    print_tree(inverted_root) # 期待値: L:20, R:9
    # print(root) は不要です

    # ... (maxDepth関連のコードは削除するかコメントアウト