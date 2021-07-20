class Solution:
    def twoSum(self, nums, target):
        temp = {}
        
        for i , j in enumerate(nums):
            r = target - j
            if r in temp:
                return([temp[r], i])
            temp[j] = i
            
        return([])


obj = Solution()
obj.twoSum()