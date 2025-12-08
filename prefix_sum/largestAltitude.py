# method 1
def largestAltitude(gain: list[int]) -> int:
    v = [0]
    for i in range(len(gain)):
        v.append(v[-1] + gain[i])
    return max(v)

# method 2
def largestAltitude(gain: list[int]) -> int:
    m = 0
    c = 0
    for i in range(len(gain)):
        c+=gain[i]
        m = max(m, c)
    return m

print(largestAltitude([-5,1,5,0,-7]))
