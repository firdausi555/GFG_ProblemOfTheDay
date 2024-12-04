class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        if len(s1)!=len(s2):
            return False
        # Below approach is throwing time limit exceed error 
        # stack=[]
        # for i in s1:
        #     stack.append(i)
        # for i in range(len(s1)):
        #     stack.insert(0,stack.pop())
        #     if "".join(stack)==s2:
        #         return True
        # return False
        
        return s2 in(s1+s1)
