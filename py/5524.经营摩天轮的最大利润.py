from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxprofit = 0
        curprofit = 0
        curcus = 0
        count = 0
        maxcount = -1
        for i in range(0, customers.__len__()):
            curcus += customers[i]
            custurn = min(4, curcus)
            turnprofit = custurn*boardingCost - runningCost
            curprofit += turnprofit
            if curprofit > maxprofit:
                maxprofit = curprofit
                maxcount = i
            curcus -= custurn
            count += 1

        while curcus != 0:
            custurn = min(4, curcus)
            turnprofit = custurn*boardingCost - runningCost
            curprofit += turnprofit
            if curprofit > maxprofit:
                maxprofit = curprofit
                maxcount = count
            curcus -= custurn
            count += 1

        if maxprofit == 0:
            return -1
        else:
            return maxcount + 1

Solution().minOperationsMaxProfit([10,10,6,4,7],3,8)