class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s += "a"
        p += "a"#避免空串

        def match(a, b):
            if a == b or a == '.' or b == '.':
                return True
            return False
        table = [[False]*(p.__len__() + 1)
                 for _ in range(s.__len__() + 1)]
        table[0][0] = True
        for i in range(0, s.__len__() + 1):
            for j in range(1, p.__len__() + 1):
                if p[j-1] != '*':
                    if match(s[i-1], p[j-1]):
                        table[i][j] = table[i-1][j-1]
                    else:
                        table[i][j] = False
                else:
                    if not match(s[i-1], p[j-2]):
                        table[i][j] = table[i][j-2]
                    else:
                        table[i][j] = table[i][j-2] or table[i-1][j]

        return table[s.__len__()][p.__len__()]
