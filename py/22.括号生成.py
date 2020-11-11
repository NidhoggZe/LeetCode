from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def nth(curans, l, r):
            if r == n:
                ans.append(curans)
                return
            if r < l:
                nth(curans+')', l, r+1)
            if l < n:
                nth(curans+'(', l+1 ,r)
        nth("", 0, 0)
        return ans


print(Solution().generateParenthesis(3))
            
