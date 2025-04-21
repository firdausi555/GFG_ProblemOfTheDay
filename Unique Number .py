from collections import Counter
class Solution:
    def findUnique(self, arr):
        return [i for i,j in Counter(arr).items() if j==1] [0]
