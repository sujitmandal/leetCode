class Solution:
    def searchInsert(self, nums, target):

        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                #return(i)
                print(i)
            else:
                result.append(nums[i])

        result.append(target)
        result.sort()

        if target not in nums:
            for i in range(len(result)):
                if result[i] == target:
                    #return(i)
                    print(i)
    
     

obj = Solution()
obj.searchInsert([1,3,5,6], 5)
obj.searchInsert([1,3,5,6], 7)
obj.searchInsert([1,3,5,6], 2)
obj.searchInsert([1,3,5,6], 0)