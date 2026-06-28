class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:

            left = 0
            right = len(row) - 1
            middle = left + (right - left)//2 #Accounting for overflow

            while left <= right:

                if row[middle] > target:
                    right = middle - 1
                    middle = left + (right - left)//2

                
                elif row[middle] < target:
                    left = middle + 1
                    middle = left + (right - left)//2
                
                else:
                    return True
        
        return False
