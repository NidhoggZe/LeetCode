from typing import List
from collections import Counter
import re

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxn = 0
        def longest(s: str, k: int):
            nonlocal maxn
            if len(s) <= maxn:
                return
            dic = Counter(s)
            spc = []
            for c in dic:
                if dic[c] < k:
                    spc.append(c)
            if not spc:
                maxn = len(s)
            else:
                restr = ''
                for c in spc:
                    restr += c + '|'
                next = re.split(restr[:-1], s)
                for ss in next:
                    longest(ss, k)
            return

        longest(s, k)
        
        return maxn

Solution().longestSubstring('bbaaacbd', 3)