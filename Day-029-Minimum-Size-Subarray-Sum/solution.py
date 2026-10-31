class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        cur = 0
        best = float("inf")

        for right in range(len(nums)):
            cur += nums[right]

            while cur >= target:
                best = min(best, right - left + 1)
                cur -= nums[left]
                left += 1

        return 0 if best == float("inf") else best

ob = Solution()
print(ob.minSubArrayLen(7,[2,3,1,2,4,3]))

# Output
# 2