# Day 03: Move Zeroes (LeetCode 283)

## Code Understanding / Approach of code: (thinking when code)
- Use two pointers: `r` (next write position) and `l` (read position).
- Both start at index 0. `l` goes from index 0 to the end and visits every element once.
- If `nums[l]` is non-zero: swap `nums[l]` with `nums[r]`, then move `r` forward by one.
- If `nums[l]` is zero: do nothing and let `l` move on.
- `r` always points to the first zero (or to the current element where the non-zero value should be swapped).
- No second loop is needed to fill zeros. The swaps push them to the end automatically.

## Dry Run Takeaway
Nothing is shifted one by one. When `l` finds a non-zero, it simply trades places with the element at `r`, so no value is lost and the order of non-zero values stays the same.
Example: `[0,1,0,3]` ends as `[1,3,0,0]`.
- `l=0` (zero): skip, `r=0`
- `l=1` (1): swap index 1 and 0 → `[1,0,0,3]`, `r=1`
- `l=2` (zero): skip, `r=1`
- `l=3` (3): swap index 3 and 1 → `[1,3,0,0]`, `r=2`
While `l` is ahead of `r`, `r` sits on a zero. That gap is what makes the swap useful.

## Pattern
**Two Pointers (read/write, same direction)**: one pointer reads every element, the other marks where the next valid element goes in the same array.
Same pattern as Remove Duplicates from Sorted Array because we have to do in-place modification of the list.

## Complexity
- **Time:** O(n), since `l` visits each element once. A swap is O(1), so it does not make the solution O(n²).
- **Space:** O(1), since no extra array is used.

## Things to remember
- My first thinking was only about the zero case (`if nums[i] == 0`). Better to think about the opposite case: what do I want to KEEP (`!= 0`)? Write the condition for the kept values, and the rest ends up behind automatically.
- Only copying (`nums[r] = nums[l]`) is not enough. `[0,1,0,2,3]` became `[1,2,3,2,3]` because the zeros were never written back.
- Copy + `nums[l] = 0` is a bug when `l == r`. It erases the value just written (`[1,0,1,0,2,3,0,5]` failed). A real swap fixes it: `nums[r], nums[l] = nums[l], nums[r]`.
- Complexity comes from loops, not from a swap. One pass + O(1) swap = O(n), not bubble sort O(n²).


## Edge Cases
- One element: `[0]` → `[0]`
- All zeros: `[0,0,0]` → `[0,0,0]`
- No zeros: `[1,2,3]` → `[1,2,3]`
- Zeros only at the start: `[0,0,1,4]` → `[1,4,0,0]`
- Zeros only at the end: `[1,2,0,0]` → `[1,2,0,0]`