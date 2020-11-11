#暴力深搜+回溯
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        hashmap = {}
        curstr = ""
        m = 0

        def dfs(i):
            nonlocal curstr, m
            if i == s.__len__():
                m = max(m, hashmap.__len__())
                return

            curstr += s[i]
            if curstr not in hashmap:
                dfs(i+1)
                hashmap[curstr] = i
                last = curstr
                curstr = ""
                dfs(i+1)
                curstr = last
                hashmap.pop(curstr)
            else:
                dfs(i+1)
            curstr = curstr[0:curstr.__len__()-1]
            return

        dfs(0)
        return m

print(Solution().maxUniqueSplit("addbsd"))