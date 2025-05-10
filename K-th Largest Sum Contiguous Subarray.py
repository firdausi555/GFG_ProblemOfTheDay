from typing import List


import heapq

class Solution:
    def kthLargest(self, arr, k) -> int:
        min_heap = []
        n = len(arr)
        
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]
                
                if len(min_heap) < k:
                    heapq.heappush(min_heap, curr_sum)
                else:
                    if curr_sum > min_heap[0]:
                        heapq.heappushpop(min_heap, curr_sum)

        return min_heap[0]
