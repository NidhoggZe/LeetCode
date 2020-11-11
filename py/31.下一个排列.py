from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            while i < j:
                t = nums[j]
                nums[j] = nums[i]
                nums[i] = t
                i += 1
                j -= 1
        i = nums.__len__()-1
        while (i >= 1):
            if nums[i] <= nums[i-1]:
                i -= 1
            else:
                break
        swap(i, nums.__len__()-1)
        if i-1 >= 0:
            for j in range(i, nums.__len__()):
                if nums[j] >= nums[i-1]:
                    t = nums[j]
                    nums[j] = nums[i-1]
                    nums[i-1] = t
                    break
        return

print(Solution().nextPermutation([2,3,1]))