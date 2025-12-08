from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        # "3[a]2[bc]"
        # 3[a2[c]]
        stack = deque()
        # [3,[,a,]
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k)*substr)
        return "".join(stack)


sol = Solution()
sol.decodeString("3[a2[c]]") # accaccacc


        