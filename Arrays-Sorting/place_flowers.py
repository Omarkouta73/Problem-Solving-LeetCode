def canPlaceFlowers(flowerbed: list[int], n: int):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            right_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
            left_empty = (i == 0) or (flowerbed[i-1] == 0)
            if right_empty and left_empty:
                flowerbed[i] = 1
                count+=1
    return count >= n

# def canPlaceFlowers(flowerbed: list[int], n: int):
#     count = 0
#     i = 0
#     while i < len(flowerbed):
#         # print(i)
#         if flowerbed[i] == 0:
#             right_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
#             left_empty = (i == 0) or (flowerbed[i-1] == 0)
#             if right_empty and left_empty:
#                 count+=1
#                 i+=2
#             else:
#                 i+=1
#         else:
#             i+=1
#     return count >= n
    
print(canPlaceFlowers([1,0,0,0,0,1], n=2))
            