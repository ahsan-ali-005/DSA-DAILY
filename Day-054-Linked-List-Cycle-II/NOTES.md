# Day 54: Linked List Cycle II (LeetCode 142)

## Code Understanding
**Approach of code: (thinking when code)**
- If the list is empty, return `None`
- Phase 1: move `slow` 1 step and `fast` 2 steps until they meet
- If `fast` or `fast.next` becomes `None`, there is no loop, so return `None`
- Phase 2: reset `fast` to `head`, then move both 1 step at a time
- The node where they meet again is the start of the loop, so return it

## Dry Run Takeaway
Meeting point is not the loop start. It only proves a loop exists. Phase 2 finds the start.

`3 → 2 → 0 → -4`, with `-4` pointing back to `2`:
- Start: slow = 3, fast = 3
- Turn 1: slow = 2, fast = 0
- Turn 2: slow = 0, fast = 2
- Turn 3: slow = -4, fast = -4 (they meet)
- Phase 2: fast = 3 (head), slow = -4
- Step 1: fast = 2, slow = 2 (meet), so the loop starts at `2`

Why it works: let `a` = distance from head to loop start, `b` = loop start to meeting point, `c` = loop length. Slow walked `a + b`, fast walked `2(a + b)`, so `a + b` is a whole number of loops. That means `a` steps from the meeting point lands exactly on the loop start.

## Pattern
**Fast & Slow Pointers (Floyd's Cycle Detection)**, same pattern as Linked List Cycle (141), with a second phase to find the loop start.

## Complexity
- **Time:** O(n), each pointer walks the list a constant number of times
- **Space:** O(1), only two pointers, no extra set

## Things to remember
- `fast = head` must run only once, after the first loop ends. I put it inside the first loop, so `fast` was reset every turn and the pointers never kept their 2-step gap
- In Phase 2 both pointers move 1 step, not 2
- Check `not fast or not fast.next` before `fast.next.next`, or it crashes on a list without a loop
- Return the node, not its value

## Edge Cases
- `[]` → `None`
- `[1]`, pos = -1 → `None`
- `[1]`, pos = 0 → node `1` (points to itself)
- `[1,2]`, pos = 0 → node `1`
- `[1,2,3]`, no loop → `None`