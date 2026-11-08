# Day 36: Evaluate Reverse Polish Notation (LeetCode 150)

## Code Understanding
Approach of code: (thinking when code)
- The operator always works on the last two numbers seen, so use a stack
- Token is a number → convert to int and push
- Token is an operator → pop two numbers, compute, push the result back
- First pop is the right operand (`b`), second pop is the left operand (`a`)
- `+ - * /` all follow `a op b`; for `/` use `int(a / b)` so it truncates toward zero
- At the end one number is left in the stack, return `stack[0]`

## Dry Run Takeaway
An operator always consumes the top two numbers and puts one result back, so the stack shrinks by one each time.

`["4","13","5","/","+"]`
- `4` → `[4]`
- `13` → `[4, 13]`
- `5` → `[4, 13, 5]`
- `/` → b=5, a=13, 13/5 = 2 → `[4, 2]`
- `+` → b=2, a=4, 4+2 = 6 → `[6]`

## Pattern
**Stack**, the most recent items are the first ones needed. Same idea as Valid Parentheses.

## Complexity
- **Time: O(n)**, each token is processed once, and push/pop are O(1)
- **Space: O(n)**, the stack can hold up to n numbers

## Things to remember
- The first pop is the right operand, the second pop is the left one (`["5","2","-"]` gives `3`, not `-3`)
- Use `int(a / b)`, not `a // b`: `//` floors toward negative infinity, so `-7 // 2 = -4` but the answer should be `-3`
- Numbers can be negative (like `"-11"`), so check `t in "+-*/"` carefully. It works here because `"-11"` is not a substring of `"+-*/"`, but a plain `"-"` is.

## Edge Cases
- `["3"]` → `3`
- `["5","2","-"]` → `3`
- `["7","-2","/"]` → `-3`
- `["-7","2","/"]` → `-3`
- `["2","1","+","3","*"]` → `9`