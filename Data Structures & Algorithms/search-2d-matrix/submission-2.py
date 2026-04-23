class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowIdx = -1

        l, r = 0, len(matrix)-1

        while l <= r:
            mid = l + (r-l) // 2
            midStart = matrix[mid][0]
            midEnd = matrix[mid][-1]

            if midStart <= target <= midEnd:
                rowIdx = mid
                break
            elif target < midStart:
                r = mid - 1
            elif target > midEnd:
                l = mid + 1

        if rowIdx == -1: return False

        row = matrix[rowIdx]

        l, r = 0, len(row) - 1

        while l <=r:
            mid = l + (r-l) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False