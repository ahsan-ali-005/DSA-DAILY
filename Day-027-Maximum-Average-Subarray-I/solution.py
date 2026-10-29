class Solution(object):
    def findMaxAverage(self, nums, k):
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[i]
        
        max_avg = cur_sum / k

        for i in range(k, len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            avg = cur_sum / k
            max_avg = max(avg, max_avg)

        return max_avg

ob = Solution()
print(ob.findMaxAverage([1,12,-5,-6,50,3], 4))

# Output
# 12.75