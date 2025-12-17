#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False

        mapping = {")":"(","]":"[","}":"{"}
        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack:
                    return False
                
                top_element = stack.pop()
                if mapping[char] != top_element:
                    return False
        
        if stack:
            return False
        return True
# class Solution:
#     def isValid(self, s: str) -> bool:
#         # 対応関係を辞書で定義すると、if-elifの連鎖を減らせます
#         mapping = {")": "(", "]": "[", "}": "{"}
#         stack = []

#         for char in s:
#             if char in mapping.values():  # 開き括弧の場合: スタックに積む
#                 stack.append(char)
            
#             elif char in mapping.keys():  # 閉じ括弧の場合
#                 # 1. スタックが空なら、対応する開き括弧がない → 無効
#                 if not stack:
#                     return False
                
#                 # 2. スタックのトップと対応するか確認
#                 top_element = stack.pop() # スタックから要素を取り出す
                
#                 # 対応する開き括弧と異なれば → 無効
#                 if mapping[char] != top_element:
#                     return False
            
#             # その他の文字（問題の制約上は通常考慮不要）
#             # else:
#             #     pass

#         # ループ終了後:
#         # スタックが空なら、全ての括弧がペアになっている → 有効 (True)
#         # スタックに要素が残っていれば、対応する閉じ括弧がない → 無効 (False)
#         return not stack

# @lc code=end
if __name__ == "__main__":
    # --- デバッグしたいテストケースをここに記述する ---
    
    # 1. Solutionクラスのインスタンスを作成
    solver = Solution()
    
    # 2. テストケースの入力値を定義
    # 例: Two Sum問題のサンプルケース
    s = "()"
    # 3. 実行結果を取得
    result = solver.isValid(s)
    
    # 4. 結果を表示 (確認用)
    print(f"Input: s={s}")
    print(s[0])
    print(f"Output: {result}")
