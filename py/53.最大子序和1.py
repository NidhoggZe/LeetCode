from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        pre = nums[0]
        for i in range(1, nums.__len__()):
            if pre > 0:
                pre = pre + nums[i]
            else:
                pre = nums[i]
            m = max(m, pre)
        return m
            