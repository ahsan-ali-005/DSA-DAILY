# Day XX: Container With Most Water (LeetCode 11)

## Code Understanding
Approach of code: (thinking when code)
- Area of a container = width × min(height of the two lines).
- Start with one pointer at each end (`l = 0`, `r = n - 1`) so the width is the largest possible.
- At every step: calculate `w = r - l`, `h = min(height[l], height[r])`, `a = w * h`, and update `max_area`.
- Move the pointer of the **shorter** line (`l += 1` if `height[l] < height[r]`, else `r -= 1`).
- Stop when `l == r`. `max_area` is the answer.

## Dry Run Takeaway
The shorter line is the bottleneck. Moving the taller line only reduces the width and can never increase the min height, so it can never give a better area. Only moving the shorter line gives a chance.

`height = [1,8,6,2,5,4,8,3,7]`
- `l=0, r=8` → w=8, h=1, area=8 → move `l` (1 is shorter)
- `l=1, r=8` → w=7, h=7, area=49 → move `r` (8 is taller than 7, so 7 is shorter side) 
- `l=1, r=7` → w=6, h=3, area=18 → move `r`
- `l=1, r=6` → w=5, h=8, area=40 → equal heights, move `r`
- remaining steps give 16, 15, 4, 6, all smaller than 49
- answer = **49**

## Pattern
**Two Pointers (opposite ends)**

Same pattern as Squares of a Sorted Array and Valid Palindrome. Here the question at every step is: "which side is no longer useful?" Answer: the shorter line, so discard it.

## Complexity
- **Time:** O(n), each step moves one pointer inward, so every line is visited at most once.
- **Space:** O(1), only a few variables.

## Things to remember
- Area depends on **both** width and height, not only the tallest lines or only the widest pair.
- Height means the **shorter** of the two lines, not the taller one.
- My confusion: I knew the pointers had to move but not which one. Rule: move the shorter line.
- If both heights are equal, moving either pointer is fine.
- Safe to discard the shorter line: with the current widest width, its best possible area is already counted.

## Edge Cases
- `[1, 1]` → `1`
- `[0, 0]` → `0`
- `[5, 5, 5]` → `10`
- `[1, 2, 3, 4, 5]` → `6`