from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            res ^= i
        
        for i in range(len(nums)):
            res ^= nums[i]

        return res