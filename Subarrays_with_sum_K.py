class Solution:
    def countSubarrays(self, arr, k):
        prefix_sum_count = {0: 1}  
        prefix_sum = 0  
        count = 0  

        for num in arr:
            prefix_sum += num  
            
            if prefix_sum - k in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]
            
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

        return count
