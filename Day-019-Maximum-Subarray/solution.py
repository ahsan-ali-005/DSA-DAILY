class Solution(object):
    def maxSubArray(self, nums):
        cur = best = nums[0]
        for n in nums[1:]:
            cur = max(n, cur + n)
            best = max(best, cur)
        return best

ob = Solution()
print(ob.maxSubArray([1,2,3,-3,4,-4,5]))

# Output
# 8