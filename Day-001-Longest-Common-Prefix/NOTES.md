# Day 01: Longest Common Prefix (LeetCode 14)

## Code Understanding / Approach of code: (thinking when code)
- Take the first word and go through its characters one by one (outer loop = columns).
- For each character, compare it with the same position in every word (inner loop).
- If a word has run out of letters (`i == len(word)`) or its letter is different, return `res`.
- If all words match at that position, add the character to `res`.
- If the loops finish without returning, the whole first word is the prefix, so return `res`.



## Dry Run Takeaway
Take the first word and compare its first character with all the other words (including the first word itself). When the character mismatches with any word's character, return the result built so far.

## Pattern
**Vertical scanning**: compare position by position across all items, and stop at the first mismatch.
Use it when the question is about what every string (or array) shares from the start.

## Complexity
- **Time:** O(n × m), where `n` is the number of words and `m` is the length of the common prefix (at most the shortest word).
- **Space:** O(1) extra (`res` is the output).

## Things to remember
- Optimized does not mean fewer loops. It means doing no more work than the input size.
- n² is bad when the input is small but the work is large. Here the input itself is large, so n × m is normal.
- The outer loop runs over characters, and the inner loop runs over words. These are two different sizes. It only becomes n² when `m ≈ n` and every word shares the whole prefix (worst case).
- In the worst case the input has n × m characters and I must read each one at least once. The work equals the input size, so no double growth of processing Hence, not O(n²).

## Edge Cases
- One word: `["abc"]` → `"abc"`
- No common prefix: `["dog", "car"]` → `""`
- One word is a prefix of the others: `["flower", "fl"]` → `"fl"`
- All words identical: `["abc", "abc"]` → `"abc"`