"""
3010. Divide an Array Into Subarrays With Minimum Cost I
https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/

You are given an array of integers nums of length n.
The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.
You need to divide nums into 3 disjoint contiguous subarrays.

Return the minimum possible sum of the cost of these subarrays.


Runtime 55ms Beats 56.41%
Memory 16.46MB Beats 70.04%

"""




class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        # convert array to list with positions
        #indexed_nums = list(enumerate(nums))
        indexed_nums = list(enumerate(nums[1:]))

        # delete first - to not compare it to anything
        #del indexed_nums[0]

        # sort the list to find best starts of new arrays
        indexed_nums.sort(key=lambda x: (x[1], x[0]))
        
        # print (nums)
        # print (indexed_nums)
        # smaller = indexed_nums[0] 
        # small = indexed_nums[1]

        # print ("smaller", smaller)
        # print ("small", small)
        
        # return nums[0]+smaller[1]+small[1]
        return nums[0]+indexed_nums[0][1]+indexed_nums[1][1]


"""
My solution without comments:

class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        indexed_nums = list(enumerate(nums[1:]))
        indexed_nums.sort(key=lambda x: (x[1], x[0]))
        return nums[0]+indexed_nums[0][1]+indexed_nums[1][1]

"""

""" 
Better solution:

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        elem = nums.pop(0)
        nums.sort()   
        return elem + nums[1] + nums[0]

"""


