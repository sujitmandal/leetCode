class Solution(object):
    def longestCommonPrefix(self, strs):
        rev = ""
        if strs is None:
            return rev #if empty list return empty string

        if len(strs) == 1:
            return strs[0] # if list contains only one word, return that word

        l = [int(len(le)) for le in strs]

        min_len = min(l) # get the minimum length of the strings in the list, so that we can iterate till minimum length
        if min_len == 0:
            return rev # if list contains empty strings, return the empty string
        else:    
            for i in range(1,min_len+1):
                l = [s.startswith(strs[0][:i]) for s in strs[1:]] # get a list contains boolean value[True,True,False] for [flower,flow,flight when comparing with string "flo"]
                if False not in l:
                    rev = strs[0][:i] # if only True in l, store the string in rev, for [flower,flow,flight] l contains only True while comparing with word "fl"
                else:
                    rev = strs[0][:i-1] # if we get False at somepoint return the previous loop word # at word "flo" we get one false so return the word "fl"
                    break
            return rev   


l = Solution()
a = l.longestCommonPrefix(["flower","flow","flight"])
b = l.longestCommonPrefix(["dog","racecar","car"])
print(a)
print(b)