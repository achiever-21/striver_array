Intuition:
---------
removing duplicate elements and not changing order of elements in an array

Approach:
first.jfif
by using i and j two pointers where i=0 and j=1 checking first second element there same or not if they are we just moving forward till new element which is not equal to i th element and just assign this new element at i+1 the position
repeating same until the j comes to end at last return array till i th element till where we removed duplicates

Complexity
Time complexity:O(N)O(N)O(N)

Space complexity:O(1)

Code
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1
        
