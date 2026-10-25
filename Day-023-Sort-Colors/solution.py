class Solution(object):
    def sortColors(self, nums):

        counts = [0,0,0]
        for n in nums:
            counts[n] += 1
        
        r,w,b = counts
        nums[:r] = [0] * r
        nums[r:r+w] = [1] * w
        nums[r+w:] = [2] * b

        return nums

ob = Solution()
print(ob.sortColors([2,1,1,0,2,0]))

# Output
# [0, 0, 1, 1, 2, 2]