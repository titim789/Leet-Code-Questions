class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def findRow (arr, target):
            length = len(arr)
            if length == 0 or length == 1:
                return 0
            
            mid = (length-1)//2

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return findRow(arr[:mid], target)
            else:
                return findRow(arr[mid+1:], target) + mid + 1
        
        def findTarget(row, target):
            length = len(row)
            if length == 0:
                return False
            if length == 1:
                if row[0] == target:
                    return True
                else:
                    return False
            mid = length // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                return findTarget(row[:mid], target)
            else:
                return findTarget(row[mid+1:], target)
        
        row = findRow([i[0] for i in matrix], target)
        if matrix[row][0] > target:
            row -= 1

        if row >= len(matrix):
            return False
        return findTarget(matrix[row], target)

        

        