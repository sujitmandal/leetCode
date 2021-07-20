class Solution:
    def removeDuplicates(self, nums):
        cur = 0
        for i in range(len(nums)):
            if nums[cur] != nums[i]:
                cur += 1
                nums[cur] = nums[i]

        print(cur + 1)
        return(cur + 1)


obj = Solution()
obj.removeDuplicates([1,1,2])
obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4])