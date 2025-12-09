class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_i = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[min_i]:
                min_i = i
        
        if min_i == len(prices)-1:
            return 0
        
        max_i = min_i + 1
        for i in range(min_i, len(prices)):
            if prices[i] > prices[max_i]:
                max_i = i
        
        return prices[max_i] - prices[min_i]
        
        
sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))