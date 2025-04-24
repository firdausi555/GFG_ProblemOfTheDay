from collections import Counter

class Solution:
    def getSingle(self, arr):
        return [i[0] for i in Counter(arr).items() if i[1] == 1][0]
