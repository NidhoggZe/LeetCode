#可能多次计入当前节点的回溯/dfs
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curans = []
        summ = 0
        candidates.sort()

        def dfs(curpos):
            nonlocal summ

            Overflow = False
            curans.append(candidates[curpos])
            summ += candidates[curpos]
            if summ == target:
                ans.append(curans.copy())
                

            elif summ < target:
                for i in range(curpos, candidates.__len__()):
                    if dfs(i):
                        break
            
            else:
                Overflow = True

            curans.pop()
            summ -= candidates[curpos]

            return Overflow

        for i in range(0, candidates.__len__()):
            if dfs(i):
                break
        return ans