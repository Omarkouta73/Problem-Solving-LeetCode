calls = 0
def fib_original(n):
    global calls
    calls += 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib_original(n-1) + fib_original(n-2)

# print(fib_original(9))
# print(calls)


def fib_memo(n, memo={}):
    global calls
    if n <= 0:
        return 0
    
    if n==1 or n==2:
        return 1
    
    if n in memo:
        return memo[n]
    
    calls += 1
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# print(fib_memo(10))
# print(calls)



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

def grid_paths_memo(i, j, m, n, memo={}):
    global calls
    calls+=1
    if i >= m or j >= n:
        return 0
    
    if i == m-1 and j == n-1:
        return 1

    if (i, j) in memo:
        return memo[(i, j)]
    
    memo[(i, j)] = grid_paths_memo(i, j+1, m, n, memo) + grid_paths_memo(i+1, j, m, n, memo)

    return memo[(i, j)]

# calls = 0
# print(grid_paths_memo(0, 0, 3, 3))
# print(calls)
