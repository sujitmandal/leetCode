class Solution:
    def reverse(self, x):
        if x >= 2**31-1 or x <= -2**31:
            return(0)
        else:
            strg = str(x)
            if x >= 0 :
                rev = strg[::-1]
            else:
                temp1 = strg[1:] 
                temp2 = temp1[::-1] 
                rev = "-" + temp2
            if int(rev) >= 2**31-1 or int(rev) <= -2**31:
                return(0)
            else: 
                return(int(rev))
            

obj = Solution()
obj.reverse()