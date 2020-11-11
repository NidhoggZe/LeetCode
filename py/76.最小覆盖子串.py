class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        j = 0
        minlen = s.__len__() + 1
        mini = 0
        minj = 0
        dic = {}
        neednum = 0
        for c in t:
            neednum += 1
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
            
        while (i <= s.__len__()):
            if neednum > 0:
                if i == s.__len__():
                    break
                if s[i] in dic:
                    dic[s[i]] -= 1
                    if dic[s[i]] >= 0:
                        neednum -= 1
                i += 1
            
            else:
                if i - j < minlen:
                    minlen = i-j
                    mini = i
                    minj = j
                if s[j] in dic:
                    dic[s[j]] += 1
                    if dic[s[j]] > 0:
                        neednum += 1
                j += 1

        if minlen == s.__len__() + 1:
            return ""
        else:
            return s[minj:mini]