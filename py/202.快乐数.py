class Solution:
    def isHappy(self, n: int) -> bool:
        dic = set()
        while n != 1:
            if n in dic:
                return False
            dic.add(n)
            newn = 0
            while n != 0:
                newn += (n%10)*(n%10)
                n //= 10
            n = newn

        return True


Solution().isHappy(19)