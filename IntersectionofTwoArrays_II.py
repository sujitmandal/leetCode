from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        i=0
        j=0
        result=[]
        nums1.sort()
        nums2.sort()
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                result.append(nums1[i])
                i+=1
                j+=1
                
        print(result)
        return(result)



obj = Solution()
obj.intersect([1, 2, 2, 1],[2, 2])
obj.intersect([4,9,5], [9,4,9,8,4])
obj.intersect([1,2,2,1],[2])