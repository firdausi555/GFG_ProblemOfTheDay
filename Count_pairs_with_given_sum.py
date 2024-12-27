class Solution:
    def countPairs(self, arr, target):
        count_map = {}
        count = 0
        
        for num in arr:
            complement = target - num  
            
            if complement in count_map:
                count += count_map[complement]
            
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        return count
