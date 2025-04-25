class Solution:
    def majorityElement(self, arr):
        freq = {}
        n = len(arr)
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > n // 2:
                return num
        
        return -1
