# BASIC
def findMaxAverage(nums: list[int], k: int) -> float:
    if len(nums) == k:
        return sum(nums)/k 
    avg = 0
    for i in range(len(nums)):
        if (i+k) <= len(nums):
            all = 0
            for j in range(i, min(i+k, len(nums))):
                all += nums[j]
            if (all/k) > avg:
                avg = (all/k)
        else:
            break
    
    return avg

# BETTER O(N*K)
def findMaxAverage(nums: list[int], k: int) -> float:
    m = float('-inf')
    for first in range((len(nums)-k)+1):
        second = first+k
        avg = sum(nums[first:second])/(second-first)
        if avg > m:
            m = avg
    return m

# BEST
def findMaxAverage(nums: list[int], k: int) -> float:
    s = sum(nums[:k])
    m = s
    for i in range(k, len(nums)):
        s += nums[i] - nums[i-k]
        if s > m:
            m = s

    return float(m) / float(k)

# THE SAME AS "BEST" BUT JUST EXPANDED AFTER I UNDERSTOOD THINGS
def findMaxAverage(nums, k):
    s = 0
    for x in nums[:k]:
        s+=x
    
    ans = s
    for i in range(k, len(nums)):
        s+=nums[i]
        s-=nums[i-k]
        ans = max(ans, s)
    
    return ans/k

print(findMaxAverage([1,12,-5,-6,50,3], k = 4)) # ANSWER: 12.75