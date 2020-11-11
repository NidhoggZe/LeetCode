from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        length = nums.__len__()
        r = nums.__len__()
        ans = [-1, -1]
        while l < r:
            mid = (l + r)//2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != nums[mid]:
                    ans[0] = mid
                    break
                else:
                    r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        l = 0
        r = nums.__len__()
        while l < r:
            mid = (l + r)//2
            if nums[mid] == target:
                if mid == length -1 or nums[mid+1] != nums[mid]:
                    ans[1] = mid
                    break
                else:
                    l = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return ans

