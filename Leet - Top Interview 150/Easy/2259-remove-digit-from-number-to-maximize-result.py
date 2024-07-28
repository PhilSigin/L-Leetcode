"""
2259. Remove Digit From Number to Maximize Result
https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

You are given a string number representing a positive integer and a character digit.
Return the resulting string after removing exactly one occurrence of digit from number 
such that the value of the resulting string in decimal form is maximized. 
The test cases are generated such that digit occurs at least once in number.

Runtime  39ms  Beats 34.83%
Memory 16.56MB Beats 23.22%

"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        """
        ### This solution from someone looks good:
        
        max_num = ""
        for i in range(len(number)):
            if number[i] == digit:
                max_num = max(curr, number[:i] + number[i+1:])
        return max_num

        """
        
        max_num = 0
        
        # I don't get it why it is not working if its
        # max_num = ""

        for i in range(len (number)):

            if number[i] == digit:
                new_num = number[:i] + number[i+1:]
                if int(new_num) > int(max_num):
                    max_num = new_num
 
        return max_num
        
