class Solution:
    def increasingTripletBF(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        # print(nums[i], " ", nums[j], " ", nums[k])
                        return True
        return False
    
    def increasingTriplet(self, nums: list[int]) -> bool:
        m1, m2 = float('inf'), float('inf')

        for x in nums:
            if x <= m1:
                m1 = x
            elif x <= m2:
                m2 = x
            else:
                return True
            
        return False

sol = Solution()
res1 = sol.increasingTriplet([2,1,5,0,4,6])
res2 = sol.increasingTriplet([5,4,3,2,1])
res3 = sol.increasingTriplet([1,2,3,4,5])
res4 = sol.increasingTriplet([1,5,0,4,1,3])

print(res1)
print(res2)
print(res3)
print(res4)



res1 = sol.increasingTripletBF([2,1,5,0,4,6])
res2 = sol.increasingTripletBF([5,4,3,2,1])
res3 = sol.increasingTripletBF([1,2,3,4,5])

# print(res1)
# print(res2)
# print(res3)
