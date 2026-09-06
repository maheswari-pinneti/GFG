class Solution:
    def pairAndSum(self, arr):
        ans = 0
        for bit in range(31):
            c = sum(x & (1 << bit) != 0 for x in arr)
            ans += c * (c - 1) // 2 * (1 << bit)
        return ans
        