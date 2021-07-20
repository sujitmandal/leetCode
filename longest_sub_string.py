s = 'pwwkew'

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Substring = {}
        length = 0
        i = 0 
        
        for j in range(len(s)):
            if s[j] in Substring:
                i = max(i, Substring[s[j]] + 1)
            Substring[s[j]] = j
            length = max(length, j - i  + 1)

        print(Substring)
        return(length)



obj = Solution()
obj.lengthOfLongestSubstring(s)