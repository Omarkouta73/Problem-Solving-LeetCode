# def moveZeroes(nums: list[int]) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     for i in range(len(nums)):
#         for j in range(len(nums)-i-1):
#             if nums[j] == 0:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     print(nums)

# def moveZeroes(nums: list[int]) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     i = 0
#     j = 0
#     while i < len(nums):
#         if nums[i] != 0:
#             nums[j] = nums[i]
#             j+=1
#         i+=1
    
#     for k in range(j, len(nums)):
#         nums[k] = 0

def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    last = 0
    for x in nums:
        if x != 0:
            nums[last] = x
            last+=1
    
    for k in range(last, len(nums)):
        nums[k] = 0
        
    # print(nums)

moveZeroes([1, 0, 2, 0, 3])