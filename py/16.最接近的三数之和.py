from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        diff = abs(nums[0] + nums[1] + nums[2] - target)
        n = len(nums)
        for k in range(n - 2):
            i = k + 1
            j = n - 1
            while i < j:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum == target:
                    return curSum
                if abs(curSum - target) < diff:
                    diff = abs(curSum - target)
                    res = curSum
                if curSum < target:
                    i += 1
                else:
                    j -= 1

        return res