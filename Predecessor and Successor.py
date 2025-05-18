class Solution:
    def findPreSuc(self, root, key):
        pre = None
        suc = None

        def helper(node):
            nonlocal pre, suc
            if not node:
                return

            if node.data == key:
                # Find predecessor (max value in left subtree)
                if node.left:
                    temp = node.left
                    while temp.right:
                        temp = temp.right
                    pre = temp

                # Find successor (min value in right subtree)
                if node.right:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    suc = temp

            elif key < node.data:
                suc = node
                helper(node.left)
            else:
                pre = node
                helper(node.right)

        helper(root)
        return pre, suc
