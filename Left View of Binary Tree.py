class Solution:
    def LeftView(self, root):
        # code here
        stack=[]
        def fn(node,level):
            if node==None:
                return

            if len(stack)==level:
                stack.append(node.data)

            fn(node.left,level+1)
            fn(node.right,level+1)
        
        fn(root,0)
        return stack
