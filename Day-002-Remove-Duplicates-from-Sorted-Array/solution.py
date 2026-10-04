class Solution(object):
    def removeDuplicates(self, nums):

        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l

ob = Solution()
print(ob.removeDuplicates([1,2,2,3,3,4,5]))

# Output
# 5