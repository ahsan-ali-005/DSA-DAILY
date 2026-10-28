# Day 26: Best Time to Buy and Sell Stock (LeetCode 121)

## Code Understanding
**Approach of code: (thinking when code)**
- `l` = buy day, `r` = sell day, `maxP` = best profit so far.
- Start with `l = 0`, `r = 1`.
- If `prices[l] < prices[r]`, it's a profit. Calculate it and update `maxP`.
- Otherwise `prices[r]` is cheaper or equal, so it becomes the new buy day: `l = r`.
- Always move `r` forward by 1.
- Buy always stays before sell because `l` is never ahead of `r`.

## Dry Run Takeaway
When a cheaper price appears, we never need to go back to the old buy day. Any future sale is better from the cheaper day.

Example `[7,1,5,3,6,4]`:
- r=1: price 1 < 7, so `l` moves to 1, `maxP` = 0
- r=2: 5 - 1 = 4, `maxP` = 4
- r=3: 3 - 1 = 2, `maxP` stays 4
- r=4: 6 - 1 = 5, `maxP` = 5
- r=5: 4 - 1 = 3, `maxP` stays 5

## Pattern
**Two Pointers (Sliding Window)**: track the best value so far (lowest buy price) while scanning once, left to right.

## Complexity
- **Time:** O(n). One pass, `r` visits each day once.
- **Space:** O(1). Only `l`, `r` and `maxP`.

## Things to remember
- Buy must come before sell, so max minus min is wrong.
- Don't compare every pair (O(n²)). Keep only the cheapest buy day so far.
- On the `else` case, move `l = r` (don't just do `r += 1` and keep the old `l`).
- Return `0` when no profit is possible, which is why `maxP` starts at 0.

## Edge Cases
- `[7,6,4,3,1]` → `0` (prices only go down)
- `[5]` → `0` (single day, loop never runs)
- `[1,2]` → `1`
- `[3,3,3]` → `0` (equal prices, no profit)