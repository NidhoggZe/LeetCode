class Solution: #自底向上
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        k = 0
        t = 0
        for k in range(1, K + 1):
            t = 1
            while t <= N and dp[k][t-1] < N:
                dp[k][t] = dp[k-1][t-1] + 1 + dp[k][t-1]
                t += 1
        
        return t - 1

# class Solution: #自顶向下
#     def superEggDrop(self, K: int, N: int) -> int:
#         def get(k, t):
#             if k == 1 and t == 1:
#                 return 1
#             elif (t < 1 or k < 1):
#                 return 0
#             else:
#                 return get(k, t - 1) + 1 + get(k-1, t-1)
        
#         n = 0
#         t = 0
#         while (n < N):
#             t += 1
#             n = get(K, t)

#         return t



Solution().superEggDrop(2,6)
            