class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        col=len(matrix[0])
        row=len(matrix)
        l=0
        h=(row*col)-1
        while l<=h:
            mid=(l+h)//2
            m1=mid//col
            m2=mid%col
            if matrix[m1][m2]==target:
                return True
            elif matrix[m1][m2]<target:
                l=mid+1    
            else:
                h=mid-1    
        return False 