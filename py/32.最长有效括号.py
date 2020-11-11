class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        maxlen = 0
        for i in range(0, s.__len__()):
            if s[i] == "(" or stack or s[stack[-1]] == ")":
                stack.append(i)
            else:
                stack.pop()
                maxlen = max(maxlen, i-(stack[-1] if stack else -1))

        return maxlen


print(Solution().longestValidParentheses(")()())()()"))
