class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        d = {}

        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for j in t:
            if j not in d or d[j] == 0:
                return False
            else:
                d[j]-=1
        return True

ob = Solution()
print(ob.isAnagram('abc','cba'))

# Output
# True