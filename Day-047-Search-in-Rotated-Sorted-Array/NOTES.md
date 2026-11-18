# Day 47: Search in Rotated Sorted Array (LeetCode 33)

## Code Understanding
Approach of code: (thinking when code)
- Normal binary search: `left`, `right`, `mid = left + (right - left) // 2`
- If `nums[mid] == target`, return `mid`
- The array is rotated, so I can't compare target with `mid` directly. First find which half is sorted
- `nums[left] <= nums[mid]` means the left half is sorted. Otherwise the right half is sorted
- Check if target lies inside the sorted half's range:
  - Left sorted: `nums[left] <= target < nums[mid]` → `right = mid - 1`, else `left = mid + 1`
  - Right sorted: `nums[mid] < target <= nums[right]` → `left = mid + 1`, else `right = mid - 1`
- If the loop ends without finding it, return `-1`

## Dry Run Takeaway
At least one half is always sorted, and a sorted half lets me say for sure whether the target is inside it.

`nums = [4,5,6,7,0,1,2]`, `target = 0`
- `l=0, r=6, mid=3` (7): left half `4..7` is sorted, 0 is not in `[4,7)` → `left = 4`
- `l=4, r=6, mid=5` (1): left half `0..1` is sorted, 0 is in `[0,1)` → `right = 4`
- `l=4, r=4, mid=4` (0): found → return `4`

## Pattern
**Binary Search** (find the sorted half, then decide)
- Same halving idea as Binary Search (LeetCode 704), with one extra step before moving a pointer

## Complexity
- **Time:** O(log n), because the search space is halved every iteration
- **Space:** O(1), only a few pointers are used

## Things to remember
- Use `<=` in `nums[left] <= nums[mid]`, because when `left == mid` the left half is a single element and still counts as sorted
- In the range checks, `<=` goes on the outer end (`nums[left]` or `nums[right]`) and `<` goes on the `mid` side, because `mid` was already checked
- Don't compare target with `mid` alone to choose a side, check the sorted half's range first

## Edge Cases
- `nums = [1], target = 1` → `0`
- `nums = [1], target = 0` → `-1`
- `nums = [4,5,6,7,0,1,2], target = 3` → `-1`
- `nums = [3,1], target = 1` → `1` (left half is one element, `left == mid`)
- `nums = [1,2,3,4,5], target = 4` → `3` (not rotated)