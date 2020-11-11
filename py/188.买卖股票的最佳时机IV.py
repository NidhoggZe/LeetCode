from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k == 0 or n < 2:
            return 0
        k = min(k, n//2)
        maxpro = [[0, -prices[0]] for _ in range(k + 1)]
        for i in range(n):
            for j in range(k, 0, -1):
                maxpro[j][0] = max(maxpro[j - 1][1] + prices[i], maxpro[j][0])
                maxpro[j - 1][1] = max(maxpro[j - 1][1], maxpro[j - 1][0] - prices[i])

        return maxpro[k][0]


Solution().maxProfit(2, [2,4,1])
                