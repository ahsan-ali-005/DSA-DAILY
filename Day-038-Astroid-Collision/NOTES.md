# Day 38: Asteroid Collision (LeetCode 735)

## Code Understanding
**Approach of code: (thinking when code)**
- Go through asteroids left to right, `stack` holds the survivors so far
- Top of the stack (`stack[-1]`) is the latest survivor, the only one the new asteroid can hit
- Collision happens only when the stack top is positive (moving right) and the new `ast` is negative (moving left)
- Use a `while` loop for the fight, because one new asteroid can destroy many
- `diff = ast + stack[-1]` tells the winner in one step:
  - `diff < 0` -> new asteroid is bigger, pop the top and keep fighting
  - `diff > 0` -> top is bigger, new asteroid explodes (`ast = 0`)
  - `diff == 0` -> both explode (`ast = 0` and pop)
- After the loop, `if ast:` push it only if it survived (0 means it exploded)

## Dry Run Takeaway
A negative asteroid keeps fighting until it dies or the stack has no right-mover left.

`[10, 2, -5]`
- 10 -> no collision, push -> `[10]`
- 2 -> positive, push -> `[10, 2]`
- -5 vs 2 -> diff = -3, 2 explodes, pop -> `[10]`
- -5 vs 10 -> diff = 5, -5 explodes, `ast = 0`
- `ast` is 0, nothing pushed -> `[10]`

## Pattern
**Stack**, same idea as Valid Parentheses and Daily Temperatures: the top of the stack is the only thing the new element interacts with, and a `while` loop handles repeated interactions.

## Complexity
- **Time: O(n)**, each asteroid is pushed once and popped at most once, so the while loop is O(n) in total, not per element
- **Space: O(n)**, the stack can hold all asteroids when none collide

## Things to remember
- Collision condition is only `stack top > 0 and ast < 0`; `+ +`, `- -` and `- +` never collide
- Use `while`, not `if`, because one asteroid can destroy several
- Adding the two values (`ast + stack[-1]`) compares sizes without abs()
- Setting `ast = 0` is the flag for "exploded", so the final push is `if ast:`
- Equal size means pop the top AND do not push the new one

## Edge Cases
- `[5, 10, -5]` -> `[5, 10]`
- `[8, -8]` -> `[]`
- `[10, 2, -5]` -> `[10]`
- `[-2, -1, 1, 2]` -> `[-2, -1, 1, 2]` (moving apart, no collision)
- `[-5, 5]` -> `[-5, 5]` (left-mover is first, they never meet)