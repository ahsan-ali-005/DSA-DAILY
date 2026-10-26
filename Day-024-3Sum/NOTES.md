# Day 20: 3Sum (LeetCode 15)

## Code Understanding
**Approach of code: (thinking when code)**
- Sort the array first, so duplicates sit together and Two Pointers works
- Fix one number `v` at index `i`, then find two numbers on its right that sum to `-v`
- `start = i + 1`, `end = last index`; check `v + nums[start] + nums[end]`
  - sum > 0 → sum is too big, move `end` left
  - sum < 0 → sum is too small, move `start` right
  - sum == 0 → save the triplet
- Skip duplicates in two places so the same triplet isn't added twice:
  - for `i`: `if i > 0 and nums[i-1] == v: continue`
  - for `start`: after a match, move `start` forward, then keep skipping while it equals the previous value

## Dry Run Takeaway
Sorting turns "find 3 numbers" into "fix one, then do Two Sum with two pointers". Duplicate skipping is part of the algorithm, not an extra.

`[-2,0,0,2,2]`
- `i=0` (-2): `start=1` (0), `end=4` (2), sum = 0 → add `[-2,0,2]`
- `start += 1` lands on the second 0, same as before → skip → `start=3`
- `start=3` (2), `end=4` (2), sum = 2 > 0 → `end -= 1`, loop ends
- `i=1` (0) and the rest find nothing; `i=2` is skipped as a duplicate
- Result: `[[-2,0,2]]`

## Pattern
**Sorting + Two Pointers (opposite ends)**, same pattern as Valid Palindrome and Squares of a Sorted Array, with a fixed outer element and duplicate skipping.

## Complexity
- **Time:** O(n²), outer loop is n and the two-pointer scan is n each time (sorting is only O(n log n))
- **Space:** O(1) extra, ignoring the output list (and the sort)

## Things to remember
- I didn't understand why to skip duplicates after a match: without it, the same triplet gets added again
- After a match I only move `start`; `end` fixes itself through the `>` and `<` checks

## Edge Cases
- `[0,0,0]` → `[[0,0,0]]`
- `[0,1,1]` → `[]`
- `[-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]`
- `[0,0,0,0]` → `[[0,0,0]]`