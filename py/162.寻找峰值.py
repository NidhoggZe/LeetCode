from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] < nums[mid-1]:
                right = mid - 1
            else:
                left = mid
        return right
