# Day 20: Valid Palindrome (LeetCode 125)

## Code Understanding
**Approach of code:**
- Put `start` at index 0 and `end` at the last index.
- Run `while start < end`. When the pointers meet or cross, every pair has been checked.
- Inside the loop, exactly one of 4 cases happens:
  - Left char is not alnum: skip it, `start += 1` only.
  - Right char is not alnum: skip it, `end -= 1` only.
  - Both are alnum but differ after `.lower()`: `return False` immediately.
  - Both are alnum and match: move both pointers inward.
- If the loop ends without a mismatch, `return True`.

## Dry Run Takeaway
Skip and compare must be separate cases. A skip moves only one pointer, and comparing happens only when both chars are valid.

`"a."`
- `L=0 ('a')`, `R=1 ('.')`: R is not alnum, so `R=0`
- `start < end` is false, so the loop stops
- Return `True`

`"race a car"`
- `r` vs `r`: match, move both
- `a` vs `a`: match, move both
- `c` vs `c`: match, move both
- `e` vs `' '`: R is a space, so skip R
- `e` vs `a`: mismatch, return `False`

## Pattern
**Two Pointers (opposite ends)**: same pattern as Squares of a Sorted Array.

## Complexity
- **Time:** O(n), each character is visited at most once.
- **Space:** O(1), no extra string is built.

## Things to remember
- Use `while`/separate cases for skipping, not a single `if`. Two symbols in a row would otherwise get compared.
- Don't compare right after a skip. The new character might still be invalid.
- Use `while start < end` instead of a fixed `for` loop. `end = len(s) - 1` makes the stop condition easy to check.
- Mismatch must `return False`. Without it, the loop keeps running and the answer is wrong.
- Don't forget the final `return True`.
- Compare with `.lower()`, otherwise `'A'` and `'a'` look different.
- `" "` is already handled by `not isalnum()`, no extra `== " "` check needed.

## Edge Cases
- `" "` → `True`
- `".,"` → `True`
- `"a."` → `True`
- `"race a car"` → `False`
- `"0P"` → `False`
- `"A man, a plan, a canal: Panama"` → `True`