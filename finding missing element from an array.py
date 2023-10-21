Intuition
finding the missing element from an array .

Approach
bruteforce we have three approaches first creating an array from a range(0,n) and checking each element from our given array vth new temp array we made.but extra space O(n)
betterjust sort the array and by using for loop check each ith element is equal to nums[i] .but O(nlogn) time complexity.
optimal
-> by using bitwise xor we can solve this problem
xor conditions: xor of two same numbers is always zero like 1^1==0
=> xor of number from range (0,l) we can get by simple where l is an total numbers
example: [0,1,2,3,4] we can xor of this array by simple formula with time complexity O(1)
formula is l=len(of array)
if l%4==0:xor=l,l%4==1:xor=1,l%4==2:xor=l+1,l%4==3:xor=0
by using 1,2 conditions we are solving this problem in O(n).

Complexity
Time complexity:O(n)O(n)O(n)
Space complexity:O(1)O(1)O(1)
Code
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor=0
        a=len(nums)
        for i in nums:
            xor=xor^i
        if a%4==0:
            return xor^a
        elif a%4==1:
            return xor^1
        elif a%4==2:
            return xor^(a+1)
        elif a%4==3:
            return xor^0
        
