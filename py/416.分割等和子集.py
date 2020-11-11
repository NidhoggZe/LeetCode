from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = nums.__len__()
        if n < 2:
            return False
        summ = 0
        for i in range(0, n):
            summ += nums[i]
        target = summ//2
        if target * 2 != summ:
            return False

        dp = [False] * (target + 1)
            
        dp[0] = True

        for i in range(0, n):
            for j in range(target - nums[i], -1, -1):
                    if dp[j] == True:
                        dp[j + nums[i]] = True;

        return dp[target]

Solution().canPartition([1, 5, 11, 5])
