class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = 'a' + s
        p = 'a' + p
        lens = len(s)
        lenp = len(p)

        def match(i, j):
            if s[i] == p[j] or p[j] == '?':
                return True
            return False

        res = [[False]*lenp for _ in range(lens)]
        
        res[0][0] = True

        for j in range(1, lenp):
            res[0][j] = (p[j] == '*')
            if res[0][j] == False:
                break

        for i in range(1, lens):
            for j in range(1, lenp):
                if p[j] == '*':
                    res[i][j] = res[i][j - 1] or res[i - 1][j]
                else:
                    if match(i, j):
                        res[i][j] = res[i - 1][j - 1]
                    else:
                        res[i][j] = False


        return res[lens - 1][lenp - 1]