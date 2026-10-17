class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1

        while l <= r:
            mid = (l+r) // 2
            # print(f"mid: {mid}")
            row = mid // cols
            col = mid % cols
            # print(f"row: {row}")
            # print(f"col: {col}")
            mid_val = matrix[row][col]

            if mid_val < target:
                l = mid + 1
            elif mid_val > target:
                r = mid - 1
            else:
                return True
        return False


        