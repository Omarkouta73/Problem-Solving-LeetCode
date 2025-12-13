def mergeAlternately(word1: str, word2: str) -> str:
    result = ""
    i=0
    while i < len(word1) and i < len(word2):
        result+=word1[i]
        result+=word2[i]
        i+=1

    while i < len(word1):
        result+=word1[i]
        i+=1

    while i < len(word2):
        result+=word2[i]
        i+=1

    return result


word1="abc"
word2="pqr"
mergeAlternately(word1, word2)