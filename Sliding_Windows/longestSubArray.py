# dynamic sliding window:
#   1. increase from right, decrease from left. (but you do according to a criteria)
#   2. Increase from right. If the criteria was broken => decrease from left to re-fulfill the criteria.
# criteria: window has only one zero
# base case: if there are no zeros => return n-1

def longestSubarray(nums: list[int]) -> int:
    n = len(nums)
    # base-case:
    if set(nums) == {1}:
        return n-1
    
    # criteria:
    left = 0
    zeros = 0
    m = 0
    for right in range(n):
        if nums[right] == 0:
            zeros+=1
        while zeros > 1:
            if nums[left] == 0:
                zeros-=1
            left+=1
        m = max(m, right-left)
    return m

nums = [0,1,1,1,0,1,1,0,1] 
print(longestSubarray(nums))


