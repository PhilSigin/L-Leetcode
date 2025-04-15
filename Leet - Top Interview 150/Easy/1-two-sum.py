""" 
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Runtime 2556ms Beats 6.43%
Memory 18.58MB Beats72.60%

"""

# my solution - worst ever!

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)

        for x in range(length):
            for y in range(length-x-1):
                sum = (nums[x]+nums[x+y+1])
                if sum == target:
                    return x,x+y+1



""" GPTs Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Хранит числа и их индексы
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

"""
