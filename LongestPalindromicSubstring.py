
class Solution:
    def longestPalindrome(self, s):
        if s == s[::-1]: return s
        cur_l, cur = 1, 1
        for i in range(1, len(s)):
            odd_l, even_l, r = i - cur - 1, i - cur, i + 1
            odd, even = s[odd_l : r], s[even_l : r]
            if odd_l >= 0 and odd == odd[::-1]:
                cur_l = odd_l
                cur += 2
            elif even_l >= 0 and even == even[::-1]:
                cur_l = even_l
                cur += 1

        print(s[cur_l : cur_l + cur])
        return s[cur_l : cur_l + cur]
 




obj = Solution()
obj.longestPalindrome('aacabdkacaa')
obj.longestPalindrome('babad')
obj.longestPalindrome('abadd')
obj.longestPalindrome('cbbd')
obj.longestPalindrome('ac')
obj.longestPalindrome('bb')
obj.longestPalindrome('a')
