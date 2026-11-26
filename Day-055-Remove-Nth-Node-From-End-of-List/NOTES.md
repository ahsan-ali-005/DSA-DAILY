# Day 55: Remove Nth Node From End of List (LeetCode 19)

## Code Understanding

**Approach of code:**

- A singly linked list only moves forward, so I can't count from the end directly
- Create `dummy` before `head`, so removing the first node is not a special case
- Put `left` on `dummy` and `right` on `head`
- Move `right` n steps ahead first (this creates a gap of n between the pointers)
- Move `left` and `right` together until `right` becomes `None`
- Now `left` is exactly one node before the target
- Delete with `left.next = left.next.next`
- Return `dummy.next` (the real head, even if the old head was deleted)

## Dry Run Takeaway

The gap between the pointers never changes, so when `right` falls off the end, `left` is just before the n-th node from the end.

`[1, 2, 3, 4, 5]`, `n = 2`:

- Start: `left = dummy`, `right = 1`
- First loop (2 steps): `right = 3`
- Second loop: `right = 4, left = 1`
- Second loop: `right = 5, left = 2`
- Second loop: `right = None, left = 3`
- `left.next` is `4`, so skip it: `3 -> 5`
- Result: `[1, 2, 3, 5]`

## Pattern

**Two Pointers (Fixed Gap) + Dummy Node**

Same dummy node idea as Merge Two Sorted Lists. Same two-pointer family as Middle of the Linked List, but here the pointers keep a fixed gap instead of different speeds.

## Complexity

- **Time:** O(L), one pass over the list (L = number of nodes)
- **Space:** O(1), only a few pointers

## Things to remember

- Make the gap first, then move both pointers together
- `left` must stop one node before the target, not on it, so I can delete with `left.next`
- Use a dummy node whenever the head can be deleted
- Return `dummy.next`, not `head`

## Edge Cases

- `[1], n = 1` → `[]`
- `[1, 2], n = 1` → `[1]`
- `[1, 2], n = 2` → `[2]` (head is removed, this is why dummy is needed)
- `[1, 2, 3, 4, 5], n = 5` → `[2, 3, 4, 5]`