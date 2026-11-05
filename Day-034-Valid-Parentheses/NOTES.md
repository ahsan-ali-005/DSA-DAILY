# Day 34: Valid Parentheses (LeetCode 20)

## Code Understanding
**Approach of code:**
- Make an empty `stack` to hold only unmatched opening brackets.
- Make a `hashmap` of closer -> opener: `")" : "("`, `"}" : "{"`, `"]" : "["`.
- Go through the string one character at a time.
- If `ch` is a closer (it is in the hashmap):
  - If the stack is non-empty and the top equals `hashmap[ch]`, pop it (pair matched).
  - Otherwise return `False`.
- If `ch` is an opener, push it onto the stack.
- At the end, return `True` only if the stack is empty.

## Dry Run Takeaway
Closers are never stored, they are only checked against the top of the stack.

`"{[]}"`:
- `{` -> push, stack: `{`
- `[` -> push, stack: `{ [`
- `]` -> top is `[`, pop, stack: `{`
- `}` -> top is `{`, pop, stack: empty -> `True`

`"([)]"`:
- `(` -> push, `[` -> push, stack: `( [`
- `)` -> top is `[`, not `(` -> `False`

## Pattern
**Stack (LIFO)**: match the most recent unmatched opener first.

## Complexity
- **Time:** O(n), one pass through the string.
- **Space:** O(n), the stack can hold all openers in the worst case.

## Things to remember
- My first version pushed every character into the stack, including closers. The stack should hold only unmatched openers.
- Check `stack` is non-empty before reading `stack[-1]`, otherwise it crashes on an empty stack.
- Returning `True` right after the loop is wrong. Leftover openers mean invalid, so the stack must be empty at the end.
- Use a stack whenever the last thing opened must be closed first (nested or paired structures).

## Edge Cases
- `")"` -> `False` (closer with an empty stack)
- `"(("` -> `False` (stack not empty at the end)
- `"([)]"` -> `False` (wrong order)
- `"(]"` -> `False` (wrong type)
- `"()[]{}"` -> `True`