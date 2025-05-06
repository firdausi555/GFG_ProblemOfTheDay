
class Solution:
    def Paths(self, root):
        def dfs(node, path, result):
            if not node:
                return
            path.append(node.data)  
            
            # If it's a leaf, add the path to result
            if not node.left and not node.right:
                result.append(list(path))
            else:
                dfs(node.left, path, result)
                dfs(node.right, path, result)
            
            path.pop()  
        
        result = []
        dfs(root, [], result)
        return result
