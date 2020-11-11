class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        def dis(x, y):
            if x > y:
                x, y = y, x
            return min(y - x, x + n - y) + 1

        now_set = [0]  
        res = [0]    
        for c in key:
            new_set = []    
            new_res = []    
            m = len(now_set)

            for i in range(n):
                if ring[i] == c:
                    new_set.append(i)
                    new_res.append(float('inf'))
                    for j in range(m):
                        new_res[-1] = min(new_res[-1], res[j] + dis(i, now_set[j]))
            
            now_set = new_set
            res = new_res
        return min(res)