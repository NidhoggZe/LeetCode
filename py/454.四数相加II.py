from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic1 = {}

        for i in A:
            for j in B:
                dic1[i+j] = dic1.setdefault(i+j, 0) + 1
        
        count = 0

        for i in C:
            for j in D:
                count += dic1.setdefault(-i-j, 0)


        return count


a=[-1,-1]
b=[-1,1]
c=[-1,1]
d=[1,-1]

Solution().fourSumCount(a,b,c,d)