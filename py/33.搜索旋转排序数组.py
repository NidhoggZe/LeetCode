from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = nums.__len__()
        l = 0
        r = length
        v = 0
        while l < r:
            mid = (l + r)//2
            if (mid == 0 or nums[mid] < nums[mid-1]) and (mid == length-1 or nums[mid] < nums[mid+1]):
                v = mid
                break
            elif nums[mid] > nums[0]:
                l = (l + r)//2 + 1
            else:
                r = (l + r)//2


        turnpoint = length - v
        def turned(p: int):
            if p >= turnpoint:
                return p - turnpoint
            else:
                return length - turnpoint + p
        l = 0
        r = length
        while l < r:
            mid = nums[turned((l + r)//2)]
            if mid == target:
                return turned((l + r)//2)
            elif mid < target:
                l = (l + r)//2 + 1
            else:
                r = (l + r)//2
        
        return -1

print(Solution().search([3, 4, 6], 6))