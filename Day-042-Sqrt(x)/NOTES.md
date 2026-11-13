# Day 42: Sqrt(x) (LeetCode 69)

## Code Understanding
**Approach of code:**
- Answer koi array element nahi, ek number hai jo `0` se `x` ke beech hai, aur ye range sorted hai, so binary search lagti hai
- `left = 0`, `right = x`, `res = 0` (res = ab tak ka sabse bara valid answer)
- Har step par `mid = left + (right - left) // 2` nikalo
- `mid * mid > x` → mid bohat bara hai, `right = mid - 1`
- `mid * mid < x` → mid valid hai, par bara bhi ho sakta hai, so `res = mid` save karo aur `left = mid + 1`
- `mid * mid == x` → perfect square, seedha `return mid`
- Loop khatam hone par `res` return karo (round down wala answer)

## Dry Run Takeaway
`res` har us mid ko yaad rakhta hai jiska square x se chhota tha, aakhir mein sabse bara wahi bachta hai.

`x = 8`:
- `left=0, right=8` → `mid=4`, `16 > 8` → `right=3`
- `left=0, right=3` → `mid=1`, `1 < 8` → `res=1`, `left=2`
- `left=2, right=3` → `mid=2`, `4 < 8` → `res=2`, `left=3`
- `left=3, right=3` → `mid=3`, `9 > 8` → `right=2`
- `left > right`, loop khatam → return `res = 2`

## Pattern
**Binary Search on Answer**: answer ek number range mein hai, condition (`mid * mid <= x`) check karke range aadhi karte jao. Same pattern as Binary Search (704) aur Search Insert Position (35), bas yahan `res` mein last valid candidate save hota hai.

## Complexity
- **Time:** O(log x), har step par search range aadhi ho jati hai
- **Space:** O(1), sirf kuch variables

## Things to remember
- Mid formula `left + right // 2` galat tha, isme sahi `left + (right - left) // 2` hai.
- `**` operator LeetCode allow nahi karta is problem mein, `mid * mid` use karna hai.
- `<` wale case mein `res = mid` save karna na bhoolo, warna floor answer ni milta.

## Edge Cases
- `0 → 0`
- `1 → 1`
- `2 → 1`
- `4 → 2` (perfect square, `else` branch se return)
- `8 → 2`
- `2147483647 → 46340` (bohat bara input, loop sirf ~31 baar chalta hai)