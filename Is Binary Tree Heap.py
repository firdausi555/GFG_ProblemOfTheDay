from collections import deque

class Solution:
    # Your Function Should return True/False
    def isHeap(self, root):
        if not root:
            return True

        queue = deque([root])
        null_seen = False

        while queue:
            node = queue.popleft()

            # Left child check
            if node.left:
                if null_seen or node.left.data > node.data:
                    return False
                queue.append(node.left)
            else:
                null_seen = True

            # Right child check
            if node.right:
                if null_seen or node.right.data > node.data:
                    return False
                queue.append(node.right)
            else:
                null_seen = True

        return True
