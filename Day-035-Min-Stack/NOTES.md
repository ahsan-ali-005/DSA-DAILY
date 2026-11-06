# Day 35: Min Stack (LeetCode 155)

## Code Understanding
**Approach of code: (thinking when code)**
- `getMin()` must be O(1), so I can't scan the stack for the minimum.
- Keep a second stack, `minStack`, that stores "minimum so far" at every level.
- `push`: append the value to `stack`, then append `min(value, current minimum)` to `minStack`.
- `pop`: pop from both stacks together so they stay in sync.
- `top` returns `stack[-1]`, `getMin` returns `minStack[-1]`.

## Dry Run Takeaway
`minStack` mirrors `stack` level by level, so the current minimum is always on top of `minStack`.

Example: `push(2)`, `push(5)`, `push(1)`, `pop()`, `getMin()`
- push(2) → stack `[2]`, minStack `[2]`
- push(5) → stack `[2, 5]`, minStack `[2, 2]` (5 is not smaller, so the old min repeats)
- push(1) → stack `[2, 5, 1]`, minStack `[2, 2, 1]`
- pop() → stack `[2, 5]`, minStack `[2, 2]`
- getMin() → `2`

## Pattern
**Stack with Auxiliary State** (a second stack stores a running answer that survives `pop`).

## Complexity
- **Time:** O(1) for every operation, because each one only touches the end of a list.
- **Space:** O(n), because `minStack` holds one entry per pushed value.

## Things to remember
- `MinStack` is not iterable, so `list(ob)` gives a `TypeError`. Print `ob.stack` and `ob.minStack` to test.
- I reused `value` for the new minimum inside `push`. A separate name like `new_min` is easier to read.
- Always push to `minStack` on every push, even when the value is not a new minimum, otherwise the two stacks go out of sync.

## Edge Cases
- `push(x)` then `pop()` → both stacks empty
- `push(3)`, `push(3)`, `pop()`, `getMin()` → `3` (duplicate minimums are handled because every push adds an entry)
- Negative values: `push(-2)`, `push(0)`, `push(-3)`, `getMin()` → `-3`
- `pop`, `top` and `getMin` are only called on non-empty stacks (given in constraints)