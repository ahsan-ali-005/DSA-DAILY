# Day 18: Longest Consecutive Sequence (LeetCode 128)

## Code Understanding
**Approach of code: (thinking when code)**
- Put all numbers in a set so "is this number present?" is O(1)
- Loop over every number `n` in the set
- Check `n - 1 not in s`. If true, `n` is the **start** of a sequence
- From a start, walk forward (`n + 1`, `n + 2`, ...) while the next number is in the set, and count the length
- Keep the max length seen and return it

## Dry Run Takeaway
Only count from the start of a sequence. Numbers in the middle are skipped, so no work is repeated.

`nums = [100, 4, 200, 1, 3, 2]` → set = {100, 4, 200, 1, 3, 2}
- `100`: 99 not in set → start. 101 not in set → length 1
- `4`: 3 is in set → middle, skip
- `200`: 199 not in set → start. 201 not in set → length 1
- `1`: 0 not in set → start. 2, 3, 4 in set, 5 not → length 4
- `3`: 2 is in set → skip
- `2`: 1 is in set → skip
- longest = **4**

## Pattern
**Hash Set + Sequence Start Check**
Same hash set idea as Contains Duplicate (fast "have I seen this?" lookup), with an extra check so we only count from the beginning of a sequence.

## Complexity
- **Time:** O(n). The inner `while` only runs from sequence starts, so each number is visited at most twice (once in the `for`, once in a `while`).
- **Space:** O(n). The set stores up to n numbers.

## Things to remember
- Sorting would work but costs O(n log n). The problem asks for O(n), so use a set.
- Loop over the set `s`, not `nums`. It removes duplicates and avoids repeated work.
- The `n - 1 not in s` check is what keeps the solution O(n). Without it, it becomes O(n²).
- Start `length = 1` because the start number itself counts.

## Edge Cases
- `[] → 0`
- `[5] → 1`
- `[1, 1, 1] → 1`
- `[1, 0, 1, 2] → 3`
- `[-1, 0, 1] → 3`
- `[10, 20, 30] → 1`