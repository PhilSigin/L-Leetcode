"""

20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
tput: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Runtime 0ms    Beats 100.00%
Memory 17.94MB Beats 32.03%

"""

class Solution:
    def isValid(self, s: str) -> bool:

        hash={')':'(',']':'[','}':'{'}
        order = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        
        amount = len(s)
        if amount %2 != 0:
            return False

        for char in s:
            if char in opening:
                order.append(char)
            else:
                numb = len(order)
                if numb==0:
                    return False
                else: 

                    if order[numb-1] == hash[char]:
                        order.pop()
                    else:
                        return False


        # Можно дичайше упростить до двух строк!
      
        numb = len(order)
        if numb==0:
            return True
        else: 
            return False
        

