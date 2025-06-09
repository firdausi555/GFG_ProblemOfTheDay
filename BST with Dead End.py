class Solution:
    def isDeadEnd(self, root):
        def helper(node, min_val, max_val):
            if not node:
                return False  

            if min_val == max_val:
                return True  # dead end

            l = helper(node.left, min_val, node.data - 1)
            r = helper(node.right, node.data + 1, max_val)

            return l or r

        return helper(root, 1, float('inf'))
