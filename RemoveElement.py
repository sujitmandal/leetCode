class Solution:
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        
        print(count)
        return(count)


obj = Solution()
obj.removeElement([3,2,2,3], 3)
obj.removeElement([0,1,2,2,3,0,4,2], 2)