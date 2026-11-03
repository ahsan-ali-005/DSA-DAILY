# Day 32: Longest Repeating Character Replacement (LeetCode 424)

## Code Understanding
**Approach of code: (thinking when code)**
- Look for the longest window where all letters can become one letter using at most `k` replacements
- In a window, keep the most frequent letter and replace all the others
- Replacements needed = window size - count of the most frequent letter
- Window is valid if `(r - l + 1) - max(counts) <= k`
- Expand `r` every step and add `s[r]` to `counts`
- If the window is invalid, shrink from the left: `counts[s[l]] -= 1`, `l += 1`, until it is valid again
- After the window is valid, update `longest` with the window size
- Return `longest`

## Dry Run Takeaway
The window is valid when only `k` letters (or fewer) are not the most frequent letter.

`s = "ABAB"`, `k = 2`
- r=0: A, window `A`, size 1, max 1, replacements 0, valid, longest = 1
- r=1: B, window `AB`, size 2, max 1, replacements 1, valid, longest = 2
- r=2: A, window `ABA`, size 3, max 2, replacements 1, valid, longest = 3
- r=3: B, window `ABAB`, size 4, max 2, replacements 2, valid, longest = 4

## Pattern
**Variable-size Sliding Window + Frequency Count**
- Same shrinking idea as Longest Substring Without Repeating Characters (shrink with `while` when the window is invalid)
- Same frequency array idea as Permutation in String

## Complexity
- **Time:** O(n), each pointer moves at most n times. `max(counts)` looks at 26 values, which is constant work (about O(26n))
- **Space:** O(1), `counts` is always size 26

## Things to remember
- Window size - max count = how many letters must be replaced
- Use `while` to shrink, not `if`, so the window is valid before updating `longest`
- `ord(ch) - 65` works because letters are uppercase (`'A'` = 65). For lowercase it would be `ord('a')`
- The window never needs to know which letter is the most frequent, only how many times it appears
- Each time a letter leaves, decrease its count in `counts`

## Edge Cases
- `s = "A"`, `k = 0` → `1`
- `s = "AAAA"`, `k = 0` → `4`
- `s = "ABAB"`, `k = 0` → `1`
- `s = "ABAB"`, `k = 2` → `4`
- `k >= len(s)` → `len(s)` (whole string can be changed)