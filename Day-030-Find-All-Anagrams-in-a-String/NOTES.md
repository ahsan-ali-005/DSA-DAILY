# Day 30: Find All Anagrams in a String (LeetCode 438)

## Code Understanding
**Approach of code: (thinking when code)**
- Anagram means same letters with same counts, so compare letter counts, not order.
- Count the letters of `p` once (`pCount`).
- Every anagram has length `k = len(p)`, so use a fixed-size window of length `k` over `s`.
- Count the first window `s[:k]`; if it equals `pCount`, index 0 is an answer.
- Slide one step at a time: the letter at `s[i]` enters, the letter at `s[i - k]` leaves.
- Update only these two counts, then compare `window == pCount`; if equal, the start index is `i - k + 1`.
- If `len(p) > len(s)`, no window can exist, so return `[]`.

## Dry Run Takeaway
Never recount the whole window. When it slides, only two letters change: one enters, one leaves.

`s = "cbaebabacd"`, `p = "abc"`, `k = 3`
- First window `"cba"` → counts match → add index 0
- i = 3: `e` enters, `c` leaves → `"bae"` → no match
- i = 4: `b` enters, `b` leaves → `"aeb"` → no match
- ...
- i = 8: `c` enters, `e`... window becomes `"bac"` → match → add index `8 - 3 + 1 = 6`
- Result: `[0, 6]`

## Pattern
**Fixed-size Sliding Window + Frequency Counting (Hash Map)**
- Add the entering item, remove the leaving item, compare.
- Related to Longest Substring Without Repeating Characters and Minimum Size Subarray Sum, but those use a variable-size window; here the size is always `k`.

## Complexity
- **Time:** O(n), where n = `len(s)`. Each step does O(1) work (two count updates plus a compare over at most 26 letters).
- **Space:** O(1). At most 26 lowercase letters in each `Counter`.

## Things to remember
- `Counter` returns `0` for a missing key, so `window[s[i]] += 1` works even when the letter is new (a normal `dict` would give `KeyError`).
- Leaving letter: `window[left] -= 1` can leave a `0` count in the Counter.
- On Python 3.10+, `Counter == Counter` ignores zero counts, so `del window[left]` is not needed on LeetCode. On Python 3.9 or older, zero counts break `==`, so delete the key when it reaches 0.
- Start index of a window ending at `i` is `i - k + 1`.
- Check the first window separately before the loop starts from `i = k`.

## Edge Cases
- `s = "ab"`, `p = "abc"` → `[]` (p longer than s)
- `s = "abab"`, `p = "ab"` → `[0, 1, 2]` (overlapping anagrams)
- `s = "a"`, `p = "a"` → `[0]`
- `s = "aaaa"`, `p = "b"` → `[]` (no match anywhere)