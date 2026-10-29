# Day 27: Maximum Average Subarray I (LeetCode 643)

## Code Understanding / Approach of code: (thinking when code)

- Window size is fixed at `k`, so I only need the sum of every block of `k` elements
- Step 1: add the first `k` elements to get the first window sum (`cur_sum`)
- Step 2: store its average as the starting `max_avg`
- Step 3: move the window one step right: add the new element `nums[i]`, remove the old element `nums[i - k]`
- Step 4: compute the average of the new window and keep the maximum
- Return `max_avg` at the end

## Dry Run Takeaway

Never re-add the whole window. New sum = old sum + entering element - leaving element.

`nums = [1, 12, -5, -6, 50, 3]`, `k = 4`

- First window `[1, 12, -5, -6]` → sum = 2
- Move right: add 50, remove 1 → sum = 51 (window `[12, -5, -6, 50]`)
- Move right: add 3, remove 12 → sum = 42 (window `[-5, -6, 50, 3]`)
- Best sum = 51 → 51 / 4 = 12.75

## Pattern

**Fixed-Size Sliding Window**

Trigger words: "subarray / substring of size k".

## Complexity

- **Time:** O(n), the first window takes k steps and the slide takes n - k steps, each step is O(1)
- **Space:** O(1), only a few variables are used

## Things to remember

- My logic was right, but I got Wrong Answer because LeetCode was set to Python 2, where `int / int` cuts the decimal (`51 / 4 = 12`). Always check that the language is Python3
- I computed the average at every step. It is enough to track the max **sum** and divide by `k` once at the end
- Do not start `max_avg` from 0, the answer can be negative. Start from the first window instead

## Edge Cases

- `[5], k = 1` → `5.0`
- `k == len(nums)` → average of the whole array
- `[-1, -2], k = 1` → `-1.0` (all negative, so max must not start at 0)
- `[0, 4, 0, 3, 2], k = 1` → `4.0`