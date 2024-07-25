"""
12. Integer to Roman

https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150

SOLUTION BY OTHER:

        symbs = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }

        result = ""
        for val in sorted(symbs.keys(), reverse=True):
            while val <= num:
                result += symbs[val]
                num -= val
        return(result)


My marks:
Runtime    53ms  Beats 27.37%
Memory  16.62MB  Beats 14.43%

"""



class Solution:
    def intToRoman(self, num: int) -> str:

        dic =  { 1: "I", 5:'V', 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M" }

        roman = ""
        div = 1000
        my_num = num
        while True:
            cur = my_num // div
            cur = int(cur)
            # print(cur, div)

            if cur < 4 : 
                i = 0 
                while i < cur:
                    i += 1
                    roman += dic[div]
            elif cur == 9:
                roman += dic[div]
                roman += dic[div*10]
            elif cur > 4:
                roman += dic[div*5]
                cur2 = cur-5
                i = 0 
                while i < cur2:
                    i += 1
                    roman += dic[div]
            elif cur == 4:
                roman += dic[div]
                roman += dic[div*5]

            my_num = my_num - cur*div
            if div == 1:
                return roman
            div /= 10
            
