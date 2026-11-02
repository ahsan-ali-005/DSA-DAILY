# Day 31: Permutation in String (LeetCode 567)

## Code Understanding
**Approach of code: (thinking when code)**
- A permutation means same letters with same counts, only the order differs
- So I need a chunk of `s2` with length exactly `len(s1)` and the same letter counts as `s1`
- Count the letters of `s1` into `need` (array of 26)
- Keep a `window` array of 26 for the current chunk of `s2`
- Each step: new letter enters (`+1`)
- If `i >= k`, the window is one letter too big, so the oldest letter `s2[i - k]` leaves (`-1`)
- If `window == need`, return `True`
- If the loop ends with no match, return `False`

## Dry Run Takeaway
Never recount the window. Only update two counters: one enters, one leaves.

`s1 = "ab"`, `s2 = "eidbaooo"`, `k = 2`
- i=0: e enters, window size 1, no match
- i=1: i enters, window `e, i`, no match
- i=2: d enters, e leaves, window `i, d`, no match
- i=3: b enters, i leaves, window `d, b`, no match
- i=4: a enters, d leaves, window `b, a`, counts match, return `True`

## Pattern
**Fixed-size Sliding Window + Frequency Count**
- Frequency counting idea is the same as Ransom Note, but here the counts are of a moving window

## Complexity
- **Time:** O(n), n = `len(s2)`. Comparing two arrays of size 26 is constant work
- **Space:** O(1), arrays are always size 26

## Things to remember
- `ord(ch) - ord('a')` turns a letter into an index (a=0 ... z=25)
- Array vs hashmap: with fixed 26 lowercase letters, use an array. A hashmap keeps keys with count `0` after a letter leaves, which breaks `window == need` unless the key is deleted
- `i >= k` means the window has grown to `k + 1` letters, so the letter at `i - k` must leave
- Window positions after sliding are `i-k+1` to `i`, always `k` letters
- Check `len(s1) > len(s2)` first, then the answer is directly `False`

## Edge Cases
- `s1` longer than `s2` → `False`
- `s1 = "a"`, `s2 = "a"` → `True`
- `s1 = "ab"`, `s2 = "eidboaoo"` → `False` (letters are there but not continuous)
- `s1 = "ab"`, `s2 = "ba"` → `True`