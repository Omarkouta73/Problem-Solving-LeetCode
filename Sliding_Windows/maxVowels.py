def maxVowels(s: str, k: int) -> int:
    vowels = set("aeiuo")
    current = 0
    for x in s[:k]:
        if x in vowels: current += 1
    ans = current
    for i in range(k, len(s)):
        if s[i] in vowels:
            current+=1
        if s[i-k] in vowels:
            current-=1
        
        ans = max(ans, current)

    return ans

print(maxVowels("abciiidef", 3))


# The window size is always exactly k. You slide the window one step at a time:
    # Add the new element (right end),
    # Remove the old element (left end).
