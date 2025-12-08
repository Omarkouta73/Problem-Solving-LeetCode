# dynamic window size


def longestOnes(nums: list[int], k: int) -> int:
    l, r, c, m = 0, 0, 0, 0
    while r < len(nums):
        if nums[r] == 0:
            c+=1 
        if c > k:
            if nums[l] == 0:
                c-=1
            l+=1
        m = max(m, r-l+1)
        r+=1
    
    return m


def longestOnes(nums: list[int], k: int) -> int:
    left = 0
    zeros = 0
    m = 0
    print("L", " ", "R", " ", "Z", " ", "M")
    print("--------------")
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros+=1
        if zeros > k:
            if nums[left] == 0:
                zeros-=1
            left = right
            # print(left, " ", right, " ", zeros, " ", m, " ", "INTR")
        m = max(m, right-left+1)
        print(left, " ", right, " ", zeros, " ", right-left+1)

    return m




# This is the canonical sliding window approach:
    # Expand right each time.
    # If the window becomes invalid (zeros > k), shrink it one step at a time from the left until it becomes valid again.
    
def longestOnes(nums: list[int], k: int) -> int:
    left = 0
    zeros = 0
    m = 0
    print("L", " ", "R", " ", "Z", " ", "M")
    print("--------------")
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros+=1
        while zeros > k:
            if nums[left] == 0:
                zeros-=1
            left+=1
            # print(left, " ", right, " ", zeros, " ", m, " ", "INTR")
        m = max(m, right-left+1)
        print(left, " ", right, " ", zeros, " ", right-left+1)

    return m


print(longestOnes([1,0,0,0,1], k = 2))


"""
A generic template for dynamic sliding window finding max window length
"""
def longest_window(nums, condition):
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