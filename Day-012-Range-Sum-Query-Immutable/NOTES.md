# Day 10: Range Sum Query - Immutable (LeetCode 303)

## Code Understanding / Approach of code: (thinking when code)
- Array never changes, but `sumRange` is called many times, so do the work once in `__init__`
- Build a `prefix` array: `prefix[i]` = running total from index 0 up to index i
- For a query, take everything up to `right`, then cut off everything before `left`
- `sumRange(left, right) = prefix[right] - prefix[left - 1]`
- If `left == 0`, nothing exists before it, so subtract 0

## Dry Run Takeaway
Prefix sum turns "add many elements" into "one subtraction".

`nums = [-2, 0, 3, -5, 2, -1]` → `prefix = [-2, -2, 1, -4, -2, -3]`

- `sumRange(0, 2)`: left is 0, so answer is `prefix[2]` = 1
- `sumRange(2, 5)`: `prefix[5] - prefix[1]` = -3 - (-2) = -1
- Check by hand: 3 + (-5) + 2 + (-1) = -1 ✓

## Pattern
**Prefix Sum**
Precompute running totals once so every range query is O(1).

## Complexity
- **Time:** `__init__` is O(n) (one pass to build prefix); each `sumRange` is O(1) (one subtraction). For k queries, total is **O(n + k)**, where n is the array size and k is the number of `sumRange` calls. Brute force would be **O(n * k)**, since each query can add up to n elements.
- **Space:** O(n) for the prefix array

## Things to remember
- Whenever a formula has `i - 1`, ask: "what happens at i = 0?"
- `prefix[-1]` in Python does not crash, it returns the last element, which gives a wrong answer silently. That is why the `left > 0` check is needed
- `right` can never be out of range because of the constraint `0 <= left <= right < nums.length`

## Edge Cases
- `sumRange(0, 0)` on `[-2]` → `-2`
- `left = 0` → `prefix[right]` (no subtraction)
- `left == right` (single element), `sumRange(3, 3)` on the example → `-5`
- Whole array, `sumRange(0, 5)` on the example → `-3`