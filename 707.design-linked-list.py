#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
from typing import Optional

# class Node:
#     """双方向リストのノード定義"""
#     def __init__(self, val):
#         self.val = val
#         self.prev = None
#         self.next = None
# class MyLinkedList:
#     def __init__(self):
#         self.size = 0
#         self.head = Node(0)
#         self.tail = Node(0)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def _get_node(self, index: int) -> Optional[None]:
#         if not (0 <= index < self.size):
#             return None
#         # 色々やってるけどとにかくノードを目的のindexの位置まで進めてるだけ
#         if index < self.size /2:
#             # 一つ
#             current = self.head.next
#             for _ in range(index):
#                 current = current.next
#         else:
#             current = self.tail.prev
#             for _ in range(self.size -1 - index):
#                 current = current.prev
#         return current
    
#     def get(self, index: int) -> int:
#         node = self._get_node(index)
#         return node.val if node else -1
    
#     def _add_node(self, prev_node: Node, next_node: Node, val: int) -> None:
#         new_node = Node(val)
#         new_node.prev = prev_node
#         new_node.next = next_node

#         prev_node.next = new_node
#         next_node.prev = new_node

#         self.size += 1
    
#     def addAtHead(self, val: int) -> None:
#         self._add_node(self.head, self.head.next, val)
    
#     def addAtTail(self, val:int) -> None:
#         self._add_node(self.tail.prev, self.tail, val)
#     def addAtIndex(self, index: int, val: int) -> None:
#         if index > self.size:
#             return
#         if index < 0:
#             index = 0
#         if index == self.size:
#             self.addAtTail(val)
#             return
        
#         next_node = self._get_node(index)
#         if next_node:
#             prev_node = next_node.prev
#             self._add_node(prev_node, next_node, val)


# from typing import Optional # <--- これを追加
# class Node:
#     """双方向リストのノード定義"""
#     def __init__(self, val):
#         self.val = val
#         self.prev = None
#         self.next = None

# class MyLinkedList:
#     # ... (既存の __init__, get, addAtHead, addAtTail, addAtIndex, deleteAtIndex は省略) ...
#     # 必要に応じて、上記のメソッド定義の下にこれを貼り付けてください。

#     def __init__(self):
#         # サイズを追跡
#         self.size = 0
#         self.head = Node(0) 
#         self.tail = Node(0)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def _get_node(self, index: int) -> Optional[Node]:
#         # ... (_get_node 実装は省略) ...
#         if index < 0 or index >= self.size:
#             return None
        
#         if index < self.size / 2:
#             current = self.head.next
#             for _ in range(index):
#                 current = current.next
#         else:
#             current = self.tail.prev
#             for _ in range(self.size - 1 - index):
#                 current = current.prev
                
#         return current
        
#     def get(self, index: int) -> int:
#         node = self._get_node(index)
#         return node.val if node else -1

#     def _add_node(self, prev_node: Node, next_node: Node, val: int) -> None:
#         new_node = Node(val)
        
#         new_node.prev = prev_node
#         new_node.next = next_node
        
#         prev_node.next = new_node
#         next_node.prev = new_node
        
#         self.size += 1

#     def addAtHead(self, val: int) -> None:
#         self._add_node(self.head, self.head.next, val)

#     def addAtTail(self, val: int) -> None:
#         self._add_node(self.tail.prev, self.tail, val)

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index > self.size:
#             return
#         if index < 0:
#             index = 0
            
#         if index == self.size:
#             self.addAtTail(val)
#             return
            
#         # 挿入位置のノードを取得
#         next_node = self._get_node(index)
#         if next_node:
#             prev_node = next_node.prev
#             self._add_node(prev_node, next_node, val)

#     def deleteAtIndex(self, index: int) -> None:
#         node_to_delete = self._get_node(index)
        
#         if node_to_delete:
#             prev_node = node_to_delete.prev
#             next_node = node_to_delete.next
            
#             prev_node.next = next_node
#             next_node.prev = prev_node
            
#             self.size -= 1

#     # --- 可視化のためのデバッグメソッド ---
#     def print_list(self):
#         """リストの内容を先頭から末尾まで走査して表示する"""
#         if self.size == 0:
#             print(f"[Size: 0] HEAD <-> TAIL")
#             return

#         output = f"[Size: {self.size}] HEAD"
#         current = self.head.next # 最初の実ノードから開始
        
#         # 実ノードからTAILの直前まで走査
#         while current != self.tail:
#             output += f" <-> {current.val}"
#             current = current.next
        
#         output += " <-> TAIL"
#         print(output)
#     # --- デバッグメソッド終了 ---



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end


############デバッグ

# MyLinkedList のインスタンス化
dll = MyLinkedList()

# 操作を実行
dll.addAtHead(1)
dll.print_list()  # 出力: [Size: 1] HEAD <-> 1 <-> TAIL

dll.addAtTail(3)
dll.print_list()  # 出力: [Size: 2] HEAD <-> 1 <-> 3 <-> TAIL

dll.addAtIndex(1, 2) # インデックス 1 に 2 を挿入
dll.print_list()  # 出力: [Size: 3] HEAD <-> 1 <-> 2 <-> 3 <-> TAIL

dll.deleteAtIndex(2) # インデックス 2 の 3 を削除
dll.print_list()  # 出力: [Size: 2] HEAD <-> 1 <-> 2 <-> TAIL