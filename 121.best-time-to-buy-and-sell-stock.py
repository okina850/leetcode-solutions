#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for curr_price in prices:
            curr_profit = curr_price - min_price
            max_profit = max(max_profit, curr_profit)
            min_price = min(min_price, curr_price)
        
        return max_profit



# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         N = len(prices)
#         if N == 1:
#             return 0
        
#         max_profit = 0
#         curr_min = prices[0]

#         for curr_price in prices:
#             max_profit = max(max_profit, curr_price - curr_min)
#             curr_min = min(curr_min,curr_price)
        
#         return max_profit

























# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         N = len(prices)
#         if N == 0:
#             return 0
#         max_profit = 0
#         min_price = prices[0]

#         for price_today in prices:
#             min_price = min(min_price,price_today)
#             max_profit = max(max_profit,price_today - min_price)
        
#         return max_profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0

#         # 1. 初期設定
#         # 最大利益は0からスタート
#         max_profit = 0
        
#         # 最小価格は、最初の要素か、それより非常に大きな値からスタート
#         # prices[0]で初期化するのが最も実用的
#         min_price = prices[0] 

#         # 2. 2日目以降の価格を走査
#         for i in range(1, len(prices)):
#             current_price = prices[i]
            
#             # a. 最大利益を更新
#             # 「今日売った場合の利益」と既存の最大利益を比較
#             current_profit = current_price - min_price
#             max_profit = max(max_profit, current_profit)
            
#             # b. 最小価格を更新 (貪欲な選択)
#             # 今日の価格が、これまでの最小価格よりも低ければ、それを新たな「買い」の候補とする
#             min_price = min(min_price, current_price)
            
#         return max_profit           

# @lc code=end

