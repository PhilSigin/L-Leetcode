# https://leetcode.com/problems/remove-element/description/

"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n= len(nums)
        i = 0
        while i<n:
            print(nums[i])
            if nums[i] == val:
                nums.pop(i)
                n -= 1
                continue
            i += 1

        # print(nums)
        return i
