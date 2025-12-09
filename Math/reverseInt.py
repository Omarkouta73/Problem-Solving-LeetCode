class Solution:
    def reverse(self, x: int) -> int:
        v = 0

        is_neg = x < 0
        if is_neg:
            x = abs(x)

        while x != 0:
            last_digit = x % 10
            if v > ((2**31 - 1) - last_digit) // 10:
                return 0
            v = v * 10 + last_digit
            x //= 10

        if is_neg:
            v*=-1
        
        
        return v

sol = Solution()
print(sol.reverse(1463847412))
