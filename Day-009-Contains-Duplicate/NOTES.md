# Day 09: Contains Duplicate (LeetCode 217)

## Code Understanding
**Approach of code:**
- Create an empty set `s` to remember the numbers already seen.
- Loop through `nums` from left to right.
- If the current number is already in `s`, a duplicate exists, so return `True` immediately.
- Otherwise, add the number to `s` and move on.
- If the loop finishes without finding a repeat, return `False`.

## Dry Run Takeaway
The set works like a memory: before adding a number, ask "have I seen this before?" If yes, stop right there.

Example: `nums = [1, 2, 3, 1]`
- 1 → not in set → add → `{1}`
- 2 → not in set → add → `{1, 2}`
- 3 → not in set → add → `{1, 2, 3}`
- 1 → already in set → return `True`

## Pattern
**Hash Set** ("have I seen this before?")

Same idea of remembering what was seen as in Ransom Note, but there I needed counts (hash map), here only presence matters, so a set is enough.

## Complexity
- **Time: O(n)**, each number is visited once and set lookup/insert takes about O(1).
- **Space: O(n)**, in the worst case (all unique) the set stores every number.

## Things to remember
- `s = {}` creates a **dict**, not a set, so `s.add()` fails. Use `s = set()`.
- Set = only "is it present?"; Hash Map = key + extra info (count or index).

## Edge Cases
- `[1]` → `False` (single element, nothing to repeat)
- `[1, 1]` → `True`
- `[1, 2, 3, 4]` → `False`
- `[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]` → `True` (stops at the first repeat)