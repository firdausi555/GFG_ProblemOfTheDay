'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    def diameter(self, root):
        self.max_diameter = 0  # Variable to store the maximum diameter found

        def height(node):
            if not node:
                return 0  # Base case: height of null node is 0

            left_height = height(node.left)
            right_height = height(node.right)

            # Update the diameter at this node
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Return height of current node
            return 1 + max(left_height, right_height)

        height(root)  # Compute height while updating diameter
        return self.max_diameter  # Return the maximum diameter found
