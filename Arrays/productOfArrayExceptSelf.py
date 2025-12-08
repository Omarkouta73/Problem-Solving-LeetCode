# # O(n^2)
# def productExceptSelf(nums):
#     results = []
#     for i in range(len(nums)):
#         prod = 1
#         for j in range(len(nums)):
#             if i != j:
#                 prod *= nums[j]
#         results.append(prod)
#     return results

# O(n)
def productExceptSelf(nums):
    output = [1]*len(nums) # [1,1,1,1]
    # left side
    left = 1
    for i in range(0, len(nums)):
        output[i] *= left
        left *= nums[i]

    # right side
    right = 1
    for j in range(len(nums)-1, -1, -1):
        output[j] *= right
        right *= nums[j]
    
    return output

print(productExceptSelf([1, 2, 3, 4]))