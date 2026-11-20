# Day 49: Merge Two Sorted Lists (LeetCode 21)

## Code Understanding
**Approach of code: (thinking when code)**
- Both lists are already sorted, so the smallest remaining node is always at the front of one of them
- Make a `dummy` node and a `tail` pointer on it, so the first real node is attached like every other node
- While both lists have nodes, compare `list1.val` and `list2.val`
- Attach the smaller node to `tail.next`, then move that list's pointer forward
- Move `tail` forward after every attach
- When one list runs out, attach the whole leftover list to `tail.next` in one step
- Return `dummy.next`, not `dummy`

## Dry Run Takeaway
The leftover list is already sorted and every value in it is >= everything merged so far, so there is no need to loop over it.

list1 = 1 → 2 → 4, list2 = 1 → 3 → 4
- 1 vs 1: equal, so `else` takes list2's 1. Merged: 1
- 1 vs 3: take list1's 1. Merged: 1 → 1
- 2 vs 3: take 2. Merged: 1 → 1 → 2
- 4 vs 3: take 3. Merged: 1 → 1 → 2 → 3
- 4 vs 4: equal, take list2's 4. list2 is now empty
- Loop ends, list1 still has 4, so `tail.next = list1`
- Result: 1 → 1 → 2 → 3 → 4 → 4

## Pattern
**Two Pointers + Dummy Node**
- One pointer per list, compare the current nodes, take the smaller one
- Dummy node removes the special case for the head
- Same two-pointer idea as Merge Sorted Array (88)

## Complexity
- **Time:** O(n + m), each node is visited once
- **Space:** O(1), existing nodes are reused, only `dummy` and `tail` are extra

## Things to remember
- `tail = tail.next` must run inside the loop, otherwise the same node gets overwritten
- Attach the leftover list after the loop, otherwise nodes are lost
- Return `dummy.next`, not `dummy`
- My own mistakes: (fill in)

## Edge Cases
- `[] , []` → `[]`
- `[] , [0]` → `[0]`
- `[1,2,4] , [1,3,4]` → `[1,1,2,3,4,4]` (duplicates go to the `else` branch)
- `[1,2,3] , [10,20]` → `[1,2,3,10,20]` (one list ends first, leftover attached)