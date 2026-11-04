# Day 33: Minimum Window Substring (LeetCode 76)

## Code Understanding
**Approach of code: (thinking when code)**
- `need = Counter(t)` stores how many of each character the window must have.
- `missing = len(t)` counts how many needed characters are still absent. The window is valid only when `missing == 0`, so the check is O(1).
- Move `r` across `s` (expand): if `need[ch] > 0`, this character was needed, so `missing -= 1`. Then always do `need[ch] -= 1`.
- While `missing == 0` (shrink): save the window if it is smaller than `best_len`.
- Remove `s[l]` by doing `need[s[l]] += 1`. If it becomes `> 0`, a needed character was lost, so `missing += 1`. Then `l += 1`.
- At the end, return `""` if `best_len` is still `inf`, otherwise return `s[best_start:best_start + best_len]`.

## Dry Run Takeaway
`need` going negative means "extra copies in the window", so removing those characters never breaks the window. Only a positive `need` after removal means the window became invalid.

`s = "ADOBECODEBANC"`, `t = "ABC"`:
- `need = {A:1, B:1, C:1}`, `missing = 3`
- r = 0 (A): needed, so `missing = 2`
- r = 1 (D): `need[D]` is 0, so it is not needed. `missing` stays 2, `need[D]` becomes -1
- r = 2 (O): same as D, `need[O]` becomes -1
- r = 3 (B): `missing = 1`
- r = 4 (E): extra, `need[E]` becomes -1
- r = 5 (C): `missing = 0`, window `ADOBEC` is valid, `best_len = 6`
- Shrink: remove A, `need[A]` becomes 1, which is `> 0`, so `missing = 1` and the window is invalid. Stop shrinking
- Later the window `BANC` is found with size 4, so `best_len = 4`

## Pattern
**Sliding Window (variable size) + Frequency Count**
Expand until valid, then shrink while valid. Same pattern as Longest Substring Without Repeating Characters and Minimum Size Subarray Sum.

## Complexity
- **Time: O(m + n)**, because `l` and `r` each move at most m steps, and building `need` costs n.
- **Space: O(1)**, because the Counter holds at most 52 distinct letters.

## Things to remember
- `Counter` returns 0 for a missing key instead of a KeyError, so `need['D']` is 0 and then becomes -1 after `-= 1`.
- Negative `need` means the window has extra copies, and positive means it still needs more.
- `inf` in `best_len` means "no valid window yet". The first valid window always beats it, and at the end it tells me to return `""`.
- Always do `need[ch] -= 1`, even for characters not in `t`. Only `missing` depends on the `> 0` check.
- Check `need[s[l]] > 0` after adding back, not before.

## Edge Cases
- `s = "a", t = "a"` → `"a"`
- `s = "a", t = "aa"` → `""`
- `s = "A", t = "B"` → `""`
- `s = "AA", t = "AA"` → `"AA"`
- `t` longer than `s` → `""`