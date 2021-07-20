class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for char in s:
            if parentheses_dict.get(char) is not None:
                stack.append(char)

            else:
                if stack:
                    peek = stack[-1]
                    if char != parentheses_dict.get(peek):
                        return False
                    else:
                        stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

      


obj = Solution()
obj.isValid("()[]{}")

obj.isValid("([)]")