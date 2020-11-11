from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        desc = 1
        asc = 0
        maxn = nums[0]
        minn = nums[nums.__len__() - 1]
        for i in range(1, nums.__len__()):
            if maxn > nums[i]:
                asc = i
            else:
                maxn = nums[i]
        for j in range(nums.__len__() - 1, -1, -1):
            if minn < nums[j]:
                desc = j
            else:
                minn = nums[j]
        return asc + 1 - desc


Solution().findUnsortedSubarray([1,2,3,4])