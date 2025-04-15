"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

ВООБЩЕ НЕ ПОНЯЛ ЭТОЙ СТРУКТУРЫ - LINKED LISTS!
ИСкал решение и понимание, не помог даже CS50
https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        def sortedmerge(list1: Optional[ListNode], list2: Optional[ListNode]):

            if list1 is None:
                return list2
            if list2 is None:
                return list1

            # Recursive merging based on smaller value
            if list1.val <= list2.val:
                list1.next = sortedmerge(list1.next, list2)
                return list1
            else:
                list2.next = sortedmerge(list1, list2.next)
                return list2

        return sortedmerge(list1, list2)



""" 
ДРУГОЕ РЕШЕНИЕ - ТОЖЕ НЕ МОЕ 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to simplify head handling
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining part
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
"""


