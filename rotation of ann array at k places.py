Intuition
we have to rotate the array in d times from right to left

Approach
approach1:simple we can an temporary array and assign all n-k elements into it then start swapping array elements from last elements at beginning the end n-k+1 replace the lements with our temporary array elmenets
*but extra space complexitybecoz of temp array

APPROACH 2:
we can observe a pattern that
=>we have k positions actually if we rotate the array at n positions we get the same array no change then no need to rotate same like if the array which is geater than length of the array we need simply we can k=k%n
=>we have to divide our array into two parts first part n-k(arr[:n-k]) and reverse it by using reverse function in python and remaning part arr[n-k:] after that revrse the complete array then we get the rotated array at k places
SAMPLE EXAMPLE:
first.jfif

Complexity
Time complexity:
O((N−K)/2)+O(K/2)O((N-K)/2)+O(K/2)O((N−K)/2)+O(K/2)

Space complexity:
O(4)O(4)O(4)

Code
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        i=0
        j=len(nums)-k-1
        r=len(nums)-1
        l=j+1
        while i<j and i!=len(nums)-k:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        while l<r and l!=len(nums):
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1 
        nums.reverse()
        return nums
