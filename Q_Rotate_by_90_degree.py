class Solution:
    
    # Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        n = len(mat)
        
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        # Step 2: Reverse the columns (not rows, as this is an anti-clockwise rotation)
        for j in range(n):
            for i in range(n // 2):
                mat[i][j], mat[n - i - 1][j] = mat[n - i - 1][j], mat[i][j]
        return mat
