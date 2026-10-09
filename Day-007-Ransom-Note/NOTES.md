# Day 07: Ransom Note (LeetCode 383)

## Code Understanding
Approach of code: (thinking when code)
- Ask: "Do I have enough of each letter?" So count first, then compare.
- Count every letter of `magazine` in a dictionary (key = letter, value = how many times it appears).
- Go through `ransomNote` one letter at a time and use up one count per letter.
- If the letter is not in the dictionary, return `False`.
- If the letter is in the dictionary but its count is `0`, return `False`.
- Otherwise reduce its count by 1.
- If the loop finishes without failing, return `True`.

## Dry Run Takeaway
Magazine is the supply, ransomNote is the demand. Fail the moment the supply runs out.

`ransomNote = "aa"`, `magazine = "ab"`
- `counter = {a:1, b:1}`
- first `a` → count is 1, use it → `{a:0, b:1}`
- second `a` → count is 0 → `return False`

## Pattern
**Frequency Counting (Hash Map)**
- Count the supply first, then use up the demand one by one.
- Use it whenever a problem asks "do I have enough of X?"

## Complexity
- **Time:** O(m + n), because both strings are read once.
- **Space:** O(1), because there are at most 26 lowercase letters in the dictionary.

## Things to remember
- Fail has **2 cases**, not 1: the letter is not in the dictionary, or its count is already `0`. I missed the first case twice.

## Edge Cases
- `ransomNote = "a"`, `magazine = "b"` → `False` (letter not in magazine)
- `ransomNote = "aa"`, `magazine = "ab"` → `False` (count runs out)
- `ransomNote = "aa"`, `magazine = "aab"` → `True`
- `ransomNote` longer than `magazine` → always `False`