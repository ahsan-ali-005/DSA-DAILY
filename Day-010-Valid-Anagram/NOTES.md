# Day 10: Valid Anagram (LeetCode 242)

## Code Understanding
**Approach of code:**
- If `len(s) != len(t)`, return `False` right away, because the letter counts can't match.
- Build a dictionary `d` for `s`: if the letter is already in `d`, add 1 to its count; otherwise add it with count 1.
- Loop over `t`: if a letter is not in `d`, or its count is already 0, return `False`.
- Otherwise reduce that letter's count by 1.
- If the loop finishes without returning, return `True`.

## Dry Run Takeaway
One dictionary is enough: count up for `s`, then count down for `t`. Any letter that is missing or already at 0 means `False`.

`s = "rat"`, `t = "car"`:
- Lengths are equal (3 and 3), so continue.
- Counter: `{r:1, a:1, t:1}`
- `t` gives `c`, which is not in `d`, so return `False`.

## Pattern
**Frequency Counting (Hash Map)**
Same pattern as Ransom Note (Day 07). Both ask "do I have enough of each letter?" and use a count dictionary.

## Complexity
- **Time:** O(n), because each string is looped over only once.
- **Space:** O(k), where k is the number of unique letters. For lowercase letters this is at most 26, so it is effectively O(1).

## Things to remember
- Check `i in d` (the dictionary), not `i in s`. `i` always comes from `s`, so `i in s` is always True and gives a `KeyError`.
- Add the length check first. Without it, `s = "ab"`, `t = "a"` wrongly returns `True`, because the leftover `b` is never noticed.
- The "count down" loop only checks that every letter of `t` is available in `s`. The length check is what makes sure nothing is left over in `s`.

## Edge Cases
- `s = "anagram", t = "nagaram"` → `True`
- `s = "rat", t = "car"` → `False`
- `s = "ab", t = "a"` → `False` (different lengths)
- `s = "a", t = "a"` → `True`
- `s = "a", t = "b"` → `False`