"""
Runtime         Memory  
38ms            16.46MB
Beats 68.83%    Beats 92.62%
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        del nums1[m:]

        nums1.extend(nums2)
        nums1.sort() 
