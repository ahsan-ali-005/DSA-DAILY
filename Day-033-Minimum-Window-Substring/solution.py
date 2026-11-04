from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        l = 0
        best_start, best_len = 0, float("inf")

        for r, ch in enumerate(s):

            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                if r - l + 1 < best_len:
                    best_start, best_len = l, r - l + 1

                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]

ob = Solution()
print(ob.minWindow("ADOBECODEBANC", "ABC"))

# Output
# BANC