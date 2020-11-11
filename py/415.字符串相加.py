class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        i, j = l1 - 1, l2 - 1
        add = 0
        res = ''
        while (i >= 0 or j >= 0):
            int1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            int2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            summ = int1 + int2 + add
            if summ >= 10:
                c = chr(summ%10 + ord('0'))
                add = 1
            else:
                c = chr(summ + ord('0'))
                add = 0

            res = c + res
        
            i -= 1
            j -= 1
        

        if add == 1:
            res = '1' + res
        return res

Solution().addStrings("1", "99")