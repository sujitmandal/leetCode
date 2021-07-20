from statistics import median 
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 = list(nums1)
        nums2 = list(nums2)
        merged_array = nums1 + nums2
        
        median_array = median(merged_array)

        print(median_array)
        return(median_array)



obj = Solution()
obj.findMedianSortedArrays()