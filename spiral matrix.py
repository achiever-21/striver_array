first traverse left-> right
top >bottom
right>left
bottom >right 
https://leetcode.com/problems/spiral-matrix/description/
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
--------------------------------------------------------------------------------------------************code*****************--------------------------------------------------------
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        a = []
        right=len(matrix[0])-1
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                a.append(matrix[top][i])
            top+=1 
            for i in range(top,bottom+1):
                a.append(matrix[i][right])
            right-=1 
            if top<=bottom:
                for i in range(right,left-1,-1):
                    a.append(matrix[bottom][i])
                bottom-=1 
            if left<=right:
                for i in range(bottom,top-1,-1):
                    a.append(matrix[i][left])
                left+=1 
        return a

