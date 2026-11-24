# Day 53: Intersection of Two Linked Lists (LeetCode 160)

## Code Understanding
**Approach of code: (thinking when code)**
- Two lists can have different lengths, so one pointer on each list will never reach the shared node at the same time
- Idea: make both pointers walk the same total distance (m + n)
- `l1` starts at `headA`, `l2` starts at `headB`
- When a pointer falls off its own list (`None`), send it to the head of the other list
- Keep moving until `l1 == l2`
- Either they meet at the intersection node, or both become `None` together (no intersection)
- Return `l1`

## Dry Run Takeaway
Switching heads cancels the length difference, so both pointers reach the intersection on the same step.

A = [1, 9, 1, **2, 4**], B = [3, **2, 4**]
- start: l1 = 1, l2 = 3
- step 1: l1 = 9, l2 = 2
- step 2: l1 = 1, l2 = 4
- step 3: l1 = 2, l2 = None
- step 4: l1 = 4, l2 = headA (1)
- step 5: l1 = None, l2 = 9
- step 6: l1 = headB (3), l2 = 1
- step 7: l1 = 2, l2 = 2 → equal, return node 2

## Pattern
**Two Pointers (switch heads / equalize path length)**
Same idea as Linked List Cycle: two pointers moving until they meet.

## Complexity
- **Time:** O(m + n), each pointer walks at most m + n nodes
- **Space:** O(1), only two pointers, no set

## Things to remember
- Compare nodes (`l1 != l2`), not values (`l1.val`), because equal values can sit in different nodes
- `None` counts as a step: the pointer must reach `None` first, then jump to the other head
- Loop condition is `l1 != l2`, not `while l1 and l2`, so the no-intersection case ends with both `None` and the loop stops
- Hash set solution works too but uses O(m) extra space; this one is O(1)

## Edge Cases
- No intersection → `None` (both pointers reach `None` together)
- Lists intersect at the head (same list) → return headA
- Same lengths → they meet in the first pass, no switch needed
- Intersection at the last node → returns that last node