class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        max_profit=0
        min_price=0
        j=1
        while j<n:

            if prices[j]<prices[min_price]:
                min_price=j
                j=min_price+1
            else:
                profit=prices[j]-prices[min_price]
                max_profit=max(max_profit,profit)
                j+=1    
        return max_profit
        


        