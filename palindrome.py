class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        Palindrome = x_str[::-1]
        
        if Palindrome == x_str:
            return(True)
        else:
            return(False)
        

obj = Solution()
obj.isPalindrome()