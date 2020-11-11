from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []

        n = len(points)
        dist = []
        for i in points:
            dist.append(i[0]*i[0] + i[1]*i[1])

        def partition(l, r):
            base = dist[l]
            basepoint = points[l]
            while (l < r):
                while l < r and dist[r] > base:
                    r -= 1
                dist[l] = dist[r]
                points[l] = points[r]
                while l < r and dist[l] <= base:
                    l += 1
                dist[r] = dist[l]
                points[r] = points[l]

            dist[l] = base
            points[l] = basepoint
            return l       

        k = -1
        l = 0
        r = n - 1
        while k != K - 1:
            if k < K:
                l = k + 1
            else:
                r = k - 1
            k = partition(l, r)

        return points[:K]