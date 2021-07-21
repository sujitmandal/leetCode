class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['I','V','X','L','C','D','M']
        value = [1,5,10,50,100,500,1000]

        romanList = []
        for i in range(6, -1, -1):
            if 4 <= num < 5:
                romanList.append('IV')

                num = num % 4

            elif 9 <= num < 10 :
                romanList.append('IX')

                num = num % 9

            elif 40 <= num < 50:
                romanList.append('XL')

                num = num % 40

            elif 90 <= num < 100:
                romanList.append('XC')

                num = num % 90

            elif 400 <= num < 500:
                romanList.append('CD')

                num = num % 400

            elif 900 <= num < 1000:
                romanList.append('CM')

                num = num % 900

            else:
                if num // value[i]:
                    romanList.append(roman[i] * (num//value[i]))

                    num = num % value[i]


        result = ''.join(romanList)

        print(result)
        return(result)


obj = Solution()
obj.intToRoman(3)
obj.intToRoman(4)
obj.intToRoman(58)