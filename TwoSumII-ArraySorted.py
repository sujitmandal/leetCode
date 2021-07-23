class Solution:
    def twoSum(self, numbers, target):
        i,j=0,len(numbers)-1
        while(i<j):
            start = numbers[i]
            end = numbers[j]
            if target>start+end:
                i+=1
            elif target<start+end:
                j-=1
            else:
                break
        
        print([i+1,j+1])
        return([i+1,j+1])
                    


obj = Solution()
obj.twoSum([2,7,11,15], 9)