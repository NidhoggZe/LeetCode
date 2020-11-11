#将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形（其实是N字形）排列，然后水平顺序输出
#要点在于同一行的字符可能是一个循环内的多种情况，拐点处可能重复判定

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = s.__len__()
        ans = ""
        for i in range(0, numRows):
            j = 0
            while j*(numRows*2-2) + i < l:
                ans += s[j*(numRows*2-2) + i]
                if i != 0 and i!= numRows-1 and (j+1)*(numRows*2-2) - i < l:
                    ans += s[(j+1)*(numRows*2-2) - i]
                j += 1
        return ans
