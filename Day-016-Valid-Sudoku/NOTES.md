# Day 16: Valid Sudoku (LeetCode 36)

## Code Understanding
**Approach of code: (thinking when code)**
- Need to check 3 rules: no repeat in a row, a column, or a 3x3 box
- Make 3 groups of sets: `rows` (9 sets), `cols` (9 sets), `boxes` (9 sets)
- Loop over every cell `(r, c)`; skip if it is `"."`
- Find the box of the cell: `(r // 3) * 3 + (c // 3)` (or tuple key `(r // 3, c // 3)`)
- If the digit is already in its row set, column set, or box set → return `False`
- Otherwise add the digit to all 3 sets
- If the loop finishes without any repeat → return `True`

## Dry Run Takeaway
Same "have I seen this before?" check as Contains Duplicate, just done in 3 places at once. Box number is the only new idea.

- Cell `(0, 0)` → `0 // 3 = 0`, `0 // 3 = 0` → `0 * 3 + 0` = box 0
- Cell `(4, 7)` → `4 // 3 = 1`, `7 // 3 = 2` → `1 * 3 + 2` = box 5
- Cell `(8, 8)` → `2 * 3 + 2` = box 8
- Example 2: `"8"` at `(0, 0)` goes in box 0; later `"8"` at `(2, 2)` is also box 0 → already in `boxes[0]` → `False`

## Pattern
**Hash Set (Seen Tracking)**, same pattern as Contains Duplicate.
One set per group (row / column / box) and check before adding.

## Complexity
- **Time: O(1)**, board is always 9 x 9 = 81 cells (O(n²) for an n x n board)
- **Space: O(1)**, always 27 sets with at most 9 digits each (O(n²) for an n x n board)

## Things to remember
- Box formula: `(r // 3) * 3 + (c // 3)`. The `* 3` is there because each box-row has 3 boxes, so numbers don't collide (`r//3 + c//3` gives the same number for different boxes)
- Easier option: use the tuple key `(r // 3, c // 3)` with `defaultdict(set)`, no formula needed (needs `import collections`)
- Check the digit **before** adding it to the sets
- Skip `"."` cells with `continue`
- It only validates filled cells, it does not solve the Sudoku

## Edge Cases
- All cells `"."` → `True`
- Same digit twice in one row → `False`
- Same digit twice in one column → `False`
- Same digit twice in one 3x3 box (different row and column) → `False`