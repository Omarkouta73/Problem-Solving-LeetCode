class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_v = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_v:
                min_v = prices[i]
            
            profit = max(profit, prices[i] - min_v)
        
        return profit


    def maxProfit_adv(self, prices):
        profit = 0
        holding = False
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                # buy
                if not holding:
                    profit -= prices[i]
                    holding = True
            elif prices[i] > prices[i+1]:
                # sell
                if holding:
                    profit+=prices[i]
                    holding = False
        if holding:
            profit+=prices[-1]
            
        return profit
    
    
    def solve(self, day, holding, prices, memo):

        if day >= len(prices):
            return 0
        
        if (day, holding) in memo:
            return memo[(day, holding)]
        
        if holding:
            # sell or skip ==> max
            sell = prices[day] + self.solve(day+1, False, prices, memo)
            skip = self.solve(day+1, True, prices, memo)
            memo[(day, holding)] = max(sell, skip)
        else:
            # buy or skip
            buy = -prices[day] + self.solve(day+1, True, prices, memo)
            skip = self.solve(day+1, False, prices, memo)
            memo[(day, holding)] = max(buy, skip)
        
        return memo[(day, holding)]

    def maxProfit_adv_rec(self, prices):
        memo = {}
        return self.solve(0, False, prices, memo)
    

sol = Solution()
print(sol.maxProfit_adv_rec([7,1,5,3,6,4]))
print(sol.maxProfit_adv_rec([1,2,3,4,5]))
print(sol.maxProfit_adv_rec([7,6,4,3,1]))
print(sol.maxProfit_adv_rec([34,82,16,74,55,46,44,25,96,80,51,62,73,26,76,30,20,30,55,6,3,93,74,80,8,13,3,82,1,35,68,22,81,63,77,41,51,84,36,46,86,71,5,65,65,91,97,57,92,96,57,97,74,33,19,42,44,22,12,26]))
