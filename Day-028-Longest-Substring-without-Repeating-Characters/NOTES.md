# Day 28: Longest Substring Without Repeating Characters (LeetCode 3)

## Code Understanding
**Approach of code:**
- Keep a window `[l, r]` that always has unique characters.
- `charSet` stores the characters currently inside the window, so the "is it already here?" check is O(1).
- Move `r` forward one character at a time.
- If `s[r]` is already in `charSet`, the window is broken. Remove `s[l]` from the set and do `l += 1`, and repeat until `s[r]` is no longer in the set (`while`, not `if`).
- Add `s[r]` to the set.
- Window length is `r - l + 1`. Update `longest` with `max`.

## Dry Run Takeaway
The best window can start anywhere, not only at index 0. On a duplicate, shrink from the left instead of stopping.

`s = "acnbcdf"`
- `r=0..3`: window grows to `acnb`, length 4
- `r=4`: `c` is a duplicate, remove `a`, then remove `c`, window becomes `nbc`
- `r=5`: add `d`, window `nbcd`, length 4
- `r=6`: add `f`, window `nbcdf`, length 5 → best = 5

## Pattern
**Sliding Window (variable size) + Set**

Template:
```
for r in range(len(s)):
    while window is invalid:
        shrink from left (l += 1)
    update answer
```
Same two-pointer movement idea as Best Time to Buy and Sell Stock (`l` and `r` only move forward), but here the window shrinks until it is valid.

## Complexity
- **Time:** O(n). `l` and `r` each move forward at most n times.
- **Space:** O(min(n, alphabet size)), because the set holds only the characters inside the window.

## Things to remember
- My first code only checked the substring starting from index 0. The answer can start anywhere.
- Use `while`, not `if`, when shrinking, because more than one removal may be needed.
- Add `s[r]` to the set only after the duplicates are removed.
- A substring must be continuous (`"pwke"` from `"pwwkew"` is a subsequence, not a substring).

## Edge Cases
- `"" → 0`
- `"a" → 1`
- `"bbbbb" → 1`
- `"abcabcbb" → 3`
- `"pwwkew" → 3`
- `"acnbcdf" → 5`