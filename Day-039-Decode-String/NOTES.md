# Day 39: Decode String (LeetCode 394)

## Code Understanding
**Approach of code: (thinking when code)**
- Push every character onto the stack as it comes, until I see a `]`.
- On `]`, pop characters until I hit `[`. Prepend each one, so the order stays correct. This gives the inner `substr`.
- Pop the `[` itself.
- Pop the digits below it and build `k` (prepend again, since numbers can have many digits).
- Push `int(k) * substr` back as one decoded string. It can now be part of an outer bracket.
- At the end, `"".join(stack)` gives the final answer.

## Dry Run Takeaway
The stack holds the unfinished outer part while I decode the inner part. A `]` always closes the innermost bracket first.

Trace of `3[a2[c]]`:
- Push `3`, `[`, `a`, `2`, `[`, `c` → stack: `['3','[','a','2','[','c']`
- `]` → pop until `[` → `substr = "c"`; pop `[`; `k = 2` → push `"cc"` → stack: `['3','[','a','cc']`
- `]` → pop until `[` → `substr = "acc"`; pop `[`; `k = 3` → push `"accaccacc"`
- Join the stack → `accaccacc`

## Pattern
**Stack (nested structure, pause and resume)**
Same idea as Valid Parentheses: process on the closing bracket and use the stack to remember the opening part.

## Complexity
- **Time:** O(n × k), roughly the size of the decoded output, because every repeat builds a longer string.
- **Space:** O(n) for the stack.

## Things to remember
- Pop until `[` first, then pop the digits. The order matters.
- `k` can be multi-digit (`10[a]`), so use a `while` loop with `isdigit()`, not a single pop.
- Prepend while popping (`stack.pop() + substr`), otherwise the string comes out reversed.
- Use `while stack and ...` when reading digits, because the stack can be empty (`2[a]` at the very start).
- The stack holds both single characters and already decoded strings. That is fine because everything is a string at the end.

## Edge Cases
- `abc` → `abc` (no brackets)
- `1[a]` → `a`
- `10[a]` → `aaaaaaaaaa` (multi-digit k)
- `2[a]bc` → `aabc` (letters after the bracket)
- `3[a]2[bc]` → `aaabcbc` (two blocks side by side)
- `2[2[2[a]]]` → `aaaaaaaa` (deep nesting)