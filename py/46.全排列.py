#考虑交换位置的方法解决，不用记录出现与否，但（原始有序数组的）输出不是字典序

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []
        n = nums.__len__()
        exist = [False]*n
        def dfs(pos):
            if exist[pos]:
                return
            ans.append(nums[pos])
            exist[pos] = True
            if ans.__len__() == n:
                res.append(ans.copy())
            else:
                for i in range(0, n):
                    dfs(i)
            ans.pop()
            exist[pos] = False
            return

        for i in range(0, n):
            dfs(i)
        
        return res