class Solution(object):
    def validPalindrome(self, s):
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                a = s[start+1: end+1]
                b = s[start:end]
                return a == a[::-1] or b == b[::-1]
            
            start += 1
            end -= 1
        return True

ob = Solution()
print(ob.validPalindrome("abac"))

# Output
# True