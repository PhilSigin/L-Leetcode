"""
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Runtime  30ms   Beats 86.50%
Memory  16.39MB  Beats 93.49%

"""


class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    def strStr(self, text: str, word: str) -> int:

        
        # using string find() method
        """
        return text.find(word)
        answer = text.find(word)
        return answer
        """

        # using two pointers

        wordle = len (word)
        textle = len (text)

        # was not working on 1 letter words without +1
        for i in range(textle-wordle+1):   
            comp = text[i:(wordle+i)]
            if comp == word:
                return i
        return -1
