from bisect import bisect_right

class Solution:
    def countLessEq(self, a, b):
        b.sort()  # Sort b[] once
        ans = []
        for x in a:
            count = bisect_right(b, x)  # Count of elements <= x
            ans.append(count)
        return ans
