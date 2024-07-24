"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

******* Great solution!!!!!

        s = s.strip()
        words = s.split()
        if words:
            return len(words[-1])
        else:
            return 0

Runtime 34ms   - Beats 63.35%
Memory 16.67MB - Beats 12.37%
            
"""



class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        l = len(s)
        # print(l)
        
        while True:
            cur_let = s[l-1]
            if cur_let == ' ':
                # print ("SPACE AT THE START")
                l-=1
            else:
                break 
        
        for n in range(l):
            cur_num = n+1
            cur_let = s[l-cur_num]
            # print(cur_num, cur_let)
            if cur_let == ' ':
                return cur_num-1

        return l
            

        
