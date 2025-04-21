"""

2145. Count the Hidden Sequences
https://leetcode.com/problems/count-the-hidden-sequences/

You are given a 0-indexed array of n integers differences, which describes the differences between each pair of consecutive integers of a hidden sequence of length (n + 1). 
More formally, call the hidden sequence hidden, then we have that differences[i] = hidden[i + 1] - hidden[i].
You are further given two integers lower and upper that describe the inclusive range of values [lower, upper] that the hidden sequence can contain.

  For example, given differences = [1, -3, 4], lower = 1, upper = 6, the hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 (inclusive).
      [3, 4, 1, 5] and [4, 5, 2, 6] are possible hidden sequences.
      [5, 6, 3, 7] is not possible since it contains an element greater than 6.
      [1, 2, 3, 4] is not possible since the differences are not correct.

Return the number of possible hidden sequences there are. If there are no possible sequences, return 0.

Example 1:
Input: differences = [1,-3,4], lower = 1, upper = 6
Output: 2
Explanation: The possible hidden sequences are:
- [3, 4, 1, 5]
- [4, 5, 2, 6]
Thus, we return 2.

Example 2:
Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
Output: 4
Explanation: The possible hidden sequences are:
- [-3, 0, -4, 1, 2, 0]
- [-2, 1, -3, 2, 3, 1]
- [-1, 2, -2, 3, 4, 2]
- [0, 3, -1, 4, 5, 3]
Thus, we return 4.

Example 3:
Input: differences = [4,-7,2], lower = 3, upper = 6
Output: 0
Explanation: There are no possible hidden sequences. Thus, we return 0.


Runtime 49ms   Beats 81.00%
Memory 31.53MB Beats 97.00%

"""


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        x = 0
        x_set = [x]
        
        for _ in range(len(differences)):
            x = x + differences[_]
            x_set.append(x)
        x_max = max(x_set)
        x_min = min(x_set)

        # diff1 = lower - x_min
        # diff2 = upper - x_max
        # answer = 1 - diff1 + diff2
        
        answer = 1 - (lower - x_min) + (upper - x_max)

        if answer <= 0:
            return 0
        return answer


# SOLUTION BELOW (but other person) is two times faster!

class Solution:
    def numberOfArraysFASTER(self, differences: List[int], lower: int, upper: int) -> int:
        pfs = list(accumulate(differences, initial = 0))

        return max(0, upper - lower - max(pfs) + min(pfs) + 1)
