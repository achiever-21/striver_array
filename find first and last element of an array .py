class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findfirst(nums,target):
            l=0
            r=len(nums)-1 
            while l<=r:
                mid=(l+r)//2 
                if nums[mid]==target:
                    if mid==0 or nums[mid-1]!=target:
                       return mid 
                    else:
                        r=mid-1 
                else:
                    if nums[mid]>target:
                        r=mid-1 
                    else:
                        l=mid+1 
            return -1
        def lastsearch(nums,target):
            l=0
            r=len(nums)-1
            while l<=r: 
                mid=(l+r)//2 
                if nums[mid]==target:
                    if mid==len(nums)-1 or nums[mid+1]!=target:
                        return mid 
                    else:
                        l=mid+1 
                else:
                    if nums[mid]>target:
                        r=mid-1 
                    else:
                        l=mid+1 
            return -1
        ans=[findfirst(nums,target),lastsearch(nums,target)]
        return ans

            

                
                 
