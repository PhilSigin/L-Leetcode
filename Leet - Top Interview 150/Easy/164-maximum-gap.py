"""
164. Maximum Gap
https://leetcode.com/problems/maximum-gap/description/

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. 
If the array contains less than two elements, return 0.

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Runtime 717ms Beats 94.46%
Memory 30.29MB Beats 62.60%

"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()

        size = len(nums)
        if size < 2:
            # nothing to compare
            return 0

        max_dif = 0
        for i in range(size-1):
            dif = nums[i+1]-nums[i]
            if dif > max_dif:
                max_dif = dif

        return max_dif
