"""
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given a roman numeral, convert it to an integer.

Runtime
63ms
Beats5.50%

Memory
16.55MB
Beats34.53%

Very bad solution after 2 weeks without python practice

"""

class Solution:
    def romanToInt(self, s: str) -> int:        
        roman =  { 'I': 1, 'V':5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        sum = 0
        previous = 0

        for element in s:
            cur_num = roman[element]

            if previous == 0:
                previous = cur_num

            else:
                if cur_num > previous:
                    cur_num -= previous
                    previous = 0
                    sum += cur_num 
                if cur_num <= previous:
                    sum += previous
                    previous = cur_num

        if previous != 0:
            sum += previous
                           
        return sum

