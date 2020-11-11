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
            maxs = max((heights.__len__() - (left[curh] + 1)) * heights[curh], maxs)
        
        return maxs