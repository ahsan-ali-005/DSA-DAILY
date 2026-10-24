# Day 22: Two Sum II - Input Array Is Sorted (LeetCode 167)

## Code Understanding

**Approach of code: (thinking when code)**

- Array is already sorted, so no hash map is needed (constant space required)
- Put `start` at index 0 and `end` at the last index
- Check `numbers[start] + numbers[end]` against `target`
- Sum too big → move `end` left to make the sum smaller
- Sum too small → move `start` right to make the sum bigger
- Sum equal → return `[start + 1, end + 1]` (answer is 1-indexed, code stays 0-indexed)
- `while start < end` keeps both pointers on different indexes

## Dry Run Takeaway

Sorted order tells which pointer to move, so one pass is enough and no pair needs to be checked twice.

`numbers = [2, 3, 4]`, `target = 6`
- `start=0, end=2`: 2 + 4 = 6 → match
- Return `[0+1, 2+1]` = `[1, 3]`

`numbers = [1, 2, 2, 3]`, `target = 3`
- `start=0, end=3`: 1 + 3 = 4 → too big, `end` moves to 2
- `start=0, end=2`: 1 + 2 = 3 → match, return `[1, 3]`

## Pattern

**Two Pointers (opposite ends)** — same pattern as Squares of a Sorted Array and Valid Palindrome.

## Complexity

- **Time:** O(n), each step moves one pointer inward, so the pointers meet after at most n steps
- **Space:** O(1), only two pointer variables

## Things to remember

- Keep the code 0-indexed, add 1 only in the return
- "Can't use the same element twice" means the same index, not the same value; `[2, 2, 3]` with target 4 is valid
- `start < end` (not `<=`) guarantees the two pointers never sit on the same index
- Compute the sum once and store it (`current = numbers[start] + numbers[end]`) instead of writing it twice
- Sorted array + pair/sum → think opposite-end pointers before a hash map

## Edge Cases

- `[2, 7, 11, 15], 9` → `[1, 2]`
- `[2, 3, 4], 6` → `[1, 3]`
- `[-1, 0], -1` → `[1, 2]` (smallest array, negative numbers)
- `[1, 2, 2, 3], 3` → `[1, 3]`
- `[2, 2, 3], 4` → `[1, 2]` (same value at two different indexes)