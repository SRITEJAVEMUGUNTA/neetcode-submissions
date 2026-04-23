class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        for r in range(N//2):
            for c in range(r, N-r-1):
                top = matrix[r][c]
                right = matrix[c][N-1-r]
                bottom = matrix[N-1-r][N-1-c]
                left = matrix[N-1-c][r]

                print(top)
                print(right)
                print(bottom)
                print(left)

                matrix[c][N-1-r] = top
                matrix[N-1-r][N-1-c] = right
                matrix[N-1-c][r] = bottom
                matrix[r][c] = left

        

        