# Day 15: Subarray Sum Equals K (LeetCode 560)

## Code Understanding

Approach of code: (thinking when code)

- A subarray sum is `prefix[end] - prefix[start-1]`, and I want it to be `k`
- So at each index I only need to find `prefix[end] - k` among earlier prefixes
- No prefix array needed: one running variable `prefix` is enough
- Hash map `seen` stores `prefix value -> how many times seen`, because the same prefix can repeat and each repeat is a different subarray
- Start with `seen = {0: 1}` so subarrays starting at index 0 are counted
- For each number: update `prefix` -> check `prefix - k` in `seen` (add its count to `count`) -> store current `prefix` in `seen`

## Dry Run Takeaway

Each step asks one question: "Have I seen `prefix - k` before?". We are storing prefix in hashmap.

`nums = [1, 2, 3]`, `k = 3`

- start: `prefix = 0`, `seen = {0: 1}`
- `1`: prefix = 1, need -2 -> not seen, store 1
- `2`: prefix = 3, need 0 -> seen once, `count = 1` (`[1, 2]`), store 3
- `3`: prefix = 6, need 3 -> seen once, `count = 2` (`[3]`), store 6
- Answer: 2

## Pattern

**Prefix Sum + Hash Map**

Same prefix idea as Range Sum Query - Immutable (Day 10), but there I used a stored prefix array to get a range sum, here I look up an earlier prefix in a hash map.

## Complexity

- **Time:** O(n), one pass, each map lookup and insert is O(1)
- **Space:** O(n), the map can hold up to n different prefixes

## Things to remember

- Check first, then store. Storing first gives wrong answers when `k = 0`
- The map stores the prefixes I have **seen**. `prefix - k` is only what I look up
- Keep a separate `count` variable for the answer. The numbers inside the map are not the answer
- Map must start with `{0: 1}`, otherwise `[3]` (a subarray from index 0) is missed
- Store counts, not just "seen or not", because one prefix can appear many times

## Edge Cases

- `nums = [1, 1, 1], k = 2` → `2`
- `nums = [3], k = 3` → `1` (needs `{0: 1}`)
- `nums = [0, 0, 0], k = 0` → `6` (repeated prefixes, count them all)
- `nums = [1, -1, 0], k = 0` → `3` (negative numbers work, so sliding window will not)