import math


class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        mid = (l + r)//2
        while (l <= r):
            mid = (l + r)//2
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1

        return l







# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0:
#             return 0
#         ans = int(math.exp(0.5 * math.log(x)))
#         return ans + 1 if (ans + 1) ** 2 <= x else ans
