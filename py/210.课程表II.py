from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pres = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            pres[pre[0]].append(pre[1])

        need = [False] * numCourses
        learned = [False] * numCourses
        order = []
        def dfs(curcourse: int):
            nonlocal order, need, learned, pres
            for i in pres[curcourse]:
                if not learned[i]:
                    if need[i]:
                        return False
                    need[i] = True
                    if not dfs(i):
                        return False
                    need[i] = False
            learned[curcourse] = True
            order.append(curcourse)
            return True



        for i in range(numCourses):
            if not learned[i]:
                if not dfs(i):
                    return []
        
        return order

Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])