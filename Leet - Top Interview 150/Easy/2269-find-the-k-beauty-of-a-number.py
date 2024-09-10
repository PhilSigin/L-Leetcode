"""
2269. Find the K-Beauty of a Number
https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/

The k-beauty of an integer num is defined as the number of substrings 
of num when it is read as a string that meet the following conditions:
- It has a length of k, It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Example:

Input: num = 430043, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "43" from "430043": 43 is a divisor of 430043.
- "30" from "430043": 30 is not a divisor of 430043.
- "00" from "430043": 0 is not a divisor of 430043.
- "04" from "430043": 4 is not a divisor of 430043.
- "43" from "430043": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.

"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        num_s = str(num)
        sucs = 0

        for i in range(len(num_s)):

            div_s = num_s[i:i+k]

            # for shorter than k numbers:
            if len(div_s) < k:
                continue

            div = int(div_s)
            
            # division by 0 exceptio
            if div == 0:
                continue
                
            else:

            # checking for remainder 
                if num%div == 0:
                    sucs += 1


        return sucs


"""
More concise colution (not mine):

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)  
        n = len(num_str)
        count = 0
        
        for i in range(n - k + 1):
            substring = num_str[i:i+k] 
            substring_int = int(substring) 
            
            if substring_int != 0 and num % substring_int == 0:
                count += 1
        
        return count

"""
