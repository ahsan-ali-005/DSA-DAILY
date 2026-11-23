# Day 52: Palindrome Linked List (LeetCode 234)

## Code Understanding

**Approach of code: (thinking when code)**

- A linked list can't be read backwards, so I can't compare the two ends directly.
- Find the middle with fast and slow pointers (fast moves 2 steps, slow moves 1).
- When fast reaches the end, slow is at the middle.
- Reverse the second half in place, starting from slow.
- Compare the first half (from head) with the reversed half (from prev).
- If any value differs, return False. If all match, return True.

## Dry Run Takeaway

After reversing, the two halves can be compared front to front, so the list becomes a simple two-pointer check.

Example: `[1,2,2,1]`

- fast, slow both start at the first node
- Step 1: fast moves to the 3rd node, slow moves to the 2nd node
- Step 2: fast moves past the end (None), slow moves to the 3rd node, so the loop stops
- Reverse from slow: `2 -> 1` becomes `1 -> 2`
- left = 1, right = 1, match
- left = 2, right = 2, match
- right is None, loop ends, return True

## Pattern

**Fast & Slow Pointers + Reverse Second Half (in-place reversal)**

Same pattern as Middle of the Linked List (find the middle), plus the in-place reversal technique.

## Complexity

- **Time: O(n)** — one pass to find the middle, one to reverse, one to compare
- **Space: O(1)** — only pointers are used, no extra list or stack

## Things to remember

- Reversal order: save `temp = slow.next`, point `slow.next = prev`, move `prev = slow`, move `slow = temp`.
- After the loop, `prev` is the head of the reversed half, not `slow`, which is None.
- Loop on `right`, not `left`, because the reversed half is the same length or shorter.
- In an odd-length list the middle node needs no special case.
- This changes the original list. The first half still points into the reversed half.
- Copying the list into an array is easier but uses O(n) space, so reversing the second half meets the follow-up.

## Edge Cases

- `[1]` → true
- `[1,2]` → false
- `[1,2,2,1]` → true
- `[1,2,3,2,1]` → true