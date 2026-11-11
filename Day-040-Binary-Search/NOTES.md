# Day 40: Binary Search (LeetCode 704)

## Code Understanding
**Approach of code:**
- Array is sorted, so one comparison at the middle can throw away half of it
- `left = 0`, `right = len(nums) - 1` mark the part still being searched
- Loop `while left <= right`:
  - `mid = (left + right) // 2`
  - `nums[mid] == target` → return `mid`
  - `nums[mid] < target` → target is on the right, so `left = mid + 1`
  - `nums[mid] > target` → target is on the left, so `right = mid - 1`
- Loop ends when `left > right` (nothing left to search) → return `-1`

## Dry Run Takeaway
Every step cuts the search space in half; `mid` is already the answer index, no need to search again.

`nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`
- left=0, right=5, mid=2 → nums[2]=3 < 9 → left=3
- left=3, right=5, mid=4 → nums[4]=9 == 9 → return 4

## Pattern
**Binary Search (halve the search space)**
- Use when the data is sorted and you need O(log n)

## Complexity
- **Time: O(log n)**, the search space halves on every step
- **Space: O(1)**, only `left`, `right`, `mid` are used

## Things to remember
- My first version returned `nums.index(target)`, which is an O(n) scan and breaks the O(log n) rule. When the match is found, `mid` already holds the index, so just `return mid`
- Condition is `left <= right` (with `<` a single remaining element would be skipped)
- Always move past `mid` (`mid + 1` / `mid - 1`), never `left = mid`, or the loop can get stuck forever
- Call the method correctly: `ob.search(nums, target)`, not `ob.print(search(...))`

## Edge Cases
- `[5], target = 5` → `0`
- `[5], target = 2` → `-1`
- target smaller than all elements → `-1`
- target larger than all elements → `-1`
- target at first or last index → that index