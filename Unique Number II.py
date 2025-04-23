from collections import Counter 
class Solution:
	def singleNum(self, arr):
	    counter=Counter(sorted(arr))
	    ans=[]
	    for i in counter.items():
	        if i[1]==1:
	            ans.append(i[0])
        return ans 
    
