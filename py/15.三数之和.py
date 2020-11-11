# 这道题考察双指针，重点在于重复答案的判定
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = nums.__len__()
        nums.sort()
        i = 0
        while i < l:
            summ = - nums[i]
            j = i + 1
            k = l - 1
            while j < k:
                if nums[j] + nums[k] == summ:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] < summ:
                    j += 1
                else:
                    k -= 1
            i += 1
            while i < l and nums[i] == nums[i-1]:  #如果nums[i] == nums[i-1]，第一个指针在第i位时i j k的组合种类肯定包含了第一个指针在第i+1位的情况
                i += 1
        return ans


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
