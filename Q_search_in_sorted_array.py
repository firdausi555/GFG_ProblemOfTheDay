class Solution:
    def search(self,arr,key):
        # Complete this function
        for i in range(len(arr)):
            if arr[i]==key:
                return i
        return -1
