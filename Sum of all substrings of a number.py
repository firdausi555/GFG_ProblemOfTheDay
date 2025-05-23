class Solution:
    def sumSubstrings(self, s):
        n = len(s)
        # mod = 10**9 + 7  # In case of larger constraints
        total = 0
        prev = 0

        for i in range(n):
            num = int(s[i])
            curr = (prev * 10 + num * (i + 1)) 
            total = (total + curr) 
            prev = curr
    return total
