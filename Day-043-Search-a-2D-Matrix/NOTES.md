# Day 43: Search a 2D Matrix (LeetCode 74)

## Code Understanding
**Approach of code:**
- Rows are sorted and each row starts after the previous row ends, so the matrix behaves like one sorted list
- Step 1: binary search on rows (`top`, `bot`) to find the one row that could hold the target
  - `target > row[-1]` → target is below, so `top = mid_row + 1`
  - `target < row[0]` → target is above, so `bot = mid_row - 1`
  - otherwise the target lies inside this row, so `break`
- If `top > bot` after the loop, no row can hold the target → return `False`
- Step 2: normal binary search inside that row (`left`, `right`)
- Found → `True`, loop ends without a match → `False`

## Dry Run Takeaway
Use the row's first and last element to decide the row, then search only inside that row.

Example: `target = 16` on `[[1,3,5,7],[10,11,16,20],[23,30,34,60]]`
- `top = 0`, `bot = 2` → `mid_row = 1`
- `16 > 20`? No. `16 < 10`? No → this is the row, `break`
- `left = 0`, `right = 3` → `mid = 1`, value `11 < 16` → `left = 2`
- `mid = 2`, value `16` → found, return `True`

## Pattern
**Binary Search (2D Matrix: first rows, then columns)**
- Same pattern as Binary Search (704) and Search Insert Position (35)
- Alternative: treat the matrix as a flat array of size `m * n` with `row = i // cols` and `col = i % cols`

## Complexity
- **Time:** O(log m + log n) = O(log(m * n)), one binary search over rows and one over columns
- **Space:** O(1), only a few pointers

## Things to remember
- After the row loop, check `top <= bot`. If it fails, the target fits no row, so return `False` immediately
- Compare the target with `row[-1]` and `row[0]` to pick the row, not with the middle element
- `row = (top + bot) // 2` is valid only because the loop broke on a matching row

## Edge Cases
- `[[1]], target = 1` → `True`
- `[[1]], target = 2` → `False`
- target smaller than `matrix[0][0]` → `False`
- target larger than the last element of the matrix → `False`
- target between two rows, e.g. `13` in the sample matrix → `False`