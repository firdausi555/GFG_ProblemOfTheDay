class Solution:

	def findMaximum(self, arr):
		# code here
		for i in range(1,len(arr)):
		    if arr[i]>arr[i-1]:
		        continue
		    else:
		        return arr[i-1]
        return arr[-1]
