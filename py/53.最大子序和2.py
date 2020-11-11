#线段树思想，维护左右端点最大和等值，O(logn)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def merge(p1, q1, l1, r1, m1, s1, p2, q2, l2, r2, m2, s2):
            l = max(l1, s1 + l2)
            r = max(r2, r1 + s2)
            m = max(m1, m2, r1 + l2)
            s = s1 + s2
            return p1, q2, l, r, m, s
        
        def getmaxSub(p, q):
            if p == q-1:
                return p, q, nums[p], nums[p], nums[p], nums[p]
            else:
                return merge(*getmaxSub(p, (p+q)//2), *getmaxSub((p+q)//2, q))

        _, _, _, _, m, _ =  getmaxSub(0, nums.__len__())
        return m
             
