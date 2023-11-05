two sum :
Complexity
Time complexity:O(n)O(n)O(n)
Space complexity:O(n)O(n)O(n)
Code:better approach 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return d[target-nums[i]],i 
            else:
                d[nums[i]]=i 
optimal approach :
we can solve these problem by sorting taking two pointers left and right 
while left <right:
adding sum=a[left=0]+a[right=n-1]
sum>k:sum-=a[j] j-=1 sum+=a[j] 
sum<k:sum-=a[i] i+=1 sum+=a[i] 
