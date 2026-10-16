class Solution(object):
    def topKFrequent(self, nums, k):
        frequency = {}
        result = []
        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for number, count in frequency.items():
            bucket[count].append(number)

        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result

ob = Solution()
print(ob.topKFrequent([1,1,1,2,2,3],3))

# Output
# [1,2,3]