candies = [2,3,5,1,3]
extraCandies = 3

def kids(candies, extraCandies):
    results = []
    for i in range(len(candies)):
        if max(candies) <= (candies[i]+extraCandies):
            results.append(True)
        else:
            results.append(False)

    return results

print(kids(candies, extraCandies))

