class Solution(object):
    def moveZeroes(self, nums):

        r = 0
        for l in range(len(nums)):
            if nums[l]:
                nums[r], nums[l] = nums[l], nums[r]
                r+=1
        return nums

ob = Solution()
print(ob.moveZeroes([0,1,2,0,3]))

# Output
# [1,2,3,0,0]
