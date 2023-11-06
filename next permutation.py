approach:we have to travrse array from back and check where the elemnt i=7 a[i]>a[i-1] stop there and swap these two numbers and sort the remaining part from a[i+1]
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=-1 
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i 
                break
        if index==-1:
            nums.reverse()
            return nums
        else:
            for i in range(len(nums)-1,-1,-1):
                if nums[i]>nums[index]:
                    nums[i],nums[index]=nums[index],nums[i] 
                    break 
        nums[index+1:]=sorted(nums[index+1:])
        return nums
                    

