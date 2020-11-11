#串中心展开，也可动态规划，只需记录[m:n]是否是对称

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.__len__()
        m = 0
        slc = ""
        for i in range(0, l):
            cur = -1
            h = i
            t = i
            while (h >= 0) and (t < l) and (s[h] == s[t]):
                h -= 1
                t += 1
                cur += 2
            if cur > m:
                m = cur
                slc = s[h+1:t]
        
        for i in range(0, l-1):
            cur = 0
            h = i
            t = i+1
            while (h >= 0) and (t < l) and (s[h] == s[t]):
                h -= 1
                t += 1
                cur += 2
            if cur > m:
                m = cur
                slc = s[h+1:t]
        
        return slc

Solution().longestPalindrome("babad")