"""
2176. Count Equal and Divisible Pairs in an Array
https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

Given a 0-indexed integer array nums of length n and an integer k, 
return the number of pairs (i, j) where 0 <= i < j < n, 
such that nums[i] == nums[j] and (i * j) is divisible by k.

### Hint used: For every possible pair of indices (i, j) where i < j, check if it satisfies the given conditions.


Example 1:
Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4
Explanation:
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

Example 2:
Input: nums = [1,2,3,4], k = 1
Output: 0
Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.



"""


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and not ((i*j)%k):
                    counter +=1

        return counter


# OTHER PERSON'S SOLUTION - with best time

class Solution:
    def countPairsExample(self, nums: List[int], k: int) -> int:
        
        index_map = defaultdict(list)   # nums[i] : [i, i2, i3 ...]
        result = 0

        for i in range(len(nums)):
            for j in index_map[nums[i]]:
                if (i * j) % k == 0:
                    result += 1

            index_map[nums[i]].append(i)

        return result
