# 121. Best Time to Buy and Sell Stock

#we use two pointers to solve this problem by keeping track of the minimum price we have seen so far and the maximum profit we can make by selling at the current price. We iterate through the list of prices and update our minimum price and maximum profit accordingly.


class Solution(object):
    def maxProfit(self, prices):
        
        maxProfit=0
        minPrice=prices[0]
       
        for i in range(len(prices)):
            
            
            if minPrice>prices[i]:
                minPrice=prices[i]
            profit=prices[i]-minPrice
            if profit> maxProfit:
                maxProfit=profit
        return maxProfit

        