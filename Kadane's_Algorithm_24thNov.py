#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ans=float('-inf')
        temp=0
        for i in range(len(arr)):
            temp+=arr[i]
            if temp>ans:
                ans=temp
            if temp<0:
                temp=0
        return ans
