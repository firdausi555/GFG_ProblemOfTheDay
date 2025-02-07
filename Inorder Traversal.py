class Solution:
    def inOrder(self, root):
        if root is None:
            return []
        
        ans = []
        ans += self.inOrder(root.left)  # Collect left subtree
        ans.append(root.data)           # Visit current node
        ans += self.inOrder(root.right) # Collect right subtree
        return ans
