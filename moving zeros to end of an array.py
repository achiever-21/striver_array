Intuition
moving all zeros to end of the array

Approach
->remove elements whose value is 0
->and also count how many number of zeros
->run a for loop to append total number of zeroes we deleted

Complexity
Time complexity:O(n)O(n)O(n)
Space complexity:o(1)o(1)o(1)
Code
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        i=0
        while i<=len(nums)-1 :
            if nums[i]==0:
                nums.pop(i)
                c+=1
                i-=1
            i+=1
        for i in range(c):
            nums.append(0)
        return nums
approach 2:
by using two pointers i and j ==0 where initlally checking ith elemnt value if the ith element is zero then we increment j until we find a nn zero element and then swap i and j th elements
if there ith and j th are not equal to zero then move forward

time complexity and space complexity :O(n)andO(1)O(n) and O(1)O(n)andO(1)
code:
lass Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        i=j=0
        while i!=len(nums) and j!=len(nums):
            if nums[i]==0 and nums[j]==0:
                j+=1
            elif nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1 
                j+=1 
            elif nums[i]!=0:
                i+=1 
                j+=1
        return nums
