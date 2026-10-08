# Day 06: Is Subsequence (LeetCode 392)

## Code Understanding / Approach of code:
- Loop over `t` (the bigger string), because every character of `t` needs to be seen at most once.
- Keep a pointer `i` on `s`. It means "how many characters of `s` are matched so far".
- If `s[i] == j`, that character is found in order, so move `i` forward.
- If it doesn't match, do nothing. The loop itself moves to the next character of `t`.
- Guard `i < len(s)` before reading `s[i]`, so it never goes out of range.
- After the loop, `i == len(s)` means all of `s` was found in order.

## Dry Run Takeaway
`i` only moves on a match, and the answer is decided by where `i` ends up.

`s = "abc"`, `t = "ahbgdc"`:
- `a` matches `s[0]`, so `i = 1`
- `h` doesn't match `b`, so `i` stays 1
- `b` matches, so `i = 2`
- `g`, `d` don't match `c`, so `i` stays 2
- `c` matches, so `i = 3`
- `i == len(s)`, so `True`

## Pattern
**Two Pointers (one pointer per string)**

## Complexity
- **Time:** O(n), where n = `len(t)`, because each character of `t` is visited once.
- **Space:** O(1), because only one extra variable `i` is used.

## Things to remember
- Loop runs on `t`, but the index `i` belongs to `s`. When the loop and the index belong to different things, the index can go out of range.
- My first version read `s[i]` without a guard. Once `i` reached `len(s)` and `t` still had characters left, it would crash.
- At first I wasn't sure `for j in t` was right. It is, because the loop variable is already the current character of `t`, so no separate `j` counter is needed.
- Checklist for every `arr[i]`: where does `i` start, when does it move, can it reach `len(arr)`, where does the guard go?

## Edge Cases
- `s = "abc", t = "ahbgdc"` → `True`
- `s = "axc", t = "ahbgdc"` → `False`
- `s = "", t = "abc"` → `True` (nothing to match)
- `s = "abc", t = "abcz"` → `True` (extra characters after `i` is done need the guard)
- `s` longer than `t` → `False`