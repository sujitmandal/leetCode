class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        cant=0
        i=0
        a,b=[0,0],[0,0]
        while i<len(s1):
            if s1[i]!=s2[i]:
                cant=cant+1        
                if cant>2:
                    return False               
                a[cant-1]=s1[i] 
                b[cant-1]=s2[i]
            i=i+1
        else:
            if a[0]==b[1] and a[1]==b[0]:
                return True
        return False


obj = Solution()
obj.areAlmostEqual(s1 = "bank", s2 = "kanb")