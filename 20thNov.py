from collections import Counter
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        ans=[]
        counter=Counter(arr)
        for i,j in counter.items():
            if j >len(arr)//3:
                ans.append(i)
        return sorted(ans)
