class Solution:
    def maximumProfit(self, prices):
        # code here
        cost=prices[0]
        profit=0
        for i in range(1,len(prices)):
            temp=prices[i]-cost
            profit=max(temp,profit)
            cost=min(prices[i],cost)
        return profit 
            
