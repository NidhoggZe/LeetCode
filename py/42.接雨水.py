from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = height.__len__()
        count = 0
        lmax = [0 for _ in range(n)]
        rmax = [0 for _ in range(n)]
        curl = 0
        curr = 0
        for i in range(1, n):
            curl = max(curl, height[i-1])
            lmax[i] = curl
        for i in range(n-2, -1, -1):
            curr = max(curr, height[i+1])
            rmax[i] = curr
        
        for i in range(0, n):
            if height[i] < min(lmax[i],rmax[i]):
                count += min(lmax[i],rmax[i]) - height[i]
        
        return count
            


Solution().trap([])