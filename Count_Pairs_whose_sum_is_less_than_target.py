class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        arr.sort()
        count = 0
        left, right = 0, len(arr) - 1
        
        while left < right:
            current_sum = arr[left] + arr[right]
            
            if current_sum < target:
                count += (right - left)
                left += 1
            else:
                right -= 1
                
        return count
