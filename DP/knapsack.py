weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7
n = len(weights)

def knapsack_or(values, weights, max_w, n):
    if n == 0 or max_w == 0:
        return 0
    
    if weights[n-1] > max_w:
        return knapsack_or(values, weights, max_w, n-1)
    
    return max(
        knapsack_or(values, weights, max_w, n-1),
        values[n-1] + knapsack_or(values, weights, max_w-weights[n-1], n-1)
    )

# print(knapsack_or(values, weights, W, n))

def knapsack_memo(values, weights, max_w, n, memo={}):
    if n == 0 or max_w == 0:
        return 0
    
    if weights[n-1] > max_w:
        memo[(n, max_w)] = knapsack_memo(values, weights, max_w, n-1, memo)

    if (n, max_w) in memo:
        return memo[(n, max_w)]
    
    memo[(n, max_w)] = max(
        knapsack_memo(values, weights, max_w, n-1, memo),
        values[n-1] + knapsack_memo(values, weights, max_w-weights[n-1], n-1, memo)
    )

    return memo[(n,max_w)]

# print(knapsack_memo(values, weights, W, n))

def knapsack_tab(values, weights, max_w, n):
    dp = [[0]*(max_w+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, max_w+1):
            if weights[i-1] <= j:
                dp[i][j] = max(
                    dp[i-1][j],
                    values[i-1] + dp[i-1][j-weights[i-1]]
                )
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][max_w]

print(knapsack_tab(values, weights, W, n))