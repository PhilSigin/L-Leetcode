"""
228. Summary Ranges
https://leetcode.com/problems/summary-ranges/

You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]


Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]

Runtime 0ms Beats 100.00%
Memory 17.88MB Beats 33.58%

"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []
        
        save = []
        cur = mem = nums[0]

        for x in range (len(nums)):
            if x+1 < len(nums):
                if nums[x+1] == cur+1:     
                    cur = nums[x+1]
                else:
                    if cur > mem:
                        save.append(f"{mem}->{cur}")
                    else:
                        save.append(f"{mem}")
                    mem = cur = nums[x+1]
            else:
                # Last number
                if nums[x] == cur:
                    if cur == mem:  
                        save.append(f"{nums[x]}")
                    else:
                        save.append(f"{mem}->{nums[x]}")
                    
        return(save)


# Now - Gemini optimized solution

class GeminiSolution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []  # List to store the summary ranges
        start = nums[0]  # Start of the current range
        end = nums[0]    # End of the current range

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                # Extend the current range if the current number is consecutive
                end = nums[i]
            else:
                # Current number is not consecutive, so close the current range and start a new one

                if start == end:
                    result.append(str(start))  # Add the single number to the result
                else:
                    result.append(str(start) + "->" + str(end))  # Add the range to the result

                start = nums[i]  # Start a new range with the current number
                end = nums[i]    # End of the new range is also the current number

        # Handle the last range after the loop
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))

        return result

