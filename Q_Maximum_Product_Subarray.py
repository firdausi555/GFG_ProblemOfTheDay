class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		res=float('-inf')
        pre=1
        suf=1
        for i in range(len(arr)):
            #if we encounter 0 in between we have to initialise the pre and suf to 1
            if pre==0:pre=1
            if suf==0:suf=1

            pre=pre*arr[i]
            suf=suf*arr[len(arr)-i-1]

            res=max(res,max(pre,suf))
        return res
