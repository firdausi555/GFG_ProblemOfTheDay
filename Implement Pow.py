class Solution:
    def power(self, b: float, e: int) -> float:
        if e == 0:
            return 1.0  # Base case: any number raised to the power 0 is 1
        
        if e < 0:
            b = 1 / b  # Convert negative exponent to positive by taking reciprocal
            e = -e
        
        half = self.power(b, e // 2)
        
        if e % 2 == 0:
            return half * half  # If exponent is even
        else:
            return half * half * b  # If exponent is odd
