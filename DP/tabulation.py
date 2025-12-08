calls = 0
def fib_original(n):
    global calls
    calls += 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib_original(n-1) + fib_original(n-2)

# print(fib_original(10))
# print(calls)


def fib_tab(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 1
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# print(fib_tab(10))

def grid_paths_original(i, j, m, n):
    global calls
    calls+=1
    if i == m-1 and j == n-1:
        return 1
    
    if i >= m or j >= n:
        return 0
    
    return grid_paths_original(i+1, j, m, n) + grid_paths_original(i, j+1, m, n)

# calls = 0
# print(grid_paths_original(0, 0, 3, 3))
# print(calls)

def grid_paths_tab(m, n):
    dp = [[0]*n for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]

print(grid_paths_tab(3, 3))


