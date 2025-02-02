"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
class Solution:
    def levelOrder(self, root):
        # Your code here
        if not root:
            return []
        
        lvl = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            temp = []
            
            for _ in range(level_size):
                node = queue.popleft()
                temp.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            lvl.append(temp)
        
        return lvl
