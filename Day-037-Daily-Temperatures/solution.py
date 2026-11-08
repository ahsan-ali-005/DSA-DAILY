class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                ans[stackIndex] = i - stackIndex

            stack.append([t, i])
        return ans

ob = Solution()
print(ob.dailyTemperatures([20,30,35,70,32]))

# Output
# [1,1,1,0,0]