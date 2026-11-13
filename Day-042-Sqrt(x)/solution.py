class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = 0

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid > x:
                right = mid - 1

            elif mid * mid < x:
                left = mid + 1
                res = mid

            else:
                return mid

        return res

ob = Solution()
print(ob.mySqrt(8))

# Output
# 2