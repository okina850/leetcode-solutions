#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node






# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prevNode = None
#         currNode = head

#         while currNode:
#             nextNode = currNode.next
#             currNode.next = prevNode
#             prevNode = currNode
#             currNode = nextNode

#         return prevNode





















# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev_node = None
#         curr_node = head
#         while curr_node:
#             next_node = curr_node.next
#             curr_node.next = prev_node
#             prev_node = curr_node
#             curr_node = next_node

#         return prev_node

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         prev = None
#         curr = head

#         while curr:
#             next_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_node
        
#         return prev



# @lc code=end

# ファイルのどこかにこの関数を定義
def print_list(head):
    if not head:
        print("None")
        return
    
    current = head
    result = []
    # ノードが10個以上ある場合は省略するなど、無限ループ対策をすることも多い
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))

# --- デバッグ実行時に利用 ---
if __name__ == "__main__":
    # リスト作成: 1 -> 2 -> 3
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)
    
    print("Original List:")
    print_list(head) # 出力: 1 -> 2 -> 3

    # メソッド呼び出し
    solver = Solution()
    reversed_head = solver.reverseList(head)
    
    print("Reversed List:")
    print_list(reversed_head) # 出力: 3 -> 2 -> 1