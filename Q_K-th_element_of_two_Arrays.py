class Solution:

    def kthElement(self, a, b, k):
        return(sorted(a+b)[k-1])
