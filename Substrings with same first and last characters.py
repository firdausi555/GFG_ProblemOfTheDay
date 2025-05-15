
from collections import Counter 
class Solution:
	def countSubstring(self, s):
	    ans=0
	    c=Counter(s)
        for i in c.values():
            ans+=i*(i+1)//2
	    return ans 
