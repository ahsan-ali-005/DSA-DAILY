# Day 45: Koko Eating Bananas (LeetCode 875)

## Code Understanding
**Approach of code: (thinking when code)**
- Search over speeds `k`, not over the array
- Smallest possible speed is `1`, largest useful speed is `max(piles)`
- Set `l, r = 1, max(piles)` and `res = r` as a safe starting answer
- Take `k = (l + r) // 2` as the speed to test
- For each pile, hours = `ceil(p / k)`; add them up to get total `hours`
- If `hours <= h`: speed works, so save `res = k` and try slower with `r = k - 1`
- Else: speed is too slow, so go faster with `l = k + 1`
- When `l > r`, `res` holds the minimum speed that works

## Dry Run Takeaway
If speed `k` works, every faster speed also works. That split is why binary search is allowed here.

`piles = [3,6,7,11]`, `h = 8`
- `l=1, r=11`, `k=6`: hours = 1+1+2+2 = 6 ≤ 8, works, `res=6`, `r=5`
- `l=1, r=5`, `k=3`: hours = 1+2+3+4 = 10 > 8, too slow, `l=4`
- `l=4, r=5`, `k=4`: hours = 1+2+2+3 = 8 ≤ 8, works, `res=4`, `r=3`
- `l=4 > r=3`, stop, return `4`

## Pattern
**Binary Search on Answer** (same pattern as Sqrt(x)). Check "does this answer work?" and move toward the smallest one that does.

## Complexity
- **Time:** O(n log m), where `m = max(piles)`. Binary search takes log m steps and each check loops over n piles.
- **Space:** O(1), only a few variables.

## Things to remember
- Search range is `1` to `max(piles)`, not the array indexes
- Use `ceil(p / k)` because a partly eaten pile still costs a full hour
- Working speed: save it in `res` and keep searching left for a smaller one
- Too-slow speed: move `l` right
- Since `k` only gets smaller on every working step, `res = k` is enough, `min` isn't needed

## Edge Cases
- `piles = [3,6,7,11], h = 8` → `4`
- `piles = [30,11,23,4,20], h = 5` → `30` (h equals number of piles, so Koko needs the max pile speed)
- `piles = [30,11,23,4,20], h = 6` → `23`
- `piles = [10], h = 10` → `1`