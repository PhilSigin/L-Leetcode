"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/


Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.


"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = [-1,0,0,0,0,3,3]
        """
        # Works but slow
        size = len(nums)
        n=0
        while n < (size-1):
            if nums[n] == nums [n+1]:
                nums.pop(n)
                size-=1
                continue
            n += 1
        """
        nums_list = list(set(nums))
        nums[:] = nums_list
        nums.sort()
        return len(nums)
