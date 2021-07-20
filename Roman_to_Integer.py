roman_dict = {
"I" : 1,
"V" : 5,
"X" : 10,
"L" : 50,
"C" : 100,
"D" : 500,
"M" : 1000
}
class Solution:
    def romanToInt(self, s: str) -> int:
        previous = 0
        current = 0
        result = 0
        for x in s[::-1]:
            current = roman_dict[x]
            if (previous > current):
                result -= current
            else:
                result += current
            previous = current

        print(result)


obj = Solution()
obj.romanToInt("III")
obj.romanToInt("XXVII")
obj.romanToInt("IV")