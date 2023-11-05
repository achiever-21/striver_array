Intuition:majority elment appearing more than n/2 times ryt.
Approach:so we can easily find that elment by traversing array at single time .so we need two variables
1.count
2.current
=>first we have to traverse array take first elment as curr=a[0] and c+=1
=>second curr !=a[i] then we hvae to decremnet our count-=1 because we dont whether it is or not our majority elment
=>whenveer we get our count=0 then simply chnage current=new elment=(a[i]) again incremnet c=1
=>in this way we can simply get our majority elment in curr.

Complexity
Time complexity:O(n)
Space complexity:O(1)
Code
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur=nums[0]
        c=0 
        for i in nums:
            if i==cur:
                c+=1 
            elif i!=cur and c!=0:
                c-=1 
            elif i!=cur  and c==0:
                cur=i 
                c=1 
        return cur
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=dict()
        l=set(nums)
        for i in l:
            d[i]=nums.count(i)
        for i,k in d.items():
            if k >len(nums)/2:
                return i
