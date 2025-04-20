"""

781. Rabbits in Forest
https://leetcode.com/problems/rabbits-in-forest/

There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" 
and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.
Given the array answers, return the minimum number of rabbits that could be in the forest.

 

Example 1:
Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Example 2:
Input: answers = [10,10,10]
Output: 11

Runtime  0ms   Beats 100.00%
Memory 18.16MB Beats 9.16%

"""

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        numbers_dict = Counter(answers)

        numbers = 0
        for i, j in numbers_dict.items():
            
            # i - how many more rabbits (+1 the one who talks)
            # j - home many rabbits say so

            if i==0:
                numbers += j
                continue

            main, remainder = divmod(j, i+1)

            if remainder:
                cur_number = (main+1)*(i+1)
            else:
                cur_number = (main) * (i + 1)

            numbers += cur_number

        return numbers


### Other persons solution

class Solution:
    def numRabbitsOther(self, answers: List[int]) -> int:
        counts = defaultdict(int)
        for a in answers:
            counts[a + 1] += 1
        total = 0
        for answer, count in counts.items():
            total += ((count + answer - 1) // answer) * answer
        return total
