# Day NN: Maximum Subarray (LeetCode 53)

## Code Understanding
**Approach of code: (thinking when code)**
- Start `cur` and `best` with `nums[0]`, so the all-negative case also works
- Loop from the second element onward
- At each number `n`, ask: extend the old chunk or restart from `n`?
- `cur = max(n, cur + n)`: `n` means restart, `cur + n` means extend
- `best = max(best, cur)`: `cur` goes up and down, so save the biggest value separately
- Return `best`

## Dry Run Takeaway
A negative running sum is a burden, so throw it away and restart from the current number.

Example `[4, -1, 2]`:
- Start: `cur = 4`, `best = 4`
- `n = -1`: `max(-1, 4 + -1)` = 3 (extend), `best = 4`
- `n = 2`: `max(2, 3 + 2)` = 5 (extend), `best = 5`

## Pattern
**Kadane's Algorithm** (1D Dynamic Programming: local decision at each index, global answer tracked separately)

## Complexity
- **Time:** O(n), one pass through the array
- **Space:** O(1), only `cur` and `best` are stored

## Things to remember
- `n` is the current number the loop is on, not the next one. `cur` is the sum of everything before it
- `cur` is the best chunk ending at this index, `best` is the best seen so far. They are two different things
- Start with `nums[0]`, not `0`, otherwise an all-negative array gives a wrong answer
- I did not understand the logic at first and needed the reveal, so I should trace the table by hand again before the next DP-style problem

## Edge Cases
- `[1]` → `1`
- `[-3, -1, -2]` → `-1`
- `[5, 4, -1, 7, 8]` → `23`
- `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` → `6`