class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        right = ['[', '{', '(']
        for c in s:
            if c in right:
                lst.append(c)
            elif lst:
                if c == ']':
                    if lst[-1] == '[':
                        lst.pop()
                    else:
                        return False
                elif c == '}':
                    if lst[-1] == '{':
                        lst.pop()
                    else:
                        return False
                else:
                    if lst[-1] == '(':
                        lst.pop()
                    else:
                        return False
            else:
                return False
        if lst:
            return False
        else:
            return True

print(Solution().isValid("()"))