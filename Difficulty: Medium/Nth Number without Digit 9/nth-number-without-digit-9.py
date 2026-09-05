class Solution:
    def findNth(self, n):
        x = int(n)
        ans = ""
        while x:
            ans = str(x % 9) + ans
            x //= 9
        return ans