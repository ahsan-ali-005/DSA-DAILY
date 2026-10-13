# Day 10: Two Sum (LeetCode 1)

## Code Understanding
Approach of code: (thinking when code)
- I need two numbers that add up to `target`, and I must return their **indices**
- For the current number `nums[i]`, the partner I need is `target - nums[i]`
- Instead of scanning the array again, I keep a hash map of what I have already seen: `value → index`
- At each step I first ask: "is the partner already in the map?"
- If yes, I return `[index of partner, i]`
- If no, I store the current number and its index in the map and move on

## Dry Run Takeaway
Check for the partner first, then store the current number. The map only holds numbers that came before me.

`nums = [2,5,7,9,11]`, `target = 20`
- i=0, x=2: need 18, not in map, store `{2:0}`
- i=1, x=5: need 15, not in map, store `{2:0, 5:1}`
- i=2, x=7: need 13, not in map, store `{2:0, 5:1, 7:2}`
- i=3, x=9: need 11, not in map, store `{..., 9:3}`
- i=4, x=11: need 9, found at index 3, return `[3, 4]`

## Pattern
**Hash Map (Complement Lookup)**
- Same idea as Contains Duplicate (Hash Set, "have I seen this before?"), but here I store the index too, because the answer needs positions, not just yes/no

## Complexity
- **Time:** O(n), one pass over the array, and each map lookup and insert is O(1)
- **Space:** O(n), the map can hold up to n numbers

## Things to remember
- Check the partner **before** inserting the current number, so the same element is never used