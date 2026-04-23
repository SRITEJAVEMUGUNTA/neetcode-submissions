class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowL, rowR = 0, len(matrix) - 1

        colLen = len(matrix[0])


        while rowL <= rowR:
            rowMid = (rowL+rowR) // 2

            if matrix[rowMid][0] <= target <= matrix[rowMid][colLen-1]:
                l, r = 0, colLen-1

                while l <= r:
                    mid = (l+r) // 2

                    if matrix[rowMid][mid] == target:
                        return True
                    elif matrix[rowMid][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                
                return False
            elif matrix[rowMid][0] > target:
                rowR = rowMid - 1
            elif matrix[rowMid][colLen - 1] < target:
                rowL = rowMid + 1
        return False

    
