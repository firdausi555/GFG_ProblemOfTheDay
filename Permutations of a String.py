from itertools import permutations

class Solution:
    def findPermutation(self, s):
        # Generate all permutations using itertools.permutations
        all_permutations = permutations(s)
        
        # Use a set to ensure unique permutations
        unique_permutations = set(all_permutations)
        
        # Convert each tuple back to a string
        result = [''.join(p) for p in unique_permutations]
        
        # Return the result in any order
        return result
