class Solution:
    def arrangeCoins(self, n: int) -> int:
        h=0
        i=0
        while i <= n:
            if n == 0:
                return n
            else:
                i += 1
                h += i
                if h == n:
                    return i
                elif n-h < i+1:
                    return i
