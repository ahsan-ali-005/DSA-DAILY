class Solution:
    def longestCommonPrefix(self, strs):

        res = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i ==  len(word) or word[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

ob = Solution()
ans = ob.longestCommonPrefix(["flower", "flight", "floor"])
print(ans)