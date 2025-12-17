#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        # 1. 初期化: ダミーノードとテールポインタのセットアップ
        dummy = ListNode()
        tail = dummy # tailはマージ中のリストの最新のノードを指す

        # 2. イテレーション: 両方のリストにノードがある限り比較と接続を繰り返す
        while list1 and list2:
            if list1.val < list2.val:
                # list1からノードを採用
                tail.next = list1
                list1 = list1.next
            else:
                # list2からノードを採用
                tail.next = list2
                list2 = list2.next
            
            # tailポインタを新しく接続したノードへ進める
            tail = tail.next

        # 3. 残りの処理: ループ終了後、どちらか一方に残ったノードをすべて接続
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # 4. 結果の返却: ダミーノードの次が、マージされたリストのヘッド
        return dummy.next
        
# @lc code=end
if __name__ == "main":
    solver = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]

    def makeHead(list):
        N = len(list)
        if N == 0:
            return None
        prev_node = ListNode(val = list.pop(), next = None)
        while list:
            prev_node = ListNode(val = list.pop(), next = prev_node)

        return prev_node

    head1 = makeHead(list1)
    head2 = makeHead(list2)

    result = solver.mergeTwoLists(head1, head2)
    print(result)

