class Solution(object):
    def majorityElement(self, nums):
        res = 0
        count = 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if res == n else -1)
        return res

ob = Solution()
print(ob.majorityElement([1,2,2,3,4,5,2,2]))

# Output
# 2