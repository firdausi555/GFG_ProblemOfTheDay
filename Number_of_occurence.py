from collections import Counter
class Solution:
    def countFreq(self, arr, target):
        #code here
        count=0
        counter=Counter(arr)
        for i , j in counter.items():
            if i==target:
                return j
        return 0
