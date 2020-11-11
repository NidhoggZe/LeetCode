class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        if n < 0:
            x = 1/x
            n = -n
        while n != 0:
            if n & 1:
                ans *= x
            n //= 2
            x *= x
        
        return ans