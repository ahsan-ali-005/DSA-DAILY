# Day 51: Linked List Cycle (LeetCode 141)

## Code Understanding
**Approach of code: (thinking when code)**
- Start `slow` and `fast` both at `head`
- Each loop: `slow` moves 1 step, `fast` moves 2 steps
- If there is a cycle, `fast` eventually catches `slow` inside it, so `slow == fast` → return `True`
- If there is no cycle, `fast` reaches the end (`None`), the loop stops → return `False`
- Loop condition `while fast and fast.next` is needed because `fast` jumps 2 nodes

## Dry Run Takeaway
Inside a cycle, the gap between `fast` and `slow` shrinks by 1 each step, so they must meet.

`[3,2,0,-4]`, tail connects back to `2`:
- Start: slow = 3, fast = 3
- Step 1: slow = 2, fast = 0
- Step 2: slow = 0, fast = 2 (0 → -4 → 2)
- Step 3: slow = -4, fast = -4 → same node → `True`

## Pattern
**Fast & Slow Pointers (Floyd's Cycle Detection)**
Same pattern as Middle of the Linked List (Day NN-1).

## Complexity
- **Time:** O(n) — fast either reaches the end or meets slow within a few loops around the cycle
- **Space:** O(1) — only two pointers, no set (this is the follow-up answer)

## Things to remember
- Check both `fast` and `fast.next` in the loop, otherwise `fast.next.next` crashes on `None`
- Compare nodes (`slow == fast`), not values (`.val`), because values can repeat
- No cycle = `fast` hits `None`, so the loop ends by itself
- Hash set also works (store visited nodes) but uses O(n) space

## Edge Cases
- `[]` → `False`
- `[1]`, no cycle → `False`
- `[1]`, `next` points to itself → `True`
- `[1,2]`, tail connects to head → `True`
- `[1,2,3]`, no cycle → `False`