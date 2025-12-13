def compress(chars) -> int:
    s = ""
    count = 1
    s += chars[0]
    for i in range(1, len(chars)):
        if chars[i] == s[-1]:
            count += 1
            if (i == len(chars)-1) and (count != 1):
                s += str(count)
        else:
            if (count != 1):
                s += str(count)
            count = 1
            s += chars[i]
    for i in range(len(s)):
        chars[i] = list(s)[i]
    return len(chars[:len(s)])


print(compress(['a', 'b', 'b', 'c', 'c', 'c']))