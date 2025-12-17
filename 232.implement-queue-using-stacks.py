#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start

# ================ 
class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []
    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def _transfer_if_needed(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.output_stack.pop()

    def peek(self) -> int:
        return self.output_stack[-1]

    def empty(self) -> bool:




# ===========Perfect Solution start==============================
# class MyQueue:

#     def __init__(self):
#         # 1. Pythonの文法修正: self.を使ってインスタンス変数として定義
#         self.input_stack = []  # push時に使うスタック (LIFO)
#         self.output_stack = [] # pop/peek時に使うスタック (LIFO)

#     def push(self, x: int) -> None:
#         # pushは常に input_stack の末尾に追加（スタック操作として合法）
#         self.input_stack.append(x)

#     def _transfer_if_needed(self):
#         """
#         PopやPeekの前に、Output Stackが空ならInput Stackから全要素を移動する
#         （これがFIFOを実現する核心ロジック）
#         """
#         if not self.output_stack:
#             while self.input_stack:
#                 # input_stackの末尾から取り出し、output_stackの末尾に追加
#                 self.output_stack.append(self.input_stack.pop())


#     def pop(self) -> int:
#         # 2. 必須のガード節: Pop/Peekの前に必ずデータ移動のチェック
#         self._transfer_if_needed()
        
#         # 3. 必須のガード節: スタックが空でないか最終チェック (問題の制約上は不要だが安全のため)
#         # Pop/Peekが呼ばれたとき、キューが空の場合の処理（ここではIndexErrorを回避）
#         if not self.output_stack:
#             raise IndexError("Queue is empty")
        
#         return self.output_stack.pop() # output_stackの末尾から取り出す（FIFOの先頭に相当）

#     def peek(self) -> int:
#         # 必須のガード節: Pop/Peekの前に必ずデータ移動のチェック
#         self._transfer_if_needed()

#         if not self.output_stack:
#             raise IndexError("Queue is empty")
            
#         return self.output_stack[-1] # output_stackの末尾を参照（FIFOの先頭に相当）

#     def empty(self) -> bool:
#         # 4. Pythonの文法修正: not を使う
#         # どちらのスタックも空であれば、キューは空
#         return not self.input_stack and not self.output_stack
#===========Perfect Solution end =========================


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

