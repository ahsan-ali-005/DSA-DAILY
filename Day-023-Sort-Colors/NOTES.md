# Day 19: Sort Colors (LeetCode 75)

## Code Understanding
**Approach of code: (thinking when code)**
- Array has only 0, 1, 2, so I don't need to compare elements, only count them
- Pass 1: count how many 0s, 1s, 2s into `counts = [r, w, b]`
- Pass 2: overwrite the array in place: first `r` slots get 0, next `w` get 1, the rest get 2
- Slice assignment (`nums[a:b] = [...]`) changes the same list, so nothing is returned

## Dry Run Takeaway
Only 3 possible values, so counting replaces sorting.

`[2,0,2,1,1,0]`
- Count: 0 appears 2 times, 1 appears 2 times, 2 appears 2 times, so `counts = [2,2,2]`
- `nums[0:2] = [0,0]`
- `nums[2:4] = [1,1]`
- `nums[4:] = [2,2]`
- Result: `[0,0,1,1,2,2]`

## Pattern
**Counting Sort (Frequency Counting)**, same idea as Ransom Note: count first, then use the counts.

## Complexity
- **Time:** O(n), two passes
- **Space:** O(1) for the 3 counters (the slice assignment makes temporary lists, so strictly O(n) in practice)

## Things to remember
- Counting only works because the values come from a tiny fixed set.
- The r and r+w is set to start because they are first excluded because the last index is not added its excluded.

## Edge Cases
- `[0]` → `[0]`
- `[2,2,2]` → `[2,2,2]`
- `[1,0]` → `[0,1]`
- `[2,1,0]` → `[0,1,2]`