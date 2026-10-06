class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            
ob = Solution()
nums1 = [1, 3, 5, 0, 0]
nums2 = [2,4]
ob.merge(nums1, 3, nums2, 2)


# Output
# [1, 2, 3, 4, 5]