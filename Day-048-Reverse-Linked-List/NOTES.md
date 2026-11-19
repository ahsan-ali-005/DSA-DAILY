# Day 48: Reverse Linked List (LeetCode 206)

## Code Understanding
**Approach of code: (thinking when code)**
- Reversing means every node's `next` must point backward instead of forward.
- Keep two pointers: `prev` (starts at `None`) and `curr` (starts at `head`).
- If I flip `curr.next` directly, I lose the rest of the list, so first save it: `nxt = curr.next`.
- Then flip the arrow: `curr.next = prev`.
- Then move both pointers forward: `prev = curr`, `curr = nxt`.
- Repeat until `curr` is `None`.
- `prev` is now the last node I visited, which is the new head, so return `prev`.

## Dry Run Takeaway
Save the next node first, then flip, then move. Order matters.

`1 → 2 → 3 → None`, start: `prev = None`, `curr = 1`
- Step 1: `nxt = 2`, `1.next = None`, `prev = 1`, `curr = 2`
- Step 2: `nxt = 3`, `2.next = 1`, `prev = 2`, `curr = 3`
- Step 3: `nxt = None`, `3.next = 2`, `prev = 3`, `curr = None`
- Loop stops, return `prev` (node 3): `3 → 2 → 1 → None`

## Pattern
**Linked List: In-place Reversal (prev / curr pointers)**

## Complexity
- **Time:** O(n), one pass, each node is visited once.
- **Space:** O(1), only `prev`, `curr`, `nxt` are used, no new nodes.

## Things to remember
- Never flip `curr.next` before saving `nxt`, or the rest of the list is lost.
- Return `prev`, not `curr`, because `curr` is `None` when the loop ends.
- My mistake: I tested with `reverseList([1,2])`, but the function needs a `ListNode`, not a Python list (`AttributeError: 'list' object has no attribute 'next'`). Build nodes first for local testing.
- My mistake: `print(...)` on a node shows only the memory address. Convert to a list to see values.
- Recursive version exists (follow-up), but iterative comes first.

## Edge Cases
- `head = []` → `[]`
- `head = [1]` → `[1]`
- `head = [1,2]` → `[2,1]`
- `head = [1,2,3,4,5]` → `[5,4,3,2,1]`