# template 1
def sliding_window(arr, k):
    window_value = 0
    for left in range(k):
        # cummulative window_value
        window_value+=arr[left]
    
    # best = what you window_valueed from left
    best = window_value

    n = len(arr)

    for right in range(k, n):
        # calculate what is the current left
        left = right - k
        window_value += arr[right] # add from right
        window_value -= arr[left] # remove from left
        best = max(best, window_value)
    
    return best


# template 2 (it is very close to the dynamic sliding widnow template)
def sliding_window(arr, k):
    left = 0
    window_value = 0
    answer = 0

    n = len(arr)
    for right in range(n):
        window_value += arr[right] # or any other logic like count zeros or add zeros...
        
        if right - left + 1 == k:
            answer = max (answer, window_value)
            window_value -= arr[left]
            l-=1
        
        return answer




# template 3 (dynamic)
def sliding_window(nums, condition):
    i = 0
    max_length = 0
    result = None

    for j in range(len(nums)):
        # Expand the window
        # Add nums[j] to the current window logic

        # Shrink the window if the condition is violated
        while not condition():  
            # Shrink the window from the left
            # Remove nums[i] from the current window logic
            i += 1

        # Update the result if the current window is larger
        if j - i + 1 > max_length:
            max_length = j - i + 1
            # Add business logic to update result

    return result