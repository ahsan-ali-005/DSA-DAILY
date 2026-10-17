# Day 13: Product of Array Except Self (LeetCode 238)

## Code Understanding

**Approach of code:**
- `answer[i]` = (product of everything to the left of i) × (product of everything to the right of i)
- Make `res = [1] * n`, this is also the output array
- Pass 1 (left → right): keep a running `left = 1`; at each `i` first do `res[i] = left`, then `left *= nums[i]`
- Pass 2 (right → left): keep a running `right = 1`; at each `i` do `res[i] *= right`, then `right *= nums[i]`
- Order matters in both passes: use the value first, then update it, so `nums[i]` never goes into its own answer

## Dry Run Takeaway

Pass 1 stores the left products, pass 2 multiplies the right products on top of them, so one array does the work of two.

`nums = [1,2,3,4]`
- Pass 1: `left` goes 1 → 1 → 2 → 6 → 24, `res = [1, 1, 2, 6]`
- Pass 2 at i=3: `res[3] = 6 × 1 = 6`, `right = 4`
- Pass 2 at i=2: `res[2] = 2 × 4 = 8`, `right = 12`
- Pass 2 at i=1: `res[1] = 1 × 12 = 12`, `right = 24`
- Pass 2 at i=0: `res[0] = 1 × 24 = 24`
- Final: `[24, 12, 8, 6]`

## Pattern

**Prefix & Suffix (running product)**, same idea as Range Sum Query (Prefix Sum), but with a running product and a second pass from the right.

## Complexity

- **Time: O(n)**, two separate loops, not nested
- **Space: O(1)** extra, `res` is the output so it doesn't count; only `left` and `right` are extra variables

## Things to remember

- In pass 2 use `res[i] *= right`, not `=`, because `res[i]` already holds the left product
- Pass 2 loop runs backwards: `range(n - 1, -1, -1)`

## Edge Cases

- `[1,2,3,4]` → `[24,12,8,6]`
- `[-1,1,0,-3,3]` → `[0,0,9,0,0]` (one zero: only the zero's own index gets a non-zero value)
- `[0,0]` → `[0,0]` (two zeros: everything becomes 0)
- `[2,3]` → `[3,2]` (minimum length)
- `[1,0]` → `[0,1]`