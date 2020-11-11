class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ''
        if numerator*denominator < 0:
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator//denominator)
        remainder = numerator - numerator//denominator*denominator
        pos = []
        loop = None
        dic = {}
        while remainder != 0:
            if remainder in dic:
                loop = [remainder, str(dic[remainder])]
                break
            oldremain = remainder
            remainder *= 10
            ans = str(remainder//denominator)
            pos.append([oldremain,ans])
            dic[oldremain] = ans
            remainder = remainder - remainder//denominator*denominator
        

        if pos:
            res += '.'
            i = 0
            for i in range(len(pos)):
                if loop and pos[i][0] == loop[0] and pos[i][1] == loop[1]:
                    break
                res += pos[i][1]
            if loop:
                res += '('
                for i in range(i, len(pos)):
                    res += pos[i][1]
                res += ')'
        return res

Solution().fractionToDecimal(4, 333)