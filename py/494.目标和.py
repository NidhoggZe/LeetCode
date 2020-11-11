class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = nums.__len__()

        summ = sum(nums)

        if summ < S:
            return 0

        dp = [0] * (2*summ + 1)
            
        dp[0] = 1

        for i in range(0, n):
            for j in range(2*summ, -1, -1):
                    if dp[j] > 0:
                        dp[j + 2*nums[i]] += dp[j]

        return dp[S + summ]