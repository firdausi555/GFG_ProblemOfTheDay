class Solution:
    def segregate(self, head):
        count = [0, 0, 0]
        current = head
        while current:
            count[current.data] += 1
            current = current.next
        
        current = head
        i = 0
        while current:
            if count[i] == 0:
                i += 1
            else:
                current.data = i
                count[i] -= 1
                current = current.next
        
        return head
