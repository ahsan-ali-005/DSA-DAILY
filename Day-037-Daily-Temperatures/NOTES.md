# Day 37: Daily Temperatures (LeetCode 739)

## Code Understanding
**Approach of code: (thinking when code)**
- For each day, I need the next day with a warmer temperature, so this is a "next greater element" problem.
- Keep a stack of days that are still waiting for a warmer day. Each item is `[temperature, index]`.
- Go through the days left to right. If today's temperature is greater than the temperature on top of the stack, that waiting day has found its answer.
- Pop it and write `ans[stackIndex] = i - stackIndex` (difference of indices, not temperatures).
- Keep popping while today is still warmer than the new top (`while`, not `if`).
- Then push today, because today is now waiting for its own warmer day.
- Days left in the stack at the end never found a warmer day, so their answer stays `0` (from `[0] * len`).

## Dry Run Takeaway
The stack does not empty every iteration. It only empties when today is warmer than all the waiting days. One big day can answer many waiting days at once.

`[10, 20, 15, 30, 40, 35]`
- i=0 (10): stack empty, push → `[(10,0)]`
- i=1 (20): 20 > 10, pop, `ans[0] = 1` → push `(20,1)`
- i=2 (15): 15 < 20, no pop, push → `[(20,1),(15,2)]`
- i=3 (30): pops 15 → `ans[2] = 1`, pops 20 → `ans[1] = 2`, stack empty, push `(30,3)`
- i=4 (40): pops 30 → `ans[3] = 1`, push `(40,4)`
- i=5 (35): 35 < 40, push → `[(40,4),(35,5)]`
- End: 40 and 35 never found a warmer day, so they stay `0`
- Answer: `[1, 2, 1, 1, 0, 0]`

## Pattern
**Monotonic Stack (Next Greater Element)**
Stack temperatures are always decreasing from bottom to top. Same stack idea as Valid Parentheses, but here we pop on a condition (warmer day) instead of a matching bracket.

## Complexity
- **Time: O(n)** — each day is pushed once and popped at most once, so the inner `while` does not make it O(n²).
- **Space: O(n)** — the stack can hold all days (for example, when temperatures keep decreasing).

## Things to remember
- In my dry run I thought the stack becomes empty after every pop. It only empties when today beats every waiting day.
- At i=3 I only filled `ans[2]` and missed `ans[1]`: one day can pop many days.
- My output comment had 5 values for a 6-element input. Output length always equals input length.
- Answer is `i - stackIndex` (days waited), not the temperature difference.
- Use `while` for popping, not `if`.
- Only the index is really needed in the stack, because `temperatures[index]` gives back the temperature.

## Edge Cases
- `[50]` → `[0]`
- `[30, 40, 50, 60]` → `[1, 1, 1, 0]`
- `[60, 50, 40, 30]` → `[0, 0, 0, 0]`
- `[70, 70, 70]` → `[0, 0, 0]` (equal is not warmer, so the condition is strict `>`)