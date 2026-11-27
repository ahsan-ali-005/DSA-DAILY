# Day 56: Add Two Numbers (LeetCode 2)

## Code Understanding
**Approach of code: (thinking when code)**
- Digits are stored in reverse, so the heads are the ones place. I can add from the head, like column addition on paper.
- Make a `dummy` node and a `cur` pointer to build the result list. `carry = 0` at the start.
- Loop `while l1 or l2 or carry`, so the loop also runs when one list is finished or only a carry is left.
- If a list has run out, use 0 for its digit: `v1 = l1.val if l1 else 0`.
- `val = v1 + v2 + carry`, then `carry = val // 10` and the digit to store is `val % 10`.
- Attach `ListNode(val)` to `cur.next` and move `cur` forward.
- Move `l1` and `l2` forward only if they exist.
- Return `dummy.next`, because `dummy` itself is a fake node.

## Dry Run Takeaway
The loop must continue while a carry is left, even when both lists are finished.

`l1 = 9 → 9 → 9`, `l2 = 1`
- Step 1: 9 + 1 + 0 = 10, store 0, carry 1
- Step 2: 9 + 0 + 1 = 10, store 0, carry 1
- Step 3: 9 + 0 + 1 = 10, store 0, carry 1
- Step 4: both lists are None, carry 1, so 0 + 0 + 1 = 1, store 1, carry 0
- Result: `0 → 0 → 0 → 1` (1000)

## Pattern
**Linked List Traversal + Carry Simulation (Dummy Head Node)**
Same dummy node idea as Merge Two Sorted Lists.

## Complexity
- **Time: O(max(m, n))**, because each node of the longer list is visited once.
- **Space: O(max(m, n))** for the new result list. No extra space is used apart from the output.

## Things to remember
- Without `or carry` in the loop condition, the last carry is lost (999 + 1 gives wrong output).
- A finished list counts as digit 0. Never call `.val` on `None`.
- Move `l1` and `l2` only if they are not None.
- The dummy node means no special case is needed for the first node of the result.
- Return `dummy.next`, not `dummy`.

## Edge Cases
- `[0], [0]` → `[0]`
- `[9,9,9], [1]` → `[0,0,0,1]`
- `[2,4,3], [5,6,4]` → `[7,0,8]`
- `[1], [9,9]` → `[0,0,1]`
- lists of different lengths → the shorter one counts as 0 after it ends