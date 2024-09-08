"""
1002. Find Common Characters
Given a string array words, return an array of all characters that show up in all strings
within the words (including duplicates). You may return the answer in any order.
https://leetcode.com/problems/find-common-characters/description/


Runtime 64ms Beats 8.14%
Memory 16.70MB Beats 20.87%

"""

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        # words = ["bella","label","roller"]
        # words = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]

        # First part - collecting ALL the letters (not in optimal way - not storing MINIMAL)

        frequencies = {}

        for word in words:
            for letter in word:
                if letter in frequencies:
                    t = word.count(letter)
                    if t < frequencies[letter]:
                        frequencies[letter] = t
                else:
                    frequencies[letter] = word.count(letter)
        
                    
        # Second part - removing letters that are not common to all words

        for letter, freq in frequencies.items():
            for word in words:
                t = word.count(letter)
                if t < freq:
                    frequencies[letter] = t
                    break


        # Converting tuples to a list 
        seen_letters = []
        for letter, frequency in frequencies.items():
            seen_letters .extend([letter] * frequency)

        return seen_letters


"""

After I finished sumbitted my solution,
asked Gemini for more optimal one, and here it is:

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = {}

        for word in words:
            freq = {}
            for char in word:
                freq[char] = freq.get(char, 0) + 1

            for char, count in freq.items():
                min_freq[char] = min(min_freq.get(char, float('inf')), count)

        result = []
        for char, count in min_freq.items():
            result.extend([char] * count)
        return result

"""
