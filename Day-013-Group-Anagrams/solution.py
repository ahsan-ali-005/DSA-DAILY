class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in d:
                d[sorted_i].append(i)
            else:
                d[sorted_i] = [i]

        return [value for key, value in d.items()]

ob = Solution()
print(ob.groupAnagrams(['bat','tab','ant','tan']))

# Output
# [['bat', 'tab'], ['ant', 'tan']]