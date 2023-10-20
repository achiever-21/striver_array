Intuition
find the array is sort or not. if the sorted array is rotated then we can say it is sorted.else not.

Approach
we can find array is sorted or not by traversing each element.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
example :[1,2,3,4]
for i in range(1,len(a)):
    if a[i-1]<a[i]:
        pass
    else:
        return False 
return True
this method is okay for sorted array but when we have rotated sorted array then we use
sample :a[1,2,3,4]
after one rotation :a1=[2,3,4,1]
after second rotation:a2= [3,4,1,2]
here we can observe a pattern in above a1 the array is sorted but at one point at (4,1) is unsorted
same like a2 also at point (4,1)
and we can aslo observe the nth element always should be less than less than 0 th element then
=>so we finally conclude that there are two conditions
there should be only one break point (where unsort takes at one position) and last element always less than starting element then only we can say our array is sorted

Complexity
Time complexity:O(n)O(n)O(n)
Space complexity:O(n)O(n)O(n)
Code
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def check(self, nums: List[int]) -> bool:
        i=0
        j=1 
        c=0
        while i<len(nums) and j<len(nums):#checking how many times the array is unsort.
            if nums[i]>nums[j]:
                c+=1 
            i+=1
            j+=1
        if nums[len(nums)-1]>nums[0]:# as per our condition last element should be less than startin element.
            c+=1 
        if c<=1:
            return True 
        else:
            return False
