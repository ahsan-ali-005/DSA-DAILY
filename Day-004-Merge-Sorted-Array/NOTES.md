# Day 04: Merge Sorted Array (LeetCode 88)

## Code Understanding / Approach of code: (thinking when code)
- Use three pointers: `i` (last real element of `nums1`), `j` (last element of `nums2`), `k` (last slot of `nums1`).
- Start from the back, because the empty space is at the end of `nums1`. Writing at the front would overwrite real numbers.
- Compare `nums1[i]` and `nums2[j]`. The bigger one goes to `nums1[k]`.
- The pointer of the array whose number was placed moves back by one. `k` always moves back by one.
- Loop runs while `j >= 0`. When `nums2` is finished, the rest of `nums1` is already in its correct place.
- If `i < 0` (`nums1` finished first), just place `nums2[j]` directly.

## Dry Run Takeaway
The biggest number is always at the end of a sorted array, so only the last elements need to be compared. Filling from the back means nothing useful is overwritten, because every number at the front has already been copied back or is still unused.

## Pattern
**Two Pointers (fill from the back)**: one pointer per array, plus a write pointer at the end of the array that has the free space.

## Complexity
- **Time:** O(m + n), since every number is visited once.
- **Space:** O(1), since no extra array is used.

## Things to remember
- I was confused about when to move `i` and when to move `j`. Rule: the pointer of the array whose number was placed moves back. The other one stays.
- Check `i >= 0` before `nums1[i]`. Otherwise `nums1[-1]` silently picks the last element in Python.
- My first thought was to fill from the front, which destroys data. When free space is at the back, think from the back.

## Edge Cases
- `nums2` is empty: `nums1 = [1], m = 1, nums2 = [], n = 0` → `[1]`
- `nums1` has no real elements: `nums1 = [0], m = 0, nums2 = [1], n = 1` → `[1]`
- All of `nums2` is smaller: `[4,5,6,_,_,_]` + `[1,2,3]` → `[1,2,3,4,5,6]`
- All of `nums2` is bigger: `[1,2,3,_,_,_]` + `[4,5,6]` → `[1,2,3,4,5,6]`
- Duplicates: `[2,2,_,_]` + `[2,2]` → `[2,2,2,2]`