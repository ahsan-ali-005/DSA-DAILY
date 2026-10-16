# Day 12: Top K Frequent Elements (LeetCode 347)

## Code Understanding
**Approach of code:**
- Count how many times each number appears using a hashmap (`number -> count`).
- Make `n + 1` buckets (list of lists). Bucket index = count, so `bucket[3]` holds all numbers that appear 3 times.
- Loop over the hashmap and append each `number` into `bucket[count]`.
- Walk the buckets from the last index down to 1 (highest count first).
- Add numbers to `result` one by one, and return as soon as `len(result) == k`.

## Dry Run Takeaway
Instead of sorting by count, use the count itself as an index. The position already gives the order.

`nums = [1,1,1,2,2,3]`, `k = 2`
- Hashmap: `{1: 3, 2: 2, 3: 1}`
- Buckets: `[[], [3], [2], [1], [], [], []]`
- Index 6, 5, 4: empty, skip
- Index 3: add `1` -> result `[1]`
- Index 2: add `2` -> result `[1, 2]`, size equals `k`, return

## Pattern
**Hash Map Frequency Count + Bucket Sort (index = count)**
- Counting part is the same pattern as Ransom Note and Group Anagrams.
- Use bucket sort when the value lives in a small known range (here 1 to n).

## Complexity
- **Time:** O(n). Count is O(n), building buckets is O(n), and the nested loop is also O(n) because each unique number is visited only once across all buckets.
- **Space:** O(n) for the hashmap and the buckets.

## Things to remember
- My mistake: I made the bucket list with `range(1, len(nums)+1)`. That makes only `n` lists (indexes 0 to n-1), so count `n` gives IndexError. To use index `n`, the size must be `n + 1`.
- `range(start, stop)` only decides how many times the loop runs. It does not decide list indexes. List indexes always start from 0.
- My mistake: reverse range start. `len(bucket)` is `n + 1`, the last index is `len(bucket) - 1`. Correct: `range(len(bucket) - 1, 0, -1)`.
- A nested loop is not always O(n^2). Count the total work done across all iterations.
- `return` only works inside a function.

## Edge Cases
- `nums = [1], k = 1` -> `[1]`
- `nums = [1,1,1], k = 1` -> `[1]` (count equals `n`, needs bucket index `n`)
- `nums = [1,2,3], k = 3` -> `[1, 2, 3]` (all in the same bucket)
- `nums = [-1,-1,2], k = 1` -> `[-1]` (negative numbers are fine, they are only values, not indexes)