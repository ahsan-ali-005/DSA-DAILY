# Day 44: Find First and Last Position of Element in Sorted Array (LeetCode 34)

## Code Understanding
**Approach of code: (thinking when code)**
- Array is sorted and O(log n) is required, so use binary search.
- Normal binary search returns when it finds the target. Here the target can repeat, so finding it is not enough.
- Need the left edge and the right edge of the block of targets, so run the search twice.
- One helper `find(first)` does both. When `nums[mid] == target`, save `res = mid` and keep searching.
  - `first = True`: `right = mid - 1` (look for an earlier target)
  - `first = False`: `left = mid + 1` (look for a later target)
- If `nums[mid] < target`: `left = mid + 1`. If `nums[mid] > target`: `right = mid - 1`.
- `res` starts at `-1`, so a missing target gives `[-1, -1]` automatically.
- Return `[find(True), find(False)]`.

## Dry Run Takeaway
Finding the target is not the end of the search, it is just a candidate answer. Save it and keep shrinking toward the edge.

`nums = [5, 7, 7, 8, 8, 10]`, `target = 8`, first = True
- `left=0, right=5, mid=2` → `7 < 8` → `left = 3`
- `left=3, right=5, mid=4` → `8` found → `res = 4`, `right = 3`
- `left=3, right=3, mid=3` → `8` found → `res = 3`, `right = 2`
- `left > right` → stop, return `3`
- Same steps with first = False give `4`, so the answer is `[3, 4]`.

## Pattern
**Binary Search (boundary search)**
- Same family as Binary Search (704) and Search Insert Position (35), but here we do not stop at the first match.
- Save the answer on a match, then keep shrinking one side.

## Complexity
- **Time: O(log n)**, two binary searches, each halves the search space.
- **Space: O(1)**, only a few variables.

## Things to remember
- Do not `return mid` when found. Save it in `res` and keep searching.
- The only difference between first and last is one line: `right = mid - 1` or `left = mid + 1`.
- Use `mid = left + (right - left) // 2`.
- `res = -1` at the start handles the "not found" case.

## Edge Cases
- `nums = [], target = 0` → `[-1, -1]`
- `nums = [5,7,7,8,8,10], target = 6` → `[-1, -1]`
- `nums = [1], target = 1` → `[0, 0]`
- `nums = [2,2,2,2], target = 2` → `[0, 3]`
- `nums = [1,2,3], target = 4` → `[-1, -1]`