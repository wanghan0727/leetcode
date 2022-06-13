class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)

        bottom_row = triangle[-1]

        for row in range(n-2, -1, -1):
            
            for col in range(row+1):
                bottom_row[col] = min(bottom_row[col], bottom_row[col+1]) + triangle[row][col]

        return bottom_row[0]

        

