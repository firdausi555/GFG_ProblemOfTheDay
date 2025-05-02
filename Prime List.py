class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def is_prime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def nearest_prime(self, n):
        if n <= 1:
            return 2
        
        left = n
        right = n

        while True:
            if self.is_prime(left):
                return left
            if self.is_prime(right):
                return right
            left -= 1
            right += 1

    def primeList(self, head):
        current = head
        while current:
            current.val = self.nearest_prime(current.val)
            current = current.next
        return head
