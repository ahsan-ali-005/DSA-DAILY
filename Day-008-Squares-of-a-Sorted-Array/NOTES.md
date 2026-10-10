# Day 08: Squares of a Sorted Array (LeetCode 977)

## Code Understanding
Approach of code: (thinking when code)
- Ask: "Where is the biggest square?" It is always at the left end or the right end, because the array is sorted and negatives become big positives.
- Square every number first.
- Put `l` at the first index and `r` at the last index.
- Compare `nums[l]` and `nums[r]`, and append the bigger one to `result`.
- Move only the winning pointer inward: `l += 1` if left won, `r -= 1` if right won.
- Repeat while `l <= r`.
- `result` was built from largest to smallest, so return `result[::-1]`.

## Dry Run Takeaway
The two ends compete, the bigger square wins, and only the winner moves. By Appending new value goes to end so reverse the list while returning.

`nums = [-4,-1,0,3,10]` → squared `[16,1,0,9,100]`
- 16 vs 100 → right wins → `[100]`, `r` moves left
- 16 vs 9 → left wins → `[100,16]`, `l` moves right
- 1 vs 9 → right wins → `[100,16,9]`
- 1 vs 0 → left wins → `[100,16,9,1]`
- 0 vs 0 → tie, right wins → `[100,16,9,1,0]`
- reverse → `[0,1,9,16,100]`

## Pattern
**Two Pointers (opposite ends)**
- Use it when the array is sorted and the answer depends on the extremes (both ends).
- Compare the two ends, use the winner, and move only that pointer.

## Complexity
- **Time:** O(n), because each element is squared once, visited once by a pointer, and reversed once.
- **Space:** O(n), for the squared list and the result.

## Things to remember
- Pointers are **indices**, not values. `r = len(nums) - 1`, not `nums[-1]`.
- A pointer moves **only when its element is used**.
- Use `while l <= r`, not `for`, because a `for` loop moves by itself.
- `r` moves **inward**, so `r -= 1`. I wrote `r += 1` by mistake.
- The result comes out largest to smallest, so reverse it at the end.

## Edge Cases
- `nums = [-3,-2,0,2,3]` → `[0,4,4,9,9]` (ties are fine)
- All negatives, e.g. `[-5,-3,-1]` → `[1,9,25]`
- All positives, e.g. `[1,2,3]` → `[1,4,9]`
- Single element, e.g. `[-2]` → `[4]` (loop runs once because `l == r`)