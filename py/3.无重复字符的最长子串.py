class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        exist = {}
        i = 0
        m = 0
        cur = 0
        head = 0
        #wcwkelkb
        while (i < s.__len__()):
            c = s[i]
            if (c not in exist) or (exist[c] < head):
                cur += 1
            else:
                m = max(m, cur)
                head = exist[c] + 1
                cur = i - head + 1
            exist[c] = i
            i += 1
        return max(m, cur)
        
            
