def reverseVowels(s: str) -> str:
    vowels = set("aeiouAEIOU")
    indicies = []
    sss = list(s)
    for i in range(len(sss)):
        if sss[i] in vowels:
            indicies.append((sss[i], i))
            sss[i] = "~"
    print(sss)
    print(indicies)
    
    indicies.sort(key=lambda x: x[1], reverse=True)
    results = [ch for ch, _ in indicies]
    print(results)

    j = 0
    i = 0
    while j < len(sss):
        if sss[j] == '~':
            sss[j] = results[i]
            i+=1
        j+=1
        
    return "".join(sss)

print(reverseVowels("A man, a plan, a canal -- Panama"))

# AceCreIm