# Day 41: Search Insert Position (LeetCode 35)

## Code Understanding
**Approach of code: (thinking when code)**
- Array sorted hai aur O(log n) chahiye, to linear scan nahi, binary search lagana hai.
- `left = 0`, `right = len(nums) - 1`, aur `while left <= right` chalana hai.
- Har step par `mid` nikalo aur `nums[mid]` ko target se compare karo:
  - equal → `mid` return
  - `nums[mid] < target` → target right side mein hai, `left = mid + 1`
  - `nums[mid] > target` → target left side mein hai, `right = mid - 1`
- Agar loop khatam ho jaye aur target nahi mila, to `left` hi insert position hai.

## Dry Run Takeaway
Target na mile to loop ke end par `left` wahi jagah hota hai jahan target sorted order mein baithta.

`nums = [1, 3, 5, 6], target = 2`
- left = 0, right = 3, mid = 1 → `3 > 2`, to `right = 0`
- left = 0, right = 0, mid = 0 → `1 < 2`, to `left = 1`
- left = 1, right = 0 → loop khatam, return `left = 1`

## Pattern
**Binary Search** (first position where value >= target), same pattern as Binary Search (LeetCode 704). Farq sirf end ka hai: 704 mein `-1` return hota hai, yahan `left` return hota hai.

## Complexity
- **Time:** O(log n), kyunke har step par search range aadhi ho jati hai.
- **Space:** O(1), sirf `left`, `right`, `mid` use hue.

## Things to remember
- Loop khatam hone par `left` ke pehle sab elements target se chhote hain, aur `left` se aage sab bade. Isi liye `left` answer hai.
- Target sab se bada ho to `left` `len(nums)` par pohanchta hai, yani array ke bahar. Ye theek hai, kyunke insert end par hi hona hai.
- `right` return nahi karna, `right` to `left` se ek peeche rehta hai.

## Edge Cases
- `[1,3,5,6], 5 → 2` (target mil gaya)
- `[1,3,5,6], 2 → 1` (beech mein insert)
- `[1,3,5,6], 7 → 4` (sab se bada, end par insert)
- `[1,3,5,6], 0 → 0` (sab se chhota, start par insert)
- `[1], 2 → 1` (single element, target bada)