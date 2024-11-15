class Solution:
    
    def isLengthEven(self, head):
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return True if count%2==0 else False
        
        
