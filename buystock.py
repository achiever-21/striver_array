Approach
->we want a max profit so we can find it by easy approach by taking buystock=nums[0] and sellingstock=[nums[i]]
so that we traverse the array if u find selling stock is less than buystock then change buystock=nums[i]
else find profit and check it with prevoius and take max one among them

Complexity
Time complexity:O(n)O(n)O(n)
Space complexity:O(1)O(1)O(1)
Code
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buystock=prices[0]
        max1=0
        for i in range(1,len(prices)):
            if buystock>prices[i]:
                buystock=prices[i]
            else:
                actual=prices[i]-buystock 
                max1=max(actual,max1)
        return max1
            
