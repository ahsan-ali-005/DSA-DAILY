from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        k = len(p)
        pCount = Counter(p)
        window = Counter(s[:k])
        result = []

        if window == pCount:
            result.append(0)

        for i in range(k, len(s)):
            window[s[i]] += 1
            left = s[i - k]
            window[left] -= 1
            if window == pCount:
                result.append(i - k + 1)

        return result

ob = Solution()
print(ob.findAnagrams("abccabbd","acb"))

# Output
# [0,3] 