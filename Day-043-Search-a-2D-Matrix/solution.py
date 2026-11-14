class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            mid_row = (top + bot) // 2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break
            
        if not (top <= bot):
            return False

        row = (top + bot) // 2
        left, right = 0, cols - 1

        while left <= right:
            mid_value = (left + right) // 2

            if target > matrix[row][mid_value]:
                left = mid_value + 1
            elif target < matrix[row][mid_value]:
                right = mid_value - 1
            else:
                return True

        return False

ob = Solution()
print(ob.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 5))

# Output
# True