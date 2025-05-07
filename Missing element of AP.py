class Solution:
    def findMissing(self, arr):
        n = len(arr)
        d = min(arr[i+1] - arr[i] for i in range(n - 1))
        for i in range(n - 1):
            if arr[i+1] - arr[i] != d:
                return arr[i] + d
        
        return arr[-1] + d
