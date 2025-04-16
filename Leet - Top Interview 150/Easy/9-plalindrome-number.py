"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Runtime   11ms  Beats 35.92%
Memory 18.10MB  Beats 19.66%

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: 
            return False
        elif x == 0: 
            return True

        x_s = str(x)
        l = len(x_s)

        process = 0

        while process < l/2:
            if x_s[process] != x_s[l-process-1]:
                return False
            process += 1

        return True

# 1 ms solution!
class Solution_OF_OTHER_PERSON:
    def isPalindrome_not_mine(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

  
