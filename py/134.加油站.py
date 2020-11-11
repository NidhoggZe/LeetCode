from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rest = 0
        currest = 0    
        curstart = 0    
        for i in range(len(gas)):
            rest += gas[i] - cost[i]
            currest += gas[i] - cost[i]
            if currest < 0:
                currest = 0
                curstart = i + 1
        
        if rest < 0:
            return -1
        else:
            return curstart