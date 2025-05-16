class Solution:
	def sortArray(self, arr, A, B, C):
	    
	    return sorted([A*(i*i)+B*(i)+C for i in arr])
