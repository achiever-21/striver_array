Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
-------------------------------------------------------+++++++++++++++++++++++-----------------------------------------++++++++++++++++++++++++++++++++++++++++--------------------------------+++++++++++++++++++++++++
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach:just compare our intervals element with new elment present in an new array
<!-- Describe your approach to solving the problem. -->
initally take a new array 
-> now add the first array from intervals 
->if the array having length>=1 then compare last element from last array in a with intervals first element from array 
two conditions 
1.if it is a array element is less than compared to interval then add this elemnt into a array 
2.else change the last element of our a array with max among two 

# Complexity
- Time complexity:o(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:o(n^2)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        r=len(intervals)
        c=len(intervals[0])
        intervals.sort()
        a=[]
        j=0
        while j<r:
            if not a or a[-1][-1]<intervals[j][0]:
                a.append(intervals[j])
            else:
                a[-1][-1]=max(intervals[j][-1],a[-1][-1])
            j+=1 
        return a

```
 
