class Solution:
    def solve(self, i, buying, prices, memo) -> int:
        if i >= len(prices):
            return 0
            
        if (i, buying) in memo:
            return memo[(i, buying)]
            
        if buying:
            buy = self.solve(i+1, not buying, prices, memo) - prices[i]
            cooldown = self.solve(i+1, buying, prices, memo)
            memo[(i, buying)] = max(buy, cooldown)
        else:
            sell = self.solve(i+2, not buying, prices, memo) + prices[i]
            cooldown = self.solve(i+1, buying, prices, memo)
            memo[(i, buying)] = max(sell, cooldown)
        
        return memo[(i, buying)]
        
    def maxProfit(self, prices) -> int:
        memo = {}
        return self.solve(0, True, prices, memo)