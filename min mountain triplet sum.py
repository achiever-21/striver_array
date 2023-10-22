Intuition
we have to find a triplet (i,j,k).where nums[j]>nums[i] and nums[j]>nums[k].

Approach
-> first we have target on mid element (nums[j])
->if mid element index is j then we have to find nums[i] it should be minimum among all elements from left part til i th index
-> same as that from j+1 index we have to find min element
-> at last we should check nums[left_min]<nums[mid] and nums[rigt_min]<nums[mid]
-> then we have take the sum of these
-> at last return the minimum sum among all outputs

Complexity
Time complexity:O(n)
Space complexity:O(1)
Code
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        a=nums[0]
        b=nums[-1]
        sum1=10**9
        l=[]
        r=[]
        l.append(0)
        for i in range(1,len(nums)-1):
            left=min(nums[:i])
            right=min(nums[i+1:])
            if nums[i]>left and nums[i]>right:
                sum1=min(sum1,nums[i]+left+right)
        if sum1==10**9:
            return -1 
        else:
            return sum1
