class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def find(first):
            left, right, res = 0, len(nums) - 1, -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    res = mid
                    if first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res

        return [find(True), find(False)]

ob = Solution()
print(ob.searchRange([5,7,7,7,8], 8))

# Output
# [4,4]