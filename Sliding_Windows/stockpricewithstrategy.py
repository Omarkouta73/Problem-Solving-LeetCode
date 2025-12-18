class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        initial_profit = 0
        for i in range(len(prices)):
            initial_profit += (prices[i] * strategy[i])
        
        max_profit = initial_profit
        
        n = len(prices)
        for start in range(0, n - k + 1):
            change = 0
            for i in range(start, start + k):
                old = prices[i] * strategy[i]
                if i < start + k//2:
                    new = 0
                else:
                    new = prices[i]
                change += new - old
            max_profit = max(max_profit, initial_profit + change)
        
        return max_profit

    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        initial_profit = 0
        n = len(prices)
        for i in range(n):
            initial_profit += (prices[i] * strategy[i])
        
        # print(initial_profit)
        
        max_profit = initial_profit


        strategy_cpy = strategy.copy()
        for left in range(k):
            if left < k//2:
                strategy_cpy[left] = 0
            else:
                strategy_cpy[left] = 1
        
        # print(strategy_cpy)
        current_profit = 0
        for i in range(n):
            current_profit += (prices[i] * strategy_cpy[i])
        
        # print(current_profit)
        max_profit = max(max_profit, current_profit)
        # print(max_profit)
        
        # strategy_cpy = strategy.copy()
        for right in range(k, n):
            left = right - k
            
            strategy_cpy[left] = strategy[left]

            start = left + 1

            for i in range(start, start + k):
                if i - start < k // 2:
                    strategy_cpy[i] = 0
                else:
                    strategy_cpy[i] = 1

        # print(strategy_cpy)
        current_profit = 0
        for i in range(n):
            current_profit += (prices[i] * strategy_cpy[i])
        
        # print(current_profit)
        max_profit = max(max_profit, current_profit)
        # print(max_profit)

        return max_profit

    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        initial_profit = 0
        n = len(prices)
        for i in range(n):
            initial_profit += (prices[i] * strategy[i])
        
        print(initial_profit)
        
        max_profit = initial_profit


        w = 0
        for left in range(k):
            lhs = prices[left]
            rhs = 0 if left < k//2 else 1
            w += (lhs * rhs)

        max_profit = max(max_profit, w + initial_profit) # 1
        # best = w # 2
        # best = w + initial_profit # 3
        
        for right in range(k, n):
            left = right - k + 1
            w += prices[right] * (1 - strategy[right])
            # mid = left + k//2
            # w -= prices[mid] * (1 - strategy[mid])
            # w += -prices[mid] * strategy[mid]
            w -= (-prices[left] * strategy[left])

            max_profit = max(max_profit, w + initial_profit)

        print(w)
        return max_profit

        
sol = Solution()
# p = sol.maxProfit(prices = [4,2,8], strategy = [-1,0,1], k = 2)
# p = sol.maxProfit(prices = [5,4,3], strategy = [1,1,0], k = 2)
p = sol.maxProfit(prices = [3, 10, 1, 7, 6], strategy = [1, -1, 0, 1, -1], k = 4)
print(p)
# 3-10+7-6=-6
# 1+7-6=2
# 3+7+6=16