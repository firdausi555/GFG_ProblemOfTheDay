from collections import Counter
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        counter=Counter(s)
        for i, j in counter.items():
            if j==1:
                return i
        return -1
    
        
