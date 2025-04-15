"""
383. Ransom Note
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Runtime 23ms    Beats 49.46%
Memory  17.87MB Beats 82.69%


"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        def count_letters(text):

            letter_counts = {}
            for char in text:
                if char in letter_counts:
                    letter_counts[char] += 1
                else:
                    letter_counts[char] = 1
            return letter_counts

        ransom_letters = count_letters(ransomNote)
        magazine_letters = count_letters(magazine)

        for key, numbers in ransom_letters.items():

            if key not in magazine_letters:
                return False 
            
            if numbers > magazine_letters[key]:
                return False 
        return True 
