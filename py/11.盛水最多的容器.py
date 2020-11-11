#双指针见笔记

class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        i = 0
        j = height.__len__() - 1
        while (i < j):
            s = (j - i) * min(height[i], height[j])
            m = max(m, s)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m