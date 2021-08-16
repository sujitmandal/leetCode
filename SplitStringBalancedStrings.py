class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, c = 0, 0
        for i in s:
            if i =='L':
                l += 1
            else:
                l -= 1
                
            if l == 0:
                c += 1
                
           
        print(c)
        return(c)
        


obj = Solution()
obj.balancedStringSplit("RLRRLLRLRL")