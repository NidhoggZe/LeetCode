#用hashmap记录是否出现过（字典同时还能将索引存为值）O(n)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(0, nums.__len__()):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            else:
                hashmap[nums[i]] = i
        return None
            