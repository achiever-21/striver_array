longestsubarray with sum k
1. for postive numbers and negative numbers
from os import *
from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    # Write your code here
    sum=0
    d={}
    maxlen=0
    for i in range(len(nums)):
        sum+=nums[i]
        if sum==k:
            maxlen=max(maxlen,i+1)
        sub=sum-k 
        if sub in d:
            maxlen=max(maxlen,i-d[sub])
        if sum not in d:
            d[sum]=i 
    return maxlen
2.for positives 
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    l=0
    r=0
    sum=a[0]
    maxlen=0
    n=len(a)
    while r<len(a):
        while l<=r and sum>k:
            sum-=a[l]
            l+=1 
        if sum==k:
            maxlen=max(maxlen,r-l+1)
        r+=1
        if r<n and sum<=k:
            sum+=a[r]
        #r+=1
    return maxlen


