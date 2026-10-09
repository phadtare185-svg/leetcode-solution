class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign of x
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the integer
        rev = 0
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
            
        # Apply original sign
        rev *= sign
        
        # Check for 32-bit signed integer overflow limits
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
            
        return rev