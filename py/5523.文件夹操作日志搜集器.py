from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs:
            if i == "../":
                count -= 1
                count = max(0, count)
            elif i == "./":
                continue
            else:
                count+=1
        return count
