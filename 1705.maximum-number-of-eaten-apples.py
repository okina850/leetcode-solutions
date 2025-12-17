#
# @lc app=leetcode id=1705 lang=python3
#
# [1705] Maximum Number of Eaten Apples
#

# @lc code=start
# 今日食べられるリンゴのうち、最も早く腐るリンゴを貪欲に選ぶ
# ヒープで「食べられるリンゴのグループ」を管理し、常に「最小の腐敗日(最も早く来る期限)」をもつリンゴを高速に参照できるようにする
# ヒープのノードに、最も早い腐敗日を持つリンゴの情報(腐敗日, リンゴの数)のペアを格納
# rootの「最も早い腐敗日」が今日よりも過去である場合popして捨てる
# 日0プに食べられるリンゴが残っていれば、最も早く腐るリンゴを食べる
# 食べた結果、リンゴの数が0になった場合、その腐敗日のエントリは削除される


import heapq
from typing import List

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        N = len(apples)
        min_heap = []       # 最小ヒープ: (腐敗日, 残りのリンゴ数)
        total_eaten = 0
        day = 0             # 現在の日数カウンター
        
        # 1. ループ: 収穫期間中 (day < N) か、まだ食べられるリンゴがヒープに残っている間
        while day < N or min_heap:
            
            # --- I. 新しいリンゴの追加 (収穫期間中のみ) ---
            if day < N and apples[day] > 0:
                # 腐敗日 = 今日 + 食べられる期間
                # days[i]は期間なので、最終日（インデックス）は day + days[day]
                rot_day = day + days[day]
                # ヒープに (腐敗日, 数) を追加
                heapq.heappush(min_heap, (rot_day, apples[day]))
            
            # --- II. 期限切れのリンゴの排除 (ガード節) ---
            # 根の腐敗日が、今日 (day) よりも過去なら捨てる
            while min_heap and min_heap[0][0] <= day:
                heapq.heappop(min_heap)
                
            # --- III. 貪欲な選択と消費 ---
            if min_heap:
                # 最小の腐敗日を持つリンゴを取り出す
                rot_day, count = heapq.heappop(min_heap)
                
                # 1個食べる
                total_eaten += 1
                count -= 1
                
                # IV. 残りのリンゴをヒープに戻す
                if count > 0:
                    heapq.heappush(min_heap, (rot_day, count))
            
            # 日を一つ進める
            day += 1
            
        return total_eaten      
# @lc code=end

