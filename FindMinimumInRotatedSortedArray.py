class Solution:
    def findMin(self, nums):
        minValue = nums[0]
        
        for i in range(1, len(nums)):
            minValue = min(minValue, nums[i])
            
        
        print(minValue)
        return(minValue)
    

obj = Solution()
obj.findMin([3,4,5,1,2])
obj.findMin([12, 1234, 45, 67])