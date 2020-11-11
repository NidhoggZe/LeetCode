from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0

        res = 0

        pres = [0]

        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            pres.append(curSum)
        
        n = len(nums) + 1

        def countAndSort(l1, r1, l2, r2):
            nonlocal n, res, lower, upper
            arr1 = pres[l1:r1]
            arr2 = pres[l2:r2]

            len1, len2 = r1 - l1, r2 - l2
            l, r = 0, 0
            for i in range(len1):
                while l < len2 and arr1[i] + lower > arr2[l]:
                    l += 1
                while r < len2 and arr1[i] + upper >= arr2[r]:
                    r += 1
                res += r - l

            pos = l1
            i, j = 0, 0
            while (i < len1 and j < len2):
                if arr1[i] < arr2[j]:
                    pres[pos] = arr1[i]
                    pos += 1
                    i += 1
                else:
                    pres[pos] = arr2[j]
                    pos += 1
                    j += 1

            while i < len1:
                pres[pos] = arr1[i]
                pos += 1
                i += 1

            while j < len2:
                pres[pos] = arr2[j]
                pos += 1
                j += 1
            return


        i = 1
        while i < n:
            j = 0
            while j + i < n:
                countAndSort(j, j + i, j + i, min(j + 2*i, n))
                j += 2*i
            i *= 2

        return res

Solution().countRangeSum([-2,5,-1],-2,2)