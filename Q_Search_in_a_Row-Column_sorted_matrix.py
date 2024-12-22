class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		for i in mat:
		    if x in i:
		        return True
		return False
