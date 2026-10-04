# Day 02: Remove Duplicates from Sorted Array (LeetCode 26)

## Code Understanding / Approach of code: (thinking when code)
- Use two pointers: `left` (next write position) and `right` (read position).
- `left` starts at 1 because the first element is always unique and already in place, so the next unique value goes at index 1.
- `right` also goes from index 1 to the end.
- If `nums[right]` is different from `nums[right-1]`, it's a new unique value: write it at `nums[left]`, then move `left` forward by one.
- If `nums[right]` is the same as `nums[right-1]`, it's a duplicate: do nothing and let `right` move on.
- At the end, return `left`. It is already the count of unique values.

## Dry Run Takeaway
Nothing is removed or shifted. `right` only reads, and `left` only marks where the next unique value gets overwritten. Duplicates are simply skipped, and the slots after `k` don't matter (LeetCode shows them as `_`).
Example: `[1,2,2,3,3,4,5]` ends as `[1,2,3,4,5,4,5]` with `left = 5`. Only the first 5 slots count.

## Pattern
**Two Pointers (left/right, same direction)**, also called read/write pointers: one pointer reads every element, the other writes the elements in the same array.
Use it when the question says "in place", "sorted", or "keep only some elements".

## Complexity
- **Time:** O(n), since `right` visits each element once.
- **Space:** O(1), since no extra array is used.

## Things to remember
- "Removing" in place really means overwriting. I don't need to delete anything.
- My first attempt used one pointer and only detected duplicates. The problem needs two jobs (reading and writing), so it needs two pointers.
- Compare `nums[right]` with `nums[right-1]` (the previous element).
- `left` is only incremented when a unique value found making it exactly equal to the number of unique values in the array.


## Edge Cases
- One element: `[1]` → `k = 1`
- All identical: `[2,2,2]` → `k = 1`
- No duplicates: `[1,2,3]` → `k = 3`
- Duplicates only at the end: `[1,2,3,3]` → `k = 3`