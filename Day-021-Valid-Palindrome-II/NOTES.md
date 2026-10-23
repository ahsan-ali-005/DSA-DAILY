# Day 21: Valid Palindrome II (LeetCode 680)

## Code Understanding
**Approach of code: (thinking when code)**
- Put `start` at the beginning and `end` at the last index.
- While `start < end`, compare `s[start]` and `s[end]`.
- If they match, move both pointers inward (`start += 1`, `end -= 1`).
- At the first mismatch, the one allowed deletion is used. Two options:
  - Delete the left character: check `s[start+1 : end+1]`
  - Delete the right character: check `s[start : end]`
- Return `True` if either slice is a palindrome, else `False`.
- If the loop ends with no mismatch, return `True`.

## Dry Run Takeaway
At the first mismatch, try both skips. After that, the rest must be a normal palindrome check, since the deletion is already used.

Example: `"abac"`
- `start=0, end=3` → `a` vs `c` → mismatch
- Option A: `s[1:4] = "bac"` → not a palindrome
- Option B: `s[0:3] = "aba"` → palindrome
- Return `True`

## Pattern
**Two Pointers (opposite ends) + one mistake allowed**
Same pattern as Valid Palindrome. The new idea is branching into two options at the first mismatch.

## Complexity
- **Time:** O(n), the pointers walk the string once and the mismatch is handled only once.
- **Space:** O(n), because slicing creates new strings. It can be O(1) with an `is_pal(l, r)` helper that uses indexes only.

## Things to remember
- At a mismatch I only wanted to check one option. Both options (left skip and right skip) must be checked, joined with `or`.
- Don't modify `start` before checking both options, or the original value is lost.
- Slice end is exclusive, so the range from `start+1` to `end` is `s[start+1 : end+1]`.
- Reverse a slice with `slice[::-1]`, not `s[start::-1]`.
- Move the pointers on a match, otherwise it is an infinite loop.
- Add `return True` after the loop.

## Edge Cases
- `"aba"` → `True` (already a palindrome)
- `"abca"` → `True` (delete `c` or `b`)
- `"abc"` → `False` (one deletion is not enough)
- `"a"` → `True` (single character)
- `"ab"` → `True` (delete either character)