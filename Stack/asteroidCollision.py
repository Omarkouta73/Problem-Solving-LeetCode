from collections import deque

class Solution:
    def asteroidCollision(self, asteroids):
        # [8,-8]
        stack = deque()
        for a in asteroids:
            if len(stack) == 0:
                stack.append(a)
                continue
            if stack[-1] > 0:
                if a > 0:
                    stack.append(a)
                else:
                    survived = True
                    while stack and stack[-1] > 0:
                        if abs(a) > stack[-1]:
                            stack.pop()
                        elif abs(a) == stack[-1]:
                            stack.pop()
                            survived = False
                            break
                        else:
                            survived = False
                            break
                    if survived:
                        stack.append(a)
                    
            else:
                stack.append(a)
                
        return list(stack)

sol = Solution()
print(sol.asteroidCollision([8,-8]))