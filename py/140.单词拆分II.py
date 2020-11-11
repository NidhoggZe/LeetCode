from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def returnNone():
            return []
        res = [None for _ in range(len(s))]

        def dfs(pos: int):
            if pos >= len(s):
                return

            if res[pos] != None:
                return

            curs = s[pos:]
            res[pos] = []
            for word in wordDict:
                if curs.startswith(word):
                    i = pos + len(word)
                    if i == len(s):
                        res[pos].append(word)
                        continue
                    dfs(i)
                    for sentence in res[i]:
                        res[pos].append(word + ' ' + sentence)

        dfs(0)

        return res[0]