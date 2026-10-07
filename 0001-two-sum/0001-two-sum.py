class Solution:
    def twoSum(self, nums, target):
        hash_map = {}

        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [hash_map[target - nums[i]], i]

            hash_map[nums[i]] = i


nums = [2,5,7,9,11]
target = 20
ob = Solution()
print(ob.twoSum(nums,target))

# Output
# [3,4]