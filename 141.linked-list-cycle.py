#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    """リストノードのクラス定義"""
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         if not head or not head.next:
#             return False
        
#         slow = head
#         fast = head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 return True
            
        
#         return False
        







# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         # エッジケース: リストが空、またはノードが一つだけの場合、サイクルはない
#         if not head or not head.next:
#             return False

#         # 1. 初期設定
#         slow = head
#         fast = head

#         # 2. ループ: fastが末尾に到達しない限り続ける
#         while fast and fast.next:
#             # 3. ポインタの移動
#             slow = slow.next        # 1ステップ移動
#             fast = fast.next.next   # 2ステップ移動
            
#             # 4. サイクルの検出（衝突）
#             if slow == fast:
#                 return True # 衝突発生 = サイクルあり

#         # 5. ループ終了（fastがNoneに到達）: サイクルなし
#         return False 
# @lc code=end

