# Day 05: Majority Element (LeetCode 169)

## Code Understanding

**Approach of code:**
- I don't count the frequency of every element. I only track one `res` (candidate) and one `count` (its lead).
- If `count == 0`, take the current number as the new `res`.
- Then if the current number equals `res`, `count += 1`. Otherwise `count -= 1`.
- Different numbers cancel each other out. The majority element appears more than n/2 times, so the others can't cancel it fully. It is the one left at the end.

## Dry Run Takeaway

A candidate can change in the middle, but the majority element always comes back and wins in the end.

Example: `[2,2,1,1,1,2,2]`
- 2 → res=2, count=1
- 2 → count=2
- 1 → count=1
- 1 → count=0
- 1 → count was 0, so res=1, count=1
- 2 → count=0
- 2 → count was 0, so res=2, count=1
- Final `res = 2`

## Pattern

**Boyer-Moore Voting (Cancel Out).**
Trigger: "more than n/2" or "majority".

## Complexity

- **Time: O(n)**, one pass over the array.
- **Space: O(1)**, only `res` and `count`.

## Things to remember

- My first thought was to count the frequency of every element (hash map). That is O(n) space. For O(1) space I only need to track one suspect.
- `count == 0` means the old candidate is fully cancelled, so pick a new one.
- The starting value `res = 0` doesn't matter, because the first element overwrites it.
- This only works because the problem guarantees a majority element exists.

## Edge Cases

- `[3]` → `3`
- `[3,3,4]` → `3`
- `[2,2,1,1,1,2,2]` → `2`