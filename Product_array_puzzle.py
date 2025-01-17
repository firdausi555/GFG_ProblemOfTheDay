class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        
        res = [1] * n
        
        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= arr[i]
        # print(res)
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= arr[i]
        
        return res
