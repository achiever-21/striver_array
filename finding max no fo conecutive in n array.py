class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        d=0
        c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1 
                d=max(d,c)
            else:
                c=0 
        return d
        
