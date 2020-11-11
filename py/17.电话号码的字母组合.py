class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = digits.__len__()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []
        if digits == "":
            return []
        def dfs(p,curstr):
            if p == l-1:
                for i in phoneMap[digits[p]]:
                    ans.append(curstr+i)
                return
            for i in phoneMap[digits[p]]:
                dfs(p+1, curstr+i)
            return
        dfs(0, "")
        return ans
                
            

             
