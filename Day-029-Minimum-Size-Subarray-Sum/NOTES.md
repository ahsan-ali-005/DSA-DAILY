# Day 29: Minimum Size Subarray Sum (LeetCode 209)

## Code Understanding
**Approach of code: (thinking when code)**
- Keep a window `[left ... right]` and a running sum `cur`.
- Move `right` forward one step at a time and add `nums[right]` to `cur` (grow).
- While `cur >= target`, the window is valid: record `right - left + 1` in `best`.
- Then remove `nums[left]` from `cur` and move `left` forward (shrink), and check again.
- `best` starts as `inf`. If it is still `inf` at the end, return `0`.

## Dry Run Takeaway
Record the length **while shrinking**, because the window is valid at that moment. Shrink in a `while` loop because the window can still be valid after removing one number.

`target = 7`, `nums = [2,3,1,2,4,3]`
- right=0..2: cur = 2, 5, 6 → not valid yet
- right=3: cur = 8 → valid, best = 4 → remove 2 → cur = 6, left = 1
- right=4: cur = 10 → valid, best = 4 → remove 3 → cur = 7, valid, best = 3 → remove 1 → cur = 6, left = 3
- right=5: cur = 9 → valid, best = 3 → remove 2 → cur = 7, valid, best = 2 → remove 4 → cur = 3, left = 5
- Answer: 2 (`[4,3]`)

## Pattern
**Sliding Window (variable size)**: grow `right` until the condition is true, then shrink `left` while it stays true. Same shape as Longest Substring Without Repeating Characters, but there the length is recorded after shrinking, and here it is recorded during shrinking.

## Complexity
- **Time: O(n)**, because `left` and `right` each move at most n times in total.
- **Space: O(1)**, because only a few variables are used.

## Things to remember
- Use `while`, not `if`, for shrinking.
- Record `best` inside the shrink loop, before removing `nums[left]`.
- Start `best` as `inf` so "no valid window" can return `0`.
- This only works because all numbers are **positive**. With negatives, shrinking does not always reduce the sum, so use Prefix Sum + Hash Map instead (like Subarray Sum Equals K).
- (Add your own mistakes from your blind rewrite here.)

## Edge Cases
- `target = 4, nums = [1,4,4]` → `1`
- `target = 11, nums = [1,1,1,1,1,1,1,1]` → `0`
- `target = 5, nums = [5]` → `1`
- `target = 100, nums = [1,2,3]` → `0`