"""

38. Count and Say
https://leetcode.com/problems/count-and-say/

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the run-length encoding of countAndSay(n - 1).

Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters 
(repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters 
(length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", 
replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

 
Example 1:
Input: n = 4
Output: "1211"

Explanation:
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"

Example 2:
Input: n = 1
Output: "1"
Explanation:
This is the base case.


Runtime 11ms Beats   23.77%
Memory 17.79MB Beats 84.76%


HAVENT USED HINTS:
Hint 1
Create a helper function that maps an integer to pairs of its digits and their frequencies. For example, 
if you call this function with "223314444411", then it maps it to an array of pairs [[2,2], [3,2], [1,1], [4,5], [1, 2]].
Hint 2
Create another helper function that takes the array of pairs and creates a new integer. 
For example, if you call this function with [[2,2], [3,2], [1,1], [4,5], [1, 2]], it should create "22"+"23"+"11"+"54"+"21" = "2223115421".
Hint 3
Now, with the two helper functions, you can start with "1" and call the two functions alternatively n-1 times. 
The answer is the last integer you will obtain.

"""


class Solution:
    def countAndSay(self, n: int) -> str:

        first_number = True
        appearances  = 0
        current_string= ""
        new_string = ""
        for nn in range(1, n+1):

            if nn == 1:
                new_string = "1"
                current_string = new_string
            else:
                new_string = ""
                current_number = int(current_string[0])
                for _ in range(len(current_string)):
                    if int(current_string[_]) == current_number and _:
                        appearances +=1
                    else:
                        if not first_number:
                            new_string += (str(appearances) + str(current_number))
                            appearances = 1
                            current_number = int(current_string[_])
                        else:
                            appearances += 1
                            first_number = False

                first_number = True

                new_string += (str(appearances) + str(current_number))
                appearances = 0

                current_string = new_string

        return new_string




# OTHER PERSON'S SOLUTION, twice as fast (6 ms vs 1 ms best)

class Solution:
    def countAndSayV2(self, n: int) -> str:
        if n == 1:
            return "1"
        prev_term = self.countAndSayV2(n - 1)
        count = 1
        res = ""
        for i in range(1, len(prev_term) + 1):
            if i < len(prev_term) and prev_term[i] == prev_term[i - 1]:
                count += 1
            else:
                res += str(count)
                res += prev_term[i - 1]
                count = 1
        return res

  
