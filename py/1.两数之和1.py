#用双指针解决 O(nlogn)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)

        i = 0
        j = sorted_nums.__len__()-1
        while i < j:
            if sorted_nums[i] + sorted_nums[j] == target:
                break
            elif sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            else:
                j -= 1
        ans = [0, 0]
        for a in range(0, nums.__len__()):
            if nums[a] == sorted_nums[i]:
                ans[0] = a
                break
        for a in range(0, nums.__len__()):
            if (nums[a] == sorted_nums[j]) & (a != ans[0]):
                ans[1] = a
                break
        return ans
        
            
        
