Second Largest
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Solution:
____________________________________________________________________
class Solution:
    def getSecondLargest(self, arr):
        return -1 if len(set(arr))==1 else sorted(set(arr))[-2]
      
