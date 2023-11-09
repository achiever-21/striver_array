You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
we can do this problem in another way with extra space .but to avoid this we follow .

Approach:
-> you will observe a pattern from both input and output .
->if u do tranverse of input matrix after that revrse each row from the matrix then u get output matrix this is the pattern u can obersve
---- so we can divide problem into two parts------------
1.tranverse the matrix
2.reverse the each row from matrix

Complexity
Time complexity:
Space complexity:
Code
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(i+1,c):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in matrix:
            i=i.reverse() 
        return matrix
