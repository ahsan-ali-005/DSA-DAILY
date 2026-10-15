# Day 11: Group Anagrams (LeetCode 49)

## Code Understanding
Approach of code: (thinking when code)
- Anagrams have the same letters, so after sorting the letters they become identical
- Use the sorted word as a key and keep a dictionary `key -> list of words`
- For each word, build the key once: `''.join(sorted(word))` (sorted returns a list, so join it back to a string)
- If the key is already in `d`, append the word to its list
- Otherwise create a new list with this word
- At the end, return only the values of the dictionary (the groups), not the keys

## Dry Run Takeaway
Anagrams always give the same key, so one dictionary lookup decides the group.

`strs = ['tab', 'bat', 'tan', 'ant']`
- `tab` → key `abt` → not in d → `d = {abt: [tab]}`
- `bat` → key `abt` → in d → `d = {abt: [tab, bat]}`
- `tan` → key `ant` → not in d → `d = {abt: [tab, bat], ant: [tan]}`
- `ant` → key `ant` → in d → `d = {abt: [tab, bat], ant: [tan, ant]}`
- Return values → `[[tab, bat], [tan, ant]]`

## Pattern
**Hash Map with Canonical Key (Grouping)**
- Same pattern idea as Ransom Note (frequency counting) and Contains Duplicate (hash set), now the sorted form / letter counts becomes the dictionary key
- Question to ask: "what is identical for every item in the same group?"

## Complexity
- **Time:** O(n · k log k), because every word of length k is sorted (n = number of words)
- **Space:** O(n · k), because all words are stored in the dictionary
- Better version: count letters in 26 slots and use `tuple(count)` as the key, time becomes O(n · k)

## Things to remember
- `sorted(word)` returns a list, and a list cannot be a dictionary key. Use `''.join(...)` (or a tuple)
- Check `key in d`, not `key in strs`
- After creating `sorted_i`, use it everywhere (I still wrote `d[sorted(i)]` in the if/else)
- Compute the key once and store it in a variable
- Return `list(d.values())` (groups only), not the dictionary
- LeetCode needs `class Solution`, `self`, `strs`, and `return` instead of `print`

## Edge Cases
- `[""]` → `[[""]]`
- `["a"]` → `[["a"]]`
- `["ab", "ba"]` → `[["ab", "ba"]]`
- `["abc", "def"]` → `[["abc"], ["def"]]` (no anagrams, each word is its own group)