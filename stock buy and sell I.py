lass Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buystock=prices[0]
        max1=0
        for i in range(len(prices)):
            if buystock>prices[i]:
                buystock=prices[i]
            else:
                actual=prices[i]-buystock 
                max1+=actual
            buystock=prices[i]
        #if buystock<prices[-1]:
        #    max1+=prices[i]-buystock
        return max1
            
        
