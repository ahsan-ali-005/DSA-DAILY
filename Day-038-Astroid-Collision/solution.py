class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                diff = ast + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    ast = 0
                else:
                    ast = 0
                    stack.pop()
            if ast:
                stack.append(ast)
        
        return stack

ob = Solution()
print(ob.asteroidCollision([10,2,-5]))

# Output
# [10]