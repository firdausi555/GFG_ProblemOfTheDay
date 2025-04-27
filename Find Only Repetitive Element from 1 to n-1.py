from collections import Counter
class Solution:
    def findDuplicate(self, arr):
        return [i for i, j in Counter(arr).items() if j==2][0]
