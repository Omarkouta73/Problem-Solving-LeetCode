def isSubsequence(s: str, t: str) -> bool:
    if len(s) < 1: return True
    if len(t) < 1: return False
    i = 0
    for x in t:
        if i >= len(s): return i == len(s) 
        if x == s[i]: i+=1
    return i == len(s)



def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j+= 1
    return i == len(s)

    
print(isSubsequence("", "baab"))