"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """ 
        Solution 3 -- the best, but Gemini helpd with the last string!
        Runtime        Memory
        160 ms         27.84MB
        Beats 52.42%   Beats 81.20%

        """
        
        size = len (nums)
        k2 = k % size 
        rot = size-k2
        nums[:] = nums[rot:] + nums[:rot]


        """ 
        Solution 2 -- strange, must be better
        Runtime         Memory
        1514 ms         27.92MB
        Beats 5.04%     Beats 53.49%


        size = len (nums)
        k2 = k % size 
        for _ in range(k2):
            nums.insert(0, nums[size-1])
            nums.pop(size)

        """


        """ 
        Solution 1
        Runtime         Memory
        1502ms          27.93MB
        Beats 5.11%     Beats 55.18%

        size = len(nums)
        for _ in range(k):
            nums.insert(0, nums[size-1])
            nums.pop(size)

        """
        
