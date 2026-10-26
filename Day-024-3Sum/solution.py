class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i,v in enumerate(nums):
            if i > 0 and nums[i-1] == v:
                continue

            start = i + 1
            end = len(nums) - 1
            while start < end:
                if v + nums[start] + nums[end] > 0:
                    end -= 1
                elif v + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    res.append([v, nums[start], nums[end]])
                    start += 1
                    while nums[start] == nums[start-1] and start < end:
                        start += 1
        return res

ob = Solution()
print(ob.threeSum([-1,0,1,2,-1,-4]))

# Output
# [[-1, -1, 2], [-1, 0, 1]]