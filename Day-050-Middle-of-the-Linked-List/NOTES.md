# Day 50: Middle of the Linked List (LeetCode 876)

## Code Understanding
**Approach of code: (thinking when code)**
- Can't jump to an index in a linked list, so I can't use `length // 2` directly
- Use two pointers, both start at `head`
- `slow` moves 1 step, `fast` moves 2 steps
- When `fast` reaches the end, `slow` has covered half the list, so it is at the middle
- Loop runs while `fast and fast.next`, so I never move `fast` two steps from `None`
- Return `slow`

## Dry Run Takeaway
When `fast` finishes, `slow` is exactly half way. The stop condition handles both odd and even lengths.

**Odd:** `1 → 2 → 3 → 4 → 5`
- start: slow = 1, fast = 1
- step 1: slow = 2, fast = 3
- step 2: slow = 3, fast = 5
- `fast.next` is `None` → stop, return 3

**Even:** `1 → 2 → 3 → 4 → 5 → 6`
- start: slow = 1, fast = 1
- step 1: slow = 2, fast = 3
- step 2: slow = 3, fast = 5
- step 3: slow = 4, fast = `None`
- `fast` is `None` → stop, return 4 (second middle)

## Pattern
**Fast & Slow Pointers (Tortoise and Hare)**
- Same two-pointer family as earlier problems, but both pointers move in the same direction at different speeds
- Reused later in Linked List Cycle, Palindrome Linked List, Reorder List

## Complexity
- **Time:** O(n), one pass, `fast` visits about n nodes
- **Space:** O(1), only two pointers

## Things to remember
- Condition order matters: `fast` first, then `fast.next`, otherwise `None.next` crashes
- `fast` checks the even case (lands on `None`), `fast.next` checks the odd case (lands on last node)
- Even length returns the second middle automatically, no extra code needed
- Linked list problem with no index or length → think two speeds

## Edge Cases
- `[1]` → `[1]`
- `[1, 2]` → `[2]`
- `[1, 2, 3]` → `[2, 3]`
- `[1, 2, 3, 4]` → `[3, 4]`