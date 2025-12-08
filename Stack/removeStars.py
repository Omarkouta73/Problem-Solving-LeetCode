from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        # Input: s = "leet**cod*e"
        # Output: "lecoe"
        stack = deque()
        for x in s:
            if x != '*':
                stack.append(x)
            else:
                stack.pop()

        return "".join(stack)
    



sol = Solution()
print(sol.removeStars("leet**cod*e"))
