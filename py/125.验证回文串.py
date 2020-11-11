class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = s.__len__() - 1
        while (i < j):
            while i < j and not ('0' <= s[i] <= '9' or 'a' <= s[i] <= 'z'):
                i += 1
            while i < j and not ('0' <= s[j] <= '9' or 'a' <= s[j] <= 'z'):
                j -= 1
            if i < j and s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        
        return True

Solution().isPalindrome("A man, a plan, a canal: Panama")