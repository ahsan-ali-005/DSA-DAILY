class NumArray(object):
    
    def __init__(self, nums):
        self.nums = nums
        self.prefix = []
        cur = 0
        for n in self.nums:
            cur+=n
            self.prefix.append(cur)
            
    def sumRange(self, left, right):
        leftSum = self.prefix[left - 1] if left > 0 else 0
        rightSum = self.prefix[right]
        return rightSum - leftSum

ob = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = ob.sumRange(2,4)
print(param_1)

# Output
# 0