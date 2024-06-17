# https://leetcode.com/problems/majority-element/
"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.


Follow-up: Could you solve the problem in linear time and in O(1) space?

# my solution is very slow! but efficient on memory
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        m = {}
        while i < n:
            if nums[i] in m:
                 m[nums[i]] += 1
                 if m[nums[i]] > (n/2):
                    return nums[i] 
            else:
                 m[nums[i]] = 1
            i +=1

        a= sorted(m.items(), key=lambda x: x[1], reverse=True)

        # b = max(m, key=m.get)
        # print (b)
        b = a[0][0]
        return b
