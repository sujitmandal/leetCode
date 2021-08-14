class Solution:
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return(nums1)

        i = j = 0
        
        while j < n:
            if nums1[i] > nums2[j] or i >= m + j:
                nums1.insert(i, nums2[j])
                nums1.pop()  
                j += 1
            else:  
				
                i += 1


obj = Solution()
obj.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)