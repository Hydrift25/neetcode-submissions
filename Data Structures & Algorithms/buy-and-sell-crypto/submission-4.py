class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        maxprofit = profit
        for price in prices[1:]:
            buy = min(buy, price)
            profit = price - buy
            maxprofit = max(profit, maxprofit)
        return maxprofit