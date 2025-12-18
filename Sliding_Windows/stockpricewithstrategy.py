class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        initial_profit = 0
        for i in range(len(prices)):
            initial_profit += (prices[i] * strategy[i])
        
        max_profit = initial_profit
        
        for start in range(0, n - k + 1):
            change = 0
            for i in range(start, start + k):
                old = prices[i] * strategy[i]
                if i < start + k//2:
                    new = 0                 # strategy → 0
                else:
                    new = prices[i]         # strategy → 1
                change += new - old
            max_profit = max(max_profit, initial_profit + change)

        
sol = Solution()
p = sol.maxProfit([5,4,3], strategy = [1,1,0], k = 2)
print(p)