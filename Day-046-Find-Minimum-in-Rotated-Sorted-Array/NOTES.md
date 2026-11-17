# Day 46: Find Minimum in Rotated Sorted Array (LeetCode 153)

## Code Understanding
**Approach of code: (thinking when code)**
- The array is two sorted parts joined together, and the minimum is where the second part starts.
- Keep `l`, `r` pointers and a `res` that stores the smallest value seen so far.
- If `nums[l] < nums[r]`, the current window is already sorted, so `nums[l]` is its minimum. Update `res` and `break`.
- Otherwise find `mid` and update `res` with `nums[mid]`.
- If `nums[mid] >= nums[l]`, `mid` is in the left sorted part, so the minimum is on the right: `l = mid + 1`.
- Else `mid` is in the right sorted part, so the minimum is on the left: `r = mid - 1`.

## Dry Run Takeaway
Compare `mid` with a boundary to find which half is sorted. The minimum is never in the sorted half (unless it's the window's start), so discard that half.

`[4,5,6,7,0,1,2]`
- `l=0, r=6`: `4 < 2`? No, so not sorted. `mid=3`, value `7`, `res=4`.
- `7 >= 4`, so the left part is sorted and the minimum is on the right: `l = 4`.
- `l=4, r=6`: `0 < 2`? Yes, the window is sorted. `res = min(4, 0) = 0`, break.
- Answer: `0`

## Pattern
**Binary Search on a partially sorted array**
Same pattern as Binary Search and Search Insert Position, but here you search for a drop point instead of a target.

## Complexity
- **Time:** O(log n), because the search space halves every step.
- **Space:** O(1), because only `l`, `r`, `mid`, `res` are used.

## Things to remember
- Recording every `mid` into `res` before discarding it means `mid` can never be lost, so `r = mid - 1` is safe.
- `nums[l] < nums[r]` is the shortcut for "this window is already sorted", which also handles an array that was not rotated.
- Use `>=` in `nums[mid] >= nums[l]` so the case `mid == l` (two-element window) moves `l` forward.

## Edge Cases
- `[1]` → `1`
- `[2,1]` → `1`
- `[1,2,3,4,5]` (not rotated) → `1`
- `[11,13,15,17]` → `11`