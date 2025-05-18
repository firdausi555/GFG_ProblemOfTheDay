class Solution:
    def findSpiral(self, root):
        if not root:
            return []

        result = []
        q = deque()
        q.append(root)
        level = 0

        while q:
            size = len(q)
            level_nodes = []

            for _ in range(size):
                node = q.popleft()
                level_nodes.append(node.data)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level % 2 == 0:
                result.extend(reversed(level_nodes))
            else:
                result.extend(level_nodes)

            level += 1

        return result
