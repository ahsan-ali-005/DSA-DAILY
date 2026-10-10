class Solution(object):
    def sortedSquares(self, nums):
        nums = [i*i for i in nums]
        l = 0
        r = len(nums) - 1
        result = []

        while l<=r:
            if nums[l] > nums[r]:
                result.append(nums[l])
                l += 1
            else:
                result.append(nums[r])
                r -= 1
        
        return result[::-1]

ob = Solution()
print(ob.sortedSquares([-3,-2,0,2,3]))

# Output
# [0,4,4,9,9]