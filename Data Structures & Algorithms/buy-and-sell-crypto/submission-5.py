class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        profit = 0
        i = len(prices) - 1
        j = i - 1
        while j >= 0:
            if prices[i] < prices[j]:
                i -= 1
                j = i - 1
            else:
                profit = prices[i] - prices[j]
                if profit > max_profit:
                    max_profit = profit
                j -= 1
        return max_profit


