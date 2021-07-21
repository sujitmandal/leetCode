class Solution:
    def myAtoi(self, s: str) -> int:
        if(len(s)==0):
            return(0)
        else:
            stringList=list(s.strip())

            if(len(stringList)==0):
                return(0)

            n=1
            if(stringList[0]=='-'):
                n=-1

            if(stringList[0]=='-' or stringList[0]=='+'):
                del stringList[0]

            ans=0
            i=0
            while(i<len(stringList) and stringList[i].isdigit()):
                ans = ans*10+(ord(stringList[i])-ord('0'))
                i+=1

            ans*=n
            minValue = min(ans,2**31-1)

        print(max(-2**31, minValue))    
        return(max(-2**31, minValue))


obj = Solution()
obj.myAtoi('42')
obj.myAtoi('-91283472332')