class Solution(object):
  def longestConsecutive(self, nums):
    s = set(nums)
    longest = 0

    for n in s:
      if n - 1 not in s:
        next_num = n + 1
        length = 1
        
        while next_num in s:
          length+=1
          next_num+=1
        longest = max(longest,length)

    return longest

ob = Solution()
print(ob.longestConsecutive([1,2,3,5,4,100,200]))

# Output
# 5