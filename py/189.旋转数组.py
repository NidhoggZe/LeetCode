from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = nums.__len__()
        if n < 2:
            return
        # count = 0
        # for i in range(0, k):
        #     lastpos = i
        #     lastnum = nums[i]
        #     while (True):
        #         curpos = (lastpos + k) % n
        #         lastnum, nums[curpos] = nums[curpos], lastnum
        #         count += 1
        #         if (curpos == i):
        #             break
        #         lastpos = curpos
        #     if count == n:
        #         return
        if k > n:
            k %= n #需要注意的点
        nums.reverse()
        for i in range(0, k//2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]

        for i in range(k, (n + k)//2):
            nums[i], nums[n - 1 + k - i] = nums[n - 1 + k - i], nums[i]
        return