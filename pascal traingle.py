Intuition
we can solve this problem by using ncr method.

Approach
first we break problem into three pieces.
1.element at nth position by using ncr.
2.finding entire row in an pascal traingle.
3.next finidng entire pascal traingle.
for suppose if u need an element at nth row and cth col we can find it by n-1Cr-1 here we can
-> we have to find (n-1)! ,(n-r)!,r! for finding each we get
time complexity: O(n-1)+O(n-r)+O(r).
but we can decrsease this time . u can observe a pattern in this below.
WhatsApp Image 2023-10-26 at 7.01.12 PM.jpegby taking a for loop we can find that in a O(n) time .

Complexity
Time complexity: O(n2)O(n^2)O(n 
2
 )

Space complexity:O(1)O(1)O(1)

Code
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l1=[]
        for i in range(1,numRows+1):
            l1.append(self.generatingrow(i))
        return l1
    def generatingrow(self,r):
        l=[1]
        ans=1
        for i in range(r-1):
            ans=ans*(r-1-i) 
            ans=ans//(i+1)
            l.append(ans) 
        return l
        
