class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        counter = {}
        for i in magazine:
            if i in counter:
                counter[i] +=1
            else:
                counter[i] = 1

        for j in ransomNote:
            if j not in counter:
                return False
            elif counter[j] == 0:
                return False
            else:
                counter[j] -= 1
        return True

ob = Solution()
print(ob.canConstruct("ab", "acbd"))

# Output
# True