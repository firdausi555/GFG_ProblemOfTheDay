
class Solution:
    def countDistinct(self, arr, k):
        res=[]
        n=len(arr)
        if n==1:
            return [1]
        i=0
        j=k-1
        while j<n:
            if j<=n:
                res.append(len(set(arr[i:j+1])))
                j+=1
                i+=1
            else:
                res.append(len(set(arr[i:])))
                break
        return res
            
