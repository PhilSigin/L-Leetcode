"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.


Runtime 39ms  Beats 41.60%
Memory 16.62MB Beats 51.07%

"""

class Solution:
    def reverseWords(self, s: str) -> str:

        s2 = s.split()
        
        """
        ####### This was my first Try.

        s2 = ""
        
        for i in range(len(s)):
            print(s[len(s)-i-1])
            s2 += s[len(s)-i-1]
            s2 += " "

        s2 = s2.strip()
        return s2
        ####### 
        
        """

        s2.reverse()
        s3 = " ".join(s2)
  
        return s3

        
