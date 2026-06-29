class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = (rows * cols) - 1

        while left <= right:
            mid = (left + right) // 2
            midVal = matrix[mid // cols][mid % cols]

            if target < midVal:
                right = mid - 1
            elif target > midVal:
                left = mid + 1
            else:
                return True
        return False