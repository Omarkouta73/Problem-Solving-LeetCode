class Solution:
    def islexi(self, strs):
        cols = len(strs[0])
        length = len(strs)
        if cols < 1: # empty string
            return True
        
        for i in range(length-1):
            if strs[i] > strs[i+1]:
                return False

        return True

    def minDeletionSize(self, strs: list[str]) -> int:    
        if self.islexi(strs):
            return 0
        
        count = 0
        n = len(strs)

        while not self.islexi(strs):
            for i in range(n):
                strs[i] = strs[i][1:]
            count+=1
        
        return count

lst = ["zyx", "wvu", "tsr"]
strs = ["ca","bb","ac"]
other = ["xc","yb","za"]
wrong1 = ["xga","xfb","yfa"]

sol = Solution()
print(sol.minDeletionSize(strs))
# print(sol.islexi(wrong1))


