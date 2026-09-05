class Solution:
    def sumOfSeries(self, n, a, b):
        MOD = 10**9 + 7
        import math
        s = lambda k: k * (k + 1) // 2
        l = a // math.gcd(a, b) * b
        return (a*s(n//a) + b*s(n//b) - l*s(n//l)) % MOD