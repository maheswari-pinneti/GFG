class Solution:
    def powMod(self, x, n, M):
        ans = 1
        while n:
            if n & 1: ans = ans * x % M
            x = x * x % M; n >>= 1
        return ans

