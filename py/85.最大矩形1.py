class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left = [0 for _ in range(heights.__len__())]
        maxs = 0
        for i in range(0, heights.__len__()):
            while (stack.__len__() != 0 and heights[stack[-1]] > heights[i]):
                curh = stack.pop()
                maxs = max((i - (left[curh] + 1)) * heights[curh], maxs)

            if stack.__len__() == 0:
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)

        while(stack.__len__() != 0):
            curh = stack.pop()
            maxs = max(
                (heights.__len__() - (left[curh] + 1)) * heights[curh], maxs)

        return maxs

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = matrix.__len__()
        if m == 0:
            return 0
        n = matrix[0].__len__()
        height = [[0]*n for _ in range(m)]
        for j in range(0, n):
            height[0][j] = ord(matrix[0][j]) - ord('0')
            for i in range(1, m):
                height[i][j] = height[i-1][j] + 1 if matrix[i][j] == '1' else 0
        
        maxs = 0
        for lines in height:
            maxs = max(maxs, self.largestRectangleArea(lines))

        return maxs