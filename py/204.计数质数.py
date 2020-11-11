

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        arr = [False] * n
        primes = []
        for i in range(2, n):
            if not arr[i]:
                arr[i] = True
                primes.append(i)
                count += 1
            for prime in primes:
                if prime * i > n - 1:
                    break
                arr[prime * i] = True
                if i % prime == 0:
                    break
        
        return count

Solution().countPrimes(100)