from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        index = [0] * len(nums)
        temp = [0] * len(nums)
        tempIndex = [0] * len(nums)
        ans = [0] * len(nums)

        def merge(a, l, mid, r): 
            nonlocal index, temp, tempIndex
            i = l
            j = mid + 1
            p = l
            while i <= mid and j <= r:
                if (a[i] <= a[j]) :
                    temp[p] = a[i]
                    tempIndex[p] = index[i]
                    ans[index[i]] += (j - mid - 1)
                    i += 1
                    p += 1
                else:
                    temp[p] = a[j]
                    tempIndex[p] = index[j]
                    j += 1
                    p += 1

            while (i <= mid):
                temp[p] = a[i]
                tempIndex[p] = index[i]
                ans[index[i]] += (j - mid - 1)
                i += 1
                p += 1

            while (j <= r):
                temp[p] = a[j]
                tempIndex[p] = index[j]
                j += 1
                p += 1
            for k in range(l, r + 1):
                index[k] = tempIndex[k]
                a[k] = temp[k]

        def mergeSort(a, l, r):
            if (l >= r):
                return
            mid = (l + r) >> 1
            mergeSort(a, l, mid)
            mergeSort(a, mid + 1, r)
            merge(a, l, mid, r)

        for i in range(0, len(nums)):
            index[i] = i

        l = 0
        r = len(nums) - 1
        mergeSort(nums, l, r)

        return ans


Solution().countSmaller([5,2,6,1])