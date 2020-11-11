from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        maxpro1 = []
        minprice = prices[0]
        curmaxpro = 0
        for i in range(n):
            minprice = min(minprice, prices[i])
            curmaxpro = max(curmaxpro, prices[i] - minprice)
            maxpro1.append(curmaxpro)

        
        maxprice = prices[n - 1]
        maxpro = 0
        curmaxpro = 0
        for i in range(n-1, -1, -1):
            maxprice = max(maxprice, prices[i])
            curmaxpro = max(curmaxpro, maxprice - prices[i])
            maxpro = max(maxpro1[i] + maxprice - prices[i], maxpro)

        return maxpro
