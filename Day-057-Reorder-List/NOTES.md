# Day 57: Reorder List (LeetCode 143)

## Code Understanding
**Approach of code: (thinking when code)**
- The result alternates front, back, front, back. A singly linked list can't walk backwards, so the back half has to be reversed first.
- Step 1: find the middle with fast/slow pointers (`slow` ends at the last node of the first half).
- Step 2: cut the list with `slow.next = None`, so the two halves are separate lists.
- Step 3: reverse the second half (`prev` becomes the new head of the reversed half).
- Step 4: weave the two halves together, one node from each in turn.
- Before changing any `next`, save the old next pointers in `tmp1` and `tmp2`, or the rest of the list is lost.

## Dry Run Takeaway
Split into two halves, reverse the back half, then interleave the halves.

Example `1 → 2 → 3 → 4 → 5`:
- Fast/slow: `slow` stops at 3, so the first half is `1 → 2 → 3` and the second half starts at 4.
- Cut: `3.next = None`, giving `1 → 2 → 3` and `4 → 5`.
- Reverse the second half: `5 → 4`.
- Weave, round 1: `1 → 5`, then `5 → 2`. Now `first = 2`, `second = 4`.
- Weave, round 2: `2 → 4`, then `4 → 3`. Now `second = None`, so the loop stops.
- Result: `1 → 5 → 2 → 4 → 3`.

## Pattern
**Fast & Slow Pointers + Reverse Linked List + Merge Two Lists**
- Same pattern as Palindrome Linked List (middle + reverse second half).
- Same weaving idea as Merge Two Sorted Lists, but alternating instead of comparing values.

## Complexity
- **Time: O(n)**. Finding the middle, reversing and merging are each one pass.
- **Space: O(1)**. Only pointers are used, and the list is changed in place.

## Things to remember
- Cut the first half with `slow.next = None` before reversing. Otherwise the last node of the first half still points into the second half and creates a loop.
- Save `tmp1` and `tmp2` before changing `first.next` and `second.next`.
- The loop runs on `while second`, because the second half is the same length or one node shorter than the first.
- Starting `fast` at `head.next` makes `slow` stop at the end of the first half. For an odd length the extra middle node stays in the first half.

## Edge Cases
- `[1]` → `[1]`
- `[1, 2]` → `[1, 2]`
- `[1, 2, 3]` → `[1, 3, 2]`
- `[1, 2, 3, 4]` → `[1, 4, 2, 3]`
- `[1, 2, 3, 4, 5]` → `[1, 5, 2, 4, 3]`