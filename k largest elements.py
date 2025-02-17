class Solution:
	def kLargest(self, arr, k):
		# Your code here

        arr=sorted(arr,reverse=True)
        temp=0
        ans=[]
        for i in arr:
            if temp<k:
                ans.append(i)
                temp+=1
        return ans 
