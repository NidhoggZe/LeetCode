from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i,j = 0,0
        last = nums[0] - 1
        for i in range(len(nums)):
            if nums[i] == last:
                continue
            last = nums[i]
            nums[j] = nums[i]
            j += 1

        return j