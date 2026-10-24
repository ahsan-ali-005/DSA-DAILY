class Solution(object):
    def twoSum(self, numbers, target):
        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                return [start+1, end+1]

ob = Solution()
print(ob.twoSum([1,2,2,3], 3))

# Output
# [1, 3]